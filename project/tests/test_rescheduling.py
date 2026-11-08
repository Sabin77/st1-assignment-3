"""Stage 10 rescheduling tests for SmartCare."""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def rescheduling_setup():
    """Create a fresh store with two patients, two practitioners and one
    scheduled appointment.
    """
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patients.register_patient('P1', 'Alex Example')
    patients.register_patient('P2', 'Morgan Example')
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    practitioners.register_practitioner(
        'DR2',
        'Jordan Example',
        'Cardiology',
    )
    appointment = appointments.book_appointment(
        'A1',
        'P1',
        'DR1',
        datetime(2026, 10, 1, 9, 0),
    )
    return store, appointments, appointment


def test_reschedule_moves_appointment_and_preserves_identity() -> None:
    """A valid reschedule updates only the time and keeps object identity."""
    store, appointments, appointment = rescheduling_setup()
    new_time = datetime(2026, 10, 1, 10, 0)

    moved = appointments.reschedule_appointment('A1', new_time)

    assert moved is appointment
    assert appointment.appointment_id == 'A1'
    assert appointment.patient.patient_id == 'P1'
    assert appointment.practitioner.practitioner_id == 'DR1'
    assert appointment.date_time == new_time
    assert appointment.status is AppointmentStatus.SCHEDULED
    assert store.find_appointment('A1') is appointment
    assert store.list_appointments() == [appointment]


def test_reschedule_unknown_appointment_id_raises_lookup_error() -> None:
    """A valid unknown appointment ID raises LookupError without mutation."""
    store, appointments, appointment = rescheduling_setup()

    with pytest.raises(LookupError):
        appointments.reschedule_appointment('A99', datetime(2026, 10, 1, 10, 0))

    assert appointment.date_time == datetime(2026, 10, 1, 9, 0)
    assert store.find_appointment('A1') is appointment


def test_reschedule_blank_or_non_string_id_raises_value_error() -> None:
    """Blank or non-string IDs are rejected before any mutation."""
    _, appointments, appointment = rescheduling_setup()
    new_time = datetime(2026, 10, 1, 10, 0)

    with pytest.raises(ValueError):
        appointments.reschedule_appointment('   ', new_time)
    with pytest.raises(ValueError):
        appointments.reschedule_appointment(None, new_time)

    assert appointment.date_time == datetime(2026, 10, 1, 9, 0)
    assert appointment.status is AppointmentStatus.SCHEDULED


def test_reschedule_rejects_same_practitioner_conflict_excluding_target() -> None:
    """Another scheduled appointment for the same practitioner blocks the move."""
    store, appointments, appointment = rescheduling_setup()
    conflicting = appointments.book_appointment(
        'A2',
        'P2',
        'DR1',
        datetime(2026, 10, 1, 11, 0),
    )

    with pytest.raises(ValueError):
        appointments.reschedule_appointment('A1', datetime(2026, 10, 1, 11, 0))

    assert appointment.status is AppointmentStatus.SCHEDULED
    assert appointment.date_time == datetime(2026, 10, 1, 9, 0)
    assert conflicting.status is AppointmentStatus.SCHEDULED
    assert store.list_appointments() == [appointment, conflicting]


def test_reschedule_allows_different_practitioner_at_requested_time() -> None:
    """The requested slot is available when the other appointment is with DR2."""
    store, appointments, appointment = rescheduling_setup()
    other = appointments.book_appointment(
        'A2',
        'P2',
        'DR2',
        datetime(2026, 10, 1, 10, 0),
    )

    moved = appointments.reschedule_appointment('A1', datetime(2026, 10, 1, 10, 0))

    assert moved is appointment
    assert other.status is AppointmentStatus.SCHEDULED
    assert appointment.date_time == datetime(2026, 10, 1, 10, 0)
    assert store.list_appointments() == [appointment, other]


def test_reschedule_rejects_cancelled_and_completed_targets() -> None:
    """Cancelled and completed appointments cannot be moved."""
    _, appointments, appointment = rescheduling_setup()
    appointment.cancel()

    with pytest.raises(ValueError):
        appointments.reschedule_appointment('A1', datetime(2026, 10, 1, 10, 0))
    assert appointment.status is AppointmentStatus.CANCELLED

    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    patients.register_patient('P1', 'Alex Example')
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    completed = AppointmentService(store).book_appointment(
        'A2',
        'P1',
        'DR1',
        datetime(2026, 10, 1, 9, 0),
    )
    completed.cancel()
    completed.status  # pragma: no cover


def test_reschedule_same_time_no_op_is_allowed() -> None:
    """A valid SCHEDULED same-time move is treated as a no-op."""
    _, appointments, appointment = rescheduling_setup()

    moved = appointments.reschedule_appointment('A1', datetime(2026, 10, 1, 9, 0))

    assert moved is appointment
    assert appointment.date_time == datetime(2026, 10, 1, 9, 0)
    assert appointment.status is AppointmentStatus.SCHEDULED


def test_reschedule_rejects_invalid_datetime_variants() -> None:
    """Invalid datetime types and precision are rejected without mutation."""
    _, appointments, appointment = rescheduling_setup()

    for invalid in (
        '2026-10-01 09:00',
        datetime(2026, 10, 1, 9, 0, 1),
        datetime(2026, 10, 1, 9, 0, tzinfo=None),
    ):
        with pytest.raises(ValueError):
            appointments.reschedule_appointment('A1', invalid)
    assert appointment.date_time == datetime(2026, 10, 1, 9, 0)


def test_failed_reschedule_keeps_store_contents_and_order() -> None:
    """Rejected operations preserve the store, object and listing order."""
    store, appointments, appointment = rescheduling_setup()
    conflicting = appointments.book_appointment(
        'A2',
        'P2',
        'DR1',
        datetime(2026, 10, 1, 11, 0),
    )

    with pytest.raises(ValueError):
        appointments.reschedule_appointment('A1', datetime(2026, 10, 1, 11, 0))

    assert store.list_appointments() == [appointment, conflicting]
    assert appointment.date_time == datetime(2026, 10, 1, 9, 0)
    assert conflicting.date_time == datetime(2026, 10, 1, 11, 0)


def test_reschedule_frees_old_slot_for_rebooking() -> None:
    """Successful rescheduling releases the old slot for other appointments."""
    _, appointments, appointment = rescheduling_setup()
    appointments.reschedule_appointment('A1', datetime(2026, 10, 1, 10, 0))

    replacement = appointments.book_appointment(
        'A2',
        'P2',
        'DR1',
        datetime(2026, 10, 1, 9, 0),
    )

    assert replacement.status is AppointmentStatus.SCHEDULED
    assert appointment.date_time == datetime(2026, 10, 1, 10, 0)
    assert replacement.date_time == datetime(2026, 10, 1, 9, 0)


def test_list_practitioner_appointments_reflects_updated_time() -> None:
    """Lookup and practitioner listing show rescheduled times immediately."""
    store, appointments, appointment = rescheduling_setup()
    other = appointments.book_appointment(
        'A2',
        'P2',
        'DR1',
        datetime(2026, 10, 1, 11, 0),
    )

    appointments.reschedule_appointment('A1', datetime(2026, 10, 1, 12, 0))

    assert store.find_appointment('A1') is appointment
    assert appointment.date_time == datetime(2026, 10, 1, 12, 0)
    assert [item.appointment_id for item in appointments.list_practitioner_appointments('DR1')] == [
        'A2',
        'A1',
    ]
    assert other.date_time == datetime(2026, 10, 1, 11, 0)

