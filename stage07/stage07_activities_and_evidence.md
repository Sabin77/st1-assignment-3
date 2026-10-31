# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | Register a patient with a valid unused ID and verify the same object is stored. | Register another patient with an existing ID and verify rejection. | Successful lookup returns the registered object; duplicate registration raises ValueError and does not replace it. |
| FR-05 Prevent practitioner conflict | Book another practitioner at the same datetime and verify that booking succeeds. | Book the same practitioner at the exact datetime while an appointment is SCHEDULED. | Different practitioner booking succeeds; conflicting booking raises ValueError and original appointment remains unchanged. |
| FR-06 Cancel appointment | Cancel a SCHEDULED appointment. | Cancel the same appointment again. | The same object changes to CANCELLED; repeated cancellation raises ValueError and status remains CANCELLED. |
| FR-07 Retain cancelled history | Cancel an appointment and retrieve it through lookup and list operations. | Check the possible loss of the cancelled appointment from history. | Lookup returns the same cancelled object and the appointment remains in the stored list; a missing record would fail the test. |

### Activity 2 Strong or weak assertion

`assert True`
Judgement: Weak/unclear. It only establishes that execution reached the statement; it checks no required result.

`assert appointment is not None`
Judgement: Weak/unclear for cancellation or booking correctness. It only shows an object exists, not its identity, status or storage.

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: Strong for the cancellation status transition. It verifies CANCELLED status, but alone does not prove retained history or object identity.

`assert len(results) > 0`
Judgement: Weak/unclear for retained history. It proves only that the collection is nonempty, not that the expected cancelled appointment remains.

`assert data_store.find_appointment('A1') is appointment`
Judgement: Strong for retention and identity. It verifies the same appointment is retrievable by ID, but should be paired with a CANCELLED status check.



### Activity 3 Boundary thinking

- Blank identifier: use an empty or whitespace-only required ID; expect ValueError under the required-text validation contract.
- Whitespace-only name: provide a name containing spaces only; expect ValueError because required names cannot be blank after trimming.
- Same-time practitioner booking: book a SCHEDULED appointment, then try booking the same practitioner at the exact datetime; expect ValueError and unchanged existing state under FR-05.
- Cancelled appointment: cancel a SCHEDULED appointment, then verify that the same object remains available through lookup and listing under FR-07.
- Invalid status transition: try to cancel an already CANCELLED or COMPLETED appointment; expect ValueError with the original status preserved under FR-06.
### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 Ã¢â‚¬â€ Non-None assertion | Object existence does not prove correct registration or identity. | Register a patient and assert the store returns the same registered Patient object. |
| 2 Ã¢â‚¬â€ Non-None assertion | An appointment may exist but have the wrong state or participants. | Book an appointment and assert its scheduled status and registered participant identities. |
| 3 Ã¢â‚¬â€ assert True | It cannot detect incorrect behaviour because the assertion always succeeds. | Cancel a scheduled appointment and assert its status becomes CANCELLED. |
| 4 Ã¢â‚¬â€ SMS notification assumption | SMS notifications are outside SmartCare's stated requirements. | Test the documented booking or cancellation result instead of invented notification behaviour. |
| 5 Ã¢â‚¬â€ SMS notification assumption | Passing an SMS-related test would not verify FR-01, FR-05, FR-06 or FR-07. | Check that a cancelled appointment remains retrievable in current-session history. |


### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?

