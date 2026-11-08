# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: Tuesday 1:30 PM
Members and UG/PG cohorts: Stanley Campbell, Shaban Mohseni,Nhat Minh Le,Sabin Lamichhane
Record owner / contribution links for each member: [complete]

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements

For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.

- Appointment disappears after cancellation.
- The data-store removal path is probably being called.
- The failing test shows store.find_appointment('A1') returns None.
- The service layer is badly designed.
- Traceback points to smartcare/services.py line 42 in the example.
  The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

Response and reason: [complete]

### A.2 Build a debugging record

Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Response and reason: 
- Chosen scenario: cancelled-history
- Expected behaviour: After `appointment_service.cancel_appointment('A1')`, `appointment_service.find_appointment('A1')` returns the same appointment object, now with status CANCELLED. A second cancel is rejected with `ValueError`, and `data_store.find_appointment('A1')` still returns the record.

- Observed behaviour: 
`find_appointment('A1')` raises `LookupError: Appointment not found` right after the cancel,
`test_cancel_twice_raises_value_error` fails with the same `LookupError`,
`test_stage7_cancelled_slot_can_be_rebooked_with_history_retained` shows `store.find_appointment("A1")` returning `None`.

- Minimal reproduction: 
```
python
data_store, appointment_service, appointment = appointment_setup()
appointment_service.cancel_appointment('A1')
appointment_service.find_appointment('A1')
```

Command: python -m pytest -q tests/test_services.py::test_cancelled_appointment_is_retained_in_history

- Hypothesis: `cancel_appointment` removes the appointment from the data store instead of only setting its status to CANCELLED, so later lookups return `None`.

- Evidences: the body of `cancel_appointment` in `smartcare/services.py`. Inspect whether it sets the status to CANCELLED  , or removes the appointment from the database.

### A.3 Test defect or product defect

A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason: Change the test that expects deletion, because it contradicts FR-07 (history must be retained). The code’s retain-and-mark-CANCELLED behaviour is the requirement. A test expecting different practitioners at the same time to conflict does not reflect AC-04.2, which defines conflicts per practitioner, so that test should be corrected, not the code.

### A.4 Refactoring smell hunt

Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.

Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. 

Explain the behaviour that must remain unchanged.

Response and reason: 
- Smell and refactorings
+ Duplicate status strings: Replace them with the existing `AppointmentStatus` enum. Stored status values and conflict and cancellation outcomes must stay the same.
+ Direct collection manipulation: Move that behind the existing `SmartCareDataStore` methods such as `find_appointment` and `has_practitioner_conflict`, without adding new architecture. The same records must be stored, found and returned.
+ Printing inside business logic: Remove the `print` or move it to the caller, and rely on return values or exceptions instead. The return value and raised exceptions must not change.
+ Validation mixed with logic: Extract validation into a helper that runs first. The same `ValueError` and `LookupError` types and conditions must apply.
+ Four nested conditionals: Use guard clauses and flatten the conditions. Every input must still take the same path to the same outcome.

- Classifying the proposed changes
+ Rename appt to appointment: refactoring. Only readability changes, with no behaviour change.
+ Extract a repeated conflict helper: refactoring. Same checks and same results, just without duplication.
+ Add rescheduling: feature. It adds new behaviour that did not exist, so it needs new requirements and tests.
+ Restore retained cancellation lookup: repair. Current behaviour violates FR-07, so behaviour does change, to match the requirement.
+ Replace a magic status string with the existing enum: refactoring. Same value with a safer representation. The enum’s value must equal the old string if it is stored or compared externally.

- Behaviour that must remain unchanged:
+ Public method signatures and return values.
+ Which exceptions are raised, with which types, for which inputs: `ValueError` for invalid input, duplicate IDs and conflicts, and `LookupError` for missing participants.
+ Conflict rules from AC-04.2.
+ Cancelled appointments stay stored with status CANCELLED.
+ Tests that currently pass must still pass.


### A.5 Traceback and hypothesis ranking

Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason:

- Failure chosen: `test_cancelled_appointment_is_retained_in_history`
+ Exception/assertion: `LookupError('Appointment not found')`, raised before `assert` could compare anything.
+ Expected: `find_appointment('A1')` returns the same appointment object, now with status CANCELLED.
+ Observed: `LookupError`. The stage 7 test shows the underlying store returning `None` for `A1` after a cancel.
+ Test line: `tests\test_services.py:147`, `assert appointment_service.find_appointment('A1')` is appointment.
+ Call path: the test calls `cancel_appointment('A1')`, which succeeds. It then calls `AppointmentService.find_appointment('A1')`, which calls `data_store.find_appointment('A1')`. That returns `None`, so `services.py:136` `raises LookupError`.
+ Requirement: FR-07

- Plausible causes
+ `SmartCareDataStore.find_appointment` hides `CANCELLED` records. The first cancel succeeded, so the record existed. The project has no public delete operation, which makes filtering at lookup more likely than deletion.
   Check: read the store’s find_appointment, then print the store’s internal appointment collection right after the cancel. If 'A1' is still in it, this is the cause.
