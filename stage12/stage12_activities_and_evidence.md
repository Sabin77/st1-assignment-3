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
| Problem and stakeholders | [response] | [response] | [response] | [response] |
| Register and find Patient and two Practitioners | [response] | [response] | [response] | [response] |
| Valid booking | [response] | [response] | [response] | [response] |
| Same practitioner exact-time conflict rejected | [response] | [response] | [response] | [response] |
| Different practitioner same time allowed | [response] | [response] | [response] | [response] |
| Cancel SCHEDULED and retain/find CANCELLED object | [response] | [response] | [response] | [response] |
| Invalid/repeated cancellation rejected | [response] | [response] | [response] | [response] |
| Default all-status listing | [response] | [response] | [response] | [response] |
| Explicit filtering / empty vs unknown / deterministic order | [response] | [response] | [response] | [response] |
| Invalid date/status/menu/lookup recovery and continued operation | [response] | [response] | [response] | [response] |
| Session-only limitation and normal exit | [response] | [response] | [response] | [response] |
| One meaningful requirement-linked pytest test explained | [response] | [response] | [response] | [response] |
| Architecture and one actual AI decision / known limitation | [response] | [response] | [response] | [response] |
| PG reschedule identity/participants/time and no-op | [response] | [response] | [response] | [response] |
| PG conflict/invalid status/failure non-mutation | [response] | [response] | [response] | [response] |
| PG old slot / current lookup/list ordering / assurance risks | [response] | [response] | [response] | [response] |
Stable demo owner / fresh process / command: [response]
PG demonstrations through service/tests or not applicable: [response]


## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | [response] | [response] | [response] |
| PascalCase and snake_case naming | [response] | [response] | [response] |
| Useful type hints and meaningful docstrings | [response] | [response] | [response] |
| Four-space indentation and imports/layout | [response] | [response] | [response] |
| Focused methods / duplication / dead or commented code | [response] | [response] | [response] |
| Globals / leakage / unnecessary inheritance or frameworks | [response] | [response] | [response] |
| No SQLite/persistence/repository ABCs/speculative features | [response] | [response] | [response] |
| Synthetic data / secrets / dependencies / provenance | [response] | [response] | [response] |
| Significant common Copilot contributions and human verification | [response] | [response] | [response] |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | [response] | [response] | [response] |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Access route or approved equivalent / limitations: [response]
Available AI evidence and missing evidence honestly disclosed: [response]


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | [response] | [response] | [response] |
| Out-of-scope capabilities and known limitations | [response] | [response] | [response] |
| Confirmed teaching Python version and dependency installation | [response] | [response] | [response] |
| Working directory / demo / interactive / test commands | [response] | [response] | [response] |
| Repository structure and architecture responsibilities | [response] | [response] | [response] |
| Responsible AI summary / synthetic-data rule | [response] | [response] | [response] |
| Release label/version and SHA links | [response] | [response] | [response] |
Root README index and project/README verified: [response]
Fresh clone or extracted ZIP / candidate identity: [response]
Verifier and clean environment / actual version: [response]
Setup/run/test commands and observed results: [response]
Missing local file or setup gap / remedy and recheck: [response]


## G Known limitations debt and release notes

Delivered features: [response]
Important fixes: [response]
Architecture/quality improvements: [response]
Known limitations: [response]
AI-assisted development note: [response]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Session-only synthetic data and minute-precision local time: [response]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [response]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [response]
Difference between accepted scope limit and unresolved required behaviour: [response]
PG assurance residual risks / owner / status or not applicable: [response]


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |
Justified no-change conclusion if no defect found: [response]
Release blockers still open / status: [response]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [response]
Independent reviewer / feedback / response: [response]
Integration commit / full recheck: [response]
Tracked and untracked file inspection / cleanliness: [response]
Secrets/staff material/caches/tool-metadata exclusion check: [response]
Candidate recovery plan / known-good SHA: [response]
Named substantive contributions: [response]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: [response]
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
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

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? [response]

2. What is feature freeze and why is it used? [response]

3. What is regression testing in a release context? [response]

4. What is a known limitation? [response]

5. What is technical debt? [response]

6. What are release notes? [response]

7. What is software maintenance? [response]

8. What is the purpose of the individual demonstration/viva? [response]

9. What should the final responsible-AI check establish before release? [response]

10. What is the main course conclusion about AI and the role of the software engineer? [response]


## N Reflection viva and handover

Strongest evidence SmartCare is ready: [response]
Weakest area: [response]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [response]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [response] |
| Two requirements and acceptance criteria | [response] |
| Domain model and architecture | [response] |
| Design trade-off | [response] |
| Meaningful test and its limits / 100 percent coverage | [response] |
| Diagnosed defect and verification | [response] |
| Shared store and session-state/query responsibilities | [response] |
| What would break if session-state lookup/query responsibilities changed? | [response] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response] |
| FR-07 retained history test | [response] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [response] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