100% code coverage only shows that the measured code executed. Tests can execute every line while using weak assertions, incorrect expectations or missing important scenarios. Therefore, complete coverage does not establish that the application satisfies its requirements.

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| FR-01 | AC-01.1 Ã¢â‚¬â€ valid patient registration | TEST-01 | Positive / Service | tests/test_services.py::test_register_patient_stores_same_object | A valid unused patient ID registers and stores the same object. | Planned Ã¢â‚¬â€ not executed | Student-authored |
| FR-01 | AC-01.2 Ã¢â‚¬â€ duplicate patient ID | TEST-02 | Negative / Service | tests/test_services.py::test_duplicate_patient_id_preserves_original | Duplicate ID raises ValueError and the original record remains unchanged. | Planned Ã¢â‚¬â€ not executed | Student-authored |
| FR-05 | AC-04.2 Ã¢â‚¬â€ different practitioner at same time | TEST-03 | Positive / Service | tests/test_services.py::test_different_practitioner_same_time_allowed | A different practitioner can be booked at the exact same time. | Planned Ã¢â‚¬â€ not executed | Student-authored |
| FR-05 | AC-04.1 Ã¢â‚¬â€ same practitioner exact-time conflict | TEST-04 | Negative / Service | tests/test_services.py::test_same_practitioner_same_time_rejected | A conflicting scheduled booking raises ValueError without changing existing state. | Planned Ã¢â‚¬â€ not executed | Student-authored |
| FR-06 | AC-05.1 Ã¢â‚¬â€ cancellation | TEST-05 | Positive / Service | tests/test_services.py::test_stage7_cancel_changes_status | Cancelling a scheduled appointment sets status to CANCELLED. | Planned Ã¢â‚¬â€ not executed | Student-authored |
| FR-06 | AC-05.3 Ã¢â‚¬â€ repeated cancellation | TEST-06 | Negative / Service | tests/test_services.py::test_stage7_repeated_cancel_preserves_status | Repeated cancellation raises ValueError and preserves CANCELLED status. | Planned Ã¢â‚¬â€ not executed | Student-authored |
| FR-07 | AC-05.2 Ã¢â‚¬â€ retained cancelled history | TEST-07 | Positive / Service | tests/test_services.py::test_stage7_cancelled_appointment_retained | The same cancelled appointment remains retrievable in current-session history. | Planned Ã¢â‚¬â€ not executed | Student-authored |
| FR-01 | Revision 2 required-field validation contract | TEST-08 | Negative / Domain | tests/test_domain.py::test_blank_patient_id_is_rejected | Whitespace-only patient ID raises ValueError. | Planned Ã¢â‚¬â€ not executed | Student-authored |
| FR-06 | Appointment domain transition contract | TEST-09 | Positive / Domain | tests/test_domain.py::test_domain_cancel_changes_status | Appointment.cancel changes SCHEDULED to CANCELLED. | Planned Ã¢â‚¬â€ not executed | Student-authored |
| FR-06 | Appointment domain transition contract | TEST-10 | Negative / Domain | tests/test_domain.py::test_domain_repeated_cancel_rejected | Repeated domain cancellation raises ValueError and keeps CANCELLED status. | Planned Ã¢â‚¬â€ not executed | Student-authored |
| FR-04 | Appointment construction contract | TEST-11 | Positive / Domain | tests/test_domain.py::test_new_appointment_starts_scheduled | A newly constructed appointment starts SCHEDULED. | Planned Ã¢â‚¬â€ not executed | Student-authored |
## C Test Design


| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| TEST-01 | FR-01 | AC-01.1 | Positive | Register valid unused patient ID | Same patient object is stored and retrievable | Tests storage identity and registration |
| TEST-02 | FR-01 | AC-01.2 | Negative | Register duplicate patient ID | ValueError; original object and record count unchanged | Tests rejection without overwriting |
| TEST-03 | FR-05 | AC-04.2 | Positive | Book different practitioner at exact same time | Both appointments stored and scheduled | Confirms conflict is practitioner-specific |
| TEST-04 | FR-05 | AC-04.1 | Negative | Book same practitioner at exact same time | ValueError; no second appointment stored | Confirms conflict and unchanged state |
| TEST-05 | FR-06 | AC-05.1 | Positive | Cancel a scheduled appointment | CANCELLED status on original object | Existing Stage 6 evidence; not claimed as a new test |
| TEST-06 | FR-06 | AC-05.3 | Negative | Cancel an already-cancelled appointment | ValueError; CANCELLED status retained | Existing Stage 6 evidence |
| TEST-07 | FR-07 | AC-05.2 | Positive | Retrieve cancelled appointment | Same object found and present in history | Existing Stage 6 evidence |
| TEST-08 | FR-01 | Revision 2 required-text contract | Boundary | Whitespace-only patient ID | ValueError | Domain validation |
| TEST-09 | FR-06 | Domain transition contract | Positive | Cancel scheduled domain appointment | Status changes to CANCELLED | Domain operation independently verified |
| TEST-10 | FR-06 | Domain transition contract | Negative | Repeat domain cancellation | ValueError and CANCELLED remains | Illegal transition independently verified |
| TEST-11 | FR-04 | Appointment construction contract | Positive | Construct appointment without explicit status | Starts SCHEDULED | Constructor default independently verified |
| TEST-12 | FR-05 | AC-04.1 | Negative | Same practitioner/time with different patient | ValueError; rejected record absent | Human-reviewed Copilot idea, patient identity boundary |
| TEST-13 | FR-05 | AC-04.1 | Boundary | Same practitioner one minute later | Both appointments stored as SCHEDULED | Human-reviewed Copilot idea, exact-time boundary |
| TEST-14 | FR-05 / FR-07 | AC-04.1 / AC-05.2 | Boundary | Rebook cancelled slot | New SCHEDULED record stored and old CANCELLED record retained | Human-modified Copilot idea, status filtering |

