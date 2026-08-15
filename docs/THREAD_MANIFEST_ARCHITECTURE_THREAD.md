# ClimaScope — Manifest del hilo de arquitectura de hilos

**Versión:** 0.1.1  
**Estado:** READY_FOR_HANDOFF  
**Ciclo:** 1  
**Idioma:** español (España)  
**Repositorio:** `gineslm/climascope`  
**Rama:** `agent/thread-architecture`

## 1. Identidad

```yaml
thread_id: thread-architecture
domain: arquitectura de hilos de trabajo
status: READY_FOR_HANDOFF
owner: línea de arquitectura del proyecto
created: 2026-08-15
current_cycle: 1
```

## 2. Responsabilidad

Diseñar y consolidar el modelo operativo que permite a ClimaScope organizar conversaciones, responsabilidades, dominios, dependencias, handoffs y trazabilidad sin depender del historial completo de ChatGPT.

## 3. Dentro de alcance

- arquitectura documental de hilos;
- identidad y responsabilidad de un hilo;
- estados y ciclos;
- manifests;
- dependencias versionadas;
- handoffs y transferencia de responsabilidad;
- separación entre propuestas y decisiones;
- autoridad documental;
- reincorporación de conversaciones existentes;
- actividad operativa e índices derivados como capacidades futuras;
- integración de esta arquitectura con las reglas maestras y el contexto de ChatGPT.

## 4. Fuera de alcance

- diseño científico de Station / Location / Scope / Evidence;
- implementación del pipeline AEMET/W2;
- Water Score;
- interpolación;
- mapa/UI;
- ampliación de adquisición de datos;
- migraciones de datos no necesarias para esta arquitectura.

## 5. Documentos autoritativos

- `docs/THREAD_ARCHITECTURE.md` — arquitectura de hilos, versión 0.1.0.
- `docs/PROJECT_WORKING_RULES.md` — reglas permanentes del proyecto, versión 1.1.0.
- `docs/CHATGPT_PROJECT_CONTEXT.md` — integración ChatGPT ↔ repositorio, versión 1.1.0.

## 6. Dependencias

- `docs/PROJECT_WORKING_RULES.md` — reglas permanentes.
- `docs/CHATGPT_PROJECT_CONTEXT.md` — protocolo de incorporación y reincorporación.

Las líneas de dominio, incluido Station/Location/Evidence y W2, son dependencias contextuales pero no pertenecen a la responsabilidad de este hilo.

## 7. Entregables completados

1. especificación `THREAD_ARCHITECTURE.md`;
2. manifest operativo de este hilo;
3. integración de la arquitectura en las reglas maestras y el contexto de ChatGPT;
4. handoff receptor único para `thread-station-location-evidence`.

## 8. Handoff siguiente

**Receptor único:** `thread-station-location-evidence`  
**Documento:** `docs/THREAD_HANDOFF_STATION_LOCATION_EVIDENCE.md`  
**Estado:** `READY_FOR_HANDOFF`

El receptor debe utilizar además `docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md` como documento de requisitos específicos de la tarea.

## 9. Criterio de cierre

El ciclo puede cerrarse porque la arquitectura está integrada en las reglas maestras, el contexto de ChatGPT y dispone de un handoff receptor único, sin asumir responsabilidades del dominio Station / Location / Scope / Evidence.

## 10. Estado abierto para futuros ciclos

Quedan deliberadamente pendientes de futuros ciclos:

- formato general definitivo de manifests;
- Activity Log persistente;
- automatización de dependencias desactualizadas;
- índices derivados;
- reglas detalladas para reestructuración de dominios.
