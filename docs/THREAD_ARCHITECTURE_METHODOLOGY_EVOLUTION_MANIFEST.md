# ClimaScope — Manifest del hilo de evolución de arquitectura y metodología

**Versión:** 0.1.0
**Estado:** Activo
**Estado del THREAD:** ACTIVE
**Ciclo:** 1
**Idioma:** español (España)
**Repositorio:** `gineslm/climascope`
**Rama raíz de conocimiento:** `knowledge`
**Rama de trabajo:** ninguna (THREAD documental)

## 1. Identidad

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
  # THREAD documental: sin work_branch/work_commit
```

`created_from_knowledge_commit` es el commit de `knowledge` desde el que se da de alta
el THREAD mediante la creación de su MANIFEST (referencia inmutable; no se actualiza
cuando `knowledge` avanza). El estado vigente del conocimiento se resuelve siempre desde
la rama `knowledge`.

## 2. Responsabilidad

Detectar, analizar, evaluar y consolidar propuestas de mejora de la arquitectura,
metodología y reglas operativas de ClimaScope originadas durante el trabajo de otros
THREAD, conservando origen y evidencia. Responsabilidad transversal de evolución
controlada; no sustituye ni resuelve el trabajo técnico de los THREAD especializados.

## 3. Dentro de alcance

- detectar y registrar mejoras de arquitectura, metodología y reglas operativas;
- recibir propuestas de otros THREAD y conservar origen/evidencia;
- contrastar cada propuesta con el conocimiento consolidado y los THREAD afectados;
- evaluar impacto, coherencia, prioridad y necesidad de consolidación;
- aceptar, rechazar o aplazar propuestas;
- consolidar las aceptadas en `knowledge`;
- detectar incoherencias entre declaraciones, MANIFESTs, HANDOFFs y reglas;
- mejorar bootstrap, trazabilidad y coordinación.

## 4. Fuera de alcance

- resolver el trabajo técnico de otros THREAD (Station/Location/Evidence, W2,
  pipeline, interpolación, mapa/UI, adquisición de datos);
- modificar la arquitectura por una observación aislada sin análisis;
- actuar como backlog genérico de tareas;
- sustituir la responsabilidad de los THREAD especializados;
- consolidar automáticamente toda propuesta recibida.

## 5. Documentos autoritativos

- `docs/THREAD_ARCHITECTURE_METHODOLOGY_EVOLUTION.md` — declaración del THREAD.
- `docs/THREAD_ARCHITECTURE_METHODOLOGY_EVOLUTION_HANDOFF.md` — HANDOFF de creación.
- `docs/THREAD_ARCHITECTURE_METHODOLOGY_EVOLUTION_IMPROVEMENTS.md` — registro de
  mejoras (borrador propuesto en este ciclo).

## 6. Dependencias

- `docs/THREAD_ARCHITECTURE.md` — arquitectura de hilos.
- `docs/THREAD_CONTEXT_BOOTSTRAP.md` — protocolo de bootstrap.
- `docs/PROJECT_WORKING_RULES.md` — reglas permanentes.
- `docs/CHATGPT_PROJECT_CONTEXT.md` — integración ChatGPT ↔ repositorio.
- MANIFESTs y HANDOFFs de los THREAD que aporten propuestas.

## 7. Entregables y validación

Entregables de este ciclo (en curso):

1. este MANIFEST;
2. registro de mejoras con formato mínimo de *improvement record*;
3. IMP-002 registrada (ausencia de MANIFEST) con decisión y evidencia.

Validación: coherencia con `THREAD_ARCHITECTURE.md` §7; consolidación en `knowledge`.

## 8. HANDOFF actual e histórico

```yaml
current_handoff:
  handoff_id: THREAD_ARCHITECTURE_METHODOLOGY_EVOLUTION_HANDOFF
  version: 1        # el HANDOFF no declara versión; asumido (ver Cuestiones abiertas)
  status: ACTIVE

handoff_history:
  - handoff_id: THREAD_ARCHITECTURE_METHODOLOGY_EVOLUTION_HANDOFF
    version: 1
    role: CREATION
    status: ACTIVE
```

## 9. Registro de mejoras vigente

- IMP-001 — `accepted` / consolidada.
- IMP-002 — `accepted` / consolidación `pending` (ausencia de MANIFEST; este documento
  es su remedio). Instancia de IMP-004.
- IMP-003 — `under_review` (semántica/nomenclatura de la referencia de conocimiento
  del MANIFEST; propuesta presentada, sin decidir).
- IMP-004 — `under_review` (ontología del modelo THREAD y taxonomía de `origin.type`;
  Alt 1 como hipótesis de trabajo; sin consolidar).

## 10. Cuestiones abiertas

- Versionado del HANDOFF: no declara `version`; se asume `1`. Convendría fijar campo.
- Observación (no abre mejora independiente): la convención de *nombre de fichero* de
  MANIFEST diverge (`THREAD_MANIFEST_ARCHITECTURE_THREAD.md` vs el patrón
  `..._MANIFEST.md` de este hilo). Queda vinculada a la futura revisión de estructura
  documental, no como mejora propia.
- Semántica/nomenclatura de la referencia de conocimiento del MANIFEST: tratada en
  **IMP-003** (`under_review`).
- `origin.type = USER_DECLARED` confirmado: el origen de la responsabilidad es una
  declaración del usuario, no una importación externa (no es `MIGRATED`) ni una
  derivación de otro hilo (no es `THREAD_DERIVED`). Ver `ORIGIN_TYPE_SEMANTICS.md` e
  IMP-004.

## 11. Referencias Git

- Commit de alta (creación del MANIFEST) = `created_from_knowledge_commit`: `1cb593d`.