+ `cancel_appointment` removes the record. This is your original hypothesis, and it fits because the record is gone after the cancel.
   Check: print the collection before and after the cancel. If 'A1' is absent afterward and was present before, it was removed, which rules out cause 1.
+ The record is still stored, but under a different key. For example, the key was altered or normalised during cancellation. This fits least, because nothing in the output hints at a key change.
   Check: compare the collection’s keys and its length before and after the cancel. If the length is unchanged but 'A1' is not a key, this is the cause.

- Why a traceback alone doesn’t establish the cause:
+ The faulty step happened earlier, inside the cancel or the store, and that part never appears in the traceback.

### A.6 Exit question

Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: Because it might lead to changing the wrong code. For example, the `LookupError` at `line 136` is correct behaviour. Editing that line would hide the problem while the real cause stays.

Classification responses (1–5, each with reason): [complete]
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: [complete]
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: [complete]

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: SHA 5518a276c258c50d100ba0550af72367599cdf37
- Baseline test command / working directory / observed result / evidence: `python -m pytest -q`,  `...\st1-assignment-3\project`, result 7 failed, 45 passed in 0.22s. Key failures: the cancelled-history tests and the stage 7 / starter conflict tests.
- Clean preparation SHA if a record-only commit followed Stage 7: [complete]
- Branch and preparer / how teammates obtained this branch: [complete]
- Downloaded tool version, source SHA256 and --check outcome: [complete]
- --apply and --verify output summaries / artefact references: [complete]
- Bounded diff inspected and recovery location (not committed): [complete]
- Prepared faulty-state commit SHA: [complete]
- Preparation or recovery issues and resolution, if any: [complete]
- Initial prepared full-suite command / result / key failures: [complete]

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: After cancel_appointment('A1'), find_appointment('A1') raises LookupError: Appointment not found, and the data store’s find_appointment('A1') returns None. The appointment disappears after cancellation.
- Expected behaviour and requirement: The appointment stays stored with status CANCELLED and can still be found and listed. Requirement: FR-07 (history must be retained). Check the exact wording in your spec.
- Minimal synthetic reproduction steps: 
+ Create a data store, an `AppointmentService`, and an appointment A1.
+ Call `cancel_appointment('A1')`.
+ Call `find_appointment('A1')`. Expected: the appointment. Observed: `LookupError`.
- Meaningful failing test path/name and exact relevant failure: 
`tests/test_services.py::test_cancelled_appointment_is_retained_in_history`, failing at `tests\test_services.py:147` with `LookupError: Appointment not found raised from smartcare\services.py:136.`
- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence: `cancel_appointment` only calls `appointment.cancel()` and does not delete. `SmartCareDataStore.find_appointment` skips appointments whose status is "cancelled", so it returns `None` and the service raises `LookupError`. Evidence: inspected both methods in services.py and data_store.py
- Smallest justified fix / diff / why other behaviour is preserved: Removed the `status.value != "cancelled"` condition so lookup matches by ID only. Blank IDs still raise `ValueError`, and unknown IDs still return `None`.
- Repair SHA / focused verification result: `e22c410005c13059fc051685c7067fe21b40ae29`. Focused test `tests/test_services.py::test_cancelled_appointment_is_retained_in_history`: failed before the fix (`LookupError: Appointment not found`), passes after (`1 passed`). Full suite after the fix: `4 failed, 48 passed`. Remaining failures are the separate practitioner-conflict fault, not F8-01.

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: Conflict checks are backwards. The same practitioner at the same time is accepted (no ValueError), while a different practitioner at the same time is rejected.
- Expected behaviour and requirement: A conflict exists only when the same practitioner already has a `SCHEDULED` appointment at that exact time. Different practitioners at the same time are allowed.
- Minimal synthetic reproduction steps: Book `A1` with `DR1` at 2026-10-01 09:00. Book `A2` with `DR1` at the same time (expected ValueError, observed: accepted). Book `A2` with `DR2` at the same time (expected: accepted, observed: ValueError).
- Meaningful failing test path/name and exact relevant failure: 
`tests/test_services.py::test_stage7_different_practitioner_same_time_allowed, line 280, ValueError: Practitioner already has a SCHEDULED appointment at this time from smartcare\services.py:122.`
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: `has_practitioner_conflict` in `data_store.py` uses `!=` instead of `==` when comparing practitioner IDs, so it flags other practitioners and misses the same one. Evidence: inspected the method and failing tests at `tests\test_services.py:267` and `:280`
- Smallest justified fix / diff / why other behaviour is preserved: 
+ Changed one operator in `SmartCareDataStore.has_practitioner_conflict`
+ Other behaviour is preserved because the other conditions are untouched: `exclude_appointment_id` still skips the excluded appointment, the time must still match exactly, and only "scheduled" appointments count, so cancelled slots can still be rebooked. `book_appointment` in `services.py` is unchanged.
- Repair SHA / focused verification result:

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry

Likely cause and why plausible: `cancel_appointment` removes the appointment from the data store instead of only setting its status to `CANCELLED`. Plausible because the record is gone after the cancel and the test failure is a “not found” error.
Evidence intended to inspect / competing explanation / discriminating check: [complete]
Member and saved sequence/time or commit showing this preceded consultation: [complete]

### F8-02 human entry

Likely cause and why plausible: [complete]
Evidence intended to inspect / competing explanation / discriminating check: [complete]
Member and saved sequence/time or commit showing this preceded consultation: [complete]

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review

Actual prompt / output reference and member: [complete]

1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
   Final human conclusion and comparison with initial hypothesis: [complete]

### F8-02 Copilot review

Actual prompt / output reference and member: [complete]

1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
   Final human conclusion and comparison with initial hypothesis: [complete]

## G. Failing to passing regression evidence

| Checkpoint                                     | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
| ---------------------------------------------- | ------------------------ | ----------------------------- | ------------------------------------ |
| F8-01 before repair                            | [complete]               | [complete]                    | [complete]                           |
| F8-01 after repair                             | [complete]               | [complete]                    | [complete]                           |
| F8-02 before repair                            | [complete]               | [complete]                    | [complete]                           |
| F8-02 after repair                             | [complete]               | [complete]                    | [complete]                           |
| Full suite after both repairs, before refactor | [complete]               | [complete]                    | [complete]                           |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: [complete]
Unrelated failures investigated / resolution: [complete or not applicable with reason]

## H. Refactoring decision and before/after verification

Smell and exact location: [complete]
Small proposed structural change / why justified: [complete before editing]
External behaviour to preserve / relevant tests: [complete]
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: [complete]
Focused and full after-refactor commands / working directory / results / evidence: [complete]
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: [complete]

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: [complete]
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: [complete]
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [complete; report honestly if none and discuss the least-supported real suggestion]
2. What evidence changed your group's view? [complete]
3. How did regression tests protect the refactoring? [complete]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: [Before changing code in response to a failure, Reproduce it and gather enough evidence to understand its cause. Check the error message, logs, inputs and environment for instance; then verify the suspected cause with a small, repeatable test, as follows this helps ensure the change fixes the actual problem rather than just masking a symptom.]

2. Where should expected behaviour come from during debugging?

Response: [Expected Behaviour should come from the requirements or specification-including agreed acceptance criteria, documented design decisions, or confirmed stakeholder expectations, not from what the code currently happens to do. If those sources are unclear or missing, clarify the intended behaviour with the relevant stakeholders before treating the failure as a bug.]

3. What is a debugging hypothesis?

Response: [Debugging hypothesis is a testable explanation for why a failure is happening . For example; " the request fails because the input is missing a required field". You then check the evidence-such as logs, inputs, or a focused test-to confirm or reject that explanation before changing the code.]

4. What is a regression test and why is it retained?

Response: [A regression test checks that a bug or previously working behaviour does not break again after the code changes. It is retained in the test suite so it can be rerun atuomatically during future changes, catching the same problem if it returns.]

5. What is meant by root cause?

Response: [The root cause is the underlying reason a problem occurred--not just the visible symptom. Finding it helps address the source of the failure so it's less likely to happen again.]

6. What is refactoring?

Response: [Refacoting is changing the internal structure of the code to make it clearer or rather easier to maintain, without changing what it does. Tests help confirm that the behaviour stays the same.]

7. What is a swallowed exception?

Response: [A swallowed exception is an error that code catches but then hides--for example, by ignoring it or returning without reporting it. This can make a failure difficult to notice or act upon.]

8. What is a code smell?

Response: [A code smell is a sign that code may be poorly strutted or harder to maintain, even it if currently works. For instance, duplicated logic, Overly long functions or unclear names. It suggests an area worth reviewing, but doesn't automatically mean there's a bug.]

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: [Github Copilots debugging diagnosis should be treated as a hypothesis, not a confirmed cause. Check it against the requirements, error messages, logs, and a reproducible test before changing code.]

10. What is the Stage 8 engineering rule?

Response: [In this context/project, the Stage 8 likely refers to ( Steve Yegge's 8 Stages of developers Evolution to AI], The 8th stage described as " The Frontier " , Building and running your own orchestrator. According to this research (Birgitta Böckeler, 2026). This stage features multi-agent autonomous hierarchies (agent swarms) where an AI manager assigns tasks to specialised AI worker, testing, and design sub-agents without a human in the intermediate loop. 
- Birgitta Böckeler. (2026, April 8). State of play: AI coding assistants. InfoQ. https://www.infoq.com/presentations/ai-coding-assistants/ 

## L. Completion and handover

- [ ] Existing project, earlier tests and stage records preserved.
- [ ] Passing Stage 7 SHA and safe preparation details recorded.
- [ ] Both defects reproduced with meaningful failing tests.
- [ ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [ ] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [ ] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [ ] Tutorial, three reflections and ten formative responses complete.
- [ ] Local recovery metadata excluded from submitted source.
- [ ] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: [complete]
Handover note: [complete]
