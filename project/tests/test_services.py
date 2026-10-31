"""Tests for Stage 6 service operations."""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def patient_setup() -> tuple[PatientService, Patient]:
    """Create a fresh store with one registered synthetic patient."""
    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    patient = patient_service.register_patient('P1', 'Alex Example')
    return patient_service, patient


def test_find_patient_returns_registered_object() -> None:
    """Verify a registered ID returns the same stored patient."""
    patient_service, patient = patient_setup()
    found = patient_service.find_patient('P1')
    assert found is patient


def test_find_patient_unknown_id_raises_lookup_error() -> None:
    """Verify an unknown valid ID raises LookupError."""
    patient_service, _ = patient_setup()
    with pytest.raises(LookupError):
        patient_service.find_patient('P99')


def test_find_patient_blank_id_raises_value_error() -> None:
    """Verify a blank or non-text ID raises ValueError."""
    patient_service, _ = patient_setup()
    with pytest.raises(ValueError):
        patient_service.find_patient('   ')
    with pytest.raises(ValueError):
        patient_service.find_patient(None)


def test_find_patient_trims_surrounding_spaces() -> None:
    """Verify an ID with surrounding spaces finds the same patient."""
    patient_service, patient = patient_setup()
    assert patient_service.find_patient('  P1  ') is patient


def test_find_patient_is_case_sensitive() -> None:
    """Verify a different letter case is treated as not found."""
    patient_service, _ = patient_setup()
    with pytest.raises(LookupError):
        patient_service.find_patient('p1')


def practitioner_setup() -> tuple[PractitionerService, Practitioner]:
    """Create a fresh store with one registered synthetic practitioner."""
    data_store = SmartCareDataStore()
    practitioner_service = PractitionerService(data_store)
    practitioner = practitioner_service.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    return practitioner_service, practitioner


def test_find_practitioner_returns_registered_object() -> None:
    """Verify a registered ID returns the same stored practitioner."""
    practitioner_service, practitioner = practitioner_setup()
    assert practitioner_service.find_practitioner('DR1') is practitioner


def test_find_practitioner_unknown_id_raises_lookup_error() -> None:
    """Verify an unknown valid ID raises LookupError."""
    practitioner_service, _ = practitioner_setup()
    with pytest.raises(LookupError):
        practitioner_service.find_practitioner('DR99')


def test_find_practitioner_blank_id_raises_value_error() -> None:
    """Verify a blank or non-text ID raises ValueError."""
    practitioner_service, _ = practitioner_setup()
    with pytest.raises(ValueError):
        practitioner_service.find_practitioner('   ')
    with pytest.raises(ValueError):
        practitioner_service.find_practitioner(None)


def test_find_practitioner_trims_surrounding_spaces() -> None:
    """Verify an ID with surrounding spaces finds the same practitioner."""
    practitioner_service, practitioner = practitioner_setup()
    assert practitioner_service.find_practitioner('  DR1  ') is practitioner


def test_find_practitioner_is_case_sensitive() -> None:
    """Verify a different letter case is treated as not found."""
    practitioner_service, _ = practitioner_setup()
    with pytest.raises(LookupError):
        practitioner_service.find_practitioner('dr1')


def appointment_setup() -> tuple[
    SmartCareDataStore,
    AppointmentService,
    Appointment,
]:
    """Create a fresh store with one booked synthetic appointment."""
    data_store = SmartCareDataStore()
    PatientService(data_store).register_patient('P1', 'Alex Example')
    PractitionerService(data_store).register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    appointment_service = AppointmentService(data_store)
    appointment = appointment_service.book_appointment(
        'A1',
        'P1',
        'DR1',
        datetime(2026, 10, 1, 9),
    )
    return data_store, appointment_service, appointment


def test_cancel_scheduled_returns_same_cancelled_object() -> None:
    """Verify cancelling a scheduled appointment returns it as CANCELLED."""
    _, appointment_service, appointment = appointment_setup()
    cancelled = appointment_service.cancel_appointment('A1')
    assert cancelled is appointment
    assert appointment.status is AppointmentStatus.CANCELLED


