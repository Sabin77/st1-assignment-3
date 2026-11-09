# Stage 11 PG assurance activities and evidence

PG-only stage. Undergraduate students are not required to complete this record. UG-only groups retain this supplied template unchanged as intentionally not applicable; do not fabricate N/A responses. Optional UG participation is unassessed.

Blank student template. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied file in stage11_pg/ in your EXISTING repository. Preserve project/, earlier records/tests and the protected common Stage 9 SHA. Do not copy staff references or fabricate AI evidence.

Group/tutorial: Group 501, Tuesday 1:30 PM.
Assessed PG members and contributions: Sabin Lamichhane — Stage 11 assurance planning, risk assessment, verification, Copilot supervision and evidence documentation.
Optional UG contributors: None confirmed for Stage 11.

## A Handover and human-first scope


Integrated Stage 10 code SHA / protected Stage 9 common SHA:
Stage 10 integrated SHA: `91b6dba334715653b806cc18f41fffe4fffeb246`.
Protected Stage 9 SHA: `46209c7a443de4520972c610e0a06831cea40886`.

Recoverable branch / baseline / actual commands, working directory and results:
Stage 11 branch: `feature/stage11-assurance`.
Starting SHA: `87f1f87386aea7e539492a4c57a4a82b351a65ed`.
The Stage 10 integrated full test suite was run using `py -m pytest -q` from `project/` and returned 71 passed in 0.12s.
The Stage 11 baseline was independently verified with 71 tests passing in 0.08s. Three assurance tests were subsequently added, and the full suite passed 74 tests in 0.13s.

Domain, store, services, queries, console, entry point, tests and rescheduling inspected:
Initial code inspection covered `project/smartcare/domain.py`, `project/smartcare/data_store.py`, `project/smartcare/services.py` and `project/tests/test_rescheduling.py`.
The shared in-memory store, patient search, appointment booking, cancellation, rescheduling and conflict-checking methods were examined.
Detailed inspection of queries, console, entry point and remaining tests is still pending.

Selected PG feature and common workflow / requirements / code locations:
Selected PG feature: Stage 10 appointment rescheduling, RES-01–RES-06 and RES-05-R2.
Common workflow: PatientService.find_patient(), SmartCareDataStore.find_patient(), appointment booking, cancellation and practitioner appointment listing.
Important code locations include `domain.py`, `services.py`, `data_store.py`, `queries.py` and their corresponding tests.

Actual available earlier AI, issue, PR and dependency evidence:
Stage 10 PR: https://github.com/Sabin77/st1-assignment-3/pull/18
Corrected Stage 10 implementation: `1d18d19`.
Rejected Copilot implementation: `e36ee41`.
Recovery: `82d81e5`.
Independent Stage 10 reviewer: Stanley Campbell (`s-campbell-dev`), APPROVED.

Missing evidence / honest limitation:
The original Stage 10 Copilot planning transcript, exact agent-mode version and teaching-team approval reference have not been independently confirmed.
The Stage 11 read-only Copilot audit was completed and its findings were independently assessed. Independent Stage 11 human review remains pending.

Assets and trust boundaries:
The application stores patient, practitioner and appointment objects in memory.
Important trust boundaries include user-supplied identifiers, appointment dates and times, application validation, the shared data store, console output, GitHub repository access and AI tool permissions.
No real patient records or credentials should be submitted to AI tools.

Scope, assumptions, exclusions and initial observations made BEFORE Copilot:
The assurance review will examine appointment integrity, patient search, status validation, practitioner conflicts, privacy, dependency provenance and the reliability of previous AI-assisted changes.
The application currently uses an in-memory store without persistence.
The initial code review shows existing validation and conflict-checking mechanisms that require independent assurance testing.
No production defect is confirmed at this stage.
Unrelated feature development, database redesign and unnecessary dependencies are excluded.

Confirmed Copilot mode / student entitlement / permissions / approval reference:
Not yet confirmed for Stage 11. The earlier Stage 10 interaction exposed approval-control limitations. The permitted Stage 11 route and permissions must be checked before agent actions.

Plan-only → human approval → bounded editing check / approved equivalent route:
The human-first scope and proposed assurance checks are being prepared before Copilot consultation.
Any Copilot audit must use the permitted course workflow. No Stage 11 agent editing or approval is claimed yet.

Overview/revision 2 availability / source:
Not yet verified against the supplied Stage 11 handout and available teaching materials.

