# ClimaScope — Manifest del hilo de arquitectura de hilos

**Versión:** 0.4.0  
**Estado:** CLOSED  
**Ciclo:** 1  
**Idioma:** español (España)  
**Repositorio:** `gineslm/climascope`  
**Rama de trabajo histórica:** `agent/thread-architecture`  
**Rama raíz de conocimiento:** `knowledge`

> **Hilo cerrado.** Su ciclo fundacional está cumplido: produjo y consolidó la arquitectura de hilos. El mantenimiento y la evolución de esa arquitectura corresponden a `thread-architecture-methodology-evolution`. Se conserva como registro de procedencia; no es una línea de trabajo activa.

## 1. Identidad

```yaml
thread_id: thread-architecture
domain: arquitectura de hilos de trabajo (ciclo fundacional)
status: CLOSED
owner: línea de arquitectura del proyecto
created: 2026-08-15
current_cycle: 1
origin:
  type: USER_DECLARED
  source_id: conversation
repository:
  knowledge_branch: knowledge
  created_from_knowledge_commit: 33757848176c6d8e3f53b5e2c35b7048b657b286
  work_branch: agent/thread-architecture
```

La rama `agent/thread-architecture` conserva el trabajo histórico de este ciclo. El estado autoritativo de conocimiento y arquitectura queda consolidado en `knowledge`.

## 2. Responsabilidad (cumplida)

Diseñar y consolidar el modelo operativo que permite a ClimaScope organizar conversaciones, responsabilidades, dominios, dependencias, HANDOFFs y trazabilidad sin depender del historial completo de ChatGPT.

## 3. Dentro de alcance

- arquitectura documental de hilos;
- identidad y responsabilidad de un hilo;
- estados y ciclos;
- manifests;
- THREAD BOOTSTRAP;
- dependencias versionadas;
- HANDOFFs y transferencia de responsabilidad;
- separación entre propuestas y decisiones;
- autoridad documental;
- reincorporación de conversaciones existentes;
- actividad operativa e índices derivados como capacidades futuras;
- integración con las reglas maestras y el contexto de ChatGPT;
- separación entre `knowledge`, `develop` y `main`.

## 4. Fuera de alcance

- diseño científico de Station / Location / Scope / Evidence;
- implementación del pipeline AEMET/W2;
- Water Score;
- interpolación;
- mapa/UI;
- ampliación de adquisición de datos;
- migraciones de datos no necesarias para esta arquitectura.

## 5. Documentos autoritativos

- `docs/THREAD_ARCHITECTURE.md` — arquitectura de hilos, versión 0.5.0.
- `docs/PROJECT_WORKING_RULES.md` — reglas permanentes del proyecto, versión 1.3.0.
- `docs/CHATGPT_PROJECT_CONTEXT.md` — integración ChatGPT ↔ repositorio, versión 1.3.0.

Todos estos documentos son autoritativos desde `knowledge` y su estado vigente se resuelve leyendo la rama, no esta lista histórica.

## 6. Dependencias

- `docs/PROJECT_WORKING_RULES.md` — reglas permanentes.
- `docs/CHATGPT_PROJECT_CONTEXT.md` — protocolo de incorporación y reincorporación.

## 7. Entregables completados

1. especificación `THREAD_ARCHITECTURE.md`;
2. manifest operativo de este hilo;
3. integración de la arquitectura en las reglas maestras y el contexto de ChatGPT;
4. formalización del THREAD BOOTSTRAP y del alta de THREAD vía MANIFEST;
5. separación explícita entre raíz `knowledge` y ciclo de software.

## 8. Continuación

La evolución controlada de la arquitectura, la metodología y las reglas —incluidas las revisiones posteriores a 0.3.0 (hasta la 0.5.0 vigente)— es responsabilidad de `thread-architecture-methodology-evolution`. Este hilo no reabre ciclo.

## 9. Referencias Git

- `created_from_knowledge_commit`: `3375784` (base histórica de alta; inmutable).
- Rama de trabajo histórica: `agent/thread-architecture`.

## 10. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 0.3.0 | 2026-08-15 | Manifest del ciclo fundacional (estado `READY_FOR_HANDOFF`). |
| 0.4.0 | 2026-08-23 | Cierre del hilo (`CLOSED`); saneo de referencias (arquitectura 0.5.0, reglas/contexto 1.3.0); campo de conocimiento migrado a la forma canónica `created_from_knowledge_commit`; retirada del handoff de salida y de la mención a «THREAD DECLARATION». |
