# ClimaScope — Contexto del proyecto para ChatGPT

**Versión:** 1.2.0  
**Estado:** Activo  
**Repositorio:** `gineslm/climascope`  
**Rama de consolidación documental:** `knowledge`

> **Idioma oficial del proyecto: español (España).** Las conversaciones y la documentación deben desarrollarse en castellano, salvo términos técnicos que convenga conservar en su forma original.

## Propósito

Este documento es el puente entre el Proyecto de ChatGPT de ClimaScope y el repositorio GitHub. Indica a las conversaciones cómo reconectarse con la fuente central de verdad del proyecto, incluidas las conversaciones que se abrieron antes de que existieran estas reglas de trabajo.

El repositorio es la memoria duradera del proyecto. Una conversación es una sesión de trabajo acotada, no la fuente de verdad.

La arquitectura operativa de los hilos está especificada en `docs/THREAD_ARCHITECTURE.md`. Los hilos deben utilizarla junto con `docs/PROJECT_WORKING_RULES.md`.

## Estado de conocimiento y ramas

ClimaScope separa el estado consolidado del conocimiento y estructura del proyecto del ciclo de integración del software:

```text
knowledge → conocimiento, arquitectura, THREADs, MANIFESTs, HANDOFFs y estado estructural consolidado
develop   → integración del software
main      → software estable/desplegable
```

`knowledge` es el **punto de entrada para descubrir el estado consolidado del proyecto**. Una nueva conversación no debe asumir que `main` contiene la arquitectura, los THREADs o los HANDOFFs internos.

Las ramas de trabajo son estados en evolución y no son autoritativas por el mero hecho de existir. Cuando un cambio modifica conocimiento o estructura autoritativos, debe consolidarse en `knowledge` mediante un commit identificable.

La existencia de un cambio consolidado en `knowledge` no implica que deba llegar a `develop` o `main`. El conocimiento puede avanzar antes, después o independientemente de su implementación en software.

## Arranque obligatorio de una conversación nueva

Antes de realizar trabajo sustantivo del proyecto:

1. Conectarse al repositorio GitHub `gineslm/climascope`.
2. Utilizar `knowledge` como referencia inicial para descubrir el estado consolidado de conocimiento y estructura.
3. Leer `docs/PROJECT_WORKING_RULES.md`.
4. Leer `docs/THREAD_ARCHITECTURE.md` cuando exista y sea aplicable.
5. Leer el informe relevante más reciente de `docs/`.
6. Leer el handoff `THREAD_*.md` relevante cuando exista.
7. Identificar la responsabilidad de esta conversación antes de ampliar el alcance.
8. Si existe un manifest aplicable, utilizarlo para reconstruir la identidad y el estado del hilo.
9. Si el THREAD tiene trabajo de software, resolver desde el MANIFEST la rama/commit de trabajo correspondiente.

No asumir que la memoria de esta conversación es más autoritativa que el repositorio.

### Entrada por HANDOFF

Si el usuario indica **«Parte del handoff `<id>`»**, primero se localiza el HANDOFF en `knowledge`. Si declara un THREAD receptor todavía inexistente, la primera responsabilidad operativa es crear/inicializar ese THREAD y su MANIFEST, registrando el origen como `HANDOFF`.

El HANDOFF transmite contexto y responsabilidad; el MANIFEST determina posteriormente el estado vigente. Un HANDOFF histórico no debe utilizarse para sustituir el estado actual del MANIFEST.

### Entrada por THREAD existente

Si el usuario indica **«Conecta con el hilo `<thread_id>`»**, se localiza primero el MANIFEST en `knowledge`. El agente debe utilizar el MANIFEST para determinar el estado, HANDOFF vigente y referencia Git actual del THREAD cuando proceda.

### Entrada desde responsabilidad nueva

Si una conversación nueva declara una responsabilidad sin HANDOFF previo, debe comprobar primero en `knowledge` si ya existe un THREAD compatible. Si no existe, se crea una declaración de THREAD de tipo `USER_DECLARED` y su MANIFEST, y se consolida en `knowledge` cuando constituya estado persistente.

## Reincorporación obligatoria de una conversación existente

Una conversación que comenzó antes de instalar este contexto puede incorporarse al proyecto mediante la instrucción:

> **Reincorpórate al contexto del proyecto.**

Cuando se reciba esta instrucción, la conversación debe:

1. Leer las reglas del proyecto, la arquitectura de hilos y la documentación actual del repositorio desde `knowledge`.
2. Revisar el trabajo ya realizado en la conversación actual.
3. Comparar la información derivada de la conversación con el repositorio.
4. Identificar información nueva, no documentada, obsoleta, duplicada, contradictoria o fuera del alcance del hilo actual.
5. Distinguir hechos, decisiones, hipótesis, trabajo pendiente y supuestos.
6. Proponer cómo sincronizar la información relevante con el repositorio.
7. No sobrescribir silenciosamente el repositorio cuando exista un conflicto; exponer el conflicto y recomendar una resolución.
8. Una vez reconciliado el estado, definir la responsabilidad, el estado y los límites de la conversación actual.

Las discrepancias deben clasificarse como `NUEVO`, `OBSOLETO`, `CONFLICTO`, `DUPLICADO` o `FUERA DE ALCANCE`, siguiendo la arquitectura de hilos.

## Contrato de responsabilidad de la conversación

Toda conversación del proyecto debe establecer:

```text
thread_id:
Responsabilidad de la conversación:
Propietario / línea de trabajo:
Estado / ciclo:
Dentro de alcance:
Fuera de alcance:
Documentos principales del repositorio:
Código / datos principales:
Entregables esperados:
Validación requerida:
Dependencias de otras líneas de trabajo:
Siguiente handoff:
```

Si la responsabilidad no es evidente, proponerla y pedir confirmación en lugar de ampliar el alcance silenciosamente.

## Disciplina de alcance

Una conversación debe trabajar en profundidad sobre una responsabilidad delimitada. Si descubre trabajo perteneciente a otra línea:

- no absorberlo simplemente porque sea técnicamente posible;
- registrarlo como dependencia, incidencia o futuro handoff;
- conservar la información necesaria para la línea responsable;
- continuar con la responsabilidad actual.

El hecho de que un hilo dependa de otro dominio no transfiere automáticamente su responsabilidad.

## Sincronización con el repositorio

Las decisiones relevantes y resultados duraderos descubiertos en una conversación deben quedar representados finalmente en GitHub. Priorizar:

- documentación versionada para metodología y decisiones;
- código y tests para comportamiento ejecutable;
- datos raw con trazabilidad;
- datos processed/derived que puedan regenerarse;
- handoffs para trabajo destinado a otra conversación;
- manifests cuando aporten valor operativo para reconstruir un hilo.

Cuando el cambio afecte a conocimiento o estructura autoritativos, la consolidación corresponde a `knowledge`. Los cambios de software siguen el ciclo de `develop` y `main` según las reglas de integración.

No tratar el historial del chat como la única copia de una decisión duradera.

## Propuestas frente a decisiones

Una conversación puede producir propuestas, hipótesis y alternativas. Deben distinguirse de las decisiones validadas.

La secuencia recomendada es:

```text
propuesta -> discusión -> decisión -> documentación -> implementación/validación
```

El chat no convierte por sí mismo una propuesta en conocimiento autoritativo.

## Jerarquía documental

Utilizar la siguiente jerarquía funcional dentro del estado consolidado de `knowledge`:

1. `docs/PROJECT_WORKING_RULES.md` — reglas permanentes de trabajo del proyecto.
2. `docs/CHATGPT_PROJECT_CONTEXT.md` — integración ChatGPT ↔ proyecto.
3. `docs/THREAD_ARCHITECTURE.md` — arquitectura operativa de los hilos.
4. Informes actuales del proyecto — estado y decisiones validadas.
5. Manifests y `docs/THREAD_*.md` — identidad, alcance y transferencias de líneas de trabajo.
6. Código, tests, configuración y datos — evidencia de implementación/fuente, según la rama correspondiente.
7. Historial de conversación — contexto de trabajo que debe sincronizarse cuando contenga conocimiento duradero.

