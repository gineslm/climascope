# ClimaScope — Project Working Rules

**Document version:** 1.0.0  
**Created:** 2026-08-15  
**Repository:** `gineslm/climascope`  
**Repository URL:** https://github.com/gineslm/climascope  
**Current working branch:** `agent/water-pipeline-audit`  
**Known local project root:** `C:\Users\User\Downloads\climate_refuge_aemet_v0_4`

## 1. Purpose

This document is the permanent operational contract for ClimaScope work across separate conversation threads. It exists so that project method, provenance, documentation practice, and handoff rules do not depend on the memory of a particular chat.

The Git repository is the central source of truth. A new thread must recover project state from the repository before making decisions or changes.

## 2. Mandatory first step for every new thread

Before doing project work, the thread must:

1. read this document;
2. inspect the current branch and Git status;
3. read the current project report(s);
4. inspect any task-specific handoff document;
5. identify the current documentation version and relevant commits;
6. inspect existing implementation/tests before proposing changes;
7. report any referenced document that is missing instead of inventing its contents.

A conversation's previous context is useful, but is not the project's authoritative record.

## 3. Repository and access

All work must be associated with the repository `gineslm/climascope`.

Required capabilities for an implementation thread:

- read repository files, branches and documentation;
- create/update files and commit changes on the agreed working branch, or create a dedicated feature branch when appropriate;
- have a local checkout when code execution or generated-data inspection is required;
- use the repository's Python environment and run `python -m pytest` for Python test validation.

Do not assume access to documents that exist only in another conversation. If they are not in the repository, request them or state that they are unavailable.

## 4. Branch and change discipline

- Do not work directly on the default branch unless explicitly requested.
- Prefer a task-specific branch such as `agent/<task>`.
- Keep unrelated changes out of the task commit.
- Do not overwrite or regenerate raw source data unnecessarily.
- Before committing, inspect `git status` and the diff/stat.
- A completed task must leave a reproducible Git state.

## 5. Documentation is versioned project state

Every substantive project document must contain a version identifier.

Recommended convention:

- major: structural/methodological change;
- minor: new documented capability, decision, or substantial section;
- patch: clarification, correction, or editorial update.

Documentation artifacts must be committed to GitHub.

The relevant project report must reference important documentation artifacts and record their current versions. This allows independent conversation threads to recover the latest state.

## 6. Reports and handoffs

The project uses three complementary document roles:

### Master rules

`docs/PROJECT_WORKING_RULES.md`

Permanent operating rules for all threads.

### Project reports

Examples include:

`docs/WATER_PIPELINE_AUDIT_REPORT.md`

Reports record what has actually been implemented, tested, measured, decided, and changed over time.

### Thread handoffs

Examples include:

`docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md`

Handoffs define the scope and starting context for a specialised next thread. They must contain repository, branch, local path when known, access requirements, objective, current state, constraints, deliverables, validation and completion protocol.

## 7. Completion protocol for every substantive thread

Before declaring a task complete:

1. run the relevant tests;
2. inspect generated outputs when applicable;
3. update the relevant report;
4. increment document version where substantive documentation changed;
5. create/update the next handoff if another thread is required;
6. commit changes with an intentional message;
7. push the agreed branch;
8. record the commit SHA in the final handoff/report;
9. state any remaining uncertainty or missing evidence.

## 8. Data provenance and evidence rules

ClimaScope must preserve the distinction between source facts, project-derived data, modelled values and qualitative evidence.

Every derived dataset or indicator should be traceable to:

- source/provider;
- source dataset or document;
- acquisition/observation period;
- transformation or calculation;
- relevant code/version;
- quality-control status.

Never silently convert missing data into zero.

Never present an interpolated or modelled value as a direct station observation.

Never treat absence of research as evidence of absence of risk.

## 9. Raw / processed / derived data

The project should progressively converge on a clear separation such as:

