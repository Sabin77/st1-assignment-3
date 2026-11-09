"""Stage 9 end-to-end console workflow tests (UI-01, UI-02)."""

import pytest

from smartcare.console import run_menu


REGISTER = [
    '1', 'P1', 'Alex Example',
    '3', 'DR1', 'Taylor Example', 'General practice',
]
BOOK_A1 = ['5', 'A1', 'P1', 'DR1', '2026-12-01 09:00']
SCHEDULED_A1 = 'A1: P1 with DR1, 2026-12-01 09:00, scheduled'
CANCELLED_A1 = 'A1: P1 with DR1, 2026-12-01 09:00, cancelled'


def run_session(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    answers: list[str],
) -> str:
    """Run the menu with scripted answers and return everything printed."""
    remaining = iter(answers)

    def fake_input(prompt: str = '') -> str:
        try:
            return next(remaining)
        except StopIteration:
            raise EOFError from None

    monkeypatch.setattr('builtins.input', fake_input)
    run_menu()
    return capsys.readouterr().out


def test_ui01_full_session_register_book_cancel_list(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """UI-01: one session registers, books, lists, cancels and keeps history."""
    output = run_session(
        monkeypatch,
        capsys,
        REGISTER + BOOK_A1
        + ['7', 'DR1', '']
        + ['6', 'A1']
        + ['7', 'DR1', '']
        + ['8'],
    )
    assert 'Registered patient: P1 Alex Example' in output
    assert 'Registered practitioner: DR1 Taylor Example (General practice)' in output
    assert output.count(SCHEDULED_A1) == 2
    assert output.count(CANCELLED_A1) == 2
    assert output.rstrip().endswith('Session ended.')


def test_ui01_find_patient_and_practitioner(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """UI-01: registered patient and practitioner can be looked up."""
    output = run_session(
        monkeypatch,
        capsys,
        REGISTER + ['2', 'P1', '4', 'DR1', '8'],
    )
    assert 'Patient found: P1 Alex Example' in output
    assert 'Practitioner found: DR1 Taylor Example (General practice)' in output


def test_ui01_conflict_rejected_without_partial_state(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """UI-01 / UI-02: a conflicting booking is rejected and not stored."""
    output = run_session(
        monkeypatch,
        capsys,
        REGISTER + BOOK_A1
        + ['5', 'A2', 'P1', 'DR1', '2026-12-01 09:00']
        + ['7', 'DR1', '']
        + ['8'],
    )
    assert (
        'Error: Practitioner already has a SCHEDULED appointment at this time'
        in output
    )
    assert 'A2:' not in output


def test_ui01_status_filter_in_listing(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """UI-01: listing applies the status filter typed by the user."""
    output = run_session(
        monkeypatch,
        capsys,
        REGISTER + BOOK_A1
        + ['6', 'A1']
        + ['7', 'DR1', 'scheduled']
        + ['7', 'DR1', 'cancelled']
        + ['8'],
    )
    assert 'No appointments found.' in output
    assert output.count(CANCELLED_A1) == 2


def test_ui02_invalid_menu_choice_recovers(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """UI-02: an invalid menu choice shows an error and the menu continues."""
    output = run_session(monkeypatch, capsys, ['9', '8'])
    assert 'Error: invalid choice' in output
    assert output.rstrip().endswith('Session ended.')


def test_ui02_invalid_date_time_leaves_no_appointment(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """UI-02: a badly formatted date/time is rejected with no partial state."""
    output = run_session(
        monkeypatch,
        capsys,
        REGISTER
        + ['5', 'A1', 'P1', 'DR1', '01/12/2026']
        + ['7', 'DR1', '']
        + ['8'],
    )
    assert 'Error: Use date/time format YYYY-MM-DD HH:MM' in output
    assert 'No appointments found.' in output


def test_ui02_unknown_participant_leaves_no_appointment(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """UI-02: booking for an unknown patient is rejected with no partial state."""
    output = run_session(
        monkeypatch,
        capsys,
        ['3', 'DR1', 'Taylor Example', 'General practice']
        + ['5', 'A1', 'P9', 'DR1', '2026-12-01 09:00']
        + ['7', 'DR1', '']
        + ['8'],
    )
    assert 'Error: Patient not found' in output
    assert 'No appointments found.' in output


def test_ui02_invalid_status_text_recovers(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """UI-02: an unknown status word gives a helpful error."""
    output = run_session(
        monkeypatch,
        capsys,
        REGISTER + ['7', 'DR1', 'urgent', '8'],
    )
    assert (
        'Error: Use status values: scheduled, cancelled, completed or all'
        in output
    )


def test_ui02_repeated_cancellation_rejected(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """UI-02: cancelling twice is rejected and the first cancel stands."""
    output = run_session(
        monkeypatch,
        capsys,
        REGISTER + BOOK_A1 + ['6', 'A1', '6', 'A1', '8'],
    )
    assert 'Error: Only SCHEDULED appointments may be cancelled' in output
    assert output.count(CANCELLED_A1) == 1


def test_ui02_duplicate_patient_keeps_original(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """UI-02: a duplicate registration is rejected and the original is kept."""
    output = run_session(
        monkeypatch,
        capsys,
        ['1', 'P1', 'Alex Example', '1', 'P1', 'Replacement', '2', 'P1', '8'],
    )
    assert 'Error: Patient ID already exists' in output
    assert 'Patient found: P1 Alex Example' in output
    assert 'P1 Replacement' not in output


def test_ui02_unknown_patient_lookup_recovers(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """UI-02: looking up an unknown patient shows an error, not a crash."""
    output = run_session(monkeypatch, capsys, ['2', 'ZZZ', '8'])
    assert 'Error: Patient not found' in output
    assert output.rstrip().endswith('Session ended.')


def test_closed_input_exits_cleanly(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Closed input (end of file) exits the menu without a crash."""
    output = run_session(monkeypatch, capsys, [])
    assert 'Input closed; exiting.' in output