La autoridad es funcional: las reglas no sustituyen a los datos, un handoff no sustituye a un informe científico y el chat no sustituye a ninguna fuente autoritativa.

## Protocolo de cierre

Antes de cerrar una línea de trabajo:

1. Ejecutar la validación o los tests relevantes.
2. Actualizar la documentación afectada.
3. Actualizar las referencias de versión del informe cuando proceda.
4. Actualizar el manifest o estado del ciclo cuando exista.
5. Hacer commit en la rama adecuada.
6. Hacer push cuando el flujo de trabajo lo requiera.
7. Registrar el SHA del commit.
8. Crear/actualizar un handoff si se espera otra conversación especializada.
9. Si el cambio modifica conocimiento o estructura autoritativos, consolidarlo en `knowledge`.
10. Si el cambio es de software, seguir el ciclo de integración correspondiente sin asumir que debe modificar `knowledge`.
11. Indicar incertidumbres restantes y elementos fuera de alcance.

## Contexto de proyecto para ChatGPT — versión compacta

El siguiente bloque puede copiarse en las instrucciones/contexto permanente del Proyecto de ChatGPT:

> **Arranque del proyecto ClimaScope**
>
> Repositorio: `gineslm/climascope`. GitHub es la fuente duradera de verdad. `knowledge` es la referencia estable para descubrir el estado consolidado de conocimiento y estructura del proyecto; `develop` y `main` representan el ciclo de integración del software. Antes de realizar trabajo sustantivo, conecta con el repositorio y lee desde `knowledge` `docs/CHATGPT_PROJECT_CONTEXT.md`, `docs/PROJECT_WORKING_RULES.md`, `docs/THREAD_ARCHITECTURE.md`, el informe relevante más reciente y cualquier manifest/handoff aplicable. No asumas que la memoria de la conversación ni `main` contienen por sí solos el estado completo del proyecto.
>
> Toda conversación debe tener una responsabilidad delimitada. Establece `thread_id`, responsabilidad, estado/ciclo, dentro de alcance, fuera de alcance, documentos principales, entregables, validación, dependencias y siguiente handoff. No absorbas silenciosamente trabajo de otra línea.
>
> Si el usuario indica «Parte del handoff `<id>`», localiza primero el HANDOFF en `knowledge`; si declara un THREAD receptor inexistente, créalo e inicialízalo como primera tarea. Si indica «Conecta con el hilo `<thread_id>`», localiza el MANIFEST en `knowledge` y utiliza su estado vigente. Si declara una responsabilidad nueva, comprueba primero si existe un THREAD compatible y, si no, créalo como `USER_DECLARED`.
>
> Las conversaciones existentes pueden reincorporarse mediante la instrucción: **«Reincorpórate al contexto del proyecto.»** Después compara el trabajo realizado en la conversación con el repositorio, identifica información nueva/obsoleta/duplicada/en conflicto/fuera de alcance y propone su sincronización. Nunca sobrescribas silenciosamente el repositorio cuando exista un conflicto.
>
> El conocimiento duradero del proyecto debe trasladarse a GitHub mediante documentación versionada, manifests o handoffs. Los cambios de conocimiento/estructura se consolidan en `knowledge`; el software sigue su ciclo en `develop` y `main`. Distingue propuestas de decisiones validadas. Al terminar, valida, documenta, actualiza el estado del hilo cuando corresponda, haz commit, registra el SHA y prepara el siguiente handoff cuando sea necesario.

## Mantenimiento

Cuando cambie el método de trabajo del proyecto, actualizar este documento y `docs/PROJECT_WORKING_RULES.md` cuando corresponda, incrementar la versión relevante y registrar el cambio en el informe del proyecto. La copia colocada en las instrucciones/contexto del Proyecto de ChatGPT debe actualizarse entonces a partir de este documento del repositorio.