Assigned PG owner / independent reviewer:
PG owner: Sabin Lamichhane (`Sabin77`).
Independent Stage 11 reviewer: To be confirmed.

## B Original tutorial activities


### B1 Risk classification

| Scenario | Risk | Why | Control |
|---|---|---|---|
| AI explains a public Python error | Low | Explaining a generic error involves no private information or repository action; the explanation can still be inaccurate. | Use sanitised examples, check official documentation and reproduce a minimal example. |
| Student pastes an API key into AI | Critical | A credential could be disclosed or retained outside the approved system and permit unauthorised access. | Never paste secrets; redact/revoke any exposed key, rotate credentials and follow incident procedures. |
| Agent proposes unknown package | High | Unverified software may be malicious, incompatible or unlicensed and introduces supply-chain risk. | Reject installation until source, version, licence, need and tutor policy are checked. |
| AI-generated code logs patient names | High | Terminal output or logs may unnecessarily disclose personal information. | Use synthetic data only, minimise outputs, inspect print/logging statements and restrict access. |
| Agent modifies deployment configuration | High | Unexpected settings can affect security, runtime behaviour, data exposure or other team members. | Apply least privilege, require prior human approval, review the full diff and preserve a rollback point. |

### B2 Green Amber Red
Choose GREEN / AMBER / RED and justify each.

| Use | Classification | Reason and policy/control |
|---|---|---|
| Ask AI to explain pytest fixture | GREEN | Low-risk conceptual support when using public or synthetic examples; independently verify the explanation. |
| Generate 100 lines of assessed domain code | AMBER | Potentially permissible only under the course AI-use policy with declared assistance, approved scope, human review and independent tests; do not claim unsupervised generated code as entirely human-authored. |
| Paste real patient record for debugging | RED | Sensitive personal information must not be submitted to AI tools; use a synthetic reproduction instead. |
| Use AI to draft test ideas then verify | GREEN | Drafting ideas is lower risk if the student checks expected behaviour, authors meaningful assertions and records AI assistance. |
| Agent autonomously deletes repository files | RED | Unapproved destructive changes can remove work and violate the human approval boundary. Require explicit authorisation and recoverable changes. |

These are risk-based classroom classifications; any more restrictive unit policy takes precedence.


### B3 VERIFY patient search
Record one concrete question/evidence item for each letter against the current PatientService/shared-store contract.

| VERIFY element | Question or evidence |
|---|---|
| Validate | Does `PatientService.find_patient()` satisfy the existing contract: stored object for known ID, `LookupError` for unknown valid ID, `ValueError` for blank/non-string ID? |
| Examine | In `services.py`, lookup delegates to `SmartCareDataStore.find_patient()` and raises `LookupError` on `None`; `data_store.py` uses `required_text()` and dictionary lookup. |
| Run meaningful tests | Existing `test_services.py` patient-lookup tests cover known, unknown, blank, surrounding-whitespace and case-sensitive IDs. The 52 common tests passed independently in 0.06s before the EOF correction. |
| Inspect risks | Verify that lookup does not construct substitute patients, modify stored records or disclose patient names unnecessarily through console output. |
| Fit architecture/policy | Lookup uses the existing shared in-memory store and service layer without adding an external API or dependency; use synthetic identities only. |
| You remain responsible | I checked the source contract and test results and recorded the privacy limitation; AI suggestions were not treated as proof. |

### B4 TRUST decision
The feature passes tests but adds an unreviewed package and logs full patient records. Should it be accepted?

| TRUST element | Reason/evidence/action |
|---|---|
| Trace | Establish the change's author, commit and reason for the new package and logging. No unreviewed changes should be silently accepted. |
| Review | Inspect all production, dependency and test diffs, including package installation and log-output statements. |
| Understand | Passing tests does not explain why an additional package is needed or why full records would be printed. |
| Secure | Reject full-record logging and assess any proposed package for security, provenance, version and licence. |
| Test | Run relevant functional, regression and privacy-oriented tests after removing unsafe behaviour. |


Decision and reason: **Reject pending remediation.** Passing functional tests does not justify introducing an unreviewed dependency or exposing full patient records. Remove the unnecessary logging, verify or reject the dependency, and independently retest before reconsidering approval.
Exit: Why is a technically correct AI-generated feature still potentially unacceptable?
A technically correct AI-generated feature may still breach privacy, licensing, security, course rules or architectural boundaries. Correctness is necessary but not sufficient for professional acceptance.