def test_cancelled_appointment_is_retained_in_history() -> None:
    """Verify a cancelled appointment can still be found and listed."""
    data_store, appointment_service, appointment = appointment_setup()
    appointment_service.cancel_appointment('A1')
    assert appointment_service.find_appointment('A1') is appointment
    assert data_store.list_appointments() == [appointment]


def test_cancel_twice_raises_value_error() -> None:
    """Verify a repeated cancellation is rejected and status is kept."""
    _, appointment_service, appointment = appointment_setup()
    appointment_service.cancel_appointment('A1')
    with pytest.raises(ValueError):
        appointment_service.cancel_appointment('A1')
    assert appointment.status is AppointmentStatus.CANCELLED


def test_cancel_completed_raises_value_error() -> None:
    """Verify a COMPLETED appointment cannot be cancelled."""
    data_store, appointment_service, _ = appointment_setup()
    completed = Appointment(
        'A2',
        data_store.find_patient('P1'),
        data_store.find_practitioner('DR1'),
        datetime(2026, 10, 1, 10),
        AppointmentStatus.COMPLETED,
    )
    data_store.add_appointment(completed)
    with pytest.raises(ValueError):
        appointment_service.cancel_appointment('A2')
    assert completed.status is AppointmentStatus.COMPLETED


def test_cancel_unknown_id_raises_lookup_error() -> None:
    """Verify an unknown valid ID raises LookupError without changes."""
    _, appointment_service, appointment = appointment_setup()
    with pytest.raises(LookupError):
        appointment_service.cancel_appointment('A99')
    assert appointment.status is AppointmentStatus.SCHEDULED


def test_cancel_blank_id_raises_value_error() -> None:
    """Verify a blank or non-text ID raises ValueError."""
    _, appointment_service, appointment = appointment_setup()
    with pytest.raises(ValueError):
        appointment_service.cancel_appointment('   ')
    with pytest.raises(ValueError):
        appointment_service.cancel_appointment(None)
    assert appointment.status is AppointmentStatus.SCHEDULED


# Stage 7: Additional service verification


def stage7_setup():
    """Fresh shared store and registered participants for each test."""
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patient = patients.register_patient("P1", "Alex Example")
    doctor1 = practitioners.register_practitioner(
        "DR1", "Taylor Example", "General practice"
    )
    doctor2 = practitioners.register_practitioner(
        "DR2", "Jordan Example", "Cardiology"
    )

    return store, patients, practitioners, appointments, patient, doctor1, doctor2


def test_stage7_register_patient_stores_same_object():
    store = SmartCareDataStore()
    service = PatientService(store)

    patient = service.register_patient("P1", "Alex Example")

    assert store.find_patient("P1") is patient
    assert store.list_patients() == [patient]


def test_stage7_duplicate_patient_preserves_original():
    store, patients, _, _, patient, _, _ = stage7_setup()

    with pytest.raises(ValueError):
        patients.register_patient("P1", "Different Person")

    assert store.find_patient("P1") is patient
    assert patient.name == "Alex Example"
    assert len(store.list_patients()) == 1


def test_stage7_duplicate_practitioner_preserves_original():
    store, _, practitioners, _, _, doctor1, _ = stage7_setup()

    with pytest.raises(ValueError):
        practitioners.register_practitioner(
            "DR1", "Different Doctor", "Neurology"
        )

    assert store.find_practitioner("DR1") is doctor1
    assert doctor1.name == "Taylor Example"
    assert len(store.list_practitioners()) == 2


def test_stage7_booking_stores_registered_participants():
    store, _, _, appointments, patient, doctor1, _ = stage7_setup()
    slot = datetime(2026, 10, 1, 9, 0)

    booked = appointments.book_appointment("A1", "P1", "DR1", slot)

    assert store.find_appointment("A1") is booked
    assert booked.patient is patient
    assert booked.practitioner is doctor1
    assert booked.date_time == slot
    assert booked.status is AppointmentStatus.SCHEDULED


