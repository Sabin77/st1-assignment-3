# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Tuesday 1:30
- Members, GitHub usernames and cohorts: Stanley Campbell (https://github.com/s-campbell-dev , UG), Shaban Mohseni,Nhat Minh Le (https://github.com/minhleee5 , UG),Sabin Lamichhane  (https://github.com/Sabin77 ,PG)
- Repository URL: https://github.com/Sabin77/st1-assignment-3.git
- Starting SHA: 22820d3125215dce5d33d1eaef2b2b6959ae431e (baseline: python -m pytest from project/, 8 passed, Python 3.13.14, pytest 8.3.5)
## A Requirement to issue activities

### FR-02 Patient Search

- Title: Find a patient using patient ID
- Context: PatientService.find_patient currently raises NotImplementedError, so the app cannot look up a registered patient. Later workflows, such as the Stage 9 menu's find option, need to retrieve the stored patient by ID.
- Requirement: FR-02 Patient Search: Find a patient by patient ID.
- Acceptance criteria: A registered patient ID returns the same stored Patient object, not a new one; an unknown valid ID raises LookupError; a blank or non-text ID raises ValueError; an ID with surrounding spaces finds the patient; a different letter case (p1 vs P1) is treated as not found.
- Scope: Complete PatientService.find_patient in services.py and add its tests in tests/test_services.py only. Out of scope: changes to domain.py or data_store.py, practitioner lookup, cancellation and Stage 9 work.
- Definition of Done: All acceptance criteria have passing tests; the full suite passes from project/ with python -m pytest; the PR is reviewed and approved by another member; the Copilot comparison is recorded; the PR is merged to main, everyone has pulled and rerun the tests, and the issue is closed.
- Owner: Stanley Campbell
- Actual issue link: https://github.com/Sabin77/st1-assignment-3/issues/2

### FR-03 supporting: Practitioner lookup

- Title: Find a practitioner using practitioner ID
- Context: PractitionerService.find_practitioner currently raises NotImplementedError, so the app cannot look up a registered practitioner. Booking and the Stage 9 practitioner listing need to retrieve the stored practitioner by ID.
- Requirement: FR-03 Practitioner Registration: Register a practitioner with unique ID, name and specialty. Practitioner lookup is a supporting operation.
- Acceptance criteria: A registered practitioner ID returns the same stored Practitioner object, not a new one; an unknown valid ID raises LookupError; a blank or non-text ID raises ValueError; an ID with surrounding spaces finds the practitioner; a different letter case (dr1 vs DR1) is treated as not found.
- Scope: Complete PractitionerService.find_practitioner in services.py and add its tests in tests/test_services.py only. Out of scope: changes to domain.py or data_store.py, patient lookup, cancellation and Stage 9 work.
- Definition of Done: All acceptance criteria have passing tests; the full suite passes from project/ with python -m pytest; the PR is reviewed and approved by another member; the Copilot comparison is recorded; the PR is merged to main, everyone has pulled and rerun the tests, and the issue is closed.
- Owner: Stanley Campbell
- Actual issue link: https://github.com/Sabin77/st1-assignment-3/issues/3

### FR-06 Appointment Cancellation with FR-07 retained history
 - Title: Cancel a scheduled appointment and keep its record
 - Context: AppointmentService.cancel_appointment currently raises NotImplementedError, so a booked appointment cannot be cancelled. The Appointment class already guards the status change; the service needs to coordinate it while keeping the appointment in session history.
 - Requirement: FR-06 Appointment Cancellation: Cancel only a SCHEDULED appointment. FR-07 Retained history: Retain the same appointment with CANCELLED status in current-session history.
 - Acceptance criteria: Cancelling a SCHEDULED appointment changes its status to CANCELLED and returns the same stored object; after cancelling, the appointment can still be found by ID and still appears in the stored appointment list; cancelling an already CANCELLED appointment raises ValueError and the status stays CANCELLED; cancelling a COMPLETED appointment raises ValueError and the status stays COMPLETED; an unknown valid ID raises LookupError; a blank or non-text ID raises ValueError.
 - Scope: Complete AppointmentService.cancel_appointment in services.py using the existing Appointment.cancel() method, and add its tests in tests/test_services.py only. Out of scope: changes to domain.py or data_store.py, deleting appointments, a workflow to complete appointments, patient or practitioner lookup and Stage 9 work.
 - Definition of Done: All acceptance criteria have passing tests; the full suite passes from project/ with python -m pytest; the PR is reviewed and approved by another member; the Copilot comparison is recorded; the PR is merged to main, everyone has pulled and rerun the tests, and the issue is closed.
 - Owner: Stanley Campbell
 - Actual issue link:https://github.com/Sabin77/st1-assignment-3/issues/4

## B Commit quality

| Original example | Strong or Weak | Reason                                                                                                            |
|---|----------------|-------------------------------------------------------------------------------------------------------------------|
| changes | [weak]         | because it is to generic and does not explain what was changed                                                    |
| final version | Weak           | in coding there is never a final version and if there is multiple its hard to find what its the final version of. |
| Add patient search by ID | Strong         | Its specific non what the context is.                                                                             |
| fix stuff | Weak           | does not explain what is to be fixed takes time and effort to find errors                                         |
| Prevent cancellation of completed appointments | Strong         | It is specific in what needs to be fixed.                                                                         |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: The scope is doing tasks out side of your specialty if change the program to much it makes it complex for the customer and mistakes have to fixed which takes time and money.
- Responsibility and architecture concerns: creates bugs and glitches that needs to be fixed harder to update and maintain. may change system architecture. makining the program incompatiability and causes conflicts and errors within the system.
- Testing and review concerns: testing can work without errors but it may not run as expected which can cause even more concerns running a program in unstable environment.
- Changes to remove or separate, with reasons: instead having one pull request, there should be four seperate pull requests patient field, code restructuring and new dependancy and cancellation PR. there needs to be four pull requests to let the team know everything you done and to keep every task independant.

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: it does not provide what test cases it did and how it came to that conclusion it is based on generic information.
- Follow-up review question 1: what was your assessment criteria based on.
- Follow-up review question 2: there is an error in the coding when ran after your assessment you anaylse and fix the problem
- Follow-up review question 3: what was the test cases considered in my code
- Follow-up review question 4: what assumption was made in testing my code 
- Follow-up review question 5: if you was building this code what would you update and change or is there i should consider.
- Additional questions if useful: [response]

## E Team workflow agreement

| Practice   | Team agreement                                                                                                                                                                                                                                                             |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Branch naming | feature/ prefix plus a short lowercase hyphenated description; one branch per issue. Examples: feature/patient-lookup, feature/practitioner-lookup, feature/cancel-appointment                                                                                             |
| Commit message convention| Imperative verb first (Add, Reject, Test); describe the behaviour that changed, not the file; summary about 50 characters. Examples: "Add patient search by ID", "Reject cancellation of completed appointments"                                                           |
| PR size | One issue per PR; no unrelated renames, refactoring, formatting changes or new dependencies, which get their own issue and PR                                                                                                                                              |
| Another-member review requirement | A different group member reviews the actual diff and approves or requests changes before merge; self-review and Copilot do not count as approval                                                                                                                           |
| Merge rule | Merge only when acceptance criteria are met, the full test suite passes, another member has approved, feedback is resolved, there are no unrelated changes and significant Copilot use is disclosed; use a merge commit; every member then pulls main and reruns the tests | 
| Significant Copilot disclosure rule | Any Copilot output we keep, change or reject in code, tests or review is significant; record it in the PR description and section H; a human checks every claim against the requirement, the code and a real test run; Copilot never approves a PR                         |


Role arrangement: Sabin Lamichhane set up and owns the shared repository. With the tutor's approval (6 October 2026), each member leads a different stage: Stanley Campbell Stage 6, Nhat Minh Le Stage 7, Shaban Mohseni Stage 8, Sabin Lamichhane PG Stages 10 and 11; Stage 12 submission is completed together. Stanley authors all three Stage 6 changes, each on its own issue, branch and PR. A different group member reviews and approves each Stage 6 PR before merge; reviewers are recorded in section G.
## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner | Acceptance criteria or precise link | Status |
|---|---|---|---|-----|
|https://github.com/Sabin77/st1-assignment-3/issues/2 | FR-02 Patient Search| Stanley Campbell | Five criteria listed in issue #2 (same object, LookupError, ValueError, spaces, case) | Open|
| https://github.com/Sabin77/st1-assignment-3/issues/3 | FR-03 supporting: Practitioner lookup | Stanley Campbell | Five criteria listed in issue #3 (same object, LookupError, ValueError, spaces, case) | Open |
| https://github.com/Sabin77/st1-assignment-3/issues/4 | FR-06 Appointment Cancellation with FR-07 retained history | Stanley Campbell | Six criteria listed in issue #4 (cancel and return same object, retained in history, repeat cancel, completed, LookupError, ValueError) | Open |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

### PR #5: Patient lookup (issue #2)

- PR link and title: https://github.com/Sabin77/st1-assignment-3/pull/5 "Add patient lookup by ID (closes #2)"
- Linked issue and requirement: https://github.com/Sabin77/st1-assignment-3/issues/2 (FR-02 Patient Search: Find a patient by patient ID)
- Feature branch: feature/patient-lookup
- Changed behaviour: PatientService.find_patient returns the stored Patient for a registered ID and raises LookupError for an unknown ID; blank or non-text IDs raise ValueError through the store's existing validation.
- Meaningful commits: https://github.com/Sabin77/st1-assignment-3/commit/fe6fa292aa4e2e7848b13287aae8365bc80fde9c (Add patient lookup by ID with LookupError for unknown IDs)
- Test command, directory and observed result: python -m pytest from project/ on fe6fa29: 13 passed (8 starter, 5 new)
- Another-member reviewer: Requested Sabin77 and minhleee5 on 29 October 2026; review pending
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: None in implementation or tests; required Copilot review comparison pending
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]
## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: [response]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