### B5 Sanitised critique only
Identify the hard-coded demo-key placeholder, unnecessary requests import, patient-ID/name logging, fabricated lookup and missing test/provenance evidence. Do not copy or run the old audit target.
This is a **sanitised hypothetical critique** based on the supplied exercise description, not a claim that these items were found in the current SmartCare repository or that the old audit target was executed.

| Concern | Observed example evidence | Severity | Correction and recheck |
|---|---|---|---|
| Hard-coded demo-key placeholder | Exercise describes a credential-like constant embedded in sample code; original target was not run or reproduced. | High if real; medium for clearly nonfunctional placeholder | Remove credential-like values from source, use approved secure configuration if required and scan diffs before acceptance. |
| Unnecessary `requests` import | Exercise describes an imported external package without a demonstrated need. | Medium | Remove the import; verify requirements and imports remain minimal. |
| Patient ID and name logging | Exercise describes printing full patient identifiers/names; actual SmartCare menu separately prints synthetic patient ID/name. | High for real data | Minimise outputs and use synthetic data. Inspect the console output and any stored logs. |
| Fabricated lookup | Exercise describes a lookup claiming to return patient data without checking the store. | High | Require store-backed lookup and tests for identity, unknown and invalid IDs; reject fabricated success paths. |
| Missing test/provenance evidence | Exercise provides no independently executed test or trusted origin for its claimed implementation. | Medium | Run meaningful tests and document version, source, author, commands and actual results. |


## C Actual risk register


| Risk | Artefact | Likelihood | Impact | Control | Status |
|---|---|---|---|---|---|
| Cancelled appointments incorrectly block rescheduling | `data_store.py`, `services.py`, `test_assurance.py` | Medium | High | Test rescheduling into a cancelled appointment's previous slot while preserving its history. | Verified: assurance test passed. No defect observed. |
| Failed rescheduling partially changes stored records | `domain.py`, `services.py`, `test_assurance.py` | Medium | High | Check original dates, statuses, object identities, participant references and listing order after a rejected conflict. | Verified: assurance test passed. No defect observed. |
| Incorrect patient lookup or unexpected record replacement | `data_store.py`, `services.py`, existing common tests | Low | High | Verify invalid and unknown IDs, and check that lookup returns the original stored Patient object. | Existing implementation inspected; dedicated Stage 11 assurance review pending. |
| Sensitive patient information exposed through logs or AI tools | `console.py`, application output, AI prompts | Medium | High | Inspect output and logging statements. Use sanitised test data and never provide real patient records or credentials to AI tools. | Privacy audit pending. |
| Unapproved external dependencies or fabricated packages | Python imports, dependency files, AI-generated suggestions | Medium | Medium | Inspect imports and dependency declarations; verify package provenance, purpose and licence before acceptance. | Dependency audit pending. |
| AI agent changes files outside approved scope | Stage 10 Copilot history and Stage 11 Git changes | Medium | High | Review changed files, restrict permissions, require human approval, and preserve recoverable Git checkpoints. | Previous Stage 10 issue documented; Stage 11 agent audit pending. |
| Regression of earlier booking and cancellation behaviour | Existing common tests and PG tests | Low | High | Run the common tests, previous PG tests and full cumulative suite independently. | Verified: 52 common, 19 previous PG, 2 assurance and 73 cumulative tests passed. |
| Unhandled EOF during an interactive operation | `project/smartcare/console.py`, `run_menu()` | Medium | Low | Verify EOF during a patient-ID prompt and assess whether graceful termination is required. | Confirmed through independent runtime reproduction. Minimal correction implemented and regression test passed. Independent review pending. |

## D Actual findings tests and corrective actions

For each of at least TWO new/materially strengthened tests, explain the earlier coverage gap and the incorrect behaviour its assertions detect. No duplicated unchanged tests. [response]

| Claim / risk / requirement | Location / version | Independent check / test | Observed result / finding or no finding | Action / owner | Recheck / limitation |
|---|---|---|---|---|---|
| Unhandled EOF during operation input | `project/smartcare/console.py`, Stage 11 branch | Independently reproduced using `unittest.mock.patch` | Confirmed unhandled `EOFError` before correction | Added graceful EOF handling and regression test; Sabin Lamichhane | 3 assurance tests and 74 cumulative tests passed after correction; independent review pending |
| Cancelled appointments must not block an available rescheduling slot | `project/tests/test_assurance.py`, commit `922bee4` | `test_cancelled_booking_does_not_block_reschedule` | No defect identified; cancelled appointment did not block the reschedule | Retained new regression coverage; Sabin Lamichhane | Passed; existing cancelled appointment remained stored |
| Failed rescheduling must preserve appointment records | `project/tests/test_assurance.py`, commit `922bee4` | `test_failed_reschedule_preserves_listing_and_store_state` | No defect identified; appointment records and listing remained unchanged | Retained new regression coverage; Sabin Lamichhane | Passed; no production correction required |

