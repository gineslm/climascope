# ClimaScope — ChatGPT Project Context

**Version:** 1.0.0  
**Status:** Active  
**Repository:** `gineslm/climascope`  
**Primary branch for the current workstream:** `agent/water-pipeline-audit`

## Purpose

This document is the bridge between the ClimaScope ChatGPT Project and the GitHub repository. It tells conversations how to reconnect to the project's central source of truth, including conversations that were opened before these working rules existed.

The repository is the durable project memory. A conversation is a bounded work session, not the source of truth.

## Mandatory startup for a new conversation

Before doing substantive project work:

1. Connect to the GitHub repository `gineslm/climascope`.
2. Read `docs/PROJECT_WORKING_RULES.md`.
3. Read the latest relevant report in `docs/`.
4. Read the relevant `THREAD_*.md` handoff when one exists.
5. Inspect the current branch and relevant repository state.
6. Identify the responsibility of this conversation before expanding scope.

Do not assume that this conversation's memory is more authoritative than the repository.

## Mandatory re-entry for an existing conversation

A conversation that started before this context was installed can be brought into the project by saying:

> Reincorpórate al contexto del proyecto.

When this happens, the conversation must:

1. Read the project rules and current repository documentation.
2. Review the work already performed in the current conversation.
3. Compare conversation-derived information against the repository.
4. Identify information that is new, undocumented, obsolete, duplicated, contradictory, or outside the current thread's scope.
5. Distinguish facts, decisions, hypotheses, pending work, and assumptions.
6. Propose how relevant information should be synchronized into the repository.
7. Do not silently overwrite the repository when a conflict exists; surface the conflict and recommend a resolution.
8. Once the state is reconciled, define the responsibility and boundaries of the current conversation.

## Conversation responsibility contract

Every project conversation should establish:

```text
Conversation responsibility:
Owner / workstream:
In scope:
Out of scope:
Primary repository documents:
Primary code / data:
Expected deliverables:
Required validation:
Dependencies on other workstreams:
Next handoff:
```

If the user has not specified the responsibility, ask for it after reading the project context. If the preceding conversation makes a clear responsibility obvious, propose it and ask the user to confirm rather than silently broadening scope.

## Scope discipline

A conversation should work deeply on one bounded responsibility. If it discovers work belonging to another workstream:

- do not absorb it merely because it is technically possible;
- record it as a dependency, issue, or future handoff;
- preserve the information needed by the responsible workstream;
- continue with the current responsibility.

Examples of potentially separate workstreams include acquisition, AEMET/QC, water aggregation, Station/Location/Evidence modelling, spatial scope, interpolation, map/UI, scoring, documentary research, and data architecture.

## Repository synchronization

Relevant decisions and durable results discovered in a conversation must eventually be represented in GitHub. Prefer:

- versioned documentation for methodology and decisions;
- code and tests for executable behaviour;
- raw data with provenance;
- processed/derived data that can be regenerated;
- thread handoffs for work intended for another conversation.

Do not treat chat history as the only copy of a durable decision.

## Conflict protocol

When conversation state and repository state disagree, classify the discrepancy:

- **NEW:** exists in the conversation but not in the repository;
- **STALE:** repository information has been superseded by validated work;
- **CONFLICT:** both contain incompatible claims or decisions;
- **DUPLICATE:** the information already exists elsewhere;
- **OUT OF SCOPE:** relevant to the project but not to this conversation.

For `CONFLICT`, do not silently choose a side. Explain the discrepancy and obtain a decision when required.

## Documentation hierarchy

Use the following hierarchy:

1. `docs/PROJECT_WORKING_RULES.md` — permanent project working rules.
2. `docs/CHATGPT_PROJECT_CONTEXT.md` — instructions for connecting a ChatGPT conversation to the project.
3. Current project reports — validated project state and decisions.
4. `docs/THREAD_*.md` — bounded workstream instructions and handoffs.
5. Code, tests, configuration, and data — implementation/source evidence.
6. Conversation history — working context that must be synchronized when it contains durable project knowledge.

If documents disagree, surface the inconsistency and determine which source should be authoritative rather than silently merging them.

## Completion protocol

Before closing a workstream:

1. Run the relevant tests or validation.
2. Update affected documentation.
3. Update report/version references when required.
4. Commit the work to the appropriate branch.
5. Push when the workflow requires it.
6. Record the commit SHA.
7. Create/update a thread handoff when another conversation is expected to continue the work.
8. State remaining uncertainties and out-of-scope items.

## ChatGPT Project context — compact version

The following block may be copied into the permanent instructions/context of the ChatGPT Project:

> **ClimaScope project bootstrap**
>
> Repository: `gineslm/climascope`. GitHub is the durable source of truth. Before substantive work, connect to the repository and read `docs/PROJECT_WORKING_RULES.md`, the latest relevant report, and any relevant `docs/THREAD_*.md` handoff. Do not assume conversation memory is authoritative over the repository.
>
> Every conversation must have a bounded responsibility. Establish: responsibility, in scope, out of scope, primary documents, deliverables, validation, dependencies, and next handoff. Ask the user to define or confirm this boundary before expanding scope.
>
> Existing conversations can be reincorporated by the instruction: **"Reincorpórate al contexto del proyecto."** Then compare the work already done in the conversation with the repository, identify new/obsolete/duplicate/conflicting/out-of-scope information, and propose synchronization. Never silently overwrite the repository when a conflict exists.
>
> Durable project knowledge must be transferred to GitHub through versioned documentation, code/tests, data with provenance, or thread handoffs. Keep workstreams separated. At completion, validate, document, commit, record the SHA, and prepare the next handoff when needed.

## Maintenance

When the project's working method changes, update this document and `docs/PROJECT_WORKING_RULES.md` as appropriate, increment the relevant version, and record the change in the project report. The copy placed in ChatGPT Project instructions/context should then be refreshed from this repository document.