"""Console helpers and a small runnable starting demonstration."""


import re
from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def parse_date_time(text: str) -> datetime:
    """Parse YYYY-MM-DD HH:MM; raise ValueError for invalid input."""
    if (
        not isinstance(text, str)
        or re.fullmatch(
            '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', text
        ) is None
    ):
        raise ValueError('Use date/time format YYYY-MM-DD HH:MM')
    try:
        return datetime.strptime(text, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError(
            'Invalid calendar date/time; use YYYY-MM-DD HH:MM',
        ) from None


def format_appointment(appointment: Appointment) -> str:
    """Return readable synthetic appointment details without changing
    state.
    """
    return (
        f'{appointment.appointment_id}: '
        f'{appointment.patient.patient_id} with '
        f'{appointment.practitioner.practitioner_id}, '
        f'{appointment.date_time:%Y-%m-%d %H:%M}, {appointment.status.value}'
    )


def run_demo() -> None:
    """Demonstrate supplied registration and booking using synthetic
    records.
    """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    patients.register_patient('P1', 'Alex Example')
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    try:
        appointments.book_appointment(
            'A1',
            'P1',
            'DR1',
            parse_date_time('2026-10-01 09:00'),
        )
        print(format_appointment(appointments.find_appointment('A1')))
    except (ValueError, LookupError) as error:
        print(f'Error: {error}')
    print('Session-only data: records are lost on exit.')


def parse_status_choice(text: str | None) -> AppointmentStatus | None:
    """Convert a user-entered status to an enum or None for all."""
    if text is None:
        return None
    value = text.strip().lower()
    if not value or value in {'all', '*'}:
        return None
    try:
        return AppointmentStatus(value)
    except ValueError as error:
        raise ValueError(
            'Use status values: scheduled, cancelled, completed or all',
        ) from error


def run_menu() -> None:
    """Stage 9: interactive menu for SmartCare session operations."""
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)

    menu = (
        '\nSmartCare menu\n'
        '1. Register patient\n'
        '2. Find patient\n'
        '3. Register practitioner\n'
        '4. Find practitioner\n'
        '5. Book appointment\n'
        '6. Cancel appointment\n'
        '7. List appointments\n'
        '8. Exit\n'
    )

    while True:
        print(menu, end='')
        try:
            choice = input('Choose an option: ').strip().lower()
        except EOFError:
            print('Input closed; exiting.')
            return

        if choice in {'8', 'exit', 'quit', 'q'}:
            print('Session ended.')
            return

        try:
            if choice in {'1', 'register patient', 'register-patient'}:
                patient_id = input('Patient ID: ').strip()
                name = input('Patient name: ').strip()
                patient = patients.register_patient(patient_id, name)
                print(f'Registered patient: {patient.patient_id} {patient.name}')
            elif choice in {'2', 'find patient', 'find-patient'}:
                patient_id = input('Patient ID: ').strip()
                patient = patients.find_patient(patient_id)
                print(f'Patient found: {patient.patient_id} {patient.name}')
            elif choice in {'3', 'register practitioner', 'register-practitioner'}:
                practitioner_id = input('Practitioner ID: ').strip()
                name = input('Practitioner name: ').strip()
                specialty = input('Specialty: ').strip()
                practitioner = practitioners.register_practitioner(
                    practitioner_id,
                    name,
                    specialty,
                )
                print(
                    'Registered practitioner: '
                    f'{practitioner.practitioner_id} '
                    f'{practitioner.name} ({practitioner.specialty})'
                )
            elif choice in {'4', 'find practitioner', 'find-practitioner'}:
                practitioner_id = input('Practitioner ID: ').strip()
                practitioner = practitioners.find_practitioner(practitioner_id)
                print(
                    'Practitioner found: '
                    f'{practitioner.practitioner_id} '
                    f'{practitioner.name} ({practitioner.specialty})'
                )
            elif choice in {'5', 'book appointment', 'book-appointment'}:
                appointment_id = input('Appointment ID: ').strip()
                patient_id = input('Patient ID: ').strip()
                practitioner_id = input('Practitioner ID: ').strip()
                date_text = input('Date/time (YYYY-MM-DD HH:MM): ').strip()
                appointment = appointments.book_appointment(
                    appointment_id,
                    patient_id,
                    practitioner_id,
                    parse_date_time(date_text),
                )
                print(f'Booked: {format_appointment(appointment)}')
            elif choice in {'6', 'cancel appointment', 'cancel-appointment'}:
                appointment_id = input('Appointment ID: ').strip()
                appointment = appointments.cancel_appointment(appointment_id)
                print(f'Cancelled: {format_appointment(appointment)}')
            elif choice in {'7', 'list appointments', 'list-appointments'}:
                practitioner_id = input('Practitioner ID: ').strip()
                status_text = input('Status (scheduled/cancelled/completed/all): ').strip()
                status = parse_status_choice(status_text)
                matches = appointments.list_practitioner_appointments(
                    practitioner_id,
                    status,
                )
                if not matches:
                    print('No appointments found.')
                else:
                    for appointment in matches:
                        print(format_appointment(appointment))
            else:
                print('Error: invalid choice')
        except (ValueError, LookupError) as error:
            print(f'Error: {error}')
