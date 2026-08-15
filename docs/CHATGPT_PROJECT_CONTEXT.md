# ClimaScope — Contexto del proyecto para ChatGPT

**Versión:** 1.0.1  
**Estado:** Activo  
**Repositorio:** `gineslm/climascope`  
**Rama principal del trabajo actual:** `agent/water-pipeline-audit`

> **Idioma oficial del proyecto: español (España).** Las conversaciones y la documentación deben desarrollarse en castellano, salvo términos técnicos que convenga conservar en su forma original.

## Propósito

Este documento es el puente entre el Proyecto de ChatGPT de ClimaScope y el repositorio GitHub. Indica a las conversaciones cómo reconectarse con la fuente central de verdad del proyecto, incluidas las conversaciones que se abrieron antes de que existieran estas reglas de trabajo.

El repositorio es la memoria duradera del proyecto. Una conversación es una sesión de trabajo acotada, no la fuente de verdad.

## Arranque obligatorio de una conversación nueva

Antes de realizar trabajo sustantivo del proyecto:

1. Conectarse al repositorio GitHub `gineslm/climascope`.
2. Leer `docs/PROJECT_WORKING_RULES.md`.
3. Leer el informe relevante más reciente de `docs/`.
4. Leer el handoff `THREAD_*.md` relevante cuando exista.
5. Inspeccionar la rama actual y el estado relevante del repositorio.
6. Identificar la responsabilidad de esta conversación antes de ampliar el alcance.

No asumir que la memoria de esta conversación es más autoritativa que el repositorio.

## Reincorporación obligatoria de una conversación existente

Una conversación que comenzó antes de instalar este contexto puede incorporarse al proyecto mediante la instrucción:

> **Reincorpórate al contexto del proyecto.**

Cuando se reciba esta instrucción, la conversación debe:

1. Leer las reglas del proyecto y la documentación actual del repositorio.
2. Revisar el trabajo ya realizado en la conversación actual.
3. Comparar la información derivada de la conversación con el repositorio.
4. Identificar información nueva, no documentada, obsoleta, duplicada, contradictoria o fuera del alcance del hilo actual.
5. Distinguir hechos, decisiones, hipótesis, trabajo pendiente y supuestos.
6. Proponer cómo sincronizar la información relevante con el repositorio.
7. No sobrescribir silenciosamente el repositorio cuando exista un conflicto; exponer el conflicto y recomendar una resolución.
8. Una vez reconciliado el estado, definir la responsabilidad y los límites de la conversación actual.

## Contrato de responsabilidad de la conversación

Toda conversación del proyecto debe establecer:

```text
Responsabilidad de la conversación:
Propietario / línea de trabajo:
Dentro de alcance:
Fuera de alcance:
Documentos principales del repositorio:
Código / datos principales:
Entregables esperados:
Validación requerida:
Dependencias de otras líneas de trabajo:
Siguiente handoff:
```

Si el usuario no ha especificado la responsabilidad, preguntarla después de leer el contexto del proyecto. Si el contexto previo de la conversación hace evidente una responsabilidad, proponerla y pedir confirmación en lugar de ampliar el alcance silenciosamente.

## Disciplina de alcance

Una conversación debe trabajar en profundidad sobre una responsabilidad delimitada. Si descubre trabajo perteneciente a otra línea:

- no absorberlo simplemente porque sea técnicamente posible;
- registrarlo como dependencia, incidencia o futuro handoff;
- conservar la información necesaria para la línea responsable;
- continuar con la responsabilidad actual.

Ejemplos de líneas potencialmente separadas son adquisición, AEMET/QC, agregación de agua, modelado Station/Location/Evidence, alcance espacial, interpolación, mapa/UI, scoring, investigación documental y arquitectura de datos.

## Sincronización con el repositorio

Las decisiones relevantes y resultados duraderos descubiertos en una conversación deben quedar representados finalmente en GitHub. Priorizar:

- documentación versionada para metodología y decisiones;
- código y tests para comportamiento ejecutable;
- datos raw con trazabilidad;
- datos processed/derived que puedan regenerarse;
- handoffs para trabajo destinado a otra conversación.

No tratar el historial del chat como la única copia de una decisión duradera.

## Protocolo de conflictos

Cuando el estado de la conversación y el del repositorio no coincidan, clasificar la discrepancia:

- **NUEVO:** existe en la conversación pero no en el repositorio;
- **OBSOLETO:** la información del repositorio ha sido sustituida por trabajo validado;
- **CONFLICTO:** ambos contienen afirmaciones o decisiones incompatibles;
- **DUPLICADO:** la información ya existe en otro lugar;
- **FUERA DE ALCANCE:** es relevante para el proyecto pero no para esta conversación.

Ante un `CONFLICTO`, no elegir una versión silenciosamente. Explicar la discrepancia y obtener una decisión cuando sea necesario.

## Jerarquía documental

Utilizar la siguiente jerarquía:

1. `docs/PROJECT_WORKING_RULES.md` — reglas permanentes de trabajo del proyecto.
2. `docs/CHATGPT_PROJECT_CONTEXT.md` — instrucciones para conectar una conversación de ChatGPT con el proyecto.
3. Informes actuales del proyecto — estado y decisiones validadas.
4. `docs/THREAD_*.md` — instrucciones y handoffs de líneas de trabajo acotadas.
5. Código, tests, configuración y datos — evidencia de implementación/fuente.
6. Historial de conversación — contexto de trabajo que debe sincronizarse cuando contenga conocimiento duradero del proyecto.

Si los documentos discrepan, exponer la inconsistencia y determinar qué fuente debe ser autoritativa en lugar de fusionarlas silenciosamente.

## Protocolo de cierre

Antes de cerrar una línea de trabajo:

1. Ejecutar la validación o los tests relevantes.
2. Actualizar la documentación afectada.
3. Actualizar las referencias de versión del informe cuando proceda.
4. Hacer commit en la rama adecuada.
5. Hacer push cuando el flujo de trabajo lo requiera.
6. Registrar el SHA del commit.
7. Crear/actualizar un handoff si se espera otra conversación especializada.
8. Indicar incertidumbres restantes y elementos fuera de alcance.

## Contexto de proyecto para ChatGPT — versión compacta

El siguiente bloque puede copiarse en las instrucciones/contexto permanente del Proyecto de ChatGPT:

> **Arranque del proyecto ClimaScope**
>
> Repositorio: `gineslm/climascope`. GitHub es la fuente duradera de verdad. Antes de realizar trabajo sustantivo, conecta con el repositorio y lee `docs/CHATGPT_PROJECT_CONTEXT.md`, `docs/PROJECT_WORKING_RULES.md`, el informe relevante más reciente y cualquier `docs/THREAD_*.md` aplicable. No asumas que la memoria de la conversación es autoritativa frente al repositorio.
>
> Toda conversación debe tener una responsabilidad delimitada. Establece: responsabilidad, dentro de alcance, fuera de alcance, documentos principales, entregables, validación, dependencias y siguiente handoff. Pide al usuario que defina o confirme estos límites antes de ampliar el alcance.
>
> Las conversaciones existentes pueden reincorporarse mediante la instrucción: **«Reincorpórate al contexto del proyecto.»** Después compara el trabajo realizado en la conversación con el repositorio, identifica información nueva/obsoleta/duplicada/en conflicto/fuera de alcance y propone su sincronización. Nunca sobrescribas silenciosamente el repositorio cuando exista un conflicto.
>
> El conocimiento duradero del proyecto debe trasladarse a GitHub mediante documentación versionada, código/tests, datos con trazabilidad o handoffs. Mantén separadas las líneas de trabajo. Al terminar, valida, documenta, haz commit, registra el SHA y prepara el siguiente handoff cuando sea necesario.

## Mantenimiento

Cuando cambie el método de trabajo del proyecto, actualizar este documento y `docs/PROJECT_WORKING_RULES.md` cuando corresponda, incrementar la versión relevante y registrar el cambio en el informe del proyecto. La copia colocada en las instrucciones/contexto del Proyecto de ChatGPT debe actualizarse entonces a partir de este documento del repositorio.