| Assurance test | Earlier gap | Input/setup | Meaningful assertion | Incorrect result detected | Evidence/result |
|---|---|---|---|---|---|
| `test_cancelled_booking_does_not_block_reschedule` | Stage 10 tested conflicts and cancellation separately but did not explicitly test rescheduling into a cancelled appointment's slot. | Two appointments for DR1 at 09:00 and 10:00; cancel the 10:00 appointment, then reschedule the 09:00 appointment to 10:00. | The reschedule succeeds; the cancelled appointment remains stored with CANCELLED status; both appointment records are retained. | A cancelled appointment incorrectly blocking an available slot, or cancellation history being deleted. | Passed — focused Stage 11 assurance suite, 2 passed in 0.03s. |
| `test_failed_reschedule_preserves_listing_and_store_state` | Stage 10 checked failed-operation state but did not explicitly compare a complete three-appointment listing and participant references before and after rejection. | Three scheduled appointments for DR1 at 09:00, 10:00 and 11:00; attempt to move A1 to the occupied 10:00 slot. | ValueError is raised; stored objects, appointment times, statuses, participant references and listing order remain unchanged. | Partial mutation, corrupted appointment order or altered stored references after rejection. | Passed — focused Stage 11 assurance suite, 2 passed in 0.03s. |
| `test_menu_handles_eof_during_operation` | The earlier tests did not verify EOF during an operation prompt. | Simulate menu option 1 followed by EOFError at the patient-ID prompt. | Menu returns normally and prints `Input closed; exiting.` without propagating EOFError. | Unhandled EOFError and unexpected termination. | Passed — 3 focused assurance tests in 0.12s; 74 cumulative tests in 0.13s. |

| Suite | Command / project working directory | Tested code SHA | Actual result | Evidence |
|---|---|---|---|---|
| Assurance focused | `py -m pytest -q tests/test_assurance.py` from `project/` | `922bee4` | 2 passed in 0.03s | PyCharm terminal output; committed assurance tests |
| Previous PG independently | `py -m pytest -q tests/test_rescheduling.py` from `project/` | `922bee4` | 19 passed in 0.03s | PyCharm terminal output |
| Common independently | `py -m pytest -q --ignore=tests/test_rescheduling.py --ignore=tests/test_assurance.py` from `project/` | `922bee4` | 52 passed in 0.06s | PyCharm terminal output |
| Full PG cumulative | `py -m pytest -q` from `project/` | `922bee4` | 73 passed in 0.08s | PyCharm terminal output |
| Integrated retest | `py -m pytest -q` from `project/` | `8ef5b2456a4acec1eb906e07d09314fda77fe5c6` | 106 passed in 0.29s | Post-merge verification on `main`; PR #21 merged |


Confirmed defect / minimal correction / before-after evidence:

The Copilot audit identified an unhandled EOFError during an interactive operation in `project/smartcare/console.py`.

I independently reproduced the defect using `unittest.mock.patch` with menu option 1 followed by EOFError. The observed output was:
`CONFIRMED: unhandled EOFError during operation`

I then added an EOFError handler within the operation exception-handling block of `run_menu()` so the application displays `Input closed; exiting.` and returns gracefully.

I added `test_menu_handles_eof_during_operation` to `project/tests/test_assurance.py`.

Post-correction results:
- Stage 11 assurance tests: 3 passed in 0.12s.
- Full cumulative test suite: 74 passed in 0.13s.
- No test failures observed.

This correction was verified locally. Independent review and post-merge testing are pending.

Preserved earlier assertions / inspected test diff:
The Stage 11 commit adds `project/tests/test_assurance.py` without modifying existing test files. The earlier common and PG suites remained passing.

Unresolved failures, action and owner:
No automated test failures remain. Dependency, privacy, Copilot audit and independent review evidence still require completion. Owner: Sabin Lamichhane.

## E VERIFY assessment