## D Arrange Act Assert Record


| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| TEST-01 | Fresh store and PatientService | Register P1 | Stored lookup is the same patient; list contains it | Checks actual persistence in current session |
| TEST-02 | Existing registered P1 | Register another P1 | ValueError; original identity and count unchanged | Detects overwriting or mutation |
| TEST-03 | Registered patient and two practitioners | Book DR1 and DR2 at same time | Both distinct appointments stored | Checks practitioner-specific restriction |
| TEST-04 | Existing scheduled DR1 appointment | Book DR1 at identical time | ValueError; original only; A2 absent | Checks conflict and no partial insertion |
| TEST-05 | Scheduled appointment | Cancel A1 | Returned object is original; status CANCELLED | Verifies service transition |
| TEST-06 | Cancelled appointment | Cancel again | ValueError; status unchanged | Verifies illegal transition |
| TEST-07 | Cancelled appointment stored | Lookup A1 and list history | Same cancelled object retained | Verifies cancellation does not delete |
| TEST-08 | Whitespace-only patient ID | Construct Patient | ValueError | Checks required-text boundary |
| TEST-09 | Scheduled domain appointment | Call cancel() | CANCELLED status | Verifies domain transition |
| TEST-10 | Cancelled domain appointment | Call cancel() again | ValueError; state unchanged | Verifies transition guard |
| TEST-11 | Valid participants and datetime | Construct Appointment | Status SCHEDULED | Verifies default initial state |
| TEST-12 | Two registered patients and scheduled DR1 booking | Book different patient with DR1 at same time | ValueError; original retained; new ID absent | Detects incorrect patient-dependent conflicts |
| TEST-13 | Two patients and DR1 | Book at 09:00 then 09:01 | Both stored and SCHEDULED | Detects overly broad time conflict |
| TEST-14 | Cancelled DR1 appointment | Book DR1 at cancelled time | Replacement SCHEDULED; previous CANCELLED retained | Verifies status filtering and retained history |

## E Domain Test Evidence


| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| TEST-08 | Blank patient ID | tests/test_domain.py::test_blank_patient_id_is_rejected | Passed |
| TEST-09 | Scheduled to CANCELLED transition | tests/test_domain.py::test_domain_cancel_changes_status | Passed |
| TEST-10 | Repeated cancellation rejected | tests/test_domain.py::test_domain_repeated_cancel_rejected | Passed |
| TEST-11 | New appointment starts SCHEDULED | tests/test_domain.py::test_new_appointment_starts_scheduled | Passed |
| Additional domain evidence | Patient trimming, blank name, practitioner fields, participant identity, completed cancellation guard, invalid datetime/participants/status | project/tests/test_domain.py | 17 domain cases passed in 0.11-second full suite |

## F Service Test Evidence


| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| TEST-01 | Patient stored and retrievable | FR-01 / AC-01.1 | tests/test_services.py::test_stage7_register_patient_stores_same_object | Passed |
| TEST-02 | Duplicate patient does not overwrite original | FR-01 / AC-01.2 | tests/test_services.py::test_stage7_duplicate_patient_preserves_original | Passed |
| TEST-03 | Different practitioner at same time allowed | FR-05 / AC-04.2 | tests/test_services.py::test_stage7_different_practitioner_same_time_allowed | Passed |
| TEST-04 | Exact-time practitioner conflict | FR-05 / AC-04.1 | tests/test_services.py::test_stage7_same_practitioner_exact_time_conflict_preserves_store | Passed |
| TEST-05 | Cancel scheduled appointment | FR-06 / AC-05.1 | tests/test_services.py::test_cancel_scheduled_returns_same_cancelled_object | Passed Ã¢â‚¬â€ supplied Stage 6 test |
| TEST-06 | Reject repeated cancellation | FR-06 / AC-05.3 | tests/test_services.py::test_cancel_twice_raises_value_error | Passed Ã¢â‚¬â€ supplied Stage 6 test |
| TEST-07 | Retain cancelled appointment history | FR-07 / AC-05.2 | tests/test_services.py::test_cancelled_appointment_is_retained_in_history | Passed Ã¢â‚¬â€ supplied Stage 6 test |
| TEST-12 | Different-patient practitioner conflict | FR-05 / AC-04.1 | tests/test_services.py::test_stage7_conflict_with_different_patient_preserves_store | Passed |
| TEST-13 | Different-minute booking accepted | FR-05 / AC-04.1 | tests/test_services.py::test_stage7_same_practitioner_different_minute_allowed | Passed |
| TEST-14 | Cancelled slot rebooked with history retained | FR-05 / AC-04.1; FR-07 / AC-05.2 | tests/test_services.py::test_stage7_cancelled_slot_can_be_rebooked_with_history_retained | Passed |
| Additional Stage 7 service evidence | Duplicate practitioner, booking identity, duplicate appointment ID and unknown participants | Relevant test_stage7_* functions in project/tests/test_services.py | Passed |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| Required patient identifier | Whitespace-only ID | ValueError; no patient created | TEST-08 |
| Patient registration | Duplicate ID P1 | ValueError; original object unchanged | TEST-02 |
| Practitioner booking conflict | Same practitioner, identical datetime | ValueError; rejected appointment absent | TEST-04 |
| Practitioner booking conflict | Different patient, same practitioner/time | ValueError; existing booking unchanged | TEST-12 |
| Exact datetime boundary | Same practitioner at 09:00 and 09:01 | Both bookings permitted at minute precision | TEST-13 |
| Cancelled history / conflict | Book at same datetime after cancellation | Replacement scheduled; previous cancelled record retained | TEST-14 |
| Appointment transition | Cancel already CANCELLED appointment | ValueError; status remains CANCELLED | TEST-10 |
| Completed appointment transition | Cancel COMPLETED appointment | ValueError; status remains COMPLETED | Additional domain evidence |
| Participant validation | Unknown patient or practitioner | LookupError; no appointment inserted | Additional service evidence |
| Appointment datetime validation | String, second precision or timezone-aware datetime | ValueError | Additional domain evidence |

## H GitHub Copilot Test Design

Requirement: FR-05 Ã¢â‚¬â€ Prevent practitioner booking conflicts.

Acceptance criterion: AC-04.1 Ã¢â‚¬â€ A practitioner must not have two SCHEDULED appointments at the exact same date and time.

Behaviour to test: Booking conflict detection must depend on the practitioner, exact datetime and SCHEDULED status, while rejected operations must leave stored records unchanged.

Human-first test idea/categories: Before requesting Copilot suggestions, I designed and implemented test_stage7_same_practitioner_exact_time_conflict_preserves_store. It books an appointment, attempts a conflicting second booking for the same practitioner and exact datetime, expects ValueError, and checks that the original appointment remains scheduled and no second appointment is stored. I also designed a positive comparison test allowing different practitioners at the same datetime.

Prompt and purpose: Asked GitHub Copilot Chat to suggest positive, negative and boundary test ideas for AC-04.1 without duplicating existing tests, inventing requirements or modifying code.

