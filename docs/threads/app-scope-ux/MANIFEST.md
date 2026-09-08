# ClimaScope — MANIFEST · thread-app-scope-ux

**Versión:** 1.0.0  
**Estado del THREAD:** ACTIVE  
**Idioma:** español (España)

## Identidad

```yaml
thread_id: thread-app-scope-ux
domain: UX / aplicación de exploración del Scope
status: ACTIVE
owner: línea de producto/UX
created: 2026-08-16
current_cycle: 1
origin:
  type: USER_DECLARED
  source_id: conversation
repository:
  knowledge_branch: knowledge
  created_from_knowledge_commit: 33757848176c6d8e3f53b5e2c35b7048b657b286
handoff:
  path: docs/threads/app-scope-ux/HANDOFF.md
  status: ACTIVE
```

## Responsabilidad

Diseñar la experiencia de usuario y la arquitectura conceptual de la aplicación que presenta y permite explorar los resultados del Scope de ClimaScope.

## Dentro de alcance

- flujo de usuario y navegación;
- mapa principal y jerarquía de información;
- visualización de Locations, Stations, Scope/Representativeness y Evidence;
- presentación de indicadores, estados de evaluación y trazabilidad;
- requisitos de datos para la interfaz.

## Fuera de alcance

- Water Score definitivo;
- interpolación;
- adquisición AEMET/W2;
- implementación de producción;
- modificación del modelo Station/Location/Evidence.

## Autoridad documental vigente

Ningún documento de conocimiento materializado todavía. Los futuros documentos de UX producidos por este THREAD quedarán bajo su autoridad salvo decisión distinta.

## Dependencias

- `docs/threads/station-location-evidence/MODEL.md`
- `docs/threads/water-pipeline/AUDIT_REPORT.md`
- documentos core de reglas y arquitectura.

## HANDOFF

`docs/threads/app-scope-ux/HANDOFF.md` es la única cola persistente de inputs pendientes de este THREAD.

## Estado actual

Ciclo activo de diseño conceptual de producto/UX. El primer objetivo es definir qué decisión o comprensión debe poder alcanzar un usuario en una sesión breve y, a partir de ello, el flujo principal antes de diseñar pantallas concretas.