| VERIFY element | Evidence | Finding/action |
|---|---|---|
| Validate against requirements | Reviewed patient lookup, booking, cancellation and RES-01–RES-06 with RES-05-R2. | Existing behaviour is supported by regression tests; Stage 11 adds assurance coverage for cancellation history and failed rescheduling. |
| Examine implementation | Inspected domain, service and shared-store logic, including appointment status checks and practitioner conflicts. | No production defect confirmed by the two new assurance scenarios. |
| Run meaningful tests | 3 Stage 11 tests passed; 19 previous PG tests and 52 common tests passed in earlier separate runs; the full cumulative suite passed 74 tests.| Accept tested behaviour. Integrated Stage 11 retest remains pending. |
| Inspect risks and assumptions | Reviewed console output, sensitive identifiers, dependency declarations and AI permissions. | Record patient-information disclosure risk and the synthetic-data-only limitation. |
| Fit architecture and policy | New tests were added without changing production modules or adding dependencies. | Existing in-memory architecture preserved. Agent permission and teaching-policy evidence remain incomplete. |
| You remain responsible | Sabin reviewed the test evidence, repository changes and audit limitations. | Require independent human review before Stage 11 integration. |

## F TRUST assessment


| TRUST element | Evidence | Status/action |
|---|---|---|
| Trace | Stage 10 implementation and Stage 11 assurance changes are linked to identifiable Git commits and PR evidence. | Traceable code history; original Copilot interaction provenance remains incomplete. |
| Review | Source inspection covered validation, service coordination, stored state and console output. | Initial review complete; independent Stage 11 review pending. |
| Understand | Appointment rescheduling preserves existing objects and checks practitioner conflicts before mutation. The store remains session-only. | Behaviour understood within the assessed scope. |
| Secure | Console inspection identified patient names and identifiers in output. No new runtime dependencies were found. | Accept only as a synthetic-data teaching application; privacy limitation remains. |
| Test | Three assurance tests passed, including the EOF regression test.| The full cumulative suite passed 74 tests. |

## G GitHub Copilot audit

Sanitised material / actual prompt, context, version and response links:
A read-only SmartCare assurance audit was requested from GitHub Copilot. The prompt instructed Copilot to examine patient lookup, appointment booking, cancellation, rescheduling, console output, dependencies and tests; distinguish observed defects from speculation; and avoid modifying, committing or pushing files.

Copilot identified seven findings covering console privacy, EOF handling, test coverage, rescheduling conflict checks, scheduling assumptions and dependency provenance.

Copilot reported auditing `main` at `87f1f87386aea7e539492a4c57a4a82b351a65ed`. The exact Copilot version/mode and a persistent link to the original chat response have not yet been recorded. A screenshot or saved transcript of this actual interaction should be retained as supporting evidence.

Evidence that human scope and initial observations preceded Copilot:
Before requesting the Stage 11 audit, I reviewed the existing SmartCare implementation, identified integrity and privacy risks, and created two additional assurance tests.

The tests were committed as `922bee4`. They covered cancelled-slot reuse during rescheduling and preservation of appointment records after a failed rescheduling attempt.

The assurance tests passed independently, and the complete suite passed 73 tests before the Copilot audit response was reviewed.

Actual supported route or approved equivalent / access limitations:
Copilot was instructed to perform a read-only audit without changing repository files. The response stated that no files were modified and no tests were run.

The audit examined the older `main` checkpoint rather than the current Stage 11 assurance branch. Its findings were therefore checked against the newer Stage 11 test commit before being accepted.

The exact approved Copilot mode, permission configuration and teaching-team approval reference remain unconfirmed.

Significant earlier AI contributions reviewed / available evidence / missing provenance:
Stage 10 included an incorrect Copilot-generated implementation, which was rejected and reverted before the manually corrected rescheduling implementation was reviewed and merged.

Stage 10 evidence:
https://github.com/Sabin77/st1-assignment-3/pull/18

Stage 11 assurance commit:
https://github.com/Sabin77/st1-assignment-3/commit/922bee48b61d83db77abcc470fd8a8ca9a5f3bfc

The original Stage 10 agent transcript and the Stage 11 Copilot audit transcript are not yet linked as independently accessible artefacts.