- Copilot test idea/candidate: Candidate 1 Ã¢â‚¬â€ Same practitioner and datetime, but a different patient.
- What it claims to verify: Conflict rejection is based on practitioner and datetime, regardless of patient identity; rejected booking does not mutate the store.
- Requirement trace: FR-05 / AC-04.1.
- Assertion quality: Strong if the exception, original object/status, list length and absence of the second appointment are all checked.
- Human critique: Copilot incorrectly called this a positive test; it is a negative test. It adds useful coverage because the existing human test used the same patient for both bookings.
- Decision: Accept as a new negative test idea, subject to implementation and execution.
- Reason: Detects implementations that incorrectly use patient identity in conflict detection.
- Final test reference if accepted/modified: Planned Ã¢â‚¬â€ tests/test_services.py::test_stage7_conflict_with_different_patient_preserves_store.
- Actual verification result: Not executed yet.

- Copilot test idea/candidate: Candidate 2 Ã¢â‚¬â€ Same practitioner at a different minute.
- What it claims to verify: Two SCHEDULED appointments for the same practitioner are allowed when datetimes differ.
- Requirement trace: FR-05 / AC-04.1, exact-time conflict boundary.
- Assertion quality: Strong if both appointment objects are stored with the intended distinct times and remain SCHEDULED.
- Human critique: Useful complementary behaviour. The exact minute difference matters because the domain supports minute-precision datetimes, not duration-based overlap rules.
- Decision: Accept as a new boundary test idea, subject to implementation and execution.
- Reason: Detects an overly broad implementation that rejects every subsequent booking for a practitioner.
- Final test reference if accepted/modified: Planned Ã¢â‚¬â€ tests/test_services.py::test_stage7_same_practitioner_different_minute_allowed.
- Actual verification result: Not executed yet.

- Copilot test idea/candidate: Candidate 3 Ã¢â‚¬â€ Cancelled appointment does not block a new booking at the same time.
- What it claims to verify: Only SCHEDULED appointments create practitioner conflicts.
- Requirement trace: FR-05 / AC-04.1 and FR-06 / AC-05.1.
- Assertion quality: Strong if both retained cancelled history and the newly stored SCHEDULED appointment are verified.
- Human critique: Valuable status boundary; the cancellation must remain in the store, not be deleted to make the test pass.
- Decision: Modify and retain as a new boundary test idea, subject to implementation and execution.
- Reason: Strengthen Copilot's suggested assertions by checking both the original CANCELLED appointment remains stored and the replacement booking succeeds.
- Final test reference if accepted/modified: Planned Ã¢â‚¬â€ tests/test_services.py::test_stage7_cancelled_slot_can_be_rebooked_with_history_retained.
- Actual verification result: Not executed yet.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak?

Candidate 1, involving a different patient and the same practitioner/time.

Why was it weak?

Its basic exception assertion did not by itself establish that a failed booking left the store unchanged. Copilot also incorrectly called this a positive test even though it verifies rejection.

How did you strengthen it?

I checked the original appointment identity, retained SCHEDULED status, unchanged appointment list and absence of the rejected appointment ID.

Accepted / modified / rejected test decisions and evidence: Candidates 1 and 2 accepted; candidate 3 modified to check retained cancelled history. The three human-reviewed test implementations are in project/tests/test_services.py and passed in the 52-test full suite.

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|-----|--------|---|---|---|
| `py -m pytest` | `project/` | `ec5cbf78fb033fcc4234a4120a345e1e4df94af9` | 24 | 0 | None Ã¢â‚¬â€ all tests passed | No defects identified in this run | Stage 7 baseline: 24 tests passed in 0.29 seconds using Python 3.13.3 and pytest 8.3.5. This confirms the integrated Stage 6 regression tests passed before adding Stage 7 tests. |
| `py -m pytest` | `project/` | Local Stage 7 working tree; SHA pending commit | 49 | 0 | None Ã¢â‚¬â€ all tests passed | No defects identified in this run | 17 domain, 24 service and 8 starter tests passed in 0.13 seconds using Python 3.13.3 and pytest 8.3.5. |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement Ã¢â€ â€™ test Ã¢â€ â€™ failure/observation Ã¢â€ â€™ diagnosis Ã¢â€ â€™ change Ã¢â€ â€™ verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? The tests verify selected domain, service and current-session storage behaviours. They do not establish full user-interface usability, performance, security or cross-session persistence. Stage 9 practitioner appointment listing is not implemented in the current services.py and is outside this Stage 7 verification.

