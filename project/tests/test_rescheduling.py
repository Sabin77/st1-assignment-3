"""Stage 10 tests for appointment rescheduling."""

from datetime import datetime, timezone

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def make_setup():
    """Create independent test data for each test."""
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    service = AppointmentService(store)

    patients.register_patient("P1", "Alex")
    patients.register_patient("P2", "Morgan")
    practitioners.register_practitioner("DR1", "Taylor", "GP")
    practitioners.register_practitioner("DR2", "Jordan", "Cardiology")

    appointment = service.book_appointment(
        "A1", "P1", "DR1", datetime(2026, 10, 1, 9, 0)
    )
    return store, service, appointment


def test_successful_reschedule_preserves_identity():
    store, service, appointment = make_setup()

    patient = appointment.patient
    practitioner = appointment.practitioner
    new_time = datetime(2026, 10, 1, 10, 0)

    result = service.reschedule_appointment("A1", new_time)

    assert result is appointment
    assert store.find_appointment("A1") is appointment
    assert appointment.appointment_id == "A1"
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner
    assert appointment.date_time == new_time
    assert appointment.status is AppointmentStatus.SCHEDULED


def test_unknown_appointment_raises_lookup_error():
    _, service, appointment = make_setup()

    with pytest.raises(LookupError):
        service.reschedule_appointment(
            "UNKNOWN", datetime(2026, 10, 1, 10, 0)
        )

    assert appointment.date_time == datetime(2026, 10, 1, 9, 0)


@pytest.mark.parametrize("invalid_id", ["", "   ", None, 123])
def test_invalid_appointment_id(invalid_id):
    _, service, appointment = make_setup()

    with pytest.raises(ValueError):
        service.reschedule_appointment(
            invalid_id, datetime(2026, 10, 1, 10, 0)
        )

    assert appointment.date_time == datetime(2026, 10, 1, 9, 0)


def test_same_practitioner_conflict_rejected():
    store, service, appointment = make_setup()

    other = service.book_appointment(
        "A2", "P2", "DR1", datetime(2026, 10, 1, 11, 0)
    )

    before = list(store.list_appointments())

    with pytest.raises(ValueError):
        service.reschedule_appointment(
            "A1", datetime(2026, 10, 1, 11, 0)
        )

    assert appointment.date_time == datetime(2026, 10, 1, 9, 0)
    assert other.date_time == datetime(2026, 10, 1, 11, 0)
    assert store.list_appointments() == before


def test_different_practitioner_same_time_allowed():
    _, service, appointment = make_setup()

    service.book_appointment(
        "A2", "P2", "DR2", datetime(2026, 10, 1, 10, 0)
    )

    result = service.reschedule_appointment(
        "A1", datetime(2026, 10, 1, 10, 0)
    )

    assert result is appointment
    assert appointment.date_time == datetime(2026, 10, 1, 10, 0)


def test_cancelled_appointment_cannot_reschedule():
    _, service, appointment = make_setup()
    service.cancel_appointment("A1")
    original_time = appointment.date_time

    for requested_time in (
        original_time,
        datetime(2026, 10, 1, 10, 0),
    ):
        with pytest.raises(ValueError):
            service.reschedule_appointment("A1", requested_time)

    assert appointment.status is AppointmentStatus.CANCELLED
    assert appointment.date_time == original_time


def test_completed_appointment_cannot_reschedule():
    store, service, appointment = make_setup()

    completed = Appointment(
        "A2",
        appointment.patient,
        appointment.practitioner,
        datetime(2026, 10, 1, 11, 0),
        AppointmentStatus.COMPLETED,
    )
    store.add_appointment(completed)
    original_time = completed.date_time

    for requested_time in (
        original_time,
        datetime(2026, 10, 1, 12, 0),
    ):
        with pytest.raises(ValueError):
            service.reschedule_appointment("A2", requested_time)

    assert completed.status is AppointmentStatus.COMPLETED
    assert completed.date_time == original_time
    assert store.find_appointment("A2") is completed


def test_same_time_no_op():
    _, service, appointment = make_setup()
    original_time = appointment.date_time

    result = service.reschedule_appointment("A1", original_time)

    assert result is appointment
    assert appointment.date_time == original_time


@pytest.mark.parametrize(
    "invalid_time",
    [
        "2026-10-01 10:00",
        None,
        datetime(2026, 10, 1, 10, 0, 1),
        datetime(2026, 10, 1, 10, 0, 0, 1),
        datetime(2026, 10, 1, 10, 0, tzinfo=timezone.utc),
    ],
)
def test_invalid_datetime_rejected(invalid_time):
    _, service, appointment = make_setup()
    original_time = appointment.date_time

    with pytest.raises(ValueError):
        service.reschedule_appointment("A1", invalid_time)

    assert appointment.date_time == original_time
    assert appointment.status is AppointmentStatus.SCHEDULED


def test_successful_move_frees_original_slot():
    _, service, appointment = make_setup()

    service.reschedule_appointment(
        "A1", datetime(2026, 10, 1, 10, 0)
    )

    replacement = service.book_appointment(
        "A2", "P2", "DR1", datetime(2026, 10, 1, 9, 0)
    )

    assert appointment.date_time == datetime(2026, 10, 1, 10, 0)
    assert replacement.date_time == datetime(2026, 10, 1, 9, 0)


def test_lookup_and_listing_show_updated_order():
    store, service, appointment = make_setup()

    other = service.book_appointment(
        "A2", "P2", "DR1", datetime(2026, 10, 1, 11, 0)
    )

    service.reschedule_appointment(
        "A1", datetime(2026, 10, 1, 12, 0)
    )

    assert service.find_appointment("A1") is appointment
    assert store.find_appointment("A1").date_time == datetime(
        2026, 10, 1, 12, 0
    )

    ordered = service.list_practitioner_appointments("DR1")

    assert [item.appointment_id for item in ordered] == ["A2", "A1"]
    assert ordered[0] is other
    assert ordered[1] is appointment


def test_domain_rejects_invalid_status_and_time():
    _, _, appointment = make_setup()
    original_time = appointment.date_time

    with pytest.raises(ValueError):
        appointment.reschedule("invalid")

    assert appointment.date_time == original_time

    appointment.cancel()

    with pytest.raises(ValueError):
        appointment.reschedule(datetime(2026, 10, 1, 10, 0))

    assert appointment.status is AppointmentStatus.CANCELLED
    assert appointment.date_time == original_time