| AI claim | Affected requirement/code/evidence | Observed vs speculative / human verification | Severity / Accept Modify Reject / reason | Outcome / correction or no change | Recheck / limit |
|---|---|---|---|---|---|
| Console prints patient names and IDs | `project/smartcare/console.py`, `run_menu()` | Confirmed by source inspection: registration and lookup print patient identifiers and names. | Medium / Accept — privacy exposure depends on terminal access and actual data entered. | Retain synthetic-data-only restriction and record privacy risk. No production change made. | Real clinical deployment would require stronger privacy controls. |
| EOF during an operation prompt is not handled | `project/smartcare/console.py`, `run_menu()` | Independently confirmed using `unittest.mock.patch`; EOFError propagated before correction. | Low / Accept — confirmed robustness defect. | Added graceful EOF handling and a regression test. | 3 assurance tests and 74 cumulative tests passed after correction; independent review pending. |
| Console lacks dedicated test coverage | Console input/output tests | Copilot did not run tests. The submitted evidence does not independently prove every console interaction is untested. | Low / Modify — treat as a test-coverage concern rather than proof of a functional defect. | Record limitation and consider targeted console tests if required by the approved scope. | Complete test inventory or coverage measurement not performed. |
| Cancelled/completed destination slots are not explicitly tested | `data_store.py`, `test_rescheduling.py`, `test_assurance.py` | Copilot audited older main SHA `87f1f87`. Stage 11 commit `922bee4` already adds and passes the cancelled-destination-slot test. | Low / Modify — cancelled-slot gap has been addressed; completed-slot case may remain separate. | Accept the already completed cancelled-slot assurance test; do not duplicate it. | 2 Stage 11 tests passed; completed-slot destination case not separately verified. |
| Scheduling rules omit duration, patient conflicts and past-date checks | `project/README.md`, conflict checking | README explicitly documents these exclusions. | Reject as a defect — the current behaviour is consistent with the documented scope. | No expansion of requirements or production changes. | Revisit only if authoritative assignment requirements say otherwise. |
| Direct domain rescheduling bypasses service conflict checking | `domain.py`, `services.py` | Confirmed architectural separation: domain validates local state, while service checks the shared store. | Low / Accept as limitation, not a confirmed service defect. | Keep supported application operations through AppointmentService. | Direct callers bypassing the service are outside the verified service workflow. |
| Dependency provenance remains incomplete | `requirements-dev.txt`, README | `pytest==8.3.5` is declared; inspected runtime code uses standard-library and local modules. | Low / Accept as provenance limitation, not evidence of an unapproved dependency. | No new dependency introduced. Record incomplete licence/source verification. | Package provenance and licence not independently verified. |

No false/rejected suggestion, if applicable:
The suggestion that the cancelled-slot case lacked coverage became outdated because Copilot inspected the earlier `main` checkpoint rather than the Stage 11 branch. The committed `test_cancelled_booking_does_not_block_reschedule` test verifies that scenario and passed.

The claim that missing duration, past-date and patient-conflict rules constituted a potential defect was also rejected as a requirement expansion. Those rules are explicitly excluded by the existing SmartCare README.

Copilot's findings were therefore reviewed against actual source files, the documented requirements and the newer committed tests instead of being accepted automatically.
## H Dependency provenance and privacy review


| Dependency/artefact | Source | Purpose | Licence/provenance | Verified? | Decision | Evidence link |
|---|---|---|---|---|---|---|
| Python standard library | Python 3.13 environment | Datetime handling, regular expressions, command-line parsing and application operations | Python standard-library provenance; individual environment installation not separately audited | Yes, source imports inspected | Accept | `project/smartcare/console.py`, `project/main.py`, `project/smartcare/domain.py` |
| pytest 8.3.5 | `project/requirements-dev.txt` | Development testing | Version pinned to 8.3.5; package licence not independently checked in this audit | Version declaration verified | Accept for existing development tests; retain provenance limitation | `project/requirements-dev.txt` |
| SmartCare local modules | Existing Group 501 repository | Patient, practitioner and appointment operations | Existing repository source and Git history | Yes | Accept for the assessed project | https://github.com/Sabin77/st1-assignment-3 |
| Stage 10 rescheduling | Stage 10 PR #18 | Guarded appointment rescheduling | Previously reviewed and merged implementation | Yes | Accept for assurance baseline | https://github.com/Sabin77/st1-assignment-3/pull/18 |
| Stage 11 assurance tests | Stage 11 commit `922bee4` | Additional integrity and regression checks | Group 501 repository; new test source recorded in Git | Yes | Accept | https://github.com/Sabin77/st1-assignment-3/commit/922bee48b61d83db77abcc470fd8a8ca9a5f3bfc |

