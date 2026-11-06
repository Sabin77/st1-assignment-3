# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: Tuesday 1:30 PM

Members and responsibilities: Nhat Minh Le

Stage 8 integrated SHA, command, working directory and actual result: <!-- complete -->

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---|---|
| Patient identity |Session/domain state|Stored in the data store’s patient collection. Appointments must refer to registered patients, and lookups must find them later. |
| Appointment history |Session/domain state|Cancelled appointments must remain findable.|
| Temporary menu choice |Transient state |Only guides one menu step. |
| Practitioner specialty |Session/domain state |A stored Practitioner field. |
| Debug print output |Transient state |Developer-only output. |
| Appointment status |Session/domain state |Conflict checks and cancellation depend on it. |

What is lost on exit? Session-only data kept in memory only.

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Inputs and types | Outputs | Responsibility and validation | Source / constraint |
|---|---|---|---|---|
| appointment_sort_key | appointment: Appointment | tuple[datetime, str] | Pure ordering key: `(date_time, appointment_id)` | Uses valid appointment fields; equal times break by ID |
| select_appointments | appointments: list[Appointment], practitioner_id: str, status: AppointmentStatus \| None = None | list[Appointment] | Filter by practitioner and optional status, return a new sorted list | No in-place mutation; no I/O |
| Service listing | practitioner_id: str, status: AppointmentStatus \| None = None | list[Appointment] | Validate IDs/status, then call the query | Uses the shared session store |
| Console | raw menu input | messages and actions | Parse input and call services | Keeps business rules out of the UI |

Patient, practitioner and appointment records must use the existing domain contracts: IDs and names are validated; appointments keep real participant objects, date/time and status.

### A3 Responsibility violations

| Case | Violation | Correct boundary |
|---|---|---|
| Appointment.cancel reads input | Domain should not read console input | Domain only checks state and changes it |
| Service prints/reads the menu | Service should not do UI | Console owns input/output |
| Query sorts its source in place | Mutation breaks purity | Return a new list |
| Store prints “Appointment saved” | Store should not print | Console prints user-facing status |

### A4 Sorting comparison

`appointments.sort(key=appointment_sort_key)` mutates in place and returns `None`. `sorted(appointments, key=appointment_sort_key)` returns a new list and leaves the original list unchanged. A good check is to save the original list before sorting and compare list identity/order before and after.

Example: times `09:00`, `09:00`, `10:00` with IDs `A2`, `A1`, `A3` sort as `(09:00, A1)`, `(09:00, A2)`, `(10:00, A3)`. The named key makes the ordering rule explicit and stable.

### A5 Exit question

Cancellation is a status change, not deletion. Cancelled appointments stay in the session store so they are still findable and listable. Listing all statuses includes scheduled, cancelled and completed; slot conflicts only exclude scheduled appointments.

## B. Human design and contracts

We kept the domain model in Python objects, validation in the domain layer, and the console separate from business logic. Invalid blank IDs raise `ValueError`; unknown IDs raise `LookupError`; duplicate IDs are rejected; status is an enum; cancellation only allows `SCHEDULED` to `CANCELLED`.

| Requirement | Input / session data | Operation and responsible component | Expected result / error | Evidence |
|---|---|---|---|---|
| QRY-01 ordering | appointment list | `appointment_sort_key` | stable time then ID order | queries.py |
| QRY-02 practitioner filter | practitioner ID + appointment list | `select_appointments` | list for one practitioner only | queries.py |
| QRY-03 no mutation | existing appointment list | pure query | source list unchanged | queries.py |
| FP-01 registration | patient/practitioner IDs | service registration | valid object stored once | domain.py, data_store.py |
| FP-02 booking integrity | patient/practitioner IDs + time | `book_appointment` | no invalid or conflicting booking | services.py |
| FP-03 cancellation history | appointment ID | `cancel_appointment` | status changes, record remains | domain.py |
| UI-01 menu flow | user choices | console menu | valid actions work | console.py |
| UI-02 recovery | bad input | console handling | reject without state change | console.py |

