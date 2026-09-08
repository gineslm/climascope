# ClimaScope — Índice de THREADs

**Versión:** 1.0.0  
**Estado:** Activo  
**Rama raíz de conocimiento:** `knowledge`

## Naturaleza

Artefacto derivado y no autoritativo de descubrimiento. Se reconstruye desde los MANIFEST. Si existe discrepancia, prevalece el MANIFEST.

## THREADs

| thread_id | status | domain | responsibility | MANIFEST | HANDOFF |
|---|---|---|---|---|---|
| `thread-architecture` | `CLOSED` | arquitectura de hilos de trabajo (ciclo fundacional) | conservar la identidad y procedencia del ciclo fundacional; la evolución vigente pertenece al THREAD de metodología | `docs/core/threads/architecture/MANIFEST.md` | `docs/core/threads/architecture/HANDOFF.md` |
| `thread-architecture-methodology-evolution` | `ACTIVE` | evolución controlada de arquitectura, metodología y reglas operativas | custodiar el estado de los problemas de arquitectura/metodología y gobernar la evolución del conocimiento de sistema | `docs/core/threads/architecture-methodology-evolution/MANIFEST.md` | `docs/core/threads/architecture-methodology-evolution/HANDOFF.md` |
| `thread-app-scope-ux` | `ACTIVE` | UX / aplicación de exploración del Scope | diseñar la experiencia de usuario y arquitectura conceptual de la aplicación | `docs/threads/app-scope-ux/MANIFEST.md` | `docs/threads/app-scope-ux/HANDOFF.md` |
| `thread-station-location-evidence` | `ACTIVE` | modelo de dominio Station / Location / Scope / Evidence | diseñar y documentar el modelo de dominio y su trazabilidad | `docs/threads/station-location-evidence/MANIFEST.md` | `docs/threads/station-location-evidence/HANDOFF.md` |
| `thread-water-pipeline` | `ACTIVE` | adquisición, QC y agregación de agua/precipitación | adquirir, controlar calidad y agregar datos de agua/precipitación con trazabilidad | `docs/threads/water-pipeline/MANIFEST.md` | `docs/threads/water-pipeline/HANDOFF.md` |

## Mantenimiento

Regenerar cuando se cree, cierre/archive/reactive o cambie de responsabilidad un THREAD, o cuando cambie la ruta de su MANIFEST/HANDOFF.
