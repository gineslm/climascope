# ClimaScope — Índice del proyecto

**Versión:** 0.1.0  
**Estado:** Activo  
**Idioma:** español (España)  
**Repositorio:** `gineslm/climascope`  
**Rama raíz de conocimiento:** `knowledge`

## Naturaleza de este documento

Artefacto de **descubrimiento**: permite localizar qué THREAD existen y dónde están sus MANIFEST. Es **derivado y no autoritativo** (`docs/core/THREAD_ARCHITECTURE.md` §15.2): debe poder reconstruirse a partir de los MANIFEST consolidados en `knowledge`. Si el índice y un MANIFEST discrepan, **prevalece el MANIFEST**. Este índice no da de alta THREAD: refleja los que ya existen.

## THREAD del proyecto

| thread_id | status | dominio | MANIFEST | handoff vigente | `created_from_knowledge_commit` |
|---|---|---|---|---|---|
| `thread-architecture` | CLOSED | arquitectura de hilos (ciclo fundacional) | `docs/core/threads/architecture/MANIFEST.md` | — | `3375784` |
| `thread-architecture-methodology-evolution` | ACTIVE | evolución de arquitectura, metodología y reglas | `docs/core/threads/architecture-methodology-evolution/MANIFEST.md` | `THREAD_ARCHITECTURE_METHODOLOGY_EVOLUTION_HANDOFF` | `1cb593d` |
| `thread-app-scope-ux` | ACTIVE | UX / aplicación de exploración del Scope | `docs/threads/app-scope-ux/MANIFEST.md` | — | `3375784` |
| `thread-station-location-evidence` | ACTIVE | modelo de dominio Station / Location / Scope / Evidence | `docs/threads/station-location-evidence/MANIFEST.md` | — | `84d8845` |

## Mantenimiento

Regenerar este índice tras cualquier alta, cierre o cambio de estado de un THREAD, o cuando cambie la ruta o identidad de un MANIFEST. El contenido de cada fila debe poder verificarse leyendo el MANIFEST correspondiente en `knowledge`.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 0.1.0 | 2026-08-23 | Primera materialización del índice derivado (IMP-008), consistente con los cuatro THREAD tras la consolidación de coherencia estructural (Lote 2A). |