def test_stage7_same_practitioner_exact_time_conflict_preserves_store():
    store, _, _, appointments, _, _, _ = stage7_setup()
    slot = datetime(2026, 10, 1, 9, 0)
    original = appointments.book_appointment("A1", "P1", "DR1", slot)

    with pytest.raises(ValueError):
        appointments.book_appointment("A2", "P1", "DR1", slot)

    assert store.list_appointments() == [original]
    assert original.status is AppointmentStatus.SCHEDULED
    assert store.find_appointment("A2") is None


def test_stage7_different_practitioner_same_time_allowed():
    store, _, _, appointments, _, _, _ = stage7_setup()
    slot = datetime(2026, 10, 1, 9, 0)

    first = appointments.book_appointment("A1", "P1", "DR1", slot)
    second = appointments.book_appointment("A2", "P1", "DR2", slot)

    assert first.practitioner.practitioner_id == "DR1"
    assert second.practitioner.practitioner_id == "DR2"
    assert first.date_time == second.date_time
    assert store.list_appointments() == [first, second]


def test_stage7_duplicate_appointment_id_preserves_original():
    store, _, _, appointments, _, _, _ = stage7_setup()
    original = appointments.book_appointment(
        "A1", "P1", "DR1", datetime(2026, 10, 1, 9, 0)
    )

    with pytest.raises(ValueError):
        appointments.book_appointment(
            "A1", "P1", "DR2", datetime(2026, 10, 1, 10, 0)
        )

    assert store.find_appointment("A1") is original
    assert store.list_appointments() == [original]


def test_stage7_unknown_participant_rejected_without_booking():
    store, _, _, appointments, _, _, _ = stage7_setup()
    slot = datetime(2026, 10, 1, 9, 0)

    with pytest.raises(LookupError):
        appointments.book_appointment("A1", "P99", "DR1", slot)

    with pytest.raises(LookupError):
        appointments.book_appointment("A2", "P1", "DR99", slot)

    assert store.list_appointments() == []
def test_stage7_conflict_with_different_patient_preserves_store():
    store, patients, _, appointments, _, _, _ = stage7_setup()
    patients.register_patient("P2", "Morgan Example")
    slot = datetime(2026, 10, 1, 9, 0)

    original = appointments.book_appointment("A1", "P1", "DR1", slot)

    with pytest.raises(ValueError):
        appointments.book_appointment("A2", "P2", "DR1", slot)

    assert store.list_appointments() == [original]
    assert store.find_appointment("A2") is None
    assert original.status is AppointmentStatus.SCHEDULED


def test_stage7_same_practitioner_different_minute_allowed():
    store, patients, _, appointments, _, _, _ = stage7_setup()
    patients.register_patient("P2", "Morgan Example")

    first = appointments.book_appointment(
        "A1", "P1", "DR1", datetime(2026, 10, 1, 9, 0)
    )
    second = appointments.book_appointment(
        "A2", "P2", "DR1", datetime(2026, 10, 1, 9, 1)
    )

    assert first.practitioner is second.practitioner
    assert first.date_time != second.date_time
    assert first.status is AppointmentStatus.SCHEDULED
    assert second.status is AppointmentStatus.SCHEDULED
    assert store.list_appointments() == [first, second]


def test_stage7_cancelled_slot_can_be_rebooked_with_history_retained():
    store, patients, _, appointments, _, _, _ = stage7_setup()
    patients.register_patient("P2", "Morgan Example")
    slot = datetime(2026, 10, 1, 9, 0)

    original = appointments.book_appointment("A1", "P1", "DR1", slot)
    appointments.cancel_appointment("A1")

    replacement = appointments.book_appointment(
        "A2", "P2", "DR1", slot
    )

    assert original.status is AppointmentStatus.CANCELLED
    assert replacement.status is AppointmentStatus.SCHEDULED
    assert store.find_appointment("A1") is original
    assert store.find_appointment("A2") is replacement
    assert store.list_appointments() == [original, replacement]
