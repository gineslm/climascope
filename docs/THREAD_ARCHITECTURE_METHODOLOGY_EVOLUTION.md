# THREAD — Architecture & Methodology Evolution

## Identity

- `thread_id`: `thread-architecture-methodology-evolution`
- `status`: `ACTIVE`
- `origin`: `USER_DECLARED`
- `knowledge_branch`: `knowledge`
- `responsibility`: identificar, analizar, evaluar y consolidar propuestas de mejora de la arquitectura, metodología y reglas operativas de ClimaScope originadas durante el trabajo de otros THREAD.

## Purpose

Este THREAD actúa como responsabilidad transversal de evolución controlada de la arquitectura y metodología del proyecto. No sustituye a los THREAD especializados ni modifica directamente su trabajo técnico.

## Scope

### In scope

- detectar y registrar mejoras de arquitectura, metodología y reglas operativas;
- recibir propuestas originadas en otros THREAD;
- conservar el origen y la evidencia de cada propuesta;
- contrastar una propuesta con el conocimiento consolidado y los THREAD afectados;
- evaluar impacto, coherencia, prioridad y necesidad de consolidación;
- aceptar, rechazar o aplazar propuestas;
- consolidar las mejoras aceptadas en `knowledge` mediante el flujo establecido;
- detectar incoherencias entre declaraciones, MANIFESTs, HANDOFFs y reglas;
- mejorar los mecanismos de bootstrap, trazabilidad y coordinación.

### Out of scope

- resolver directamente el trabajo técnico de otros THREAD;
- modificar la arquitectura por una observación aislada sin análisis;
- convertirse en un backlog genérico de tareas;
- sustituir la responsabilidad de los THREAD especializados;
- consolidar automáticamente toda propuesta recibida.

## Improvement lifecycle

```text
observation
    ↓
proposal
    ↓
under_review
    ↓
accepted / rejected / deferred
    ↓
consolidated (si procede)
```

Toda propuesta debe conservar como mínimo:

- identificador;
- THREAD de origen;
- resumen;
- evidencia o referencia al documento/conversación que la origina;
- estado;
- decisión y justificación cuando se cierre.

## Knowledge authority

`knowledge` es la fuente autoritativa del estado consolidado. La rama de trabajo asociada al THREAD contiene el trabajo operativo, pero no sustituye al estado consolidado.

Cuando se cree o actualice un MANIFEST, cualquier referencia al estado desde el que nació debe utilizar `created_from_knowledge_commit` como referencia histórica. No debe utilizarse un campo ambiguo `knowledge_commit` para representar el estado actual.

## Initial improvement seed

Este THREAD nace con una propuesta de mejora derivada de las pruebas del protocolo de bootstrap:

**Separar explícitamente el commit de conocimiento desde el que se crea un THREAD (`created_from_knowledge_commit`) del estado vigente de la rama `knowledge`.**

Origen: pruebas de creación y reconexión de THREAD realizadas antes de la creación de este THREAD.

Estado inicial: `accepted` y ya incorporado a la arquitectura/documentación vigente.

## Dependencies

- `THREAD_ARCHITECTURE.md`
- `THREAD_CONTEXT_BOOTSTRAP.md`
- `PROJECT_WORKING_RULES.md`
- MANIFESTs y HANDOFFs de los THREAD que aporten propuestas

## Operating principle

> El conocimiento de evolución debe poder recorrer el camino de vuelta hasta su origen. Una mejora consolidada no pierde la referencia al THREAD que la detectó ni a la evidencia que justificó su análisis.
