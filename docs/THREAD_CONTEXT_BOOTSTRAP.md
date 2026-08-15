# ClimaScope — New Thread Context Bootstrap

**Document version:** 1.0.0  
**Created:** 2026-08-15  
**Repository:** `gineslm/climascope`  
**Repository URL:** https://github.com/gineslm/climascope  
**Default project root (known):** `C:\Users\User\Downloads\climate_refuge_aemet_v0_4`  
**Purpose:** reusable context/instruction block for opening a new ClimaScope conversation.

## 1. Purpose

This document is the standard bootstrap instruction for a new conversation working on ClimaScope.

Its purpose is to make each conversation:

- independent of previous chat history;
- connected to the central repository;
- aware of the current project method and documentation;
- explicitly scoped to one responsibility;
- prevented from silently taking responsibility for unrelated areas.

The repository is the source of truth. The conversation is a working session, not the permanent project memory.

## 2. Bootstrap instruction

When this document is supplied as project context, the conversation should follow this sequence before substantive work:

> **ClimaScope project bootstrap**
>
> Work against the central GitHub repository `gineslm/climascope`.
>
> First read `docs/PROJECT_WORKING_RULES.md`. Then inspect the current branch, Git status, the latest relevant project report, and any task-specific handoff referenced by the user or found in `docs/`.
>
> Treat GitHub as the authoritative project record. Do not assume that information exists merely because it appeared in another conversation. If a referenced document is missing from the repository, report that fact and request it rather than inventing its contents.
>
> Before making substantive changes, report the relevant documentation versions and current branch.
>
> **Then stop and ask the project owner to define the responsibilities of this conversation:**
>
> 1. What specific part of ClimaScope is this conversation responsible for?
> 2. What is explicitly outside its scope?
> 3. Is the task design/documentation, implementation/code, data acquisition/QC, research/evidence, analysis/scoring, or another defined area?
> 4. Which task-specific handoff or document governs the work, if any?
> 5. What is the expected deliverable for this conversation?
>
> Do not start unrelated work while waiting for the responsibility boundary, unless the user has already supplied a sufficiently explicit scope.

## 3. Responsibility boundary

Every substantive conversation should establish a compact responsibility contract before work expands.

Recommended format:

```text
CONVERSATION RESPONSIBILITY

Owner/task:
In scope:
Out of scope:
Primary documents:
Primary code/data:
Expected deliverable:
Validation required:
Next handoff, if applicable:
```

The conversation must actively enforce this boundary.

### In-scope work

The conversation may:

- inspect project context needed to perform its assigned task;
- modify files directly relevant to the assigned task;
- add or update tests relevant to those changes;
- update documentation required to preserve the decision trail;
- create a handoff for the next specialised conversation.

### Out-of-scope work

The conversation must not silently:

- redesign unrelated subsystems;
- download broad datasets merely because they are available;
- modify raw source data without an explicit reason;
- define final scoring rules when the task is only data preparation;
- introduce interpolation when the assigned task does not cover it;
- perform exhaustive documentary research when the task is only quantitative screening;
- change project-wide methodology without documenting and escalating the decision;
- consume another conversation's responsibility merely because the work appears adjacent.

If an adjacent issue blocks the assigned task, record it as a dependency/open question rather than expanding scope automatically.

## 4. Required repository orientation

The first repository-oriented inspection should normally cover:

```text
1. docs/PROJECT_WORKING_RULES.md
2. latest relevant project report
3. relevant THREAD_* handoff
4. README.md where applicable
5. relevant source code
6. relevant tests
7. Git branch/status/diff
```

Do not inspect the entire repository indiscriminately. Start with the minimum context needed to establish the task boundary and then expand only where the assigned task requires it.

## 5. Current project documentation hierarchy

The project currently uses three principal document roles:

### Master rules

`docs/PROJECT_WORKING_RULES.md`

Permanent operating rules for all conversations. It defines provenance, branch discipline, documentation, data semantics and completion rules. fileciteturn46file0L2-L2

### Project reports

Example:

`docs/WATER_PIPELINE_AUDIT_REPORT.md`

Reports record implemented work, validated results, decisions, scope changes and current status. The latest water report is version 0.3.0 and records the current AEMET/W2 state. fileciteturn34file0L2-L2

### Task-specific handoffs

Example:

`docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md`

