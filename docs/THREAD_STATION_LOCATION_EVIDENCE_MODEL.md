# Handoff de nuevo hilo: modelo Station / Location / Evidence

**Versión del documento:** 0.1.3  
**Proyecto:** ClimaScope  
**Repositorio:** `gineslm/climascope`  
**Rama raíz de conocimiento:** `knowledge`  
**Rama de trabajo asociada:** `agent/water-pipeline-audit`

> **Regla de bootstrap:** esta copia del HANDOFF puede encontrarse desde una rama de trabajo histórica. Su presencia en esa rama no la convierte en fuente de verdad. Antes de leer o utilizar cualquier otro documento de proyecto desde esta rama, el agente DEBE cambiar conceptualmente a `knowledge` y reconstruir desde allí el estado consolidado.

## Fuente de verdad y precedencia

La autoridad para reconstruir el proyecto es:

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

La rama `agent/water-pipeline-audit` es únicamente una rama de trabajo. **No puede utilizarse para determinar por sí sola reglas vigentes, arquitectura, identidad de THREADs, MANIFESTs, HANDOFF vigente, decisiones consolidadas ni estado global del proyecto.**

Si el agente entra inicialmente por `agent/water-pipeline-audit`, debe tratar esa entrada como un estado de trabajo potencialmente obsoleto y saltar primero a `knowledge`. No debe tomar como vigentes las versiones documentales encontradas en la rama de trabajo hasta contrastarlas con `knowledge`.

**Base de conocimiento:**

```yaml
knowledge_basis:
  branch: knowledge
  commit: 33757848176c6d8e3f53b5e2c35b7048b657b286
```

El commit anterior es histórico. El MANIFEST/estado consolidado vigente puede actualizarlo posteriormente.

## Objetivo

Diseñar y documentar el modelo de dominio:

```text
Station -> Location -> Scope/Representativeness -> Evidence
```

Primero diseño; no implementar prematuramente interpolación ni Water Score definitivo.

## Decisiones ya consolidadas

1. Una estación no representa automáticamente una ubicación cercana.
2. El mapa debe distinguir estaciones físicas y alcance/representatividad espacial.
3. Observado en estación, relevante para ubicación y modelado/interpolado para ubicación son estados semánticamente distintos.
4. La interpolación queda aplazada y, si se introduce, debe conservar método, trazabilidad e incertidumbre.
5. La adquisición e investigación son progresivas.
6. `not_assessed` no significa ausencia de riesgo.
7. Los datos cuantitativos y la evidencia cualitativa/documental son tipos de evidencia distintos que pueden asociarse a una ubicación.
8. Deben preservarse AEMET raw/W2 y su trazabilidad salvo migración deliberada.

## Alcance

Resolver:

- modelo canónico `Station`;
- modelo `Location`;
- `Scope / Representativeness`;
- abstracción `Evidence`;
- cardinalidades y relaciones;
- trazabilidad;
- estados de adquisición/investigación;
- requisitos del mapa;
- prerrequisitos de una futura interpolación;
- estrategia de implementación/migración compatible con AEMET/W2.

Fuera de alcance inmediato: ampliación indiscriminada de adquisición, interpolación de producción, Water Score definitivo y reinterpretación silenciosa de datos existentes.

## Protocolo de inicio

Al recibir este HANDOFF:

1. entrar en `knowledge`;
2. leer `docs/CHATGPT_PROJECT_CONTEXT.md`;
3. leer `docs/PROJECT_WORKING_RULES.md`;
4. leer `docs/THREAD_ARCHITECTURE.md`;
5. localizar el MANIFEST y el estado consolidado del THREAD;
6. validar la versión vigente del HANDOFF desde `knowledge`;
7. solo después resolver `work_branch` y consultar `agent/water-pipeline-audit` para trabajo operativo;
8. si las versiones de la rama de trabajo difieren, tratar las de `knowledge` como autoritativas y señalar la discrepancia;
9. no continuar basándose únicamente en documentos encontrados en la rama de trabajo.

## Entregables

1. modelo de dominio documentado;
2. estructuras propuestas para `Station`, `Location`, `Scope/Representativeness` y `Evidence`;
3. relaciones/cardinalidades;
4. trazabilidad;
5. estados de adquisición/investigación;
6. requisitos de mapa;
7. decisión explícita sobre interpolación y prerrequisitos;
8. plan de migración sin alterar innecesariamente AEMET raw/W2;
9. validaciones/tests cuando exista implementación;
10. actualización versionada del informe correspondiente.

## Protocolo de cierre

Al terminar: validar, documentar, actualizar MANIFEST/HANDOFF cuando proceda, hacer commit, registrar SHA y consolidar en `knowledge` cualquier cambio que modifique conocimiento o estructura autoritativos.

## Instrucción de inicio

> Trabaja desde este HANDOFF. Antes de utilizar cualquier documento de la rama de trabajo, entra en `knowledge`, reconstruye el estado consolidado y resuelve desde el MANIFEST el estado vigente y la rama de trabajo asociada. La rama de trabajo nunca sustituye a `knowledge` como fuente de verdad global. Después continúa con el diseño `Station / Location / Scope / Evidence` sin escribir código de producción hasta cerrar el modelo.
