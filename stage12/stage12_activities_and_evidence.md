# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: [Tuesday 1:30 PM]
Members and UG/PG applicability: [Stanley Campbell (UG), Shaban Mohseni (UG), Nhat Minh Le (UG), Sabin Lamichhane (PG)]


## A Release scope and starting SHA

Release label/version and requirements baseline: [SmartCare A3 Stage 12 RC1]
Common starting SHA / branch / applicable members: [46209c7a443de4520972c610e0a06831cea40886,(Merge of PR #17, Stage 9) on main; All four members. Re-run at this SHA: 52 Passed]
PG starting SHA / branch / applicable members or not applicable: [87f1f87386aea7e539492a4c57a4a82b351a65ed (main, Stage 10 integrated via PR #18); Sabin Lamichhane. Stage 11 assurance tests exist only on origin/feature/stage11-assurance (922bee4, adds project/tests/test_assurance.py).
Working-state review and approved integration: [Main was cloned clean (no uncommitted changes). Release corrections were made on release/stage12 from 87f1f87, requires team conformation to integrate release/stage12 into main.]
Protected common candidate and PG differences: [The common behaviour is unchanged from 46209c7; PG adds Appointment.reschedule, AppointmentService.reschedule_appointment, tests/test_rescheduling.py (19 tests) and the README section. The 52 common tests pass on both the common SHA and the release candidate.]
Feature freeze / owner / verifier: [freeze at 87f1f87; after it only release corrections (no new behaviour). Owner Shaban Mohseni. It is required per team to confirm verifier name and freeze date.]


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: [Do not release (yet). Passing tests show only that the tested behaviour works. A user cannot reproduce the setup, an unreviewed dependency is an unassessed supply-chain risk, and an undocumented limitation misleads users. All three are quick to fix; once the README is completed, the dependency is reviewed (or removed) and the limitation documented, the candidate can be re-assessed for release with documented limitations.]

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works | [test_cancelled_appointment_is_retained_in_history, test_stage7_cancelled_slot_can_be_rebooked_with_history_retained] | [test_services.py, RC] | [Shaban Mohseni/ Team to Confirm] | [Yes] | [None] |
| Architecture responsibilities are appropriate | [Code review E; domain / store / services / queries / console separation] | [smartcare/, RC] | [[Shaban Mohseni/ Team to Confirm] | [Yes] | [Store lookups made consistent (H-1)] |
| Rescheduling is safe — PG only | [19 tests in test_rescheduling.py (identity, conflict, status, no-op, slot release, ordering)] | [RC] | [Stanley Campbell reviewed PR #18 (Stage 10 record)] | [Yes for RES-01–06] | [Not in console menu] |
| AI use is responsible — common recheck / PG assurance | [Copilot decisions in Stage 6–10 records; Stage 11 not integrated] | [stage06/–stage10_pg/] | [Shaban Mohseni/ Team to Confirm] | [Partialy] | [Stage 11 assurance must be integrated and recorded for PG] |
| System is maintainable | [Docstrings, type hints, enum use, README structure] | [RC] | [Team to Confrim] | [Yes after H-1/H-2] | [None] |
| FR-01–03 register/find and validation | [test_domain.py field tests; test_find_patient_*, test_find_practitioner_*, duplicate tests] | [RC] | [Team to Confirm] | [Yes] | [None] |
| FR-04–05 booking/conflict rules | [test_stage7_same_practitioner_exact_time_conflict_preserves_store, test_stage7_different_practitioner_same_time_allowed, test_stage7_same_practitioner_different_minute_allowed] | [test_services.py, RC] | [Team to Confirm] | [Yes] | [None] |
| FR-06–08 cancellation/history/find | [test_cancel_* (6 tests), retained-history tests] | [test_services.py, RC] | [Team to Confirm] | [Yes] | [None] |
| FR-09 and QRY/FP listing/filter/order/purity | [select_appointments / appointment_sort_key pure query; test_lookup_and_listing_show_updated_order; demo listing steps] | [queries.py, RC] | [Team to Confirm] | [Partly] | [No dedicated unit test of query purity in the current suite; covered by demo and service tests] |
| UI full console sequence and error recovery | [Scripted run of python main.py --interactive] | [stage12/demo_console_transcript.txt] | [Team to Confirm] | [Yes] | [Console has no automated test (limitation)] |
| Session-only scope / FR-10 retired | [In-memory dicts only; README limitations; demo prints session-only notice] | [data_store.py, project/README.md, RC] | [Team to Confirm] | [Yes] | [None] |
| PG RES and assurance integration | [RES tests pass in full suite; assurance tests pass when added but are unmerged] | [RC; origin/feature/stage11-assurance 922bee4] | [Team to COnfirm] | [No (assurance)] | [Integrate and record Stage 11 before PG release] |


## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | [As above] | [project/, python -m pytest -q] | [46209c7] | [52 passed in 0.07s] | [Re-run in this stage] |
| Complete PG if applicable | [As above] | [project/, python -m pytest -q] | [87f1f87 (before corrections)] | [71 passed in 0.10s; with unmerged test_assurance.py added: 73 passed] | [Re-run in this stage] |
| Affected focused checks after correction | [As above] | [project/, python -m pytest -q tests/test_services.py tests/test_rescheduling.py] | [842de68] | [46 passed in 0.02s] | [Release correction commit] |
| Full integrated recheck | [As above] | [project/, python -m pytest -q] | [842de68] | [71 passed in 0.03s] | [Release correction commit] |


Prior assertions preserved / reviewed test diff: [no test file was changed (git diff 87f1f87 842de68 -- project/tests is empty). Common tests run independently on the RC (test_domain.py test_services.py test_starter.py): 52 passed; rescheduling only: 19 passed.]


Remaining failure / limitation: [no failing tests. The console menu is checked by a scripted run only, and the Python 3.13 run has not been confirmed in this stage.]


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | [Clinic reception staff booking practitioners for patients; patients and practitioners as affected parties] | [Overview problem statement] | [Explained verbally] | [Viva] |
| Register and find Patient and two Practitioners | [P1 Alex Example; DR1 Taylor Example (General practice); DR2 Jordan Example (Physiotherapy)] | [FR-01–03] | [Registered and found P1 and DR2] | [Transcript lines 1–5] |
| Valid booking | [A1, P1, DR1, 2026-10-01 09:00] | [FR-04] | [Booked: A1 … scheduled] | [Transcript line 6] |
| Same practitioner exact-time conflict rejected | [A2, P1, DR1, 2026-10-01 09:00] | [FR-05, AC-04.2] | [Error: Practitioner already has a SCHEDULED appointment at this time] | [Line 7] |
| Different practitioner same time allowed | [A3, P1, DR2, 2026-10-01 09:00] | [AC-04.2] | [Booked: A3 … DR2 … scheduled] | [Line 8] |
| Cancel SCHEDULED and retain/find CANCELLED object | [Cancel A1, then list DR1 (all)] | [FR-06, FR-07] | [Cancelled: A1 … cancelled; A1 still listed as cancelled] | [Lines 10, 13–14, 22–23] |
| Invalid/repeated cancellation rejected | [Cancel A1 again; cancel ZZ] | [FR-06] | [Only SCHEDULED appointments may be cancelled; Appointment not found] | [Lines 11–12] |
| Default all-status listing | [DR1, blank status] | [FR-09] | [A4 (08:00) then A1 (09:00, cancelled)] | [Lines 13–14] |
| Explicit filtering / empty vs unknown / deterministic order | [DR1 cancelled; DR2 completed; DRX all] | [FR-09, QRY] | [Only A1; No appointments found.; Practitioner not found; ordered by time then ID] | [Lines 15–17] |
| Invalid date/status/menu/lookup recovery and continued operation | [Status pending; date 2026-13-01 09:00; patient NOPE; menu 9] | [UI recovery] | [Clear error each time; the menu continued and a later listing worked] | [Lines 18–23] |
| Session-only limitation and normal exit | [Option 8; python main.py demo] | [FR-10 retired] | [Session ended.; demo prints Session-only data: records are lost on exit.] | [Line 24; demo run] |
| One meaningful requirement-linked pytest test explained | [test_stage7_cancelled_slot_can_be_rebooked_with_history_retained] | [FR-07, AC-04.2] | [Asserts that the cancelled A1 remains in the store as CANCELLED and that its slot can be rebooked; this would fail if cancellation deleted A1 (F8-01) or if the conflict rule counted cancelled appointments] | [test_services.py:347] |
| Architecture and one actual AI decision / known limitation | [Domain/store/service/query layers; Stage 10 Copilot commit e36ee41 reverted (82d81e5) and reimplemented manually] | [Responsible AI] | [Decision recorded in the Stage 10 record] | [stage10_pg/] |
| PG reschedule identity/participants/time and no-op | [Service-level tests] | [RES-01–03] | [Passing: test_successful_reschedule_preserves_identity, test_same_time_no_op] | [test_rescheduling.py] |
| PG conflict/invalid status/failure non-mutation | [Service-level tests] | [RES-04–05] | [Passing: test_same_practitioner_conflict_rejected, test_cancelled_…, test_completed_appointment_cannot_reschedule, test_invalid_datetime_rejected] | [test_rescheduling.py] |
| PG old slot / current lookup/list ordering / assurance risks | [Service-level tests] | [RES-06, RES-05-R2] | [Passing: test_successful_move_frees_original_slot, test_lookup_and_listing_show_updated_order; assurance tests not yet merged] | [test_rescheduling.py] |

Stable demo owner / fresh process / command: [Requires team confirmation; fresh process, python main.py --interactive from project/. ]

PG demonstrations through service/tests or not applicable: [through the service and tests/test_rescheduling.py, because rescheduling is not in the menu.]


## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | [domain.py, services.py, queries.py] | [No finding. The domain guards transitions, services coordinate, and the query returns a new sorted list without mutation or I/O] | [No change] |
| PascalCase and snake_case naming | [All modules] | [No finding] | [No change] |
| Useful type hints and meaningful docstrings | [data_store.py find_appointment, has_practitioner_conflict] | [Both lacked docstrings after the Stage 8 repairs] | [Docstrings added (H-1); 71 passed] |
| Four-space indentation and imports/layout | [main.py] | [Missing two blank lines before if __name__; stale docstring ("intentionally incomplete" menu)] | [Corrected (H-3)] |
| Focused methods / duplication / dead or commented code | [data_store.py] | [find_appointment used a linear scan and duplicated the blank-ID check, unlike the other find methods; conflict check used the magic string "scheduled"] | [Changed to a dict lookup with required_text and AppointmentStatus.SCHEDULED (H-1)] |
| Globals / leakage / unnecessary inheritance or frameworks | [All modules] | [No globals or inheritance; there is one known minor duplication: the status guard appears in both Appointment.reschedule and the service] | [Accepted as debt (G)] |
| No SQLite/persistence/repository ABCs/speculative features | [smartcare/] | [No finding; standard library only] | [No change] |
| Synthetic data / secrets / dependencies / provenance | [Repository tree, requirements-dev.txt] | [Only synthetic names and no secrets. The only dependency is pytest==8.3.5. .idea/ IDE metadata was tracked] | [.idea/ untracked and ignored (H-4)] |
| Significant common Copilot contributions and human verification | [Stage 6–9 records] | [Recorded per stage; Copilot review comparisons are in the Stage 6 record] | [No new AI-generated code in Stage 12] |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | [Stage 10 record; Stage 11 record] | [Stage 10 records an unapproved Copilot commit that was reverted. The Stage 11 VERIFY/TRUST record is blank on main] | [PG release blocked until Stage 11 is completed (J)] |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| [Stage 10 Copilot implementation (e36ee41) presented as ready] | [RES-01–06; services.py, domain.py] | [Diff review against RES requirements and the approval workflow (Stage 10 record)] | [Rejected: committed before approval and incomplete] | [Reverted in 82d81e5; manual reimplementation 1d18d19; 19 RES tests pass] |

- Any suggestions used during the stage 12 review; none were used for the corrections in H, but team confirmation is required. 

Access route or approved equivalent / limitations: [GitHub Copilot]

Available AI evidence and missing evidence honestly disclosed: [the available evidence is the Copilot decisions in the Stage 6 and Stage 10 records and commits e36ee41/82d81e5., Though links or references to saved copilot prompts/outputs are not in the repository.]


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | [project/README.md › intro, Included scope] | [Shaban Mohseni; Requires team confirmation] | [Rewritten; it previously described the Stage 6 starter TODOs] |
| Out-of-scope capabilities and known limitations | [Out of scope and known limitations] | [Shaban Mohseni; Requires team confirmation] | [Added] |
| Confirmed teaching Python version and dependency installation | [Setup] | [Shaban Mohseni; Requires team confirmation] | [Present (Python 3.13, pytest 8.3.5, pip install -r requirements-dev.txt)] |
| Working directory / demo / interactive / test commands | [Setup] | [Shaban Mohseni; Requires team confirmation] | [--interactive was previously undocumented; added] |
| Repository structure and architecture responsibilities | [Structure and responsibilities] | [Shaban Mohseni; Requires team confirmation] | [Updated to include queries.py and the PG tests] |
| Responsible AI summary / synthetic-data rule | [Responsible AI and data] | [Shaban Mohseni; Requires team confirmation] | [Added] |
| Release label/version and SHA links | [project/README.md header; root README group index] | [Shaban Mohseni; Requires team confirmation] | [Label added; root index completed with the tested SHA] |

Root README index and project/README verified: [links to project/README.md and all stage records resolve to existing files. The group index has been completed.]


Fresh clone or extracted ZIP / candidate identity: [a fresh clone of main was tested at 87f1f87; the git archive ZIP of the candidate was extracted and tested (K).]


Verifier and clean environment / actual version: [he check ran on a clean Linux VM with Python 3.11.17 and pytest 8.3.5. ; verification on Python 3.13.]


Setup/run/test commands and observed results: [pip install pytest==8.3.5 succeeded; python main.py printed the A1 demo line and the session-only notice; python -m pytest -q returned 71 passed]


Missing local file or setup gap / remedy and recheck: [the project README was outdated (remedied, H-2). No missing files were found.]


## G Known limitations debt and release notes

Delivered features: [patient/practitioner registration and lookup; booking with the practitioner exact-time conflict rule; cancellation with retained history; ordered, filterable practitioner listing; interactive menu; PG guarded rescheduling.]


Important fixes: [F8-01, cancelled appointments hidden by store lookup (code fix 74e7011; e22c410, cited in the Stage 8 record, changes only that record), integrated via PR #13; F8-02, reversed practitioner comparison in the conflict check (42b858c, PR #13). Both are confirmed present in the RC code and covered by the passing Stage 7 tests.]


Architecture/quality improvements: [store lookups made consistent with enum-based status checks; README rewritten; IDE metadata removed from version control.]


Known limitations: [in-memory session only; no menu option for rescheduling or direct appointment lookup; naive local minute-precision times; no durations.]


AI-assisted development note: [Copilot was used for review comparisons and the Stage 10 plan/proposal. The Stage 10 Copilot commit was rejected and reverted; all accepted code was human-reviewed and verified by tests.]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| [] | [PG feature usable only via the service] | [Medium] | [Add a menu option and a console test] | [Accepted; not required by RES scope] |


Session-only synthetic data and minute-precision local time: [accepted scope limits (FR-10 retired; validate_date_time rejects seconds and time zones]


Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [out of scope and excluded.]


Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [single-user console, no time-zone policy, no monitoring, plain-text interface without an accessibility review.]


Difference between accepted scope limit and unresolved required behaviour: [a scope limit (such as no persistence) was agreed and documented; unresolved required behaviour would be a failing requirement. None was found for the common scope; the PG Stage 11 assurance is unfinished required work.]


PG assurance residual risks / owner / status or not applicable: [Stage 11 not integrated; owner Sabin Lamichhane; status open.]


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| [response] | [find_appointment scanned a list and repeated blank-ID validation; has_practitioner_conflict compared status.value == "scheduled"; neither had docstrings] | [Low; risk of drift from the enum] | [Release owner; refactor without behaviour change] | [data_store.py: dict .get(required_text(...)); any(...) with AppointmentStatus.SCHEDULED; docstrings] | [Same error message confirmed for '', spaces, None, 5; focused 46 passed; full 71 passed (842de68)] | [None] |


Justified no-change conclusion if no defect found: [no functional defect was found in the common or PG behaviour; all corrections are structural or documentation-only, and no test was modified.]


Release blockers still open / status: [1- Stage 11 PG assurance not integrated or recorded (PG only). 2- Independent human review and merge of release/stage12 pending.]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [earlier integrations: PR #13 (Stage 8), #16/#17 (Stage 9), #18 (Stage 10). Stage 12 diff: 87f1f87..842de68 on branch release/stage12.]


Independent reviewer / feedback / response: [Requires Team Consultation]


Integration commit / full recheck: [merge SHA on main; rerun python -m pytest -q (expected 71 passed for the common + PG suite)]]


Tracked and untracked file inspection / cleanliness: [git status was clean after the commit; tracked files are the root README, .gitignore, project/ and the stage folders only.]


Secrets/staff material/caches/tool-metadata exclusion check: [o .env, __pycache__, .pyc, Stage 8 utility or recovery folders are tracked; .idea/ was removed (H-4).]


Candidate recovery plan / known-good SHA: [known-good common 46209c7, PG 87f1f87; recover with git checkout <sha> or git revert of the release commit.]


Named substantive contributions: [From Git history: Stanley Campbell (25 commits; Stage 6 issues/PRs, PR #18 review), Sabin Lamichhane (15 commits; Stage 7, Stage 10, Stage 11 branch), Nhat Minh Le (minhleee5/Nhat, 15 commits; Stage 8–9, PR #13/#17 merges), Shaban Mohseni (AceOfSpade-Py,11 commits; Stage 12 owner).]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [READY WITH DOCUMENTED LIMITATIONS (common) and NOT YET READY (PG) until Stage 11 is integrated, Stage 11 is yet to be compeleted and final review requires team confirmation]


Approver / date / rationale and evidence: [approver and date.] Rationale: all 71 tests pass, the demo meets every common requirement, and the limitations are documented; the PG assurance evidence is incomplete.]


What risks remain / conditions / owners: [Stage 11 integration (Sabin Lamichhane); Python 3.13 verification and PR review of release/stage12, to which requires team confirmation]


Can the team explain the system: [Yes]


Can a change be recovered: [yes; known-good SHAs and the recovery commands are in I.]


Common decision / PG decision where different: [common release with limitations; PG held.]


## K Final tested release SHA

Exact common tested SHA: [842de684735dea316765edb567ec10103c1a6a3a (common tests: 52 passed); protected Stage 9 common SHA 46209c7 (52 passed).]


Exact PG tested SHA or not applicable: [842de684735dea316765edb567ec10103c1a6a3a (71 passed). This excludes the unmerged Stage 11 tests.]


Final submitted SHA / repository URL: [[response](https://github.com/Sabin77/st1-assignment-3), team to confirm: SHA on main after merging and the evidence-only commit]


Evidence-only later commit and difference explanation: [the commit that adds this record, stage12/demo_console_transcript.txt and the root README index changes only Markdown/text, not executable code.]


Executable changes after testing and re-verification: [none after ( When you make changes, and no change is required after ( place the latest Verification Here(  ) ]


Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [Require team confirmation]


Deadline/timezone: [response]


Repository access arrangement: [response]


Mixed-candidate upload arrangement: [response]


Oral/video recording/accessibility arrangements: [response]


Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? [A specific, identified version (an exact SHA) that is believed to be releasable and is tested and reviewed as a whole before the release decision.]

2. What is feature freeze and why is it used? [A point after which no new features are added and only corrections are allowed. It stabilises the candidate so that testing and review evidence remain valid.]

3. What is regression testing in a release context? [Rerunning the complete accumulated suite on the exact candidate to confirm that previously working behaviour, including earlier repairs, still works after the final changes.]

4. What is a known limitation? [A documented gap or constraint in the released software that users should know about, such as session-only data.]

5. What is technical debt? [Structural or quality shortcuts that work now but make future change harder or riskier. It is recorded with its impact and a planned action.]

6. What are release notes? [A concise summary for users and maintainers of what the release delivers, fixes, improves and does not do.]

7. What is software maintenance? [Changing software after release to correct defects, adapt to new conditions, or improve structure and behaviour while preserving what already works.]

8. What is the purpose of the individual demonstration/viva? [To confirm that each member understands the system and their own contribution, and can explain and justify decisions independently of AI.]

9. What should the final responsible-AI check establish before release? [That significant AI contributions are identified, verified by humans against requirements and tests, and free of invented requirements, unreviewed dependencies, secrets or real data, with any limitations disclosed.]

10. What is the main course conclusion about AI and the role of the software engineer? [AI can accelerate work, but its output is a hypothesis. The engineer remains responsible for requirements, verification, design judgement and the release decision.]


## N Reflection viva and handover

Strongest evidence SmartCare is ready: [71 requirement-linked tests pass on the exact candidate, and the scripted console run demonstrates every common requirement, including error recovery.]


Weakest area: [Waiting for stage 11 to be completed]


How AI use changed from Stage 1 to Stage 12: [Major Uses were remained the same]


Start doing — engineering and AI use: [record Copilot prompts and outputs at the time they are used; add console tests.]


Stop doing — engineering and AI use: [granting an assistant write/commit access before a plan is approved;]


Continue doing — engineering and AI use: [human-first hypotheses, small reviewed PRs and full-suite reruns before merging.]


What worked / caused rework / future delivery improvement: [Stage 7 regression tests caught both F8 defects; rework came from the unapproved Copilot commit and stale documentation. Updating the README with each feature would prevent the second problem.]


One paragraph — If AI can write code why do we still need software engineers: [in SmartCare, AI could produce plausible code quickly, but it could not decide that cancelled appointments must be retained (FR-07), notice that a conflict check compared the wrong practitioner, or judge that a commit made before approval should be reverted. Those decisions came from requirements, tests and accountable human review. Engineers define the problem, verify behaviour against evidence, manage risk and take responsibility for the release; AI is a fast assistant inside that process, best explaination is its not a replacement for it.]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [Clinic staff need conflict-free appointment booking with retained history; patients and practitioners are affected (Stage 6 record).] |
| Two requirements and acceptance criteria | [FR-05/AC-04.2: conflicts only for the same practitioner at the exact time. FR-07: cancelled appointments are retained as CANCELLED.] |
| Domain model and architecture | [Patient, Practitioner, Appointment, AppointmentStatus; one shared SmartCareDataStore; services; pure query; console.] |
| Design trade-off | [In-memory dictionaries keep the design simple and testable but give up persistence (FR-10 retired).] |
| Meaningful test and its limits / 100 percent coverage | [test_stage7_cancelled_slot_can_be_rebooked_with_history_retained checks history and the conflict rule. Full coverage would still not prove that requirements are complete or the UI is correct.] |
| Diagnosed defect and verification | [F8-01: the store lookup filtered out cancelled appointments; the filter was removed (74e7011); the retained-history test now passes.] |
| Shared store and session-state/query responsibilities | [The store owns state; services coordinate through it; select_appointments only reads and returns a new list.] |
| What would break if session-state lookup/query responsibilities changed? | [If lookup filtered by status again, FR-07 and the cancellation tests would fail. If the query mutated or sorted the store, ordering and history guarantees would break.] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [Cancellation changes one appointment's own state under its own rule. Conflicts need knowledge of other appointments, so the service checks them through the store.] |
| FR-07 retained history test | [test_cancelled_appointment_is_retained_in_history (test_services.py:143).] |
| Actual AI change rejected/modified or honestly accepted with verification | [Stage 10 Copilot commit e36ee41 rejected and reverted (82d81e5).] |
| Unresolved limitation / future production work | [Persistence, authentication and a time-zone policy; console rescheduling.] |
| Personal implementation contribution | [Each member shall independently complete this ( Shaban Mohseni: Contributed on Stage 8  1/4Partialy AID and Stage 12 finalisment).] |
| Personal test/review/design/integration contribution | [Each member shall independently complete this ( Shaban Mohseni:  Contributed on Stage 81/4Partialy AID and Stage 12 finalisment ] |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