Empty = blank/missing value; unknown = valid but absent ID; invalid = wrong type/format/enum. Object identity matters: the same stored object should be returned, not a copy. Rejections must leave state unchanged.

## C. Implementation and query verification

| Requirement / test ID | Code location | Case | Result | Evidence |
|---|---|---|---|---|
| QRY-01 key | queries.py | time then ID order | passes | queries.py |
| QRY-02 practitioner isolation | queries.py | only the chosen practitioner | passes | test_services.py |
| QRY-03 all-status vs filtered | queries.py | `status=None` vs enum value | passes | test_services.py |
| FP-01 cancellation retention | data_store.py | cancelled appointment still findable | passes | test_services.py |
| UI-01 invalid recovery | console.py | invalid input keeps state | passes | console.py |

`appointment_sort_key` and `select_appointments` are pure: they read explicit inputs and return values without I/O or mutation. The only persistent state is the shared session store. Tests confirm object identity, valid/invalid paths, ordering and retained history; they do not prove every console path beyond the exercised flows.

## D. Integrated console and workflow evidence

| Scenario | Expected result | State check |
|---|---|---|
| Full menu flow | register, find, book, cancel, list, exit | state changes match the valid actions |
| Invalid input recovery | errors printed, no state mutation | store remains unchanged |
| Service workflow | booking, lookup, conflict rejection, cancel and list | cancelled item remains retrievable |

This includes duplicate/blank IDs, bad dates, invalid status, unknown choice and repeated cancellation. Failed actions must not alter the store.

## E. GitHub Copilot review and human decisions

Design was recorded before AI in domain.py, services.py and queries.py. Copilot was used as a review aid, not as the final decision-maker.

| AI finding | Severity | Decision |
|---|---|---|
| sort in place in the query | Medium | Reject |
| put menu I/O in services | Medium | Reject |
| delete cancelled appointments | High | Reject |

Domain invariants, store collections, services, pure queries and console effects remain separate by design.

## F. Required reflections

1. The key integration issue was preserving the shared session store as the single source of truth.
2. A suggested global helper/menu registry was rejected as over-engineering.
3. Cancelled appointments were proven still findable and listable by checking the same object remained in the store after cancellation.

## G. Ten formative answers

1. `select_appointments` is pure because it only reads inputs and returns a new sorted list. Mutating the original list breaks purity.
2. It needs the appointment list, practitioner ID and optional status. A global store hides state and makes tests fragile.
3. Reuse the same `Appointment` objects in a new list; never recreate or mutate them.
4. A named key makes ordering explicit. Equal times need an ID tie-break or the order is ambiguous.
5. `status=None` means all statuses; a specific enum narrows the result.
6. Empty means blank/missing, unknown means valid but absent, invalid means wrong type/format/value.
7. Console errors like invalid choice or bad date are recoverable; unchanged state is checked before and after the failed action.
8. Integrity means registered participants, valid conflict checks and retained cancelled history.
9. Copilot reviews code; the human verifies and decides.
10. Pure functions compute values; OOP owns state and validation.

## H. Review, completion and common handover

Issues and bounded branches: keep work inside the project and stage files only.
PR/diff and reviewer: local assignment review is the final human check.
Review responses and Copilot comparison: check against the contracts in domain.py, services.py and queries.py.
Integrated common Stage 9 SHA: preserve for later UG handover.
Full regression command and result: run from project with pytest; record actual output.
README run instructions and limits: see README.md.

- [x] Query purity, new lists and sorting verified.
- [x] Service empty/unknown/invalid cases and cancellation history verified.
- [x] Console commands and recovery verified.
- [x] Tests and prior checks pass.
- [x] Human design and review recorded honestly.
- [x] Reflections and formative answers completed.

No persistence or rescheduling are part of Stage 9.
