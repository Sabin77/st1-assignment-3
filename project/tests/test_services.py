"""Tests for Stage 6 service operations."""

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Patient, Practitioner
from smartcare.services import PatientService, PractitionerService


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

