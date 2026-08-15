# ClimaScope — Manifest del hilo de arquitectura de hilos

**Versión:** 0.1.0  
**Estado:** ACTIVE  
**Ciclo:** 1  
**Idioma:** español (España)  
**Repositorio:** `gineslm/climascope`  
**Rama:** `agent/thread-architecture`

## 1. Identidad

```yaml
thread_id: thread-architecture
 domain: arquitectura de hilos de trabajo
status: ACTIVE
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
- `docs/PROJECT_WORKING_RULES.md` — reglas permanentes del proyecto.
- `docs/CHATGPT_PROJECT_CONTEXT.md` — integración ChatGPT ↔ repositorio.

## 6. Dependencias

- `docs/PROJECT_WORKING_RULES.md` — reglas permanentes.
- `docs/CHATGPT_PROJECT_CONTEXT.md` — protocolo de incorporación y reincorporación.

Las líneas de dominio, incluido Station/Location/Evidence y W2, son dependencias contextuales pero no pertenecen a la responsabilidad de este hilo.

## 7. Entregables

1. especificación `THREAD_ARCHITECTURE.md`;
2. manifest operativo de este hilo;
3. integración mínima de la arquitectura en las reglas maestras y el contexto ChatGPT;
4. validación documental de coherencia;
5. handoff siguiente si queda trabajo especializado pendiente.

## 8. Criterio de cierre

El ciclo puede cerrarse cuando la arquitectura esté integrada en las reglas maestras, la documentación sea coherente y versionada, y quede definido el siguiente trabajo necesario sin asumir responsabilidades de otros dominios.

## 9. Estado abierto

Quedan deliberadamente pendientes de futuros ciclos:

- formato general definitivo de manifests;
- Activity Log persistente;
- automatización de dependencias desactualizadas;
- índices derivados;
- reglas detalladas para reestructuración de dominios.
