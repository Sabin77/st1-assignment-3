# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Tuesday 1:30
- Members, GitHub usernames and cohorts: Stanley Campbell (https://github.com/s-campbell-dev , UG), Shaban Mohseni(AceofSpade-Py, UG) ,Nhat Minh Le (https://github.com/minhleee5 , UG),Sabin Lamichhane  (https://github.com/Sabin77 ,PG)
- Repository URL: https://github.com/Sabin77/st1-assignment-3.git
- Starting SHA: 22820d3125215dce5d33d1eaef2b2b6959ae431e (baseline: python -m pytest from project/, 8 passed, Python 3.13.14, pytest 8.3.5)
## A Requirement to issue activities

### FR-02 Patient Search

- Title: Find a patient using patient ID
- Context: Right now, find_practitioner just comes up with an error message (NotImplementedError), so the app can't look up a registered practitioner. Later, the Stage 9 practitioner listing will need it to find a practitioner by their ID.
- Requirement: FR-02 Patient Search: Find a patient by patient ID.
- - Context: Right now, find_practitioner just comes up with an error message (NotImplementedError), so the app can't look up a registered practitioner. Later, the Stage 9 practitioner listing will need it to find a practitioner by their ID.
- Acceptance criteria: A registered practitioner ID returns the same stored Practitioner object, not a new one; an ID with surrounding spaces locates the practitioner; a different letter case (dr1 vs. DR1) is handled as not found; an unknown valid ID raises LookupError; a blank or non-text ID raises ValueError.
- Scope: Finish PractitionerService.find_practitioner in services.py and add its tests to tests/test_services.py only. Changes to domain.py or data_store.py, patient lookup, cancellation and Stage 9 work are all outside the scope.
- Definition of Done: The PR is reviewed and approved by another member; the Copilot comparison is documented; all acceptance criteria have passing tests; the entire suite passes from project/ with python -m pytest; the PR is merged to main, everyone has pulled and rerun the tests, and the issue is closed.
- Owner: Stanley Campbell
- Actual issue link: https://github.com/Sabin77/st1-assignment-3/issues/2

### FR-03 supporting: Practitioner lookup

- Title: Find a practitioner using practitioner ID
- Context: PractitionerService.find_practitioner currently raises NotImplementedError, so the app cannot look up a registered practitioner. Booking and the Stage 9 practitioner listing need to retrieve the stored practitioner by ID.
- Requirement: FR-03 Practitioner Registration: Register a practitioner with unique ID, name and specialty. Practitioner lookup is a supporting operation.
- Acceptance criteria: A registered practitioner ID returns the same stored Practitioner object, not a new one; an unknown valid ID raises LookupError; a blank or non-text ID raises ValueError; an ID with surrounding spaces finds the practitioner; a different letter case (dr1 vs DR1) is treated as not found.
- Scope: Finish AppointmentService.cancel_appointment in services.py using the cancel() method, and test it in tests/test_services.py. Out of scope: changes to domain.py or data_store.py, deleting appointments, a workflow to complete appointments, patient or practitioner lookup and Stage 9 work.
- Definition of Done: The PR is reviewed and approved by another member; the Copilot comparison is documented; all acceptance criteria have passing tests; the entire suite passes from project/ with python -m pytest; the PR is merged to main, everyone has pulled and rerun the tests, and the issue is closed.
- Owner: Stanley Campbell
- Actual issue link: https://github.com/Sabin77/st1-assignment-3/issues/3

### FR-06 Appointment Cancellation with FR-07 retained history
- Title: Cancel a scheduled appointment and keep its record
- Context:cancel_appointment just comes up with an error message (NotImplementedError), so a booked appointment can't be cancelled. The Appointment class already has a cancel() method that only allows a SCHEDULED appointment to be cancelled, so the service needs to use it while keeping the appointment in current-session history.
- Requirement: FR-06 Appointment Cancellation: Cancel only a SCHEDULED appointment. FR-07 Retained history: Retain the same appointment with CANCELLED status in current-session history.
- Acceptance criteria: When a scheduled appointment is cancelled, it becomes cancelled and the same stored object is returned. It can still be found by its ID and still appears in the list. Cancelling again raises a ValueError and it stays cancelled. Trying to cancel a completed appointment raises a ValueError and it stays completed. LookupError occurs for an unknown ID, while ValueError is raised for a blank or non-text ID.
- Scope: Complete AppointmentService.cancel_appointment in services.py using the existing Appointment.cancel() method, and add its tests in tests/test_services.py only. Out of scope: changes to domain.py or data_store.py, deleting appointments, a workflow to complete appointments, patient or practitioner lookup and Stage 9 work.
- Definition of Done: All acceptance criteria have passing tests; the full suite passes from project/ with python -m pytest; the PR is reviewed and approved by another member; the Copilot comparison is recorded; the PR is merged to main, everyone has pulled and rerun the tests, and the issue is closed.
- Owner: Stanley Campbell 
- Actual issue link:https://github.com/Sabin77/st1-assignment-3/issues/4

## B Commit quality

| Original example | Strong or Weak | Reason                                                                                                                                                            |
|---|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| changes | Weak | because it is too generic and does not explain what was changed                                                                                                   |
| final version | Weak| It says nothing about what was changed or what the final version is. When someone changes it is no longer a final version and can create multiple final versions. |
| Add patient search by ID | Strong | It displays an action that was performed. It clearly links to a functional requirement (FR-02)                                                                    |
| fix stuff | Weak | does not explain what is to be fixed and where. Also, takes time and effort to find errors                                                                        |
| Prevent cancellation of completed appointments | Strong | It is specific in what it did fix. It names the exact rule the commit enforces                                                                                    |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.
- Scope concerns: The goal of this PR is to cancel an appointment, but it also introduces a new dependency, re-organises other code and renames patient information. These extras have no linked issues and are not related to the acceptance criteria, so the reviewer cannot check them against anything.
- Responsibility and architecture concerns: Renaming unrelated fields in the patient might break other code and tests that still use the old names. Unrelated code can be reorganised to move rules to the wrong layer, e.g. outside of the domain classes. The new dependency causes setup problems for every team member, since SmartCare only uses the standard library.
- Testing and review concerns: One big diff with many mixed changes makes it easy for the reviewer to miss problems. A passing test suite does not prove the safety of the extra changes, nor does it show which tests cover which changes. Because of the new dependency, each member has to install and verify it in their own configuration.
- Changes to remove or separate, with reasons: This PR should only retain the cancellation change. The renaming and the restructuring should each have their own issue first and then their own PR, so they can be judged on their own merits. The team should first determine whether the new dependency is actually necessary.

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: it does not provide what test cases it did and how it came to that conclusion it is based on generic information.
- Follow-up review question 1: what was your assessment criteria based on.
- Follow-up review question 2: “What does the code do if the ID is null or invalid?”
- Follow-up review question 3: what was the test cases considered in my code
- Follow-up review question 4: what assumption was made in testing my code 
- Follow-up review question 5: has there been any changes that is not documented.
- Additional questions if useful: [response]

## E Team workflow agreement

| Practice | Team agreement                                                                                                                                                                                                                                                            |
|-|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Branch naming | Every branch name starts with the feature/ prefix, followed by a short lowercase hyphenated description, with one branch allocated per issue. Examples include: feature/patient-lookup, feature/practitioner-lookup, feature/cancel-appointment. |                                                                                            |
| Commit message convention | First use an imperative verb (Add, Reject, Test); describe the altered behaviour rather than the file; keep the summary to about 50 characters. Examples: "Add patient search by ID", "Reject cancellation of completed appointments" |                                                           |
| PR size | Just one issue per PR; no unrelated renaming, refactoring, formatting changes or new dependencies, as these receive their own issue and PR. |
| Another-member review requirement | Before merging, a separate group member examines the actual diff and either approves or asks for changes; Copilot and self-review do not count as approval.|                                                                                                                           |
| Merge rule | Merge only when acceptance criteria are met, the entire test suite passes, another member has approved, feedback is resolved, there are no unrelated changes, and significant Copilot use is reported; use a merge commit; each member then pulls main and reruns the tests. |
| Significant Copilot disclosure rule | Any Copilot output we retain, modify, or reject in code, tests, or review is significant; note it in the PR description and section H; a human verifies each claim against the requirement, the code, and an actual test run; Copilot never approves a PR. |

Role arrangement: Sabin Lamichhane set up and owns the shared repository. With the tutor's approval (6 October 2026), each member leads a different stage: Stanley Campbell Stage 6, Nhat Minh Le Stage 7, Shaban Mohseni Stage 8, Sabin Lamichhane PG Stages 10 and 11; Stage 12 submission is completed together. Stanley authors all three Stage 6 changes, each on its own issue, branch and PR. A different group member reviews and approves each Stage 6 PR before merge; reviewers are recorded in section G.
## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner | Acceptance criteria or precise link | Status |
|---|---|---|---|-----|
|https://github.com/Sabin77/st1-assignment-3/issues/2 | FR-02 Patient Search| Stanley Campbell | Five criteria listed in issue #2 (same object, LookupError, ValueError, spaces, case) | Open|
| https://github.com/Sabin77/st1-assignment-3/issues/3 | FR-03 supporting: Practitioner lookup | Stanley Campbell | Five criteria listed in issue #3 (same object, LookupError, ValueError, spaces, case) | Open |
| https://github.com/Sabin77/st1-assignment-3/issues/4 | FR-06 Appointment Cancellation with FR-07 retained history | Stanley Campbell | Six criteria listed in issue #4 (cancel and return same object, retained in history, repeat cancel, completed, LookupError, ValueError) | Open |

## G Pull request evidence

Repeat this block per PR. Record actual events, not ## H Copilot collaboration record

### PR #5: Patient lookup (issue #2)

- ### PR #5: Patient lookup (issue #2)

- PR link and title: https://github.com/Sabin77/st1-assignment-3/pull/5 "Add patient lookup by ID (closes #2)"
- Linked issue and requirement: https://github.com/Sabin77/st1-assignment-3/issues/2 (FR-02 Patient Search: Find a patient by patient ID)
- Feature branch: feature/patient-lookup
- Changed behaviour: PatientService.find_patient returns the stored Patient for a registered ID and raises LookupError for an unknown ID; blank or non-text IDs raise ValueError through the store's existing validation.
- Meaningful commits: https://github.com/Sabin77/st1-assignment-3/commit/fe6fa292aa4e2e7848b13287aae8365bc80fde9c (Add patient lookup by ID with LookupError for unknown IDs); 792d44d (Update find_patient docstring and add final newline)
- Test command, directory and observed result: python -m pytest from project/ on fe6fa29: 13 passed (8 starter, 5 new); rerun on 792d44d: 13 passed
- Another-member reviewer: Sabin Lamichhane (Sabin77). minhleee5 was also requested but did not review.
- Human observations recorded before Copilot: https://github.com/Sabin77/st1-assignment-3/pull/5#issuecomment-6492891680, PR comment by Sabin77, labelled as his independent human review before the Copilot comparison
- Requirement, responsibilities, test assertions and unrelated-scope checks: Sabin confirmed the method uses the shared store, returns the same registered object, raises LookupError for unknown IDs and relies on the store's validation; he ran the five new tests individually and the full suite (13 passed, Python 3.13.3, pytest 8.3.5) and found no issues.
- Key feedback: Human review found no issues. Copilot (Optional): test_services.py had no final newline. Author self-check: the find_patient docstring still described the unfinished starter.
- Author response/change and verification: Commit 792d44d updated the docstring and added the final newline; no behaviour change; python -m pytest from project/: 13 passed. Response comment: [link to your comment]
- Reviewer recheck and approval: https://github.com/Sabin77/st1-assignment-3/pull/5#pullrequestreview-5711433014; Sabin77 approved after rechecking commit 792d44d
- Merge outcome and SHA: Merged into main by merge commit d0bbc25ab07a99400a10d6646df827a672167e73
- Significant Copilot assistance: Part H review comparison only (see section H); no Copilot use in implementation or tests
- Linked issue closure: Issue #2 closed automatically when PR #5 was merged
- Each member updated main: Stanley Campbell: git pull --ff-only to d0bbc25, 13 passed; [other members: name, SHA and result when they confirm]
- Integrated verification after merge: python -m pytest from project/ on d0bbc25: 13 passed


### PR #6: Practitioner lookup (issue #3)

- PR link and title: https://github.com/Sabin77/st1-assignment-3/pull/6 "Add practitioner lookup by ID (closes #3)"
- Linked issue and requirement: https://github.com/Sabin77/st1-assignment-3/issues/3 (FR-03 Practitioner Registration; practitioner lookup is a supporting operation)
- Feature branch: feature/practitioner-lookup
- Changed behaviour: PractitionerService.find_practitioner returns the stored Practitioner for a registered ID and raises LookupError for an unknown ID; blank or non-text IDs raise ValueError through the store's existing validation; docstring describes the current behaviour.
- Meaningful commits: https://github.com/Sabin77/st1-assignment-3/commit/19e782e0caa0804d399caf53b852fa3d0843afe6 (Add practitioner lookup by ID with LookupError for unknown IDs); https://github.com/Sabin77/st1-assignment-3/commit/88ccd13c427c1b338a7047f36578629e9189e36c (Restore blank lines between top-level definitions, found in the author's own diff check)
- Test command, directory and observed result: python -m pytest from project/ on 88ccd13: 18 passed (8 starter, 5 patient, 5 practitioner)
- Another-member reviewer: Sabin Lamichhane (Sabin77)
- Human observations recorded before Copilot: [https://github.com/Sabin77/st1-assignment-3/pull/6#issuecomment-6534833264; Sabin recorded his independent human review before consulting Copilot
- Requirement, responsibilities, test assertions and unrelated-scope checks: Sabin confirmed practitioner lookup uses the shared data store, returns the same registered practitioner object and handles unknown or invalid IDs according to FR-03; he ran the full suite (18 passed, Python 3.13.3, pytest 8.3.5).
- Key feedback: No blocking issues. Copilot (Optional): consider an explicit empty-string ('') ID test.
- Author response/change and verification: No code change needed; the optional '' test was deferred because the existing '   ' test already covers blank input.
- Reviewer recheck and approval:https://github.com/Sabin77/st1-assignment-3/pull/6#issuecomment-6534901208
- Merge outcome and SHA: Merged into main by Sabin77 with merge commit 94070f167d59b5f8d7332b13021ffeadf4ae96a8
- Significant Copilot assistance: Part H review comparison by Sabin (see section H); no Copilot use in implementation or tests
- Linked issue closure: Issue #3 closed automatically when PR #6 was merged
- Each member updated main: Stanley Campbell: git pull --ff-only to 94070f1, 18 passed; [other members when they confirm]
- Integrated verification after merge: python -m pytest from project/ on 94070f1: 18 passed

### PR #7: Appointment cancellation (issue #4)

- PR link and title: https://github.com/Sabin77/st1-assignment-3/pull/7 "Add appointment cancellation that retains history (closes #4)"
- Linked issue and requirement: https://github.com/Sabin77/st1-assignment-3/issues/4 (FR-06 Appointment Cancellation; FR-07 Retained history; AC-05.1/05.2/05.3)
- Feature branch: feature/cancel-appointment
- Changed behaviour: AppointmentService.cancel_appointment finds the stored appointment through find_appointment, cancels it through Appointment.cancel() and returns the same object; unknown IDs raise LookupError; blank or non-text IDs raise ValueError; CANCELLED or COMPLETED appointments raise ValueError and keep their status; nothing is deleted.
- Meaningful commits: https://github.com/Sabin77/st1-assignment-3/commit/d52e35d95a2e031a2fbf2446c12dc270635d5db9 (Add appointment cancellation that retains history)
- Test command, directory and observed result: python -m pytest from project/ on d52e35d: 24 passed (8 starter, 5 patient, 5 practitioner, 6 cancellation)
- Another-member reviewer: Sabin Lamichhane (Sabin77)
- Human observations recorded before Copilot: https://github.com/Sabin77/st1-assignment-3/pull/7 (Sabin77's "Independent Human Review – PR #7" comment, posted before his Copilot comparison)
- Requirement, responsibilities, test assertions and unrelated-scope checks: Sabin confirmed the service locates the existing appointment, delegates cancellation to the Appointment domain object and returns the same object without deleting it; the six tests cover the acceptance criteria; changes were limited to the service and test files; he ran py -m pytest on d52e35d (24 passed, Python 3.13.3, pytest 8.3.5).
- Key feedback: No blocking issues. Optional: test_services.py lacks a final newline; the docstring could mention invalid IDs; Copilot suggested an extra domain-level cancellation test.
- Author response/change and verification: No code change before merge. The newline and docstring items were judged optional and non-blocking; the domain-level test was deferred to Stage 7, where domain testing is required.
- Reviewer recheck and approval: https://github.com/Sabin77/st1-assignment-3/pull/7 (Sabin77 approved after independently testing d52e35d: 24 passed)
- Merge outcome and SHA: Merged into main by s-campbell-dev with merge commit ec5cbf78fb033fcc4234a4120a345e1e4df94af9
- Significant Copilot assistance: Part H review comparison by Sabin (see section H); no Copilot use in implementation or tests
- Linked issue closure: Issue #4 closed automatically when PR #7 was merged
- Each member updated main: Stanley Campbell: git pull --ff-only to ec5cbf7, 24 passed; [other members when they confirm]
- Integrated verification after merge: python -m pytest from project/ on ec5cbf7: 24 passed

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

### PR #5 Copilot review (patient lookup)

- Member and task: Stanley Campbell; required Part H Copilot review comparison for PR #5 (issue #2, FR-02)
- Prompt/purpose and relevant issue/diff: Stage 6 Part H prompt in Copilot Chat (PyCharm, Copilot Free) with issue #2's acceptance criteria and the PR #5 diff at fe6fa29; run after Sabin's human review was recorded
- Summary of output: No Critical or Important findings. Optional: test_services.py ends without a final newline. Two review questions: confirm the store trims, validates and uses case-sensitive lookup; confirm test_services.py is discovered by pytest. Copilot stated it had not run the tests.
- Human check against actual code, requirements and tests: The diff shows the "No newline at end of file" marker. data_store.find_patient calls required_text, then an exact dictionary lookup. pytest collected tests/test_services.py with 13 passed.
- Decision — Accept / Modify / Reject: Accept (final newline); review questions checked, no code change needed
- Reason: The newline finding was real and harmless to fix; both questions were answered by the existing code and an observed test run.
- Verification/evidence: Commit 792d44d; python -m pytest from project/: 13 passed; PR comment 
https://github.com/Sabin77/st1-assignment-3/pull/5#issue-6091513235


### PR #6 Copilot review (practitioner lookup)

- Member and task: Sabin Lamichhane (Sabin77); required Part H Copilot review comparison for PR #6 (issue #3, FR-03)
- Prompt/purpose and relevant issue/diff: Copilot review of the PR #6 diff and relevant source files, run after Sabin's independent human review [confirm with Sabin that the Part H prompt was used]
- Summary of output: No Critical or Important issues; confirmed the five acceptance criteria were covered. Optional suggestion: add an explicit empty-string ('') ID test.
- Human check against actual code, requirements and tests: Sabin checked the suggestion against the existing tests; the '   ' test and the store's required_text validation already reject blank input; full suite 18 passed.
- Decision — Accept / Modify / Reject: Accept the findings; the optional '' test was deferred
- Reason: The implementation and existing tests already satisfy the stated acceptance criteria; the extra test is optional and would not change behaviour.
- Verification/evidence: https://github.com/Sabin77/st1-assignment-3/pull/6#issuecomment-6534901208; 18 passed in 0.09 seconds

### PR #7 Copilot review (appointment cancellation)

- Member and task: Sabin Lamichhane (Sabin77); required Part H Copilot review comparison for PR #7 (issue #4, FR-06/FR-07)
- Prompt/purpose and relevant issue/diff: Copilot review of the PR #7 diff and relevant repository contracts, run after Sabin's independent human review
- Summary of output: No Critical findings or functional blockers. Optional observations: the docstring could explicitly mention invalid IDs; an extra domain-level cancellation test could strengthen state-transition evidence; test_services.py lacks a final newline. Copilot did not execute the tests.
- Human check against actual code, requirements and tests: Sabin confirmed the method delegates to Appointment.cancel(), returns the same stored object and preserves history; he independently tested d52e35d (24 passed).
- Decision — Accept / Modify / Reject: Accept the functional findings; defer the domain-level test to Stage 7; treat the docstring and newline as optional, non-blocking
- Reason: No correctness issues; Stage 7 specifically requires domain tests; the formatting items do not change behaviour.
- Verification/evidence: https://github.com/Sabin77/st1-assignment-3/pull/7 (Sabin77's "Human vs Copilot Review Comparison – PR #7" comment); 24 passed on d52e35d
- 
## I Human versus Copilot review comparison

### PR #6 (practitioner lookup)

- Human reviewer noticed before consulting Copilot: Sabin confirmed practitioner lookup uses the shared data store, returns the same registered practitioner object and handles unknown or invalid IDs according to FR-03; he ran the full suite (18 passed).
- Copilot noticed: No Critical or Important issues; confirmed the five acceptance criteria were covered; optional suggestion of an explicit empty-string ('') ID test.
- Overlap: Both reviews found no correctness or scope issues.
- What did the human reviewer notice that Copilot did not: Observed test execution on a real machine (18 passed).
- What did Copilot identify that the human reviewer initially missed: The option of an explicit empty-string ID test.
- Unsupported or incorrect Copilot suggestion: None identified; the suggestion was valid but optional.
- Human judgement accepted, modified or rejected, and why: Sabin accepted the findings but deferred the optional test, because the existing blank-ID test and validation already satisfy the acceptance criteria.
- Which evidence justified merge approval: Sabin's independent review, all five acceptance criteria covered by tests, and the full suite passing (18 passed), including the starter tests.

### PR #5 (patient lookup)

- Human reviewer noticed before consulting Copilot: Sabin confirmed correct use of the shared store, same-object return, LookupError for unknown IDs and reliance on store validation; he ran the five new tests individually and the full suite (13 passed) and found no issues.
- Copilot noticed: No Critical or Important issues; an Optional missing final newline in test_services.py; two questions about store behaviour and test discovery.
- Overlap: Both found the implementation met FR-02, with no correctness or scope problems.
- What did the human reviewer notice that Copilot did not: Observed test execution on a real machine (13 passed); Copilot could not run tests and said so.
- What did Copilot identify that the human reviewer initially missed: The missing final newline in test_services.py.
- Unsupported or incorrect Copilot suggestion: None identified; both questions were checked against data_store.py and the pytest output and confirmed the existing behaviour.
- Human judgement accepted, modified or rejected, and why: In PR #5 I accepted a Copilot suggestion to add a final newline because the diff showed it was missing and the fix didn't change behaviour. The two questions did not require any code change as I have checked data_store.py and the pytest output which confirmed the existing behaviour.
- Which evidence justified merge approval: Sabin reviewed the diff and ran the tests himself. All 5 acceptance criteria in issue #2 have a test, and the full suite passed (13 passed) including the 8 starter tests which shows the change did not break other parts of the programme.

### PR #7 (appointment cancellation)

- Human reviewer noticed before consulting Copilot: Sabin confirmed the service locates the existing appointment, delegates cancellation to the Appointment domain object and returns the same object without deleting it; the six tests cover the criteria; changes were limited to the expected files; he ran the suite on d52e35d (24 passed) and noticed the missing final newline.
- Copilot noticed: No Critical findings; the same delegation, identity and history points; optional docstring wording on invalid IDs; an optional extra domain-level test; the missing final newline.
- Overlap: Both found the implementation delegates to Appointment.cancel(), returns the same stored object and preserves history; both noticed the missing final newline.
- What did the human reviewer notice that Copilot did not: Observed test execution on a real machine (24 passed); Copilot did not run the tests.
- What did Copilot identify that the human reviewer initially missed: The docstring could mention invalid IDs, and a domain-level cancellation test could add state-transition evidence.
- Unsupported or incorrect Copilot suggestion: None identified; the suggestions were valid but optional.
- Human judgement accepted, modified or rejected, and why: Sabin accepted the functional findings, deferred the domain-level test to Stage 7 where domain testing is required, and treated the docstring and newline as optional because they do not change behaviour.
- Which evidence justified merge approval: Sabin's independent review and test run (24 passed on d52e35d), all six acceptance criteria covered by tests, and no unrelated changes; after merge, main at ec5cbf7 also passed 24 tests.

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

### Stanley Campbell (s-campbell-dev)

- Member: Stanley Campbell (s-campbell-dev, UG)
- Implementation: Completed all three Stage 6 service operations: PatientService.find_patient (PR #5), PractitionerService.find_practitioner (PR #6) and AppointmentService.cancel_appointment (PR #7). https://github.com/Sabin77/st1-assignment-3/pull/5, https://github.com/Sabin77/st1-assignment-3/pull/6, https://github.com/Sabin77/st1-assignment-3/pull/7
- Testing: Created tests/test_services.py with 16 tests, one per acceptance criterion across issues #2, #3 and #4, including identity checks and status-unchanged checks after errors; full suite 24 passed on d52e35d.
- Review: Not applicable for Stage 6; my PRs were reviewed by Sabin77.
- Issue refinement: Wrote issues #2, #3 and #4 with context, acceptance criteria, scope and Definition of Done, and corrected the FR-03 wording to match the Overview. https://github.com/Sabin77/st1-assignment-3/issues/2, https://github.com/Sabin77/st1-assignment-3/issues/3, https://github.com/Sabin77/st1-assignment-3/issues/4
- Design and responsibility discussion: Chose to reuse the existing store validation for the lookups, and find_appointment plus Appointment.cancel() for cancellation, so domain rules stay in the domain and no validation is duplicated.
- Debugging or integration: Responded to PR #5 review (docstring update and final newline, 792d44d); restored blank lines found in my own diff check (88ccd13); merged PR #5 (d0bbc25); pulled and verified main after each merge (13 and 18 passed); set up a clean local environment and recovered work after editing an outdated copy.
- Documentation or team support: Maintained the Stage 6 record (sections A to M) and PR descriptions; ran the PR #5 Copilot comparison (section H). Process guidance from Claude was used and disclosed in the PR descriptions.

### [Teammate name] ([GitHub username])

- Member: [response]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

- Member: [response]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

## K Exit question

A high commit count can be a case of quantity over quality. There could have been a lot of errors, or someone being mentored and shown how to commit. Also, different people have different workloads, and the number of commits does not show how important their work is to the project. For example, PR #5 had only 2 commits but delivered a working patient lookup feature with 5 tests, and Sabin made 0 commits but his review was still a real contribution.
[response]

## L Stage 6 formative questions

1. What is version control?
Version control is a system that allows teams to collaborate on projects and recover and correct errors by monitoring changes over time to retrieve data.

2. Why is a feature branch useful?
A feature branch isolates the development of a project from the main code. This allows you to write tests and refine code without affecting other team members' code.

3. What makes a commit a good engineering commit?
A good engineering commit is clear and logical. It allows teammates to understand why a change was made and to trace bugs.

4. What is a pull request?
A pull request is a request to merge code from one branch to another. It allows team members to review the code and provide feedback before it is merged into the main branch. It also allows for discussion and collaboration on the code changes.

5. What is the purpose of code review?
The purpose of a code review is to ensure software quality, maintain code accuracy and share expertise across the team before code is merged into the main repository. Reviewers read the changes and comment on them.

6. What does a Git diff show?
Git diff allows you to compare changes in a Git repository and shows the modifications that have been made.

7. What is a Definition of Done?
The definition of done is when the team agrees on a checklist that includes technicalities, functionality, code quality, and adherence to project requirements.

8. What is the appropriate role of GitHub Copilot in pull-request review?
Copilot assists in reviewing code by providing suggestions, recommendations and identifying possible issues. However, the final decision belongs to the reviewer, to ensure code quality and keep the integrity of the project. Copilot only supports the reviewer, and its suggestions must be checked; the human reviewer should write their own observations first, before asking Copilot for a review.

9. Why should individual contribution not be judged only by commit count?
The number of commits should not be the measure of someone's contribution to a project, because it does not reflect the quality or impact of the work they did. Other factors, such as collaboration, problem solving and mentoring, are also important. Overall, a person's work should be evaluated on quality, not quantity.

10. What is the Stage 6 engineering rule?
The rule is a cycle: update main, create a focused issue and branch, write the code and tests, then push the changes and open a pull request. A team member reviews the changes first, and then Copilot reviews them; after approval the PR is merged, and everyone updates main and verifies the integrated tests.

## M Completion and handover

- Starting SHA: 22820d3125215dce5d33d1eaef2b2b6959ae431e
- Final Stage 6 code SHA: ec5cbf78fb033fcc4234a4120a345e1e4df94af9
- Test command: python -m pytest
- Working directory: project/
- Observed result: 24 passed (8 starter, 5 patient, 5 practitioner, 6 cancellation) on ec5cbf7
- PR and another-member reviewer: https://github.com/Sabin77/st1-assignment-3/pull/5, https://github.com/Sabin77/st1-assignment-3/pull/6, https://github.com/Sabin77/st1-assignment-3/pull/7; all reviewed and approved by Sabin77
- Unresolved issue or none: None blocking. Optional, not done: the PR #6 Copilot suggestion of an explicit empty-string ID test was deferred because the existing blank-ID test covers it. PR #7 optional items: the final newline in test_services.py and docstring wording on invalid IDs were judged non-blocking; a domain-level cancellation test was deferred to Stage 7.
- Stage 7 handover status: Ready for tutor checkpoint once this record is merged and every member has confirmed main at ec5cbf7
- Final submitted SHA if later than tested SHA: the Stage 6 record PR merge (evidence-only; no code changes after ec5cbf7)

- [x] Three Stage 6 service targets completed and checked.
- [x] Original supplied tests retained and passing.
- [x] At least two focused issues link requirements and acceptance criteria.
- [x] Feature work reviewed by another member using the actual diff.
- [x] Human-first review and required Copilot comparison recorded.
- [x] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [x] Only synthetic data included; confidential peer material kept out.
- [x] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
