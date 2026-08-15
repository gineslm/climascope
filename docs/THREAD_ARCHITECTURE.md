# ClimaScope — Arquitectura de hilos de trabajo

**Versión:** 0.2.0  
**Estado:** Especificación operativa  
**Idioma:** español (España)  
**Repositorio:** `gineslm/climascope`

## 1. Propósito

Este documento formaliza el modelo operativo de los hilos de trabajo de ClimaScope. Complementa `docs/PROJECT_WORKING_RULES.md` y `docs/CHATGPT_PROJECT_CONTEXT.md`; no los sustituye ni duplica sus reglas generales.

Su objetivo es que una conversación pueda **crear, incorporar, continuar o cerrar una línea de trabajo** sin depender del historial completo del chat.

La unidad persistente de trabajo es el **THREAD de proyecto**, no la conversación de ChatGPT. GitHub es la fuente duradera de verdad.

Una conversación es una **instancia operativa de IA** que se conecta a un THREAD. Puede haber distintas instancias de conversación trabajando sobre el mismo THREAD a lo largo de su ciclo de vida, siempre respetando el manifest y el estado vigente.

## 2. Principios

1. Un THREAD es una entidad persistente de trabajo; no es un chat.
2. Una conversación es una instancia operativa que puede conectarse a un THREAD.
3. Toda instancia debe tener una responsabilidad delimitada.
4. Una conversación no es por sí misma una fuente autoritativa del proyecto.
5. El conocimiento duradero debe sincronizarse con el repositorio.
6. Cada responsabilidad debe tener un propietario o línea de trabajo identificable.
7. Un THREAD no absorbe silenciosamente trabajo perteneciente a otra línea.
8. Las dependencias documentales deben poder identificarse y, cuando sea relevante, fijarse a una versión.
9. Un HANDOFF representa una transferencia de responsabilidad y puede declarar la creación de un THREAD receptor.
10. El MANIFEST es la autoridad sobre el estado actual del THREAD; un HANDOFF antiguo no puede sustituirlo.
11. Los conflictos entre conversación y repositorio se hacen explícitos; no se resuelven silenciosamente.
12. El cierre de un THREAD termina un ciclo de trabajo, no elimina su conocimiento.
13. Las vistas o índices derivados no sustituyen a las fuentes autoritativas.

## 3. Modelo conceptual

El sistema documental se organiza en las siguientes categorías:

```text
KNOWLEDGE  → qué sabe el proyecto
THREAD     → unidad persistente de responsabilidad
MANIFEST   → estado operativo actual del THREAD
HANDOFF    → declaración/transferencia de responsabilidad
ACTIVITY   → qué ocurrió durante la evolución del trabajo
DERIVED    → vistas o índices regenerables
```

Estas categorías son complementarias:

- **KNOWLEDGE** incluye metodología, especificaciones, decisiones e informes validados.
- **THREAD** define una unidad persistente de responsabilidad y su ciclo de vida.
- **MANIFEST** permite reconstruir la identidad y estado actual del THREAD.
- **HANDOFF** transmite contexto y responsabilidad entre hilos y puede actuar como declaración de creación de un receptor.
- **ACTIVITY** conserva eventos operativos significativos sin convertirse en una copia de las conversaciones.
- **DERIVED** contiene índices, resúmenes o vistas que pueden reconstruirse desde las fuentes.

## 4. THREAD como entidad persistente

Un THREAD existe independientemente de que haya una conversación abierta en ChatGPT. Su identidad se conserva en el repositorio mediante un MANIFEST.

Como mínimo, un THREAD debe poder identificarse mediante:

```yaml
thread_id:
domain:
status:
owner:
created:
current_cycle:
responsibility:
origin:
```

El `thread_id` es el identificador primario y permanece estable durante la vida del THREAD. Si la misma responsabilidad vuelve a abrirse posteriormente, se crea un nuevo ciclo o una nueva unidad de trabajo según determine el MANIFEST.

### 4.1 Origen del THREAD

Todo THREAD debe registrar cómo fue declarado inicialmente:

```yaml
origin:
  type: HANDOFF | USER_DECLARED | MIGRATED
  source_id:
```

- `HANDOFF`: el THREAD fue declarado por otro THREAD mediante una transferencia.
- `USER_DECLARED`: una conversación nueva declaró directamente una responsabilidad sin HANDOFF previo.
- `MIGRATED`: una responsabilidad o conversación existente fue formalizada posteriormente como THREAD.

El origen es histórico: no cambia porque el THREAD reciba posteriormente otros HANDOFF.

## 5. THREAD DECLARATION

