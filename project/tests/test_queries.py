"""Stage 9 tests for pure query functions and service listing."""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.queries import appointment_sort_key, select_appointments
from smartcare.services import AppointmentService, PractitionerService


def make_appointments() -> list[Appointment]:
    """Return synthetic appointments in deliberately unsorted order."""
    patient = Patient('P1', 'Alex Example')
    dr1 = Practitioner('DR1', 'Taylor Example', 'General practice')
    dr2 = Practitioner('DR2', 'Morgan Example', 'General practice')
    return [
        Appointment('A3', patient, dr1, datetime(2026, 12, 1, 11)),
        Appointment('A2', patient, dr1, datetime(2026, 12, 1, 9)),
        Appointment('A5', patient, dr2, datetime(2026, 12, 1, 8)),
        Appointment(
            'A4',
            patient,
            dr1,
            datetime(2026, 12, 1, 10),
            AppointmentStatus.CANCELLED,
        ),
        Appointment('A1', patient, dr1, datetime(2026, 12, 1, 9)),
    ]


def test_qry01_selects_only_requested_practitioner() -> None:
    """QRY-01: only DR1 is selected; DR2 is the control."""
    result = select_appointments(make_appointments(), 'DR1')
    assert {a.appointment_id for a in result} == {'A1', 'A2', 'A3', 'A4'}
    assert all(a.practitioner.practitioner_id == 'DR1' for a in result)


def test_qry02_no_status_includes_all_statuses() -> None:
    """QRY-02: omitted status includes every status."""
    result = select_appointments(make_appointments(), 'DR1', None)
    assert {a.status for a in result} == {
        AppointmentStatus.SCHEDULED,
        AppointmentStatus.CANCELLED,
    }


def test_qry02_status_filter_applies() -> None:
    """QRY-02: an explicit AppointmentStatus filter applies."""
    result = select_appointments(
        make_appointments(),
        'DR1',
        AppointmentStatus.CANCELLED,
    )
    assert [a.appointment_id for a in result] == ['A4']


def test_qry02_no_matches_returns_new_empty_list() -> None:
    """QRY-02: no matches gives a new empty list."""
    appointments = make_appointments()
    result = select_appointments(
        appointments,
        'DR1',
        AppointmentStatus.COMPLETED,
    )
    assert result == []
    assert result is not appointments


def test_qry03_orders_by_time_then_id() -> None:
    """QRY-03: ascending date/time, then appointment ID for a tie."""
    result = select_appointments(make_appointments(), 'DR1')
    assert [a.appointment_id for a in result] == ['A1', 'A2', 'A4', 'A3']


def test_qry03_source_list_and_objects_unchanged() -> None:
    """QRY-03 / FP-01: source order and object fields are unchanged."""
    appointments = make_appointments()
    original_order = list(appointments)
    original_fields = [
        (a.appointment_id, a.date_time, a.status) for a in appointments
    ]
    result = select_appointments(appointments, 'DR1')
    assert appointments == original_order
    assert [
        (a.appointment_id, a.date_time, a.status) for a in appointments
    ] == original_fields
    assert all(a in appointments for a in result)


def test_fp02_distinct_list_for_empty_and_sorted_input() -> None:
    """FP-02: a new list is returned for empty and already sorted input."""
    empty: list[Appointment] = []
    assert select_appointments(empty, 'DR1') is not empty
    sorted_input = select_appointments(make_appointments(), 'DR1')
    again = select_appointments(sorted_input, 'DR1')
    assert again == sorted_input
    assert again is not sorted_input


def test_fp03_sort_key_returns_time_then_id() -> None:
    """FP-03: the key is (date/time, ID) and is repeatable."""
    appointment = make_appointments()[0]
    assert appointment_sort_key(appointment) == (
        datetime(2026, 12, 1, 11),
        'A3',
    )
    assert appointment_sort_key(appointment) == appointment_sort_key(
        appointment,
    )


def test_fp03_sort_key_works_as_first_class_function() -> None:
    """FP-03: the key can be passed to sorted() as a function."""
    ordered = sorted(make_appointments(), key=appointment_sort_key)
    assert [a.appointment_id for a in ordered] == [
        'A5',
        'A1',
        'A2',
        'A4',
        'A3',
    ]


def test_qry04_invalid_query_inputs_raise_value_error() -> None:
    """QRY-04: blank or non-text ID and non-enum status raise ValueError."""
    appointments = make_appointments()
    with pytest.raises(ValueError):
        select_appointments(appointments, '   ')
    with pytest.raises(ValueError):
        select_appointments(appointments, None)
    with pytest.raises(ValueError):
        select_appointments(appointments, 'DR1', 'cancelled')


def test_sort_key_rejects_non_appointment() -> None:
    """The sort key rejects a value that is not an Appointment."""
    with pytest.raises(ValueError):
        appointment_sort_key('A1')


def test_qry04_service_listing_known_empty_and_unknown() -> None:
    """QRY-04: known with no matches is empty; unknown is LookupError."""
    data_store = SmartCareDataStore()
    PractitionerService(data_store).register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    service = AppointmentService(data_store)
    assert service.list_practitioner_appointments('DR1') == []
    with pytest.raises(LookupError):
        service.list_practitioner_appointments('DR99')
    with pytest.raises(ValueError):
        service.list_practitioner_appointments('   ')