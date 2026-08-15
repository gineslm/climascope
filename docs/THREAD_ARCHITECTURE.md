# ClimaScope — Arquitectura de hilos de trabajo

**Versión:** 0.1.0  
**Estado:** Propuesta operativa inicial  
**Idioma:** español (España)  
**Repositorio:** `gineslm/climascope`

## 1. Propósito

Este documento formaliza el modelo operativo de los hilos de trabajo de ClimaScope. Complementa `docs/PROJECT_WORKING_RULES.md` y `docs/CHATGPT_PROJECT_CONTEXT.md`; no los sustituye ni duplica sus reglas generales.

Su objetivo es que una conversación pueda incorporarse, continuar o cerrar una línea de trabajo sin depender del historial completo del chat.

La unidad persistente de trabajo es el **hilo de proyecto**, no la conversación de ChatGPT. GitHub es la fuente duradera de verdad.

## 2. Principios

1. Una conversación debe tener una responsabilidad delimitada.
2. Una conversación no es por sí misma una fuente autoritativa del proyecto.
3. El conocimiento duradero debe sincronizarse con el repositorio.
4. Cada responsabilidad debe tener un propietario o línea de trabajo identificable.
5. Un hilo no absorbe silenciosamente trabajo perteneciente a otra línea.
6. Las dependencias documentales deben poder identificarse y, cuando sea relevante, fijarse a una versión.
7. Un HANDOFF representa una transferencia de responsabilidad, no una simple lista de tareas.
8. Los conflictos entre conversación y repositorio se hacen explícitos; no se resuelven silenciosamente.
9. El cierre de un hilo termina un ciclo de trabajo, no elimina su conocimiento.
10. Las vistas o índices derivados no sustituyen a las fuentes autoritativas.

## 3. Modelo conceptual

El sistema documental se organiza en las siguientes categorías:

```text
KNOWLEDGE  → qué sabe el proyecto
THREAD     → quién es responsable de trabajar sobre ello
HANDOFF    → cómo se transfiere una responsabilidad
ACTIVITY   → qué ocurrió durante la evolución del trabajo
DERIVED    → vistas o índices regenerables
```

Estas categorías son complementarias:

- **KNOWLEDGE** incluye metodología, especificaciones, decisiones e informes validados.
- **THREAD** define una unidad de responsabilidad y su estado.
- **HANDOFF** transmite contexto y responsabilidad entre hilos.
- **ACTIVITY** conserva eventos operativos significativos sin convertirse en una copia de las conversaciones.
- **DERIVED** contiene índices, resúmenes o vistas que pueden reconstruirse desde las fuentes.

## 4. Identidad de un hilo

Un hilo debe poder identificarse mediante, al menos:

```yaml
thread_id:
domain:
status:
owner:
created:
current_cycle:
responsibility:
```

El `thread_id` debe permanecer estable durante su ciclo de vida. Si una misma responsabilidad vuelve a abrirse posteriormente, se crea un nuevo ciclo o una nueva unidad de trabajo según determine el manifest del proyecto.

## 5. Contrato de responsabilidad

Toda conversación sustantiva debe poder responder:

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

Este contrato amplía las reglas ya definidas en `CHATGPT_PROJECT_CONTEXT.md`. Si la responsabilidad no es evidente, debe proponerse y confirmarse antes de ampliar el alcance.

## 6. Manifest del hilo

El manifest es el contrato persistente que permite reconstruir la identidad y el estado de un hilo sin leer su historial completo.

Como mínimo debe resolver:

- identidad del hilo;
- dominio y responsabilidad;
- estado y ciclo actual;
- documentos autoritativos;
- dependencias;
- trabajo recibido;
- entregables esperados;
- validación;
- siguiente transferencia prevista;
- cuestiones abiertas.

El formato concreto del manifest puede evolucionar. No se crea un manifest separado para cada hilo hasta que exista una necesidad operativa real; el sistema debe evitar proliferación documental innecesaria.

## 7. Estados del hilo

Se adopta provisionalmente el siguiente conjunto:

```text
PROPOSED
ACTIVE
BLOCKED
READY_FOR_HANDOFF
CLOSED
ARCHIVED
```

- `PROPOSED`: responsabilidad definida pero todavía no iniciada.
- `ACTIVE`: trabajo en curso.
- `BLOCKED`: el trabajo no puede avanzar por una dependencia o decisión pendiente.
- `READY_FOR_HANDOFF`: el resultado está preparado para transferirse.
- `CLOSED`: el ciclo de trabajo ha terminado y su estado persistente está documentado.
- `ARCHIVED`: referencia histórica sin trabajo activo.

El estado debe reflejar el repositorio, no una impresión temporal de la conversación.

## 8. Ciclos de trabajo

Una responsabilidad puede tener varios ciclos:

```text
responsabilidad X
  ├── ciclo 1 → CLOSED
  ├── ciclo 2 → CLOSED
  └── ciclo 3 → ACTIVE
```

Reabrir una responsabilidad no debe borrar ni reescribir el historial del ciclo anterior. El nuevo ciclo debe indicar qué conocimiento, documentos y decisiones hereda.

## 9. Dependencias

Las dependencias entre hilos deben ser explícitas.

Cuando una dependencia documental sea relevante para la reproducibilidad, debe fijarse a una versión:

```yaml
dependency:
  document: docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md
  version: 0.1.1
  status: current
```

Si la dependencia cambia de versión, el hilo debe poder detectar que su contexto puede haber quedado desactualizado y revisar la compatibilidad antes de continuar.

Una dependencia no transfiere automáticamente responsabilidad. La responsabilidad sigue perteneciendo al hilo propietario del dominio correspondiente.

