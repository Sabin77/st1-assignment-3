# Stage 10 PG agentic rescheduling activities and evidence

PG-only stage. Undergraduate students are not required to complete this record. UG-only groups retain this supplied template unchanged as intentionally not applicable; do not fabricate N/A responses. Optional UG help is voluntary and unassessed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage10_pg/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Protect the common Stage 9 SHA and UG Stage 12 pathway.

This is a blank student record. Use actual accessible links and concise evidence; do not invent an agent session, test result or approval. Retain this record's headings when linking equivalent issue/PR evidence.

Group/tutorial: Group 501, Tuesday 1:30 PM.
Assessed PG members and roles: Sabin Lamichhane — PG member responsible for Stage 10 appointment rescheduling, implementation, testing, Copilot supervision and evidence documentation.
Optional UG contributors: Stanley Campbell (`s-campbell-dev`) — independent reviewer of Stage 10 PR #18.

## A Access baseline and recovery

- Confirmed GitHub Copilot feature/mode, version/environment and teaching-team approval reference: GitHub Copilot was used for the Stage 10 planning interaction and initial implementation proposal. PyCharm was used for the final manual implementation. The exact Copilot agent mode/version and teaching-team approval reference have not been independently confirmed.

- Actual account access and tool permissions check: GitHub Copilot could inspect repository files and propose changes. However, the available GitHub write tools committed and pushed changes, rather than editing only the local working tree. This permission limitation was identified after the first incorrect implementation.

- Live route or convenor-confirmed equivalent staged interaction: A Copilot plan-only interaction and an implementation proposal were performed. The original plan was reviewed against RES-01–RES-06 and RES-05-R2. The agent workflow was not fully compliant with the intended approval controls, so the corrected implementation was completed manually in PyCharm.

- Access limitation and tutor resolution if applicable: The GitHub write tools could not safely perform local edits without committing or pushing. No tutor-approved alternative has been confirmed. This remains a limitation of the recorded agent workflow.