A handoff narrows the responsibility of a specialised next conversation and records its starting state, constraints and deliverables. The current Station/Location/Evidence handoff is version 0.1.0. fileciteturn35file0L2-L2

## 6. Known current project state

At the creation of this bootstrap document:

- repository: `gineslm/climascope`;
- current working branch for the water audit: `agent/water-pipeline-audit`;
- local project root known to the project: `C:\Users\User\Downloads\climate_refuge_aemet_v0_4`;
- AEMET/W2 work has been completed and locally validated with 13 tests;
- current AEMET raw and W2 outputs are under `data/raw/aemet/`;
- stations audited include `8416`, `3195`, and `7012D`;
- the next planned specialised design task is Station / Location / Scope / Evidence;
- interpolation is currently deferred;
- broad acquisition is currently deferred until prioritisation is designed;
- documentary research is intended to be progressive and prioritised rather than exhaustive.

These statements are context only. The latest report and handoff take precedence if versions or decisions have changed.

## 7. Scope isolation rules

ClimaScope should be developed as a set of bounded workstreams. Typical responsibilities may include:

```text
A. Project method / documentation
B. Station catalogue and acquisition
C. Climate data / QC
D. Water data / QC / aggregation
E. Station-Location-Scope domain model
F. Documentary evidence / qualitative research
G. Spatial analysis / interpolation
H. Scoring / ranking
I. Map / application UX
J. Data architecture / persistence
K. Testing / CI / release engineering
```

A conversation should normally own one primary workstream and, if necessary, a small number of explicitly named secondary dependencies.

Workstream labels are organisational aids, not permission to change unrelated project areas.

## 8. Escalation instead of scope expansion

When the conversation discovers a problem outside its responsibility, use:

```text
DISCOVERED OUT-OF-SCOPE ISSUE
Issue:
Why it matters to current task:
Evidence:
Recommended owner/workstream:
Blocking? yes/no
Proposed next handoff:
```

Only expand scope when the project owner explicitly authorises it or when the current task definition already includes that responsibility.

## 9. Documentation discipline

If a conversation makes a substantive methodological decision, the decision must not remain only in chat.

The conversation should:

1. identify the relevant report/document;
2. update its version;
3. record the decision and rationale at the appropriate level;
4. commit the documentation to GitHub;
5. reference the resulting commit in the closing message.

The master rules are changed only for project-wide operating rules, not for every task-level detail.

Task-specific decisions belong in the relevant report or handoff.

## 10. Data safety

The bootstrap inherits the project rules:

- preserve raw source material;
- never silently turn missing into zero;
- distinguish observed, derived and modelled values;
- preserve source/provenance;
- do not regenerate large datasets unnecessarily;
- do not treat `not_assessed` as `no risk`;
- use tests and QC before promoting data to analytical use.

## 11. Completion protocol

A substantive conversation should close with:

```text
RESPONSIBILITY CLOSED

In-scope work completed:
Out-of-scope issues discovered:
Files changed:
Data changed:
Tests/validation:
Documentation versions:
Branch:
Commit SHA:
Remaining uncertainty:
Next handoff:
```

The final project state must be reproducible from GitHub without requiring the historical conversation.

## 12. Copy/paste compact version for new conversations

The following block can be used directly as the opening context of a new conversation:

> **ClimaScope — conversation bootstrap**
>
> Repository: `gineslm/climascope`  
> Project root: `C:\Users\User\Downloads\climate_refuge_aemet_v0_4`  
> Source of truth: GitHub repository  
>
> Before doing any work, read `docs/PROJECT_WORKING_RULES.md`, then the latest relevant report and any task-specific `docs/THREAD_*` handoff. Inspect the relevant code/tests and report the current branch and documentation versions. Do not invent missing project documents; request them if needed.
>
> After orientation, ask me to define:
> 1. the responsibility of this conversation;
> 2. what is explicitly out of scope;
> 3. the primary documents/code/data it should work on;
> 4. the expected deliverable;
> 5. the required validation.
>
> Keep this conversation narrowly scoped. If you discover an adjacent issue, record it as an out-of-scope dependency rather than silently expanding the task. Any substantive decision must be versioned in the repository documentation. At completion, provide the files changed, tests, documentation versions, branch, commit SHA and next handoff if required.

## 13. Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-15 | Initial standard bootstrap protocol for independent, responsibility-bounded ClimaScope conversations. |