## 10. HANDOFF

Un HANDOFF debe representar una transferencia explícita entre una responsabilidad de origen y una responsabilidad receptora.

Debe incluir, cuando proceda:

- hilo emisor;
- hilo receptor previsto;
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

Un HANDOFF no autoriza al receptor a modificar silenciosamente decisiones de otra línea. Si detecta un conflicto, debe registrarlo y remitirlo al propietario correspondiente.

## 11. Propuestas y decisiones

Una conversación puede producir propuestas, hipótesis o alternativas. No deben confundirse con decisiones validadas.

La transición recomendada es:

```text
propuesta → discusión → decisión → documentación → implementación/validación
```

Una propuesta permanece como propuesta hasta que la autoridad correspondiente la adopta. El chat no convierte por sí solo una propuesta en conocimiento autoritativo.

## 12. Activity Log

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

Son candidatos a registrar: decisiones de arquitectura, transferencias, cambios de estado, bloqueos resueltos, cambios de dependencia y cierres de ciclos.

La implementación del Activity Log queda deliberadamente abierta hasta que el proyecto determine una necesidad real de automatización o consulta.

## 13. Autoridad documental

La autoridad se interpreta de forma separada por función:

| Información | Fuente principal |
|---|---|
| Reglas permanentes | `PROJECT_WORKING_RULES.md` |
| Integración ChatGPT ↔ proyecto | `CHATGPT_PROJECT_CONTEXT.md` |
| Arquitectura de hilos | `THREAD_ARCHITECTURE.md` |
| Estado/metodología validada | informes y documentos de conocimiento vigentes |
| Responsabilidad de un hilo | manifest/handoff correspondiente |
| Transferencia de responsabilidad | HANDOFF |
| Comportamiento ejecutable | código y tests |
| Datos observados | datos fuente + procedencia |
| Historial operativo | Activity Log, cuando exista |
| Conversación | contexto no autoritativo que debe sincronizarse |

Si dos fuentes con autoridad comparable discrepan, debe exponerse el conflicto y determinarse cuál debe prevalecer. No se debe fusionar silenciosamente información incompatible.

## 14. Reincorporación de conversaciones existentes

La instrucción de entrada es:

> **Reincorpórate al contexto del proyecto.**

El flujo es:

```text
conversación existente
        ↓
leer reglas y arquitectura
        ↓
leer manifest/handoff e informes relevantes
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

Las discrepancias se clasifican como:

- `NUEVO`: aparece en la conversación pero no en el repositorio;
- `OBSOLETO`: el repositorio contiene una versión sustituida por trabajo validado;
- `CONFLICTO`: existen afirmaciones o decisiones incompatibles;
- `DUPLICADO`: la información ya existe en otro lugar autoritativo;
- `FUERA DE ALCANCE`: pertenece al proyecto pero no al hilo actual.

La conversación no debe sobrescribir silenciosamente el repositorio ante un `CONFLICTO`.

## 15. Separación de dominios

Los dominios deben mantenerse desacoplados cuando tengan responsabilidades, datos, validaciones o criterios metodológicos diferentes.

Por ejemplo, adquisición, AEMET/QC, agregación de agua, Station/Location/Evidence, alcance espacial, interpolación, mapa/UI, scoring e investigación documental pueden ser líneas distintas.

Encontrar una dependencia entre dominios no justifica absorber el trabajo del otro dominio.

## 16. Cierre y reapertura

El cierre de un hilo sustantivo debe seguir el protocolo de `PROJECT_WORKING_RULES.md` y, como mínimo, dejar:

- decisiones y resultados persistentes documentados;
- validación realizada;
- documentos versionados;
- archivos/datos afectados;
- rama y SHA;
- incertidumbres restantes;
- siguiente HANDOFF, si existe.

Un hilo cerrado puede volver a originar trabajo mediante un nuevo ciclo. El nuevo ciclo debe referenciar el conocimiento heredado y no alterar retrospectivamente el ciclo anterior salvo corrección documental explícita.

## 17. Relación con la documentación existente

Este documento **complementa**:

- `docs/PROJECT_WORKING_RULES.md`, que contiene las reglas permanentes de trabajo;
- `docs/CHATGPT_PROJECT_CONTEXT.md`, que conecta las conversaciones de ChatGPT con el repositorio;
- informes de proyecto, que contienen el estado validado de líneas concretas;
- `docs/THREAD_*.md`, que actúan como handoffs especializados.

No sustituye los documentos de dominio ni define la metodología científica de ClimaScope.

## 18. Migración gradual

La adopción debe ser progresiva.

1. Formalizar esta arquitectura sin reestructurar todavía los dominios existentes.
2. Actualizar las reglas maestras y el contexto ChatGPT para referenciarla.
3. Utilizar el modelo en los nuevos hilos y en conversaciones antiguas que se reincorporen.
4. Crear manifests individuales solo cuando aporten valor operativo.
5. Introducir Activity Log o índices derivados únicamente cuando exista una necesidad demostrable.
6. No migrar ni renombrar documentos de dominio por razones puramente estilísticas.

## 19. Estado de esta especificación

La versión `0.1.0` establece el modelo conceptual y operativo inicial. Quedan deliberadamente abiertos para futuras iteraciones:

- formato definitivo de `THREAD_MANIFEST`;
- ubicación y formato de un Activity Log persistente;
- automatización de detección de dependencias desactualizadas;
- índices derivados de hilos;
- reglas detalladas de reestructuración de dominios;
- automatización de comprobaciones de coherencia entre manifests, handoffs y documentos.

Estas cuestiones no deben bloquear el uso manual del modelo.