Una **THREAD DECLARATION** es el acto mediante el cual una responsabilidad pasa a convertirse en un THREAD formal.

Puede originarse de tres formas:

```text
                 THREAD DECLARATION
                         │
            ┌────────────┼────────────┐
            ▼            ▼            ▼
         HANDOFF     USER_DECLARED   MIGRATED
            │            │            │
            └────────────┼────────────┘
                         ▼
                       THREAD
                         │
                         ▼
                      MANIFEST
```

La declaración no equivale todavía a trabajo técnico. Primero se inicializa la identidad, alcance, dependencias y estado del THREAD.

## 6. MANIFEST del THREAD

El MANIFEST es el **contrato persistente y fuente autoritativa del estado operativo actual del THREAD**. Permite reconstruir su identidad sin leer el historial completo de una conversación.

Como mínimo debe resolver:

- `thread_id`;
- dominio y responsabilidad;
- propietario/línea de trabajo;
- estado actual;
- ciclo actual;
- origen de la declaración;
- documentos autoritativos;
- dependencias;
- trabajo recibido;
- entregables esperados;
- validación;
- handoff actual, si existe;
- historial relevante de handoffs;
- cuestiones abiertas;
- siguiente transferencia prevista.

### 6.1 Handoff actual e histórico

El MANIFEST debe evitar que una conexión al THREAD seleccione arbitrariamente un HANDOFF antiguo.

Como mínimo, cuando existan handoffs:

```yaml
current_handoff:
  handoff_id:
  version:
  status: ACTIVE

handoff_history:
  - handoff_id:
    version:
    role: CREATION | TRANSFER | UPDATE
    status: SUPERSEDED | CLOSED | ACTIVE
```

La regla es:

> **Para conectar con un THREAD se consulta primero su MANIFEST. El MANIFEST determina el estado y el HANDOFF vigente. Nunca se selecciona un HANDOFF simplemente por ser el primero o el más antiguo encontrado.**

Un HANDOFF histórico puede conservarse indefinidamente como trazabilidad aunque ya no sea vigente.

### 6.2 Ubicación y formato

El formato y ubicación definitivos del MANIFEST pueden evolucionar. Mientras la arquitectura se prueba, se permite un manifest documental por THREAD cuando aporte valor operativo.

No se debe crear una proliferación de manifests derivados que dupliquen información de otros documentos sin necesidad.

## 7. Estados del THREAD

Se adopta provisionalmente el siguiente conjunto:

```text
PROPOSED
ACTIVE
BLOCKED
READY_FOR_HANDOFF
CLOSED
ARCHIVED
```

- `PROPOSED`: responsabilidad declarada pero todavía no inicializada o aceptada.
- `ACTIVE`: trabajo en curso.
- `BLOCKED`: el trabajo no puede avanzar por una dependencia o decisión pendiente.
- `READY_FOR_HANDOFF`: el resultado está preparado para transferirse.
- `CLOSED`: el ciclo de trabajo ha terminado y su estado persistente está documentado.
- `ARCHIVED`: referencia histórica sin trabajo activo.

El estado debe reflejar el repositorio, no una impresión temporal de la conversación.

## 8. THREAD BOOTSTRAP

El **THREAD BOOTSTRAP** es el protocolo universal mediante el cual una nueva instancia de conversación se incorpora al sistema.

### 8.1 Entrada por HANDOFF

Cuando el usuario indique:

> **«Parte del handoff `<id>`.»**

el agente debe:

1. localizar el HANDOFF;
2. identificar el `thread_id` receptor;
3. buscar el MANIFEST del receptor;
4. comprobar si el THREAD ya está inicializado;
5. si no existe, crear/inicializar el THREAD y su MANIFEST a partir de la declaración contenida en el HANDOFF;
6. registrar `origin.type: HANDOFF` y el `source_id` del HANDOFF;
7. resolver documentos autoritativos y dependencias;
8. validar que el contexto del HANDOFF sigue siendo compatible con el estado del repositorio;
9. pasar el THREAD a `ACTIVE` cuando la inicialización sea válida;
10. informar del diagnóstico de incorporación y comenzar el trabajo.

La creación del THREAD es la **primera responsabilidad operativa** del agente cuando el HANDOFF declara un receptor todavía inexistente.

### 8.2 Entrada directa a un THREAD existente

Cuando el usuario indique:

> **«Conecta con el hilo `<thread_id>`.»**

el agente debe:

1. localizar el MANIFEST del THREAD;
2. verificar su identidad y estado;
3. leer el `current_handoff` si existe, sin utilizar automáticamente HANDOFF históricos;
4. resolver las dependencias vigentes;
5. comprobar si existen cambios relevantes desde el último estado conocido;
6. informar del diagnóstico de incorporación;
7. continuar el trabajo dentro de la responsabilidad vigente.

La conexión directa **no crea un nuevo THREAD** ni reinicia el ciclo.

### 8.3 Entrada desde una conversación nueva con responsabilidad declarada

Cuando una conversación nueva, ya dentro del contexto del proyecto, declare una responsabilidad sin HANDOFF previo, el agente debe:

1. comprobar si ya existe un THREAD que cubra esa responsabilidad;
2. si existe, proponer/conectar con el THREAD correspondiente en lugar de duplicarlo;
3. si no existe, crear una nueva THREAD DECLARATION de tipo `USER_DECLARED`;
4. crear su MANIFEST;
5. establecer identidad, responsabilidad, alcance, dependencias y estado;
6. pasar a `ACTIVE` cuando la declaración sea suficientemente clara;
7. comenzar el trabajo.

El usuario no necesita conocer la estructura interna del MANIFEST para declarar una responsabilidad.

### 8.4 Entrada desde una conversación histórica

Cuando una conversación antigua se reincorpore mediante:

> **«Reincorpórate al contexto del proyecto.»**

el agente debe reconstruir la responsabilidad a partir de la conversación y del repositorio y determinar:

```text
¿existe THREAD compatible?
   │
   ├── SÍ → conectar con el THREAD
   │
   └── NO → proponer/inicializar THREAD de tipo MIGRATED
```

Debe aplicar además las reglas de reconciliación documental de la sección de reincorporación.

## 9. Conexión, creación y transferencia no son lo mismo

Estas operaciones deben mantenerse separadas:

### Crear THREAD

Convierte una responsabilidad declarada en una entidad persistente con MANIFEST.

### Conectar con THREAD

Asocia una nueva instancia de conversación a un THREAD existente y recupera su estado vigente.

### Transferir responsabilidad

Mueve o declara la responsabilidad de una línea a otra mediante un HANDOFF. Puede iniciar la creación de un THREAD receptor o actualizar el estado de uno ya existente.

Una nueva conversación conectada a un THREAD no crea por sí misma un nuevo ciclo ni un nuevo THREAD.

## 10. Contrato de responsabilidad

Toda instancia de conversación sustantiva debe poder responder:

```text
THREAD al que está conectada:
Responsabilidad:
Propietario / línea de trabajo:
Dentro de alcance:
Fuera de alcance:
Documentos principales:
Código / datos principales:
Entregables esperados:
Validación requerida:
Dependencias:
Handoff actual:
```

Este contrato amplía las reglas ya definidas en `CHATGPT_PROJECT_CONTEXT.md`. Si la responsabilidad no es evidente, debe proponerse antes de ampliar el alcance.

## 11. Estados y ciclos de trabajo

Una responsabilidad puede tener varios ciclos:

```text
THREAD X
  ├── ciclo 1 → CLOSED
  ├── ciclo 2 → CLOSED
  └── ciclo 3 → ACTIVE
```

Reabrir una responsabilidad no debe borrar ni reescribir el historial del ciclo anterior. El nuevo ciclo debe indicar qué conocimiento, documentos y decisiones hereda.

## 12. Dependencias

Las dependencias entre THREADs deben ser explícitas.

Cuando una dependencia documental sea relevante para la reproducibilidad, debe fijarse a una versión:

```yaml
dependency:
  document: docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md
  version: 0.1.1
  status: current
```

Si la dependencia cambia de versión, el THREAD debe poder detectar que su contexto puede haber quedado desactualizado y revisar la compatibilidad antes de continuar.

Una dependencia no transfiere automáticamente responsabilidad.

## 13. HANDOFF

Un HANDOFF es un artefacto de transferencia entre THREADs o una declaración inicial de un THREAD receptor.

Debe incluir, cuando proceda:

- identificador del HANDOFF y versión;
- THREAD emisor;
- THREAD receptor previsto;
- objetivo;
- estado actual;
- decisiones ya adoptadas;
- restricciones;
- documentos y versiones relevantes;
- código/datos afectados;
- validación realizada;
- cuestiones abiertas;
- trabajo fuera de alcance;
- commit/SHA de referencia.

El receptor debe poder continuar sin reconstruir la conversación completa.

El HANDOFF no es la autoridad sobre el estado posterior del THREAD. Una vez creado el receptor, el MANIFEST pasa a ser la referencia de estado actual.

## 14. Propuestas y decisiones

Una conversación puede producir propuestas, hipótesis o alternativas. No deben confundirse con decisiones validadas.

