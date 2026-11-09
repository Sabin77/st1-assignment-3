"""Stage 8 regression tests for repaired defects F8-01 and F8-02."""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


WHEN = datetime(2026, 12, 1, 9)


def booked_setup() -> tuple[
    SmartCareDataStore,
    AppointmentService,
    Appointment,
]:
    """Create a store with P1, DR1, DR2 and one booked appointment A1."""
    data_store = SmartCareDataStore()
    PatientService(data_store).register_patient('P1', 'Alex Example')
    practitioners = PractitionerService(data_store)
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    practitioners.register_practitioner(
        'DR2',
        'Morgan Example',
        'General practice',
    )
    appointment_service = AppointmentService(data_store)
    appointment = appointment_service.book_appointment('A1', 'P1', 'DR1', WHEN)
    return data_store, appointment_service, appointment


def test_f801_store_finds_cancelled_appointment() -> None:
    """F8-01: the store still returns an appointment after cancellation."""
    data_store, appointment_service, appointment = booked_setup()
    appointment_service.cancel_appointment('A1')
    assert data_store.find_appointment('A1') is appointment
    assert appointment.status is AppointmentStatus.CANCELLED


def test_f801_service_finds_cancelled_appointment() -> None:
    """F8-01: service lookup does not raise LookupError after cancellation."""
    _, appointment_service, appointment = booked_setup()
    appointment_service.cancel_appointment('A1')
    assert appointment_service.find_appointment('A1') is appointment


def test_f801_cancelled_appointment_still_listed() -> None:
    """F8-01 / FR-07: cancelled history stays in store and service listings."""
    data_store, appointment_service, appointment = booked_setup()
    appointment_service.cancel_appointment('A1')
    assert data_store.list_appointments() == [appointment]
    assert appointment_service.list_practitioner_appointments('DR1') == [
        appointment,
    ]


def test_f802_same_practitioner_same_time_conflicts() -> None:
    """F8-02: the same practitioner at the same time is a conflict."""
    data_store, _, _ = booked_setup()
    assert data_store.has_practitioner_conflict('DR1', WHEN) is True


def test_f802_different_practitioner_same_time_no_conflict() -> None:
    """F8-02 / AC-04.2: another practitioner at the same time is allowed."""
    data_store, appointment_service, _ = booked_setup()
    assert data_store.has_practitioner_conflict('DR2', WHEN) is False
    other = appointment_service.book_appointment('A2', 'P1', 'DR2', WHEN)
    assert other.practitioner.practitioner_id == 'DR2'


def test_f802_same_practitioner_booking_rejected_without_change() -> None:
    """F8-02 / AC-04.1: a conflicting booking is rejected and not stored."""
    data_store, appointment_service, appointment = booked_setup()
    with pytest.raises(ValueError):
        appointment_service.book_appointment('A2', 'P1', 'DR1', WHEN)
    assert data_store.list_appointments() == [appointment]


def test_f802_cancelled_slot_does_not_conflict() -> None:
    """F8-02: only SCHEDULED appointments conflict, so a cancelled slot frees."""
    data_store, appointment_service, _ = booked_setup()
    appointment_service.cancel_appointment('A1')
    assert data_store.has_practitioner_conflict('DR1', WHEN) is False
    rebooked = appointment_service.book_appointment('A2', 'P1', 'DR1', WHEN)
    assert rebooked.status is AppointmentStatus.SCHEDULED


def test_f802_excluded_appointment_is_ignored() -> None:
    """F8-02: the optional excluded appointment ID is skipped."""
    data_store, _, _ = booked_setup()
    assert data_store.has_practitioner_conflict(
        'DR1',
        WHEN,
        exclude_appointment_id='A1',
    ) is False