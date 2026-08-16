# ClimaScope — MANIFEST del THREAD de diseño de aplicación Scope

**Versión:** 0.1.0  
**THREAD:** `thread-app-scope-ux`  
**Estado:** ACTIVE  
**Origen:** `USER_DECLARED`  
**Repositorio:** `gineslm/climascope`  
**Rama de conocimiento:** `knowledge`  
**Idioma:** español (España)

## 1. Responsabilidad

Diseñar la experiencia de usuario y la arquitectura conceptual de la aplicación que presenta y permite explorar los resultados del Scope de ClimaScope.

La aplicación debe permitir pasar de una visión territorial/global a una ubicación concreta y, desde ella, explorar estaciones relevantes, representatividad, indicadores y evidencia, manteniendo la distinción entre observación directa, resultado derivado y evidencia documental.

## 2. Dentro de alcance

- experiencia de usuario;
- objetivo y flujo principal de navegación;
- mapa principal;
- visualización de Locations;
- visualización de Stations y Scope/Representativeness;
- presentación de Evidence;
- presentación de indicadores y resultados del Scope;
- estados de evaluación y evidencia;
- arquitectura conceptual de pantallas y componentes;
- jerarquía de información;
- requisitos de datos para la interfaz;
- trazabilidad visible para el usuario.

## 3. Fuera de alcance

- definición del Water Score definitivo;
- implementación de interpolación;
- ampliación de adquisición AEMET;
- modificación del pipeline W2;
- implementación de producción de la aplicación;
- reinterpretación de observaciones de estación como valores de ubicación.

## 4. Dependencias

### Conocimiento

- `docs/PROJECT_WORKING_RULES.md` — reglas permanentes;
- `docs/CHATGPT_PROJECT_CONTEXT.md` — integración ChatGPT/proyecto;
- `docs/THREAD_ARCHITECTURE.md` — arquitectura de THREADs;
- `docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md` — modelo Station / Location / Scope / Evidence;
- `docs/WATER_PIPELINE_AUDIT_REPORT.md` — estado del pipeline y requisitos de presentación.

### Modelo de dominio

El diseño depende conceptualmente de:

```text
Station -> Location -> Scope/Representativeness -> Evidence
```

La aplicación debe respetar que una estación no representa automáticamente cualquier ubicación cercana y que observado, relevante para una ubicación y modelado/interpolado son estados semánticamente distintos.

## 5. Entregables

1. objetivo de usuario y propuesta de valor de la aplicación;
2. flujo principal de navegación;
3. arquitectura conceptual de la aplicación;
4. definición de pantallas y componentes principales;
5. comportamiento conceptual del mapa;
6. forma de presentar resultados y evidencia;
7. requisitos de datos y metadatos expuestos por la interfaz;
8. decisiones de diseño documentadas;
9. handoff posterior si se requiere implementación especializada.

## 6. Validación

Las propuestas deberán comprobarse frente a:

- reglas permanentes de ClimaScope;
- modelo Station / Location / Scope / Evidence vigente;
- trazabilidad de resultados;
- distinción entre observado, derivado, modelado e investigación documental;
- estados explícitos de evaluación, incluyendo `not_assessed` cuando corresponda;
- principio de que el mapa es una capa de navegación sobre la evidencia y no un sustituto de ella.

## 7. Ciclo actual

**Ciclo:** diseño conceptual de producto/UX.  
**Estado:** ACTIVE.

Primer objetivo del ciclo: responder qué decisión o comprensión debe poder alcanzar un usuario tras utilizar ClimaScope durante una sesión breve y, a partir de ello, definir el flujo de usuario antes de diseñar pantallas concretas.

## 8. Dependencias y coordinación

Este THREAD consume el modelo Station / Location / Scope / Evidence y los resultados derivados del pipeline, pero no modifica por sí mismo esas líneas de trabajo.

Si durante el diseño aparece una necesidad que requiere cambiar el modelo de dominio, el pipeline o la metodología de scoring, deberá registrarse como dependencia/propuesta y transferirse a la línea responsable en lugar de absorberla silenciosamente.

## 9. Estado de conocimiento de arranque

Base de conocimiento utilizada para inicializar este THREAD:

```yaml
branch: knowledge
commit: 33757848176c6d8e3f53b5e2c35b7048b657b286
```

Este SHA es la base indicada por el handoff consultado al crear el THREAD; el estado posterior de `knowledge` prevalece cuando exista una actualización.

## 10. Handoff

No existe todavía un handoff de salida. Se creará cuando el ciclo de diseño alcance un resultado suficientemente consolidado para transferir responsabilidad a otra línea.

## 11. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 0.1.0 | 2026-08-16 | Creación del THREAD y MANIFEST para el diseño de la aplicación que presenta los resultados del Scope. |
