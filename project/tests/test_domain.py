
"""Stage 7 domain tests for SmartCare.

Tests the public validation and state-transition contracts.
Uses only synthetic data.
"""

from datetime import datetime, timezone

import pytest

from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)


def make_appointment(
    status=AppointmentStatus.SCHEDULED,
):
    """Create a new appointment using synthetic participants."""
    patient = Patient("P1", "Alex Example")
    practitioner = Practitioner(
        "DR1", "Taylor Example", "General practice"
    )
    return Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 10, 1, 9, 0),
        status,
    )


# Patient domain tests

def test_blank_patient_id_is_rejected():
    with pytest.raises(ValueError):
        Patient("   ", "Alex Example")


def test_patient_fields_are_trimmed():
    patient = Patient(" P1 ", " Alex Example ")
    assert patient.patient_id == "P1"
    assert patient.name == "Alex Example"


def test_blank_patient_name_is_rejected():
    with pytest.raises(ValueError):
        Patient("P1", "   ")


# Practitioner domain tests

def test_practitioner_fields_are_validated_and_trimmed():
    practitioner = Practitioner(
        " DR1 ", " Taylor Example ", " General practice "
    )
    assert practitioner.practitioner_id == "DR1"
    assert practitioner.name == "Taylor Example"
    assert practitioner.specialty == "General practice"


@pytest.mark.parametrize(
    "practitioner_id,name,specialty",
    [
        ("", "Taylor Example", "General practice"),
        ("DR1", " ", "General practice"),
        ("DR1", "Taylor Example", " "),
    ],
)
def test_practitioner_blank_required_fields_are_rejected(
    practitioner_id, name, specialty
):
    with pytest.raises(ValueError):
        Practitioner(practitioner_id, name, specialty)


# Appointment domain tests

def test_new_appointment_starts_scheduled():
    appointment = make_appointment()
    assert appointment.status is AppointmentStatus.SCHEDULED


def test_appointment_retains_participant_identity():
    appointment = make_appointment()
    assert appointment.patient.patient_id == "P1"
    assert appointment.practitioner.practitioner_id == "DR1"
    assert appointment.date_time == datetime(2026, 10, 1, 9, 0)


def test_domain_cancel_changes_status():
    appointment = make_appointment()
    appointment.cancel()
    assert appointment.status is AppointmentStatus.CANCELLED


def test_domain_repeated_cancel_rejected():
    appointment = make_appointment()
    appointment.cancel()

    with pytest.raises(ValueError):
        appointment.cancel()

    assert appointment.status is AppointmentStatus.CANCELLED


def test_completed_appointment_cannot_be_cancelled():
    appointment = make_appointment(AppointmentStatus.COMPLETED)

    with pytest.raises(ValueError):
        appointment.cancel()

    assert appointment.status is AppointmentStatus.COMPLETED


@pytest.mark.parametrize(
    "date_time",
    [
        "2026-10-01 09:00",
        datetime(2026, 10, 1, 9, 0, 1),
        datetime(2026, 10, 1, 9, 0, tzinfo=timezone.utc),
    ],
)
def test_invalid_appointment_time_is_rejected(date_time):
    patient = Patient("P1", "Alex Example")
    practitioner = Practitioner(
        "DR1", "Taylor Example", "General practice"
    )

    with pytest.raises(ValueError):
        Appointment("A1", patient, practitioner, date_time)


def test_invalid_appointment_participant_is_rejected():
    practitioner = Practitioner(
        "DR1", "Taylor Example", "General practice"
    )

    with pytest.raises(ValueError):
        Appointment(
            "A1",
            None,
            practitioner,
            datetime(2026, 10, 1, 9, 0),
        )


def test_invalid_appointment_status_is_rejected():
    patient = Patient("P1", "Alex Example")
    practitioner = Practitioner(
        "DR1", "Taylor Example", "General practice"
    )

    with pytest.raises(ValueError):
        Appointment(
            "A1",
            patient,
            practitioner,
            datetime(2026, 10, 1, 9, 0),
            "CANCELLED",
        )