Coverage if used: Not measured.

Which uncovered areas matter, and why does coverage percentage alone not establish correctness? Additional combinations of invalid inputs, unexpected failures and integration behaviours may remain untested. Even 100% statement coverage can pass with weak assertions or incorrect requirements; coverage shows execution, not correct outcomes.

Optional fixtures/parametrisation used and why, if any: pytest.mark.parametrize was used in test_domain.py to verify several invalid required-field and datetime cases concisely. Fresh store setup helper functions keep service tests isolated.

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| Stage 7 domain and service testing | `feature/stage07-testing` | Pending | Pending teammate review | 17 domain tests and 11 additional service tests implemented; full suite passed | 52 passed, 0 failed; PR pending |
| Stage 7 Copilot test review | `feature/stage07-testing` | To be included in Stage 7 PR | Human review by Sabin; independent teammate review pending | Accepted two test ideas and modified one; strengthened assertions to verify unchanged state and retained history | Three human-reviewed tests passed |
| Stage 7 evidence and traceability | `feature/stage07-testing` | To be included in Stage 7 PR | Pending | Documented test design, acceptance-criterion mapping, Copilot critique and regression results | Evidence prepared; integration pending |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| Sabin | Created `test_domain.py`, implemented 17 domain test cases, extended `test_services.py` with 11 service test cases, performed regression testing, reviewed Copilot suggestions, strengthened test assertions, and prepared Stage 7 testing evidence. | `project/tests/test_domain.py`; `project/tests/test_services.py`; Section H and J of this record |
| Other group members | Add only contributions actually completed or reviewed during Stage 7. | Add relevant GitHub commits, PR comments or review links when available |

## N Formative Questions

1. What question does verification answer?
Are we building the software correctly according to its specified requirements and contracts?

2. What question does validation answer?
Are we building the right software for its intended users and needs?

3. What is a unit test?
An automated test of one small, independently checkable behaviour, such as a domain validation or state transition.

4. What is a pytest fixture?
A reusable setup mechanism that supplies test data or resources to tests, often with a fresh state for isolation.

5. What is parametrisation in pytest?
Running one test function against multiple input and expected-result combinations using pytest.mark.parametrize.

6. What is regression testing?
Rerunning previous tests after changes to check that previously working behaviour still works.

7. What does code coverage tell us, and what does it not prove?
It measures which code was executed during tests. It does not prove assertions are strong, requirements are complete or results are correct.

8. What makes an assertion weak?
It checks something too general or irrelevant, so a defective implementation could still pass, such as assert True.

9. What is the appropriate role of GitHub Copilot as a test assistant?
It may suggest candidate tests and edge cases, but humans must check requirement traceability, assertions, existing contracts and real test results before accepting its output.

10. What is the Stage 7 engineering rule?
Design tests from actual requirements, check observable outcomes and preserve regression evidence; human review determines whether generated tests are valid.

## O Stage Completion

Tested Stage 7 main SHA: Pending Ã¢â‚¬â€ Stage 7 has not yet been merged into main.

Full-suite result: 52 passed, 0 failed, in 0.11 seconds on local branch feature/stage07-testing (Python 3.13.3, pytest 8.3.5).

Unresolved defects and effect on baseline: None identified in the executed 52-test regression suite. This does not establish that the application is defect-free.

Clean working tree and integration evidence: Pending. Stage 7 changes have been staged locally but not yet committed, reviewed or merged. Local PyCharm configuration file .idea/SmartCare_Starter.iml is modified and intentionally excluded from the Stage 7 commit.

Stage 8 handover status: Pending successful Stage 7 review, merge and verification on main. No Stage 8 work is claimed in this record.

All tutorial/formative responses and traceability/Copilot decisions complete: Sections AÃ¢â‚¬â€œN prepared; final check required before submission.