[response]

## L Stage 6 formative questions

1. What is version control?
Version control is a system that moniotors changes over time to recover data over time and allows teams to callaboratew on project and recover and fix mistakes.

In software development it is used to source code it can track digital files including conmfigures files. there are core concepts to control firstly,the repository which is alsso known as repo this allows the data to track history of projects and folders,the revision is a snaphot of files at a specific pointwhich includea a unique ID and a timestamp as well as author and a message describing what changes, the branch creates a seperate and isolated copy of the project so the author can focus on fixing the issue at hand rather than interrupting the who program, merging this allows to combine change from one brach back to the main branch
2. Why is a feature branch useful?

A feature branch isolates the development of a project fom the main code. This allows to write test and refine code without effecting other team members code.

3. What makes a commit a good engineering commit?

A good engineer commit is clear and logical. It allows teammates to understand why a change was made and trace bugs

4. What is a pull request?

A pull request is a proposal to merge code changes from one branch to another.

A pull request is the ability to pull a program from git to make changes.

5. What is the purpose of code review?

The puropse of a code review is to ensure software quality,maintain code accuracy, and share expertise across the team before code into the main reposository

6. What does a Git diff show?

It allows to compare changes in git repositrory and show modifications that has been made.

7. What is a Definition of Done?

Is a checklist agreed within the team which includes technicalities,functionality and the quality of the code and meeting the requirements of teh project.

8. What is the appropriate role of GitHub Copilot in pull-request review?

Github is automated personal assistant to the person. it's role is to handle to analyse the code give feedback posibble errors and improvements, so the engineer can focus on aritechure and business logic.

9. Why should individual contribution not be judged only by commit count?

[response]

10. What is the Stage 6 engineering rule?

[response]

## M Completion and handover

-  Starting SHA: 22820d3125215dce5d33d1eaef2b2b6959ae431e
- Final Stage 6 code SHA: [response]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
