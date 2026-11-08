# Stage 10 PG agentic rescheduling activities and evidence

PG-only stage. Undergraduate students are not required to complete this record. UG-only groups retain this supplied template unchanged as intentionally not applicable; do not fabricate N/A responses. Optional UG help is voluntary and unassessed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage10_pg/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Protect the common Stage 9 SHA and UG Stage 12 pathway.

This is a blank student record. Use actual accessible links and concise evidence; do not invent an agent session, test result or approval. Retain this record's headings when linking equivalent issue/PR evidence.

Group/tutorial: [response]
Assessed PG members and roles: [response]
Optional UG contributors: [response or none]

## A Access baseline and recovery

- Confirmed GitHub Copilot feature/mode, version/environment and teaching-team approval reference: [response]
- Actual account access and tool permissions check: [response]
- Live route or convenor-confirmed equivalent staged interaction: [response]
- Access limitation and tutor resolution if applicable: [response]
- Protected Stage 9 common SHA / recoverable reference: [response]
- Common baseline command / project working directory / actual result: [response]
- Clean branch and preparer / recovery baseline: [response]
- Evidence-only later SHA if different / explanation: [response]

## B Tutorial activities

### B1 Rewrite the vague task

“Improve SmartCare appointment scheduling.” Write your bounded goal, requirements, exclusions, constraints, acceptance criteria and Definition of Done: [response]
Predicted changed files and human test intentions: [response]

### B2 Judge every proposed plan step

| Proposed step | Accept / Modify / Reject | Requirement evidence and reason |
|---|---|---|
| Redesign database schema | [response] | [response] |
| Add notifications | [response] | [response] |
| Introduce calendar library | [response] | [response] |
| Modify Patient | [response] | [response] |
| Add rescheduling | [response] | [response] |
| Rewrite all tests | [response] | [response] |

### B3 Six proposed changes

| File or action | Expected? | Review concern and evidence needed |
|---|---|---|
| Appointment in project/smartcare/domain.py | [response] | [response] |
| project/smartcare/services.py | [response] | [response] |
| Proposed sqlite_repository.py / schema change | [response] | [response] |
| Patient fields in project/smartcare/domain.py | [response] | [response] |
| requirements-dev.txt adds calendar package | [response] | [response] |
| Existing appointment assertions weakened | [response] | [response] |

### B4 Approval gate

Agent says “All tests pass.” Give at least SIX distinct checks before approval.
1. [response]
2. [response]
3. [response]
4. [response]
5. [response]
6. [response]
Additional checks if useful: [response]

### B5 Exit question

Why does increasing AI autonomy increase rather than decrease the importance of software engineering discipline? [response]

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
- Baseline/recovery link: Repository: https://github.com/Sabin77/st1-assignment-3

  Protected Stage 9 baseline SHA: `b016f8f2c0ad0c7be51c5eed8dea39ba35cadcac`

  Baseline commit: https://github.com/Sabin77/st1-assignment-3/commit/b016f8f2c0ad0c7be51c5eed8dea39ba35cadcac

  Test command: `py -m pytest -q`

  Working directory: `project/`

  Observed result: **52 passed in 0.08 seconds**.

  The `main` branch was up to date with `origin/main`, and the working tree was clean.

  Stage 10 branch: `feature/stage10-rescheduling`.

  The baseline remains recoverable through Git history.

- Evidence that human analysis preceded agent use: Before consulting GitHub Copilot for Stage 10, I reviewed the assignment requirements and confirmed that the existing SmartCare application passed all 52 tests.

  I identified the required rescheduling behaviour, expected positive and negative scenarios, relevant domain and service responsibilities, existing datetime validation and practitioner conflict handling.

  I prepared this Section C specification before requesting the agent's implementation plan.

  The actual Copilot prompt, response, human review decisions and approval will be documented in Section D.

  No agent implementation or approval is claimed at this stage.

## D Agent plan and approval

Actual plan-only prompt/context and response or confirmed equivalent artefacts: [links]

| Plan step / action | Requirement link | Reason | Expected files | Accept / Modify / Reject | Conditions / evidence |
|---|---|---|---|---|---|
| Add `Appointment.reschedule()` | RES-01, RES-02, RES-06 | Keep datetime validation and state changes within the domain object. | `project/smartcare/domain.py` | Accept | Only SCHEDULED appointments can move. Reuse `validate_date_time`; preserve identity and state on failure. |
| Add `AppointmentService.reschedule_appointment()` | RES-01–RES-04, RES-06 | Coordinate lookup, status validation and practitioner conflicts before mutation. | `project/smartcare/services.py` | Accept | Reuse `find_appointment()` and `has_practitioner_conflict()` with target ID exclusion. |
| Add focused rescheduling tests | RES-01–RES-06, RES-05-R2 | Verify positive, negative and boundary scenarios independently. | `project/tests/test_rescheduling.py` | Accept | Check meaningful results, identity, conflicts, invalid inputs, state preservation, old-slot reuse and listing order. |
| Document PG rescheduling | Stage 10 documentation | Explain the new feature and its session-only limitations. | `project/README.md` | Accept | Do not claim persistence or unverified results. |
| Complete Stage 10 evidence | Stage 10 Sections D–K | Record actual planning, implementation, verification and review evidence. | `stage10_pg/stage10_activities_and_evidence.md` | Accept | Record only actual Copilot activity, test results, commits, reviews and human decisions. |

**Actual plan-only prompt/context and response:**
GitHub Copilot Stage 10 planning interaction, reviewed before implementation.
The saved prompt and response are retained as planning evidence.

**Approved bounded scope:**
Only `domain.py`, `services.py`, `test_rescheduling.py` and the PG README note may be changed by the agent. The Stage 10 evidence record is maintained by the human PG member.

