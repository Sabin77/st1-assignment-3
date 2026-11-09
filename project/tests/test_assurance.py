
"""Stage 11 assurance tests for SmartCare integrity."""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def make_assurance_setup():
    """Create isolated registered participants and appointment services."""
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patients.register_patient("P1", "Alex")
    patients.register_patient("P2", "Morgan")
    patients.register_patient("P3", "Casey")
    practitioners.register_practitioner("DR1", "Taylor", "GP")

    return store, appointments


def test_cancelled_booking_does_not_block_reschedule():
    """Cancelled history must not reserve a practitioner's time."""
    store, service = make_assurance_setup()

    original = service.book_appointment(
        "A1", "P1", "DR1", datetime(2026, 10, 1, 9, 0)
    )
    cancelled = service.book_appointment(
        "A2", "P2", "DR1", datetime(2026, 10, 1, 10, 0)
    )

    service.cancel_appointment("A2")

    result = service.reschedule_appointment(
        "A1", datetime(2026, 10, 1, 10, 0)
    )

    assert result is original
    assert original.date_time == datetime(2026, 10, 1, 10, 0)
    assert original.status is AppointmentStatus.SCHEDULED
    assert store.find_appointment("A2") is cancelled
    assert cancelled.status is AppointmentStatus.CANCELLED
    assert cancelled.date_time == datetime(2026, 10, 1, 10, 0)
    assert len(store.list_appointments()) == 2


def test_failed_reschedule_preserves_listing_and_store_state():
    """A rejected conflict must not corrupt stored appointment history."""
    store, service = make_assurance_setup()

    first = service.book_appointment(
        "A1", "P1", "DR1", datetime(2026, 10, 1, 9, 0)
    )
    second = service.book_appointment(
        "A2", "P2", "DR1", datetime(2026, 10, 1, 10, 0)
    )
    third = service.book_appointment(
        "A3", "P3", "DR1", datetime(2026, 10, 1, 11, 0)
    )

    before_records = tuple(store.list_appointments())
    before_listing = tuple(service.list_practitioner_appointments("DR1"))
    before_state = tuple(
        (
            appointment.appointment_id,
            appointment.date_time,
            appointment.status,
            appointment.patient,
            appointment.practitioner,
        )
        for appointment in before_records
    )

    with pytest.raises(ValueError):
        service.reschedule_appointment(
            "A1", datetime(2026, 10, 1, 10, 0)
        )

    after_records = tuple(store.list_appointments())
    after_listing = tuple(service.list_practitioner_appointments("DR1"))
    after_state = tuple(
        (
            appointment.appointment_id,
            appointment.date_time,
            appointment.status,
            appointment.patient,
            appointment.practitioner,
        )
        for appointment in after_records
    )

    assert len(after_records) == 3
    assert all(
        before is after
        for before, after in zip(before_records, after_records)
    )
    assert all(
        before is after
        for before, after in zip(before_listing, after_listing)
    )
    assert before_state == after_state
    assert after_listing == (first, second, third)