```text
data/
├── raw/          # source material; preserved and traceable
├── processed/    # cleaned/normalised representations
├── derived/      # indicators, scores, map layers, models
└── reports/      # generated or publication-facing outputs
```

Existing paths must not be moved solely for stylistic reasons. Migration requires a deliberate decision and documentation.

Current AEMET work is under `data/raw/aemet/`, including raw JSON, `.NO_DATA` acquisition evidence, QC outputs and W2 monthly/annual CSV outputs. Treat these as existing project state unless a documented migration is approved.

## 10. Station, Location and Evidence principles

The domain model must distinguish at least:

```text
Station -> observations
Location -> user-facing place/site being evaluated
Scope/Representativeness -> spatial relevance between stations and locations
Evidence -> quantitative, derived, or documentary support
```

A station observation is not automatically the value for every nearby location.

If interpolation is introduced later, it must be explicitly labelled as modelled/interpolated and retain method, provenance and uncertainty.

Quantitative station data and qualitative/documentary evidence are different evidence types but may both attach to a location.

## 11. Progressive acquisition and research

Do not attempt to download or investigate every possible location before prioritisation exists.

The preferred pipeline is:

```text
candidate
  -> screened
  -> quantitative data acquired
  -> QC passed
  -> documentary research prioritised
  -> assessed
  -> promoted / deprioritised / rejected
```

The project should prioritise promising locations/stations first and expand progressively.

Documentary research should also be proportional to the promise and relevance of a candidate. A location that has not yet been researched must remain explicitly `not_assessed` or equivalent, not `low risk` or `no risk`.

## 12. Map principles

The future map should be able to distinguish:

- physical stations;
- evaluated locations;
- station coverage/scope;
- direct observations;
- derived indicators;
- modelled/interpolated values;
- data quality;
- documentary evidence;
- provenance.

Spatial scope is a representation of relevance, not proof that a station measures conditions identically across the whole scope.

Interpolation is deferred until the Station/Location/Scope model and its uncertainty requirements are designed.

## 13. Current documented project state

At the time of version 1.0.0 of these rules:

- the water pipeline has been audited around AEMET stations `8416`, `3195` and `7012D`;
- W2 monthly and annual precipitation aggregation has been implemented and tested;
- the current aggregation preserves observed precipitation totals while exposing missing days, coverage and completeness;
- the test suite reached 13 tests after the latest aggregation changes;
- the next planned specialised task is the Station / Location / Scope / Evidence domain model.

For the detailed current state, read the latest `docs/WATER_PIPELINE_AUDIT_REPORT.md` and the task-specific handoff.

## 14. Known documentation inventory

The following project documents are known to be present and relevant from the current repository context:

| Document | Role | Version known |
|---|---|---:|
| `docs/PROJECT_WORKING_RULES.md` | Permanent project operating rules | 1.0.0 |
| `docs/WATER_PIPELINE_AUDIT_REPORT.md` | Water pipeline audit/report | 0.3.0 |
| `docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md` | Next-thread handoff | 0.1.0 |

This inventory is not a claim that these are the only documents ever created in other conversations. A document is part of the project method only once it is committed to the repository or otherwise explicitly incorporated into the report.

## 15. How to start a new thread

A new thread should receive a short instruction such as:

> Work on ClimaScope from the central GitHub repository. First read `docs/PROJECT_WORKING_RULES.md`, then the latest project report and the task-specific handoff. Treat GitHub as the source of truth, preserve provenance, do not invent missing project documents, and follow the completion protocol. Report the current documentation versions and branch before making substantive changes.

The task-specific handoff then defines the actual objective.

## 16. How to close a thread

The closing message should state:

- what was implemented or decided;
- tests/validation performed;
- documentation version changes;
- files/data affected;
- branch and commit SHA;
- unresolved questions;
- next handoff document, if applicable.

This keeps future threads independent of the historical chat while preserving the project's decision trail in Git.