**Forbidden changes:**
No databases, persistence, new dependencies, notifications, unrelated Patient/Practitioner changes, cancellation changes, weakened tests or console extensions.

**Verification plan:**
Run focused rescheduling tests, the independent existing suite and the cumulative full suite. Review the actual production diff and test diff separately.

**Human plan approver:**
Sabin Lamichhane (PG owner).

**Human approval before edits:**
To be recorded when I explicitly approve implementation through the approved Copilot interface.

**Tool permissions and expanded-scope requests:**
Plan-only interaction completed without file edits or command execution, as reported by Copilot. Actual IDE mode and tool permissions require confirmation. Any expanded scope requires separate approval.
## E Production diff review

Actual proposal / branch diff / version reviewed: [links]

| File | Change purpose and reason | Requirement / test link | Expected? | Architecture OK? | Decision | Notes / correction |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |

Every changed file inspected, including new/untracked files: [evidence]
Unexpected changes, scope creep, secrets/dependencies/configuration, unrelated cleanup: [response or none with evidence]

## F Separate test review

| Test | Criterion | Actual assertion | Assertion meaningful / adequate? | Agent changed expected behaviour? | Human or agent authorship | Decision and reason |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |

Comparison with original common tests / any proposed weakening: [response]
Independent human checks and corrections: [response]

## G Actual verification

| Requirement / acceptance scenario | Test or demonstration | Meaningful expected result | Actual result | Evidence / version |
|---|---|---|---|---|
| RES-01 / AC-RES-01 successful move | [response] | [response] | [response] | [response] |
| RES-02 same object and participant identities | [response] | [response] | [response] | [response] |
| RES-03 / AC-RES-02 unknown and invalid IDs | [response] | [response] | [response] | [response] |
| RES-04 / AC-RES-03 conflicting practitioner | [response] | [response] | [response] | [response] |
| AC-RES-04 different practitioner allowed | [response] | [response] | [response] | [response] |
| RES-06 / AC-RES-05 cancelled and completed | [response] | [response] | [response] | [response] |
| RES-05-R2 / AC-RES-06-R2 lookup and listing order | [response] | [response] | [response] | [response] |
| Self-exclusion and same-time no-op | [response] | [response] | [response] | [response] |
| Invalid datetime and failed-state snapshots | [response] | [response] | [response] | [response] |
| Successful old-slot reuse | [response] | [response] | [response] | [response] |

| Suite | Command / working directory | Code SHA | Actual count and result | Evidence |
|---|---|---|---|---|
| Focused PG | [response] | [response] | [response] | [response] |
| Common independently | [response] | [response] | [response] | [response] |
| Full cumulative | [response] | [response] | [response] | [response] |
| Integrated retest | [response] | [response] | [response] | [response] |

Failures / diagnosis / corrections and reruns / unresolved concerns: [response]

## H Decisions corrections and independent review

| Significant agent action | Human review and evidence | Accept / Modify / Reject and reason | Manual correction or recovery | Recheck evidence |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |

Final proposal decision: [Accepted / Accepted after modification / Rejected]
Evidence supporting decision: [response]
If rejected, how the required feature was subsequently completed and verified: [response or not applicable]
Saved proposal and targeted recovery details if needed: [response or not applicable]
Human explanation of every changed method and limitations: [response]
Another PG / willing UG / tutor reviewer, actual PR/diff review and feedback: [links]
Corrections, recheck and actual approval before integration: [links]
Integrated PG SHA / common protected SHA: [response]
Each assessed PG member's implementation, supervision and test contribution: [response and links]
Optional UG help, acknowledged separately: [response or none]

## I Four reflections

1. Which agent change had the greatest blast radius? [response]
2. Did the plan predict it? [response]
3. What did you reject or manually correct? [response; report honestly if none]
4. What evidence justified final approval? [response]

## J Ten formative questions

1. What is the difference between an AI assistant and an engineering agent? [response]
2. What is the simplified agent loop used in Stage 10? [response]
3. Why should an agent plan be reviewed before repository edits begin? [response]
4. What is meant by the blast radius of a software change? [response]
5. Why is diff review essential for agentic changes? [response]
6. What is a human approval gate? [response]
7. What is test accommodation and why is it dangerous? [response]
8. What is rollback in the context of agentic software engineering? [response]
9. Who remains accountable for accepted agentic changes? [response]
10. What is the Stage 10 engineering rule? [response]

## K Completion and Stage 11 handover

- [ ] Common Stage 9 checkpoint protected; UG pathway unaffected.
- [ ] RES-01–06 and RES-05-R2 implemented in the same project.
- [ ] Domain/service boundaries, current exceptions and coding standard preserved.
- [ ] Positive/negative/boundary cases and failed-state checks verified.
- [ ] Common tests remain valid and independently passing; full suite passes.
- [ ] Plan reviewed before bounded actions; every file and test diff inspected.
- [ ] Actual agent route, decisions, corrections and rechecks recorded honestly.
- [ ] No unrelated features, persistence, dependencies or staff solutions introduced.
- [ ] Another-member or tutor review and integrated retest complete.
- [ ] Tutorial, four reflections, ten formative responses and PG contributions complete.
- [ ] Each PG member can explain their code and supervision.
- [ ] README PG note, actual integrated SHA and limitations recorded.

Unresolved issues / owner / action: [response]
Stage 11 handover references to extension, tests, dependencies and actual AI/review evidence: [response]
Submitted SHA / explanation if later than tested code: [response]
Stage 11 materials are supplied from the beginning. Begin Stage 11 only after Stage 10 has been integrated, verified and recorded. UG follows the protected common code from Stage 9 to Stage 12.
