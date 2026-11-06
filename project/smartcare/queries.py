"""Stage 9 contracts for pure collection processing."""


from datetime import datetime

from smartcare.domain import Appointment, AppointmentStatus, required_text


def appointment_sort_key(appointment: Appointment) -> tuple[datetime, str]:
    """Return the date/time and appointment ID ordering key without side
    effects.
    """
    if not isinstance(appointment, Appointment):
        raise ValueError('Appointment key requires an Appointment object')
    return (appointment.date_time, appointment.appointment_id)


def select_appointments(
    appointments: list[Appointment],
    practitioner_id: str,
    status: AppointmentStatus | None = None,
) -> list[Appointment]:
    """Return a new list for this practitioner, optionally filtered by
    status.

    Order by date/time then appointment ID using appointment_sort_key.
    Do not mutate the source list/objects or perform input/output.
    """
    if not isinstance(practitioner_id, str):
        raise ValueError('Practitioner ID must be a string')
    required_text(practitioner_id, 'Practitioner ID')
    if status is not None and not isinstance(status, AppointmentStatus):
        raise ValueError('Status must be an AppointmentStatus value or None')

    matching = [
        appointment
        for appointment in appointments
        if appointment.practitioner.practitioner_id == practitioner_id
        and (status is None or appointment.status is status)
    ]
    return sorted(matching, key=appointment_sort_key)
