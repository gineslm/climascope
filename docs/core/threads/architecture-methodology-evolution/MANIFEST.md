# ClimaScope — MANIFEST · thread-architecture-methodology-evolution

**Versión:** 1.0.0  
**Estado del THREAD:** ACTIVE  
**Ciclo:** 1  
**Idioma:** español (España)

## Identidad

```yaml
thread_id: thread-architecture-methodology-evolution
domain: evolución controlada de arquitectura, metodología y reglas operativas
status: ACTIVE
owner: línea de metodología/arquitectura del proyecto
created: 2026-08-16
current_cycle: 1
origin:
  type: USER_DECLARED
  source_id: conversation
repository:
  knowledge_branch: knowledge
  created_from_knowledge_commit: 1cb593d73820c90d9f6886673a46ae787a2846f4
handoff:
  path: docs/core/threads/architecture-methodology-evolution/HANDOFF.md
  status: ACTIVE
```

## Responsabilidad

Custodiar el estado de los problemas de arquitectura, metodología y reglas operativas de ClimaScope, evaluar propuestas procedentes de otros THREADs y gobernar la evolución del conocimiento de sistema dentro de ese alcance.

## Dentro de alcance

- arquitectura de THREADs, MANIFEST y HANDOFF;
- reglas permanentes y bootstrap;
- estrategia Git para conocimiento/decisiones;
- plantillas e índices de descubrimiento;
- coherencia de artefactos operativos entre THREADs;
- evolución de la gobernanza documental.

## Fuera de alcance

- conocimiento científico de Station/Location/Evidence;
- adquisición, QC y agregación de agua/clima;
- UX de producto;
- cambios técnicos en otros dominios salvo propuestas dirigidas a sus HANDOFFs.

## Autoridad documental vigente

- `docs/core/THREAD_ARCHITECTURE.md`
- `docs/core/PROJECT_WORKING_RULES.md`
- `docs/core/PROJECT_AGENT_CONTEXT.md`
- `docs/core/THREAD_CONTEXT_BOOTSTRAP.md`
- `docs/core/GIT_COMMIT_RULES.md`
- `docs/core/THREAD_INDEX_TEMPLATE.md`
- `docs/core/DOCUMENT_INDEX_TEMPLATE.md`
- `docs/core/THREAD_INDEX.md` cuando exista
- `docs/core/DOCUMENT_INDEX.md` cuando exista

## Dependencias

- MANIFESTs y HANDOFFs de todos los THREADs cuando una propuesta afecte a su coherencia.
- Documentos del corpus relevantes para evaluar cambios transversales.

## HANDOFF

`docs/core/threads/architecture-methodology-evolution/HANDOFF.md` es la única cola persistente de inputs pendientes de este THREAD. Las decisiones ya resueltas pertenecen al historial Git, no a este MANIFEST ni a un registro paralelo.

## Cuestiones abiertas

- posible futura taxonomía de tipos de THREAD;
- organización física futura del corpus;
- automatización de validaciones de coherencia entre índices, MANIFESTs y documentos.