Actual runtime imports / test-tool dependencies / versions checked:
The code inspection found standard-library imports, including `datetime`, `re` and `argparse`, together with local SmartCare modules. The only declared development dependency is `pytest==8.3.5`. No additional third-party runtime package was identified in the inspected files. An independent installed-package inventory and licence check have not been completed.

Secret/data/output/input/permission/minimisation checks and evidence:
A PowerShell source scan searched for print statements, logging, requests, API keys, tokens and passwords.

The scan identified console output of patient identifiers and names during registration and lookup. Appointment formatting also exposes patient and practitioner identifiers, appointment times and status.

These outputs are part of the interactive teaching application, but they represent a privacy concern if real patient information were entered.

No API key or password match was returned by this keyword scan. This does not establish that the entire repository is free of secrets.

The application should use synthetic records only. Real patient records and authentication credentials must not be placed in AI prompts, screenshots or public repository evidence.

Requirements/model/code/tests/Stage 10 provenance links:
Repository: https://github.com/Sabin77/st1-assignment-3
Stage 9 PR: https://github.com/Sabin77/st1-assignment-3/pull/17
Stage 10 PR: https://github.com/Sabin77/st1-assignment-3/pull/18
Stage 11 assurance commit: `922bee4`.

Bias/hidden assumptions / name formats / unnecessary fields / accessibility / scheduling policy:
The application validates patient and practitioner names as non-blank text but does not implement comprehensive real-world identity verification or privacy controls.

Scheduling validation requires naive datetimes at minute precision. The application does not implement timezone conversion, appointment duration, patient availability or broader clinical scheduling policies.

The text-based interface may have accessibility limitations. These are outside the bounded Stage 11 code changes but should be acknowledged before any real-world deployment.

Policy questions or unresolved provenance / responsible contact:
The original Copilot interaction transcript, exact agent permissions and teaching-team approval reference remain unverified. Package licence verification and a comprehensive security audit are also outstanding.

Responsible PG member: Sabin Lamichhane. Any additional course-policy or approved-agent-route questions should be referred to the tutor or unit convenor.

## I Independent review and final audit statement

Human reviewer / PR or diff link / feedback:
Stanley Campbell (`s-campbell-dev`) independently reviewed Stage 11 PR #21 and approved the final implementation commit `e83b9d8`. He ran the full test suite and confirmed 74 tests passed. His review covered the EOF correction, three assurance tests and Stage 11 evidence document.
Review: https://github.com/Sabin77/st1-assignment-3/pull/21

Corrections and recheck / approval before integration:
The original EOF defect was reproduced, corrected and regression-tested. Stanley approved the final Stage 11 PR. After merging, I ran `py -m pytest -q` from `project/` on the integrated main branch and obtained 106 passed in 0.29s.

Accountable reviewer and PG member sign-off:
PG owner: Sabin Lamichhane.
Independent human reviewer: Stanley Campbell (`s-campbell-dev`), APPROVED on PR #21.

Integrated PG SHA / protected common SHA:
Stage 11 integrated SHA: `8ef5b2456a4acec1eb906e07d09314fda77fe5c6`.
Protected Stage 9 common SHA: `46209c7a443de4520972c610e0a06831cea40886`.

## J Reflections

1. **Which risk would have been easy to miss if you only checked whether tests passed?** The original 71 tests passed, but a read-only Copilot review pointed out that an EOF during a patient-ID prompt could crash the menu. I reproduced the error before correcting it. Likewise, a test result alone would not reveal that patient names are printed to a console or that dependency provenance is incomplete. This showed me why security, privacy and code inspection matter alongside automated tests.

2. **Which AI audit finding was false or overstated? If none, state honestly and explain verification.** The audit reported missing coverage for rescheduling into a cancelled slot. That was accurate for the older `main` checkpoint it inspected, but not for our Stage 11 branch, where I had already added and passed that assurance test. The suggested scheduling-policy gaps (appointment duration, patient conflict and past-date checks) were also not confirmed defects because the README excludes those features. I compared the claims against the actual branch, tests and documented requirements before deciding.

3. **What evidence supports your final trust decision?** I used the actual source files and Git history, independent PowerShell regression runs, an intentional pre-fix EOF reproduction, a corrective regression test and a critical review of Copilot's findings. The latest local verification showed 3 assurance tests and 74 total tests passing. I still regard the work as requiring independent Stage 11 review and post-merge testing; I would not describe it as fully approved before those checks occur.


## K Ten formative questions


1. **What does least privilege mean?** Give an AI agent or person only the minimum permissions needed. For a read-only audit, it should inspect and report rather than edit, commit or push.

