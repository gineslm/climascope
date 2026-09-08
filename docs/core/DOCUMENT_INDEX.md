# ClimaScope — Índice documental

**Versión:** 1.1.0  
**Estado:** Activo  
**Rama raíz de conocimiento:** `knowledge`

## Naturaleza

Artefacto derivado y no autoritativo de descubrimiento del corpus. Todos los THREADs pueden leer el corpus; `authority_thread` indica exclusivamente quién puede evolucionar directamente cada documento.

MANIFESTs, HANDOFFs e índices derivados no forman parte de este corpus documental: son artefactos operativos o de descubrimiento.

## Documentos

| path | purpose / scope | authority_thread | authority_manifest |
|---|---|---|---|
| `README.md` | punto de entrada general al proyecto, estructura vigente y ejecución básica | `thread-architecture-methodology-evolution` | `docs/core/threads/architecture-methodology-evolution/MANIFEST.md` |
| `docs/core/THREAD_ARCHITECTURE.md` | arquitectura operativa de THREADs, MANIFEST, HANDOFF y gobernanza documental | `thread-architecture-methodology-evolution` | `docs/core/threads/architecture-methodology-evolution/MANIFEST.md` |
| `docs/core/PROJECT_WORKING_RULES.md` | reglas operativas permanentes del proyecto | `thread-architecture-methodology-evolution` | `docs/core/threads/architecture-methodology-evolution/MANIFEST.md` |
| `docs/core/PROJECT_AGENT_CONTEXT.md` | integración entre agente y repositorio | `thread-architecture-methodology-evolution` | `docs/core/threads/architecture-methodology-evolution/MANIFEST.md` |
| `docs/core/THREAD_CONTEXT_BOOTSTRAP.md` | secuencia operativa para incorporar una conversación a un THREAD | `thread-architecture-methodology-evolution` | `docs/core/threads/architecture-methodology-evolution/MANIFEST.md` |
| `docs/core/GIT_COMMIT_RULES.md` | estrategia Git para registrar decisiones y su porqué | `thread-architecture-methodology-evolution` | `docs/core/threads/architecture-methodology-evolution/MANIFEST.md` |
| `docs/core/THREAD_INDEX_TEMPLATE.md` | forma canónica del índice materializado de THREADs | `thread-architecture-methodology-evolution` | `docs/core/threads/architecture-methodology-evolution/MANIFEST.md` |
| `docs/core/DOCUMENT_INDEX_TEMPLATE.md` | forma canónica del índice materializado del corpus documental | `thread-architecture-methodology-evolution` | `docs/core/threads/architecture-methodology-evolution/MANIFEST.md` |
| `docs/threads/station-location-evidence/MODEL.md` | modelo Station / Location / Scope / Evidence | `thread-station-location-evidence` | `docs/threads/station-location-evidence/MANIFEST.md` |
| `docs/threads/water-pipeline/AUDIT_REPORT.md` | estado científico/técnico auditado del pipeline de agua | `thread-water-pipeline` | `docs/threads/water-pipeline/MANIFEST.md` |
| `docs/threads/water-pipeline/SOURCE_AUDIT.md` | auditoría de fuentes para el pipeline de agua | `thread-water-pipeline` | `docs/threads/water-pipeline/MANIFEST.md` |
| `docs/threads/water-pipeline/W1_PRECIPITATION_QC.md` | semántica y resultados de QC de precipitación W1 | `thread-water-pipeline` | `docs/threads/water-pipeline/MANIFEST.md` |

## Mantenimiento

Regenerar cuando se cree, elimine o mueva un documento del corpus, cambie sustancialmente su ámbito o se transfiera su autoridad de evolución a otro THREAD.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 2026-09-08 | Primera materialización del índice documental. |
| 1.1.0 | 2026-09-08 | Se incorpora `README.md` como documento de entrada general bajo autoridad de metodología/arquitectura. |
