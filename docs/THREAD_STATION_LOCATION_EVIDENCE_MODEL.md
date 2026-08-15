# Handoff de nuevo hilo: modelo Station / Location / Evidence

**Versión del documento:** 0.1.4  
**Proyecto:** ClimaScope  
**Repositorio:** `gineslm/climascope`  
**Rama raíz de conocimiento:** `knowledge`  
**Rama de trabajo asociada:** `agent/water-pipeline-audit`

## Fuente de verdad y precedencia

El repositorio es la fuente central de verdad. Para este HANDOFF, `knowledge` es la raíz de conocimiento y el punto de entrada para reconstruir el estado consolidado del proyecto.

La rama `agent/water-pipeline-audit` es únicamente la **rama de trabajo asociada**. No constituye una fuente alternativa de verdad global y no debe utilizarse para reconstruir por sí sola el estado actual del THREAD.

El orden obligatorio es:

```text
knowledge
   ↓
reglas + contexto + arquitectura
   ↓
MANIFEST / HANDOFF vigente
   ↓
estado consolidado
   ↓
agent/water-pipeline-audit (solo trabajo asociado)
```

Si una instancia entra inicialmente por una rama de trabajo, debe tratar esa rama como potencialmente obsoleta y volver a `knowledge` antes de utilizar sus documentos como estado vigente. Las versiones de `knowledge` prevalecen sobre versiones encontradas en la rama de trabajo para reglas, arquitectura, identidad de THREAD, MANIFEST, HANDOFF, decisiones y estado global.

**Base histórica de conocimiento:**

```yaml
knowledge_basis:
  branch: knowledge
  commit: 33757848176c6d8e3f53b5e2c35b7048b657b286
```

Este commit identifica la base que originó el HANDOFF; el MANIFEST puede registrar posteriormente una base más reciente.

## Objetivo

Diseñar y documentar el modelo de dominio:

```text
Station -> Location -> Scope/Representativeness -> Evidence
```

Esta es primero una tarea de diseño. No implementar prematuramente interpolación ni Water Score definitivo.

## Decisiones ya consolidadas

1. Una observación de estación no es automáticamente el valor de una ubicación cercana.
2. El mapa debe distinguir estaciones físicas y alcance/representatividad espacial.
3. Deben distinguirse semánticamente: observado en estación, relevante para ubicación y modelado/interpolado para ubicación.
4. La interpolación queda aplazada y, si se introduce, debe conservar método, trazabilidad e incertidumbre.
5. La adquisición e investigación son progresivas.
6. `not_assessed` nunca significa ausencia de riesgo.
7. Datos cuantitativos de estaciones y evidencia cualitativa/documental son tipos de evidencia diferentes que pueden asociarse a una ubicación.
8. Deben preservarse AEMET raw/W2 y su trazabilidad salvo migración deliberada.

## Alcance

Resolver:

- modelo canónico `Station`;
- modelo `Location`;
- `Scope / Representativeness`;
- abstracción `Evidence`;
- cardinalidades y relaciones;
- trazabilidad;
- estados de adquisición/investigación progresivos;
- requisitos del mapa;
- prerrequisitos de futura interpolación;
- estrategia de implementación/migración compatible con AEMET/W2.

Fuera de alcance inmediato: ampliación indiscriminada de adquisición, interpolación de producción, Water Score definitivo y reinterpretación silenciosa de datos existentes.

## Protocolo de inicio

Al recibir este HANDOFF:

1. entrar en `knowledge`;
2. leer `docs/CHATGPT_PROJECT_CONTEXT.md`;
3. leer `docs/PROJECT_WORKING_RULES.md`;
4. leer `docs/THREAD_ARCHITECTURE.md`;
5. localizar el MANIFEST y reconstruir el estado consolidado del THREAD;
6. validar la versión vigente del HANDOFF desde `knowledge`;
7. solo después resolver `work_branch` y consultar `agent/water-pipeline-audit` para trabajo operativo;
8. si las versiones de la rama de trabajo difieren, tratar las de `knowledge` como autoritativas y señalar la discrepancia;
9. nunca reconstruir el estado global exclusivamente desde la rama de trabajo.

## Entregables

1. modelo de dominio documentado;
2. estructuras propuestas para `Station`, `Location`, `Scope/Representativeness` y `Evidence`;
3. relaciones/cardinalidades;
4. trazabilidad;
5. máquina de estados de adquisición/investigación;
6. requisitos orientados al mapa;
7. decisión explícita sobre interpolación y prerrequisitos;
8. plan de migración sin alterar innecesariamente AEMET raw/W2;
9. validaciones/tests cuando exista implementación;
10. actualización versionada del informe correspondiente.

## Protocolo de cierre

Al terminar: validar, documentar, actualizar MANIFEST/HANDOFF cuando proceda, hacer commit, registrar SHA y consolidar en `knowledge` cualquier cambio que modifique conocimiento o estructura autoritativos.

## Instrucción de inicio

> Trabaja desde este HANDOFF. Antes de utilizar cualquier documento de una rama de trabajo, entra en `knowledge`, reconstruye el estado consolidado y resuelve desde el MANIFEST el estado vigente y la rama de trabajo asociada. La rama de trabajo nunca sustituye a `knowledge` como fuente de verdad global. Después continúa con el diseño `Station / Location / Scope / Evidence` sin escribir código de producción hasta cerrar el modelo.