2. **What is provenance in AI-assisted software engineering?** Provenance is the traceable origin and history of code, data, dependencies and AI suggestions, supported by commits, prompts, versions and review records.

3. **What is data minimisation?** Collecting, processing and displaying only information necessary for the task. For SmartCare teaching work, synthetic patient records and minimal console output reduce exposure.

4. **What is dependency hallucination?** When an AI proposes or describes a package, API or version that does not exist, is unnecessary or is unsupported by evidence. Its source and suitability must be checked before use.

5. **What is software supply-chain risk?** Risk introduced through external packages, build tools, sources or updates, including compromised code, licences, insecure versions and unverified maintainers.

6. **What does the VERIFY framework ask students to do?** Validate claims against requirements, examine the code, run meaningful tests, inspect risks, check architectural/policy fit and retain human responsibility.

7. **What does the TRUST framework ask students to do?** Trace the origin, review changes, understand behaviour, assess security and test claims independently before accepting work.

8. **What does an AMBER AI-use classification mean in this course?** A use requiring care and controls rather than automatic acceptance: check unit rules, limit scope, review the result, independently test it and declare assistance where required. The official course policy takes precedence over this risk-based interpretation.

9. **Who remains responsible for professionally accepted AI-assisted software?** The human developer, reviewer and accountable team, not the AI tool.

10. **What is the Stage 11 engineering rule?** Do not trust a feature merely because AI says it works or tests pass. Verify scope, provenance, privacy, security, meaningful behaviour and human approval, and document unresolved limitations.


## L Completion and Stage 12 handover

- [x] Actual SmartCare scope and human-first observations recorded.
- [x] All tutorial activities and every VERIFY/TRUST element completed in the evidence record.
- [x] At least two meaningful assurance tests with added-value explanations; three local tests passed after the EOF correction.
- [x] Actual findings/no-findings and corrective actions or no-change rationale recorded.
- [x] Earlier assertions retained; common and previous PG suites passed independently before the EOF correction, and full cumulative suite passed after it.
- [x] Copilot claims independently checked; accept/modify/reject decisions and limitations recorded honestly.
- [x] Dependency/provenance/privacy review and residual limitations recorded, including unresolved provenance details.
- [x] Independent Stage 11 human review, integration and post-merge retest recorded.
- [x] All three reflections and ten formative responses answered.
- [x] Final accountable reviewer approval and Stage 11 integrated handover completed.

Unresolved issues / owner / handover action: Sabin Lamichhane must commit and push the latest EOF correction and evidence, request a new independent Stage 11 PR review, address feedback, merge only with valid approval and rerun the full suite on `main`. The original Copilot audit transcript should be saved if available. No approval or integration is invented.

Tested code SHA / command / working directory / observed result: Before the EOF correction, Stage 11 test commit `922bee48b61d83db77abcc470fd8a8ca9a5f3bfc` was based on 87f1f87; the user reported `py -m pytest -q tests/test_assurance.py` (2 passed in 0.03s), separate Stage 10 tests (19 passed in 0.03s), separate common tests (52 passed in 0.06s), and full suite (73 passed in 0.08s), all from `project/`. After the local EOF correction and third test, `py -m pytest -q tests/test_assurance.py` returned 3 passed in 0.12s and `py -m pytest -q` returned 74 passed in 0.13s. The SHA containing the latest edits is not yet confirmed.

Final submitted SHA / later evidence-only change explanation:
The verified Stage 11 integration SHA was `8ef5b2456a4acec1eb906e07d09314fda77fe5c6`. The integrated suite passed 106 tests in 0.29s. Any subsequent documentation-only commit must be recorded separately as the final submitted SHA.
Stage 12 handover links to same project/tests/assurance conclusion and limitations: Repository https://github.com/Sabin77/st1-assignment-3 ; initial Stage 11 test commit https://github.com/Sabin77/st1-assignment-3/commit/922bee48b61d83db77abcc470fd8a8ca9a5f3bfc ; Stage 10 PR https://github.com/Sabin77/st1-assignment-3/pull/18 . Stage 11 PR https://github.com/Sabin77/st1-assignment-3/pull/21. The Stage 12 team should work from the final reviewed and integrated Stage 11 SHA only, preserve the protected Stage 9 pathway and 74-test suite (or the actual integrated count), and note the synthetic-data and provenance limits.

Begin Stage 12 after the previous applicable stage is integrated, verified and recorded. Its handout and blank record are already supplied.