- Protected Stage 9 common SHA / recoverable reference: `46209c7a443de4520972c610e0a06831cea40886` (Stage 9 integration, PR #17). The earlier `b016f8f2c0ad0c7be51c5eed8dea39ba35cadcac` was the local Stage 10 starting checkpoint, not the final Stage 9 integration checkpoint.

- Common baseline command / project working directory / actual result: `py -m pytest -q`, run from `project/`. The initial local checkpoint returned 52 passed in 0.08s. After recovery, the original 52 tests passed again in 0.09s.

- Clean branch and preparer / recovery baseline: Sabin Lamichhane created `feature/stage10-rescheduling` with a clean working tree. The incorrect Copilot commit `e36ee41` was reversed by revert commit `82d81e5`. The Stage 10 human specification was preserved in commit `1cab504`.

- Evidence-only later SHA if different / explanation: The corrected implementation and evidence were committed as `1d18d19`. A later evidence-only correction commit and final integrated SHA are to be recorded after completion.

## B Tutorial activities

### B1 Rewrite the vague task

“Improve SmartCare appointment scheduling.” Write your bounded goal, requirements, exclusions, constraints, acceptance criteria and Definition of Done:

Implement appointment rescheduling in the existing SmartCare application. Only SCHEDULED appointments may move to valid available times. The same appointment object, ID, patient and practitioner must be preserved. Invalid IDs, invalid datetimes, same-practitioner conflicts and changes to CANCELLED or COMPLETED appointments must be rejected without mutation. A valid same-time no-op is permitted. Updated appointment times must appear through lookup and sorted listing within the current session.

The implementation must reuse existing domain validation, service coordination and data-store conflict checking. Database redesign, notifications, external libraries, persistence and unrelated changes are excluded.

Definition of Done: meaningful acceptance tests pass, previous tests remain valid, production and test diffs are reviewed, actual agent decisions are recorded, and the completed work receives independent review.

Predicted changed files and human test intentions:

Expected files: `project/smartcare/domain.py`, `project/smartcare/services.py`, `project/tests/test_rescheduling.py`, `project/README.md` and this Stage 10 evidence record.

Tests should cover successful moves, object identity, invalid and unknown IDs, practitioner conflicts, different-practitioner availability, CANCELLED/COMPLETED states, invalid datetimes, same-time no-op, old-slot reuse, failed-state preservation and updated listing order.

### B2 Judge every proposed plan step

| Proposed step | Accept / Modify / Reject | Requirement evidence and reason |
|---|---|---|
| Redesign database schema | Reject | SmartCare uses an in-memory store. Rescheduling does not require a schema change or persistence. |
| Add notifications | Reject | Notifications are outside RES-01–RES-06 and would introduce unnecessary functionality. |
| Introduce calendar library | Reject | Existing `datetime` validation and conflict checking are sufficient. No new dependency is required. |
| Modify Patient | Reject | Rescheduling changes the appointment time, not patient identity or details. |
| Add rescheduling | Accept | Required by RES-01–RES-06 and RES-05-R2. Implement through Appointment and AppointmentService. |
| Rewrite all tests | Reject | Existing common tests must be preserved. Add focused tests without weakening earlier assertions. |


### B3 Six proposed changes

| File or action | Expected? | Review concern and evidence needed |
|---|---|---|
| Appointment in project/smartcare/domain.py | Yes | Add a guarded rescheduling method. Verify status checks, datetime validation and unchanged identity. |
| project/smartcare/services.py | Yes | Coordinate lookup and practitioner conflict checking before mutation. Verify exceptions and same-object return. |
| Proposed sqlite_repository.py / schema change | No | Persistence and database redesign are unnecessary and outside the approved requirements. |
| Patient fields in project/smartcare/domain.py | No | Patient data should remain unchanged. Review the diff for unrelated modifications. |
| requirements-dev.txt adds calendar package | No | No external calendar package is needed. Reject unapproved dependency changes. |
| Existing appointment assertions weakened | No | Existing tests must remain meaningful and unchanged. Compare the original and final tests. |


### B4 Approval gate

Agent says “All tests pass.” Give at least SIX distinct checks before approval.
1. Inspect the actual changed-file list and confirm that all changes are within the approved scope.
2. Review the domain and service diffs to ensure validation and conflict checks occur before mutation.
3. Review the new tests separately to check that their assertions reflect the actual requirements.
4. Run the focused rescheduling tests independently.
5. Run the original common tests without the new test file.
6. Run the complete test suite and confirm the cumulative result.
   
Additional checks if useful: Verify that the appointment object is preserved, CANCELLED/COMPLETED appointments cannot move, the original slot becomes available after a successful move, no unnecessary dependencies were introduced, and an independent reviewer has checked the final committed code.

### B5 Exit question

Why does increasing AI autonomy increase rather than decrease the importance of software engineering discipline? 

Greater AI autonomy allows an agent to make changes across multiple files and potentially execute commands or commit code. This increases the consequences of mistakes. In our Stage 10 work, Copilot committed an incomplete implementation before the required approval, demonstrating why permission controls, requirement boundaries, diff reviews, regression tests and human approval gates remain essential.

## C Human task specification before AI

- Goal: Add an appointment rescheduling feature to the existing SmartCare application.
- Requirements RES-01–06 with RES-05-R2: Implement RES-01–RES-06, including RES-05-R2. Only scheduled appointments can move to valid available times. Keep the same appointment object, ID and participants. Reject invalid IDs, datetimes, conflicting bookings and cancelled/completed appointments without changing state.
- Out of scope: Database redesign, persistence, notifications, payments, authentication, external calendar libraries and unrelated changes.
- Architecture constraints: Add a domain-level rescheduling operation in Appointment and a coordinating method in AppointmentService. Reuse the existing datetime validator and SmartCareDataStore.has_practitioner_conflict() helper.
- Acceptance criteria: Successful rescheduling preserves identity, rejects conflicts, permits a valid same-time no-op, frees the old slot and updates appointment lookup and practitioner listing.
- Definition of Done: All specified scenarios have meaningful tests; the existing tests still pass; changes have been independently reviewed; the approved Copilot workflow and human decisions are documented.
- Issue / PG owner: Sabin Lamichhane (GitHub: Sabin77)
- Human expected positive, negative and boundary tests: 
  1. **Successful rescheduling:** A SCHEDULED appointment moves to a free datetime while preserving the same object, ID, patient and practitioner.
  2. **Unknown ID:** A valid but unknown appointment ID raises `LookupError`.
  3. **Invalid ID:** Blank or non-string appointment IDs raise `ValueError`.
  4. **Practitioner conflict:** Another SCHEDULED appointment for the same practitioner at the requested datetime causes `ValueError`.
  5. **Different practitioner:** An appointment can move to a datetime occupied by a different practitioner.
  6. **Invalid status:** CANCELLED and COMPLETED appointments cannot be rescheduled, including same-time requests.
  7. **Same-time no-op:** Rescheduling a SCHEDULED appointment to its existing datetime is allowed.
  8. **Invalid datetime:** Non-datetime values, timezone-aware datetimes and values with nonzero seconds or microseconds raise `ValueError`.
  9. **State preservation:** Rejected requests do not modify appointment fields or stored records.
  10. **Old-slot reuse:** A successful move makes the original slot available for another appointment with the same practitioner.
  11. **Lookup and listing:** The updated datetime is visible through appointment lookup and sorted practitioner listing.
- Allowed files:  - `project/smartcare/domain.py` — Add `Appointment.reschedule()`.
  - `project/smartcare/services.py` — Add `AppointmentService.reschedule_appointment()`.
  - `project/tests/test_rescheduling.py` — Add meaningful tests.
  - `project/README.md` — Document the rescheduling feature.
  - `stage10_pg/stage10_activities_and_evidence.md` — Record implementation and review evidence.
- Forbidden/unnecessary files and changes: Do not modify unrelated Patient or Practitioner functionality, existing cancellation/history rules or correct previous tests.

  Do not introduce databases, persistence, notifications, payments, authentication, external calendar packages, unnecessary dependencies or unrelated console functionality.

  Any additional file changes must be justified by the requirements and receive human approval.
- Baseline/recovery link:

  Repository: https://github.com/Sabin77/st1-assignment-3

  Protected Stage 9 integrated SHA: `46209c7a443de4520972c610e0a06831cea40886`

  Stage 9 integration reference: https://github.com/Sabin77/st1-assignment-3/pull/17

  Stage 10 local starting checkpoint: `b016f8f2c0ad0c7be51c5eed8dea39ba35cadcac`

  Starting checkpoint: https://github.com/Sabin77/st1-assignment-3/commit/b016f8f2c0ad0c7be51c5eed8dea39ba35cadcac

  Working directory: `project/`

  Baseline command: `py -m pytest -q`

  Observed baseline result: 52 passed in 0.08s.

  Recovery: Incorrect Copilot commit `e36ee41` was reverted in `82d81e5`. The recovered common tests passed independently.

  Corrected Stage 10 implementation commit: `1d18d19`.

  The common Stage 9 code remains recoverable through Git history.

- Evidence that human analysis preceded agent use: Before consulting GitHub Copilot for Stage 10, I reviewed the assignment requirements and confirmed that the existing SmartCare application passed all 52 tests.

  I identified the required rescheduling behaviour, expected positive and negative scenarios, relevant domain and service responsibilities, existing datetime validation and practitioner conflict handling.

  I prepared this Section C specification before requesting the agent's implementation plan.

The Copilot planning interaction, implementation problems, recovery and human review decisions are documented in Sections D and H.

The initial Copilot implementation was rejected and reverted. The corrected implementation was independently reviewed and approved in PR #18.
## D Agent plan and approval

Actual plan-only prompt/context and response or confirmed equivalent artefacts:

GitHub Copilot was used to prepare an initial implementation plan for Stage 10 appointment rescheduling. The planning discussion covered RES-01–RES-06 and RES-05-R2, including the proposed domain method, service method, focused tests and scope restrictions.

I reviewed the proposed plan before proceeding. However, the subsequent Copilot implementation was not completed within the intended human approval controls. The incorrect implementation commit `e36ee41` was rejected and reverted in `82d81e5`.

The corrected implementation was completed manually and committed as `1d18d19`.

Implementation and review evidence:
https://github.com/Sabin77/st1-assignment-3/pull/18

Incorrect agent implementation:
https://github.com/Sabin77/st1-assignment-3/commit/e36ee41f29e36bbb4ab3e5e096194837cee1c70c

Recovery:
https://github.com/Sabin77/st1-assignment-3/commit/82d81e5

Corrected implementation:
https://github.com/Sabin77/st1-assignment-3/commit/1d18d19

Original Copilot plan-only prompt and response:
Not linked here; the original interaction would need to be supplied separately as a screenshot or saved transcript.
| Plan step / action | Requirement link | Reason | Expected files | Accept / Modify / Reject | Conditions / evidence |
|---|---|---|---|---|---|
| Add `Appointment.reschedule()` | RES-01, RES-02, RES-06 | Keep datetime validation and state changes within the domain object. | `project/smartcare/domain.py` | Accept | Only SCHEDULED appointments can move. Reuse `validate_date_time`; preserve identity and state on failure. |
| Add `AppointmentService.reschedule_appointment()` | RES-01–RES-04, RES-06 | Coordinate lookup, status validation and practitioner conflicts before mutation. | `project/smartcare/services.py` | Accept | Reuse `find_appointment()` and `has_practitioner_conflict()` with target ID exclusion. |
| Add focused rescheduling tests | RES-01–RES-06, RES-05-R2 | Verify positive, negative and boundary scenarios independently. | `project/tests/test_rescheduling.py` | Accept | Check meaningful results, identity, conflicts, invalid inputs, state preservation, old-slot reuse and listing order. |
| Document PG rescheduling | Stage 10 documentation | Explain the new feature and its session-only limitations. | `project/README.md` | Accept | Do not claim persistence or unverified results. |
| Complete Stage 10 evidence | Stage 10 Sections D–K | Record actual planning, implementation, verification and review evidence. | `stage10_pg/stage10_activities_and_evidence.md` | Accept | Record only actual Copilot activity, test results, commits, reviews and human decisions. |

**Actual plan-only prompt/context and response:**
GitHub Copilot provided a plan-only response for the Stage 10 implementation. The proposed steps covered the domain method, service coordination, focused tests, README documentation and evidence requirements.

The plan was reviewed against RES-01–RES-06 and RES-05-R2 before implementation.

**Approved bounded scope:**
Only the existing domain and service files, the new rescheduling test file, the project README and the Stage 10 evidence record were required.

**Forbidden changes:**
Database redesign, persistence, notifications, new dependencies, unrelated participant changes, weakened tests and unrelated console changes were excluded.
**Verification plan:**
Run focused PG tests, original common tests independently and the cumulative suite. Inspect production code separately from the new tests.

**Human plan approver:**
Sabin Lamichhane (PG owner).

**Human approval before edits:**
The initial plan was reviewed, but the first implementation did not follow the required approval boundary. Copilot created and pushed commit `e36ee41` before the intended approval process was completed.

The implementation was rejected because the domain method was missing, file contents were incorrectly assembled, and some tests were defective.

**Tool permissions and expanded-scope requests:**
The available GitHub write tools committed or pushed changes instead of applying local working-tree edits. After identifying the limitation, the incorrect commit was reverted in `82d81e5`.

The corrected implementation was completed manually in PyCharm. No further autonomous commit or push was accepted.

**Final corrected implementation:**

Commit: `1d18d19`

Review: https://github.com/Sabin77/st1-assignment-3/pull/18

## E Production diff review

Actual proposal / branch diff / version reviewed: (https://github.com/Sabin77/st1-assignment-3/pull/18)

| File | Change purpose and reason | Requirement / test link | Expected? | Architecture OK? | Decision | Notes / correction |
|---|---|---|---|---|---|---|
| `project/smartcare/domain.py` | Add `Appointment.reschedule()` with status and datetime validation before mutation. | RES-01, RES-02, RES-06 | Yes | Yes | Accept | Changes only `_date_time`; retains the original object and participants. |
| `project/smartcare/services.py` | Add rescheduling workflow, lookup, conflict checking and return of the existing appointment. | RES-01–RES-04, RES-06 | Yes | Yes | Accept | Reuses `validate_date_time()` and `has_practitioner_conflict()` with target exclusion. |
| `project/README.md` | Document supported rescheduling behaviour and session-only limitation. | Stage 10 documentation | Yes | Yes | Accept | Stage 10 feature note added and included in the committed implementation. |
| `project/tests/test_rescheduling.py` | Add positive, negative and boundary tests for rescheduling. | RES-01–RES-06, RES-05-R2 | Yes | Yes | Accept | 19 tests passed; reviewed separately in Section F. |
| `stage10_pg/stage10_activities_and_evidence.md` | Document actual planning, correction, verification and review evidence. | Stage 10 evidence | Yes | Yes | Accept with documentation corrections | Stanley identified the Stage 9 SHA and committed-code verification corrections. |
Every changed file inspected, including new/untracked files:
Reviewed the local production diffs for `domain.py` and `services.py`, the new `test_rescheduling.py`, and the README diff. The README required a further documentation update. The Stage 10 evidence record remains under completion.

Unexpected changes, scope creep, secrets/dependencies/configuration, unrelated cleanup:
No unrelated production or dependency changes identified in the reviewed diff. The earlier incorrect Copilot commit was reverted. `git diff --check` reported only Windows LF/CRLF conversion warnings.

## F Separate test review

| Test | Criterion | Actual assertion | Assertion meaningful / adequate? | Agent changed expected behaviour? | Human or agent authorship | Decision and reason |
|---|---|---|---|---|---|---|
| `test_successful_reschedule_preserves_identity` | RES-01, RES-02 | Same appointment object, patient, practitioner and ID; updated datetime. | Yes | No | Manually added after rejected agent proposal | Accept |
| `test_unknown_appointment_raises_lookup_error` | RES-03 | Unknown ID raises `LookupError`; existing time remains unchanged. | Yes | No | Manual | Accept |
| `test_invalid_appointment_id` | RES-03 | Invalid IDs raise `ValueError`; original time is preserved. | Yes | No | Manual | Accept |
| `test_same_practitioner_conflict_rejected` | RES-04 | Conflict raises `ValueError`; appointment times and store contents remain unchanged. | Yes | No | Manual | Accept |
| `test_different_practitioner_same_time_allowed` | AC-RES-04 | Rescheduling succeeds when the existing booking belongs to another practitioner. | Yes | No | Manual | Accept |
| `test_cancelled_appointment_cannot_reschedule` | RES-06 | CANCELLED status rejects moves and same-time requests without mutation. | Yes | No | Manual | Accept |
| `test_completed_appointment_cannot_reschedule` | RES-06 | Actual COMPLETED appointment rejects moves and retains its stored identity and datetime. | Yes | No | Manual correction of previous agent test defect | Accept |
| `test_same_time_no_op` | Self-exclusion | Same-time request succeeds and retains the original appointment. | Yes | No | Manual | Accept |
| `test_invalid_datetime_rejected` | Date/time validation | Invalid types, seconds, microseconds and timezone-aware datetimes raise `ValueError`. | Yes | No | Manual correction of previous agent test defect | Accept |
| `test_successful_move_frees_original_slot` | Old-slot reuse | Another appointment can be booked into the released slot. | Yes | No | Manual | Accept |
| `test_lookup_and_listing_show_updated_order` | RES-05-R2 | Lookup shows the updated time; practitioner listing is correctly reordered. | Yes | No | Manual | Accept |
| `test_domain_rejects_invalid_status_and_time` | Domain invariants | Invalid time and illegal status are rejected without changing the appointment time. | Yes | No | Manual | Accept |

Comparison with original common tests / any proposed weakening:
The original 52 tests were retained unchanged and passed independently. No previous assertions were weakened to accommodate the new feature.

Independent human checks and corrections:
The earlier Copilot proposal contained an invalid COMPLETED-state test and an incorrect timezone-aware datetime example. These were identified during review. The corrected manually added tests construct an actual COMPLETED appointment and use `timezone.utc` for the timezone-aware case. The resulting 19 focused tests passed independently.

## G Actual verification

| Requirement / acceptance scenario | Test or demonstration | Meaningful expected result | Actual result | Evidence / version |
|---|---|---|---|---|
| RES-01 / AC-RES-01 successful move | `test_successful_reschedule_preserves_identity` | A SCHEDULED appointment moves to a valid free time. | Passed | Local `test_rescheduling.py` |
| RES-02 same object and participant identities | `test_successful_reschedule_preserves_identity` | The appointment object, ID, patient and practitioner remain unchanged. | Passed | Local `test_rescheduling.py` |
| RES-03 / AC-RES-02 unknown and invalid IDs | `test_unknown_appointment_raises_lookup_error`; `test_invalid_appointment_id` | Unknown IDs raise `LookupError`; blank and invalid IDs raise `ValueError`. | Passed | Local `test_rescheduling.py` |
| RES-04 / AC-RES-03 conflicting practitioner | `test_same_practitioner_conflict_rejected` | A conflicting SCHEDULED appointment for the same practitioner blocks the move without mutation. | Passed | Local `test_rescheduling.py` |
| AC-RES-04 different practitioner allowed | `test_different_practitioner_same_time_allowed` | An appointment with another practitioner at the requested time does not block rescheduling. | Passed | Local `test_rescheduling.py` |
| RES-06 / AC-RES-05 cancelled and completed | `test_cancelled_appointment_cannot_reschedule`; `test_completed_appointment_cannot_reschedule` | CANCELLED and COMPLETED appointments cannot move, including same-time attempts. | Passed | Local `test_rescheduling.py` |
| RES-05-R2 / AC-RES-06-R2 lookup and listing order | `test_lookup_and_listing_show_updated_order` | Lookup and practitioner listing show the new time and correct order in the current session. | Passed | Local `test_rescheduling.py` |
| Self-exclusion and same-time no-op | `test_same_time_no_op` | A SCHEDULED appointment can retain its own existing time without creating a conflict. | Passed | Local `test_rescheduling.py` |
| Invalid datetime and failed-state snapshots | `test_invalid_datetime_rejected`; `test_domain_rejects_invalid_status_and_time`; `test_same_practitioner_conflict_rejected` | Invalid values raise `ValueError`, and rejected operations preserve the appointment's existing state. | Passed | Local `test_rescheduling.py` |
| Successful old-slot reuse | `test_successful_move_frees_original_slot` | The original appointment slot becomes available after a successful move. | Passed | Local `test_rescheduling.py` |

| Suite | Command / working directory | Code SHA | Actual count and result | Evidence |
|---|---|---|---|---|
| Focused PG | `py -m pytest -q tests/test_rescheduling.py` from `project/` | Local uncommitted changes after `82d81e5` | 19 passed in 0.06s | PyCharm terminal output |
| Common independently | `py -m pytest -q --ignore=tests/test_rescheduling.py` from `project/` | Local uncommitted changes after `82d81e5` | 52 passed in 0.07s | PyCharm terminal output |
| Full cumulative | `py -m pytest -q` from `project/` | Local uncommitted changes after `82d81e5` | 71 passed in 0.23s | PyCharm terminal output |
| Integrated retest | `py -m pytest -q` from `project/` | `91b6dba334715653b806cc18f41fffe4fffeb246` | 71 passed in 0.12s | Local integrated main verification |
Failures / diagnosis / corrections and reruns / unresolved concerns:
The original common suite passed 52 tests. After the corrected Stage 10 implementation, the focused PG suite passed 19 tests, the existing tests independently passed 52 tests, and the cumulative suite passed 71 tests.

The earlier Copilot-generated implementation `e36ee41` was rejected and reverted in `82d81e5` because it omitted the domain method, contained incorrectly assembled file contents and included defective tests.

The corrected implementation was committed in `1d18d19`.

Stanley Campbell (`s-campbell-dev`) independently reviewed PR #18 and ran `python -m pytest` from `project/` against commit `1d18d19`, using Python 3.13.14 and pytest 8.3.5. His result was 71 passed.

Review decision: APPROVED, with documentation corrections requested.

Review: https://github.com/Sabin77/st1-assignment-3/pull/18

The protected Stage 9 integrated SHA was corrected to `46209c7`. The original local test results remain recorded separately from the reviewer's committed-code verification.

Post-merge integration testing remains pending.

## H Decisions corrections and independent review

| Significant agent action | Human review and evidence | Accept / Modify / Reject and reason | Manual correction or recovery | Recheck evidence |
|---|---|---|---|---|
| Copilot proposed the rescheduling implementation plan | Plan compared with RES-01–RES-06 and RES-05-R2 | Accept with bounded scope | Limited planned changes to domain, service, tests, README and evidence | Requirements and test plan reviewed |
| Copilot committed and pushed incomplete code | Commit `e36ee41` contained incorrectly assembled files and omitted the domain method | Reject — violated the approval boundary and did not satisfy the specification | Reverted in `82d81e5` | Recovered common suite: 52 passed |
| Copilot proposed invalid COMPLETED and timezone tests | Test proposal inspected separately | Reject/Modify — tests did not check the intended behaviour | Created a genuine COMPLETED-state test and used `timezone.utc` with a separate microseconds case | 19 focused tests passed |
| Corrected manual implementation | Domain, service and test diffs reviewed | Accept — requirements preserved and no common tests weakened | Committed corrected implementation as `1d18d19` | Full local suite: 71 passed |
| Independent human PR review | Stanley Campbell reviewed PR #18 and ran the committed tests | Accept, with documentation corrections | Correct protected Stage 9 SHA and clarify committed-code verification | Stanley confirmed 71 passed on `1d18d19` |

Final proposal decision: Accepted after modification. The original agent-generated implementation was rejected; the final manually corrected implementation was independently approved.

Evidence supporting decision: The domain and service diffs, 19 focused passing tests, 52 independently passing common tests, 71 cumulative passing tests, and Stanley's approved GitHub review.

If rejected, how the required feature was subsequently completed and verified: After rejecting and reverting the incorrect Copilot commit, the rescheduling methods and tests were manually implemented in PyCharm. The corrected implementation passed the full test suite.

Saved proposal and targeted recovery details if needed: Incorrect commit `e36ee41`; revert commit `82d81e5`; corrected implementation `1d18d19`; PR #18.

Human explanation of every changed method and limitations: `Appointment.reschedule()` validates the appointment status and requested datetime before changing `_date_time`. `AppointmentService.reschedule_appointment()` retrieves the stored appointment, checks its status, validates the new datetime, checks practitioner conflicts while excluding the target appointment, and calls the domain method. The feature preserves identity and operates only within the current in-memory session. It does not provide restart persistence or a new console command.

Another PG / willing UG / tutor reviewer, actual PR/diff review and feedback: Stanley Campbell (`s-campbell-dev`) independently reviewed PR #18 and submitted APPROVED. He verified 71 passing tests on committed code and requested correction of the Stage 9 baseline SHA and committed-code evidence.

Review link: https://github.com/Sabin77/st1-assignment-3/pull/18

Corrections, recheck and actual approval before integration: Stanley's independent approval was recorded on 9 November 2026. The requested documentation corrections are being applied before integration. Any required renewed review must be obtained after the correction commit.

Integrated PG SHA / common protected SHA: Stage 10 integrated SHA `91b6dba334715653b806cc18f41fffe4fffeb246`. Protected Stage 9 SHA `46209c7a443de4520972c610e0a06831cea40886`.
Each assessed PG member's implementation, supervision and test contribution: Sabin Lamichhane prepared the requirements specification, reviewed Copilot's plan, identified defective agent changes, performed Git recovery, implemented the corrected rescheduling methods, added and ran tests, inspected changes and documented evidence.

Optional UG help, acknowledged separately: Stanley Campbell independently reviewed PR #18 and verified 71 tests.

## I Four reflections

1. Which agent change had the greatest blast radius? 
The first Copilot implementation had the greatest blast radius because it incorrectly assembled existing files, omitted the required domain method and pushed an incomplete commit. This could have disrupted existing SmartCare functionality if it had been merged without review.

2. Did the plan predict it? 
No. The plan identified the correct bounded files and requirements, but the implementation did not follow the proposed structure. This showed that an acceptable plan does not guarantee correct execution.

3. What did you reject or manually correct? 
I rejected the initial Copilot implementation and reverted its commit. I then manually added the domain and service methods and corrected the rescheduling tests. In particular, I fixed the COMPLETED-appointment test and the timezone-aware datetime test.

4. What evidence justified final approval? 
The corrected implementation passed 19 new rescheduling tests and all 52 existing tests. The full suite passed 71 tests. I also reviewed the production and test diffs, and Stanley independently tested the committed code and approved PR #18. The remaining documentation corrections and final integrated retest must still be completed.

## J Ten formative questions

1. What is the difference between an AI assistant and an engineering agent?

An AI assistant mainly provides suggestions, explanations or code examples. An engineering agent can also inspect files, use tools, modify code and potentially execute commands. Therefore, agent actions require stronger supervision.

2. What is the simplified agent loop used in Stage 10?

The simplified loop is: understand the task, inspect the environment, propose a plan, obtain approval, perform bounded actions, verify results and return control to the human reviewer.

3. Why should an agent plan be reviewed before repository edits begin?

Plan review helps detect unnecessary changes, incorrect assumptions and risks before they affect the code. It also establishes which files and operations the agent is allowed to change.

4. What is meant by the blast radius of a software change?

Blast radius refers to the number of components, behaviours or users potentially affected by a change. A small method-level change generally has a narrower blast radius than replacing entire modules or changing the repository structure.

5. Why is diff review essential for agentic changes?

A diff shows exactly what changed. It allows the human reviewer to identify unintended edits, removed behaviour, changed dependencies and weakened tests rather than trusting the agent's description.

6. What is a human approval gate?

A human approval gate is a required checkpoint where a responsible person reviews proposed actions and decides whether the agent may continue. It prevents autonomous changes from proceeding without appropriate supervision.

7. What is test accommodation and why is it dangerous?

Test accommodation occurs when tests are weakened or modified to accept incorrect software behaviour instead of fixing the underlying problem. It is dangerous because the tests may pass while the requirements remain unsatisfied.

8. What is rollback in the context of agentic software engineering?

Rollback means returning the project to an earlier safe state after an unsuccessful change. In Stage 10, the incorrect Copilot commit was reversed using Git, preserving the original baseline and change history.

9. Who remains accountable for accepted agentic changes?

The human developer and responsible team remain accountable. An AI agent may assist with implementation, but humans must verify correctness, review risks and approve integration.

10. What is the Stage 10 engineering rule?

Review the plan before allowing changes, keep agent actions within an approved scope, inspect every relevant diff, verify behaviour using meaningful tests, and retain human responsibility for final acceptance.

## K Completion and Stage 11 handover

- [x] Common Stage 9 checkpoint protected; UG pathway unaffected.
- [x] RES-01–06 and RES-05-R2 implemented in the same project.
- [x] Domain/service boundaries, current exceptions and coding standard preserved.
- [x] Positive/negative/boundary cases and failed-state checks verified.
- [x] Common tests remain valid and independently passing; full suite passes.
- [x] Plan reviewed before bounded actions; every file and test diff inspected.
- [x] Actual agent route, decisions, corrections and rechecks recorded honestly.
- [x] No unrelated features, persistence, dependencies or staff solutions introduced.
- [ ] Another-member or tutor review and integrated retest complete.
- [x] Tutorial, four reflections, ten formative responses and PG contributions complete.
- [x] Each PG member can explain their code and supervision.
- [ ] README PG note, actual integrated SHA and limitations recorded.


Unresolved issues / owner / action:
Stanley's independent PR review is APPROVED, but the documentation corrections and post-merge verification remain outstanding. Sabin Lamichhane will complete these corrections, merge the reviewed changes when approval requirements are satisfied, and rerun the integrated suite. The exact approved Copilot agent mode and teaching-team approval reference are not confirmed.

Stage 11 handover references to extension, tests, dependencies and actual AI/review evidence:
Stage 10 implementation commit: `1d18d19`.
Stage 10 PR: https://github.com/Sabin77/st1-assignment-3/pull/18
Protected Stage 9 integrated SHA: `46209c7`.
Verification: 19 focused PG tests, 52 original common tests and 71 cumulative tests passed.
Independent reviewer: Stanley Campbell (`s-campbell-dev`), APPROVED.
Runtime dependencies remain unchanged; SmartCare uses the existing in-memory design.
Stage 11 will use the integrated Stage 10 code after the final merge and verification.

Submitted SHA / explanation if later than tested code:
Pending final integration and evidence commit. Record the actual final submitted SHA before submission.
