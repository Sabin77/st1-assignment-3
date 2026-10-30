"""Tests for Stage 6 service operations."""

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Patient
from smartcare.services import PatientService


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