La transición recomendada es:

```text
propuesta → discusión → decisión → documentación → implementación/validación
```

Una propuesta permanece como propuesta hasta que la autoridad correspondiente la adopta. El chat no convierte por sí solo una propuesta en conocimiento autoritativo.

## 15. Activity Log

El proyecto puede mantener un registro de actividad para eventos operativos significativos. No debe utilizarse como copia íntegra de conversaciones.

Una entrada puede representar:

```text
fecha
thread
acción
tipo
resultado
documentos afectados
commit
```

La implementación del Activity Log queda abierta hasta que exista una necesidad real.

## 16. Autoridad documental

La autoridad se interpreta de forma separada por función:

| Información | Fuente principal |
|---|---|
| Reglas permanentes | `PROJECT_WORKING_RULES.md` |
| Integración ChatGPT ↔ proyecto | `CHATGPT_PROJECT_CONTEXT.md` |
| Arquitectura de hilos | `THREAD_ARCHITECTURE.md` |
| Estado/metodología validada | informes y documentos de conocimiento vigentes |
| Identidad y estado actual de THREAD | MANIFEST |
| Transferencia/declaración de responsabilidad | HANDOFF |
| Comportamiento ejecutable | código y tests |
| Datos observados | datos fuente + procedencia |
| Historial operativo | Activity Log, cuando exista |
| Conversación | contexto no autoritativo que debe sincronizarse |

Si dos fuentes con autoridad comparable discrepan, debe exponerse el conflicto y determinarse cuál debe prevalecer.

## 17. Reincorporación de conversaciones existentes

El flujo es:

```text
conversación existente
        ↓
leer reglas y arquitectura
        ↓
identificar THREAD por manifest/histórico
        ↓
comparar conversación ↔ repositorio
        ↓
clasificar discrepancias
        ↓
proponer sincronización
        ↓
confirmar responsabilidad y límites
        ↓
continuar trabajo
```

Las discrepancias se clasifican como `NUEVO`, `OBSOLETO`, `CONFLICTO`, `DUPLICADO` o `FUERA DE ALCANCE`.

La conversación no debe sobrescribir silenciosamente el repositorio ante un `CONFLICTO`.

## 18. Separación de dominios

Los dominios deben mantenerse desacoplados cuando tengan responsabilidades, datos, validaciones o criterios metodológicos diferentes.

Encontrar una dependencia entre dominios no justifica absorber el trabajo del otro dominio.

## 19. Cierre y reapertura

El cierre de un THREAD sustantivo debe dejar:

- decisiones y resultados persistentes documentados;
- validación realizada;
- documentos versionados;
- archivos/datos afectados;
- rama y SHA;
- incertidumbres restantes;
- siguiente HANDOFF, si existe;
- estado actualizado del MANIFEST.

Un THREAD cerrado puede volver a originar trabajo mediante un nuevo ciclo. El nuevo ciclo debe referenciar el conocimiento heredado y no alterar retrospectivamente el ciclo anterior salvo corrección documental explícita.

## 20. Relación con la documentación existente

Este documento complementa:

- `docs/PROJECT_WORKING_RULES.md`;
- `docs/CHATGPT_PROJECT_CONTEXT.md`;
- informes de proyecto;
- manifests de THREAD;
- `docs/THREAD_*.md` y HANDOFFs especializados.

No sustituye los documentos de dominio ni define la metodología científica de ClimaScope.

## 21. Migración gradual

1. Formalizar esta arquitectura sin reestructurar los dominios existentes.
2. Actualizar reglas maestras y contexto ChatGPT para referenciarla.
3. Utilizar THREAD BOOTSTRAP en nuevos hilos y conversaciones reincorporadas.
4. Crear manifests individuales cuando aporten valor operativo; durante la prueba son obligatorios para THREADs formalizados.
5. Introducir Activity Log o índices derivados únicamente cuando exista necesidad demostrable.
6. No migrar ni renombrar documentos de dominio por razones puramente estilísticas.

## 22. Estado de esta especificación

La versión `0.2.0` incorpora la distinción formal entre THREAD, MANIFEST, HANDOFF e instancia conversacional y define el THREAD BOOTSTRAP para los tres orígenes iniciales de un THREAD.

Quedan abiertos para futuras iteraciones:

- formato definitivo de `THREAD_MANIFEST`;
- ubicación y formato de Activity Log persistente;
- automatización de detección de dependencias desactualizadas;
- índices derivados de THREADs;
- reglas detalladas de reestructuración de dominios;
- automatización de comprobaciones de coherencia entre manifests, handoffs y documentos.
