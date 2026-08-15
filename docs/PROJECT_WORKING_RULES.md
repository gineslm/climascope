# ClimaScope — Reglas de trabajo del proyecto

**Versión del documento:** 1.2.0  
**Creado:** 2026-08-15  
**Repositorio:** `gineslm/climascope`  
**Rama de consolidación documental:** `knowledge`

> **Idioma oficial del proyecto: español (España).** La documentación, decisiones, handoffs e informes deben redactarse en castellano salvo que exista una razón técnica para conservar un término original.

## 1. Propósito

Este documento es el contrato operativo permanente para el trabajo de ClimaScope entre conversaciones independientes. Existe para que el método del proyecto, la trazabilidad, la práctica documental y las reglas de transferencia no dependan de la memoria de una conversación concreta.

El repositorio Git es la fuente central de verdad. El estado consolidado de conocimiento y estructura se mantiene en `knowledge`; el ciclo de software utiliza `develop` y `main`. Un hilo nuevo debe recuperar el estado del proyecto desde `knowledge` antes de tomar decisiones o realizar cambios.

La arquitectura operativa de los hilos está especificada en `docs/THREAD_ARCHITECTURE.md`. Este documento establece las reglas permanentes; la especificación de hilos define el modelo de identidad, estados, ciclos, dependencias y transferencias.

## 2. Primer paso obligatorio en cada hilo nuevo

Antes de realizar trabajo del proyecto, el hilo debe:

1. entrar en la rama `knowledge` como referencia inicial de conocimiento/estructura consolidada;
2. leer este documento;
3. leer `docs/THREAD_ARCHITECTURE.md` cuando exista y sea aplicable;
4. inspeccionar el estado consolidado y las referencias Git relevantes;
5. leer el/los informe(s) actual(es) del proyecto;
6. inspeccionar cualquier documento de handoff específico de la tarea;
7. identificar la versión vigente de la documentación y los commits relevantes;
8. inspeccionar la implementación y los tests existentes antes de proponer cambios;
9. resolver desde el MANIFEST la rama/commit de trabajo cuando el THREAD tenga implementación;
10. informar de cualquier documento referenciado que falte en lugar de inventar su contenido.

El contexto previo de una conversación es útil, pero no constituye el registro autoritativo del proyecto.

## 3. Repositorio y acceso

Todo trabajo debe estar asociado al repositorio `gineslm/climascope`.

Capacidades requeridas para un hilo de implementación:

- leer archivos, ramas y documentación del repositorio;
- crear/actualizar archivos y hacer commits en la rama de trabajo acordada, o crear una rama específica cuando proceda;
- disponer de un checkout local cuando sea necesario ejecutar código o inspeccionar datos generados;
- utilizar el entorno Python del repositorio y ejecutar `python -m pytest` para validar los tests de Python.

No se debe asumir acceso a documentos que existan únicamente en otra conversación. Si no están en el repositorio, deben solicitarse o indicarse como no disponibles.

## 4. Modelo de ramas y consolidación

El proyecto separa el ciclo de conocimiento del ciclo de software:

```text
knowledge → conocimiento y estructura consolidados
develop   → integración del software
main      → software estable/desplegable
```

### `knowledge`

`knowledge` es la línea estable de consolidación del conocimiento y del estado estructural del proyecto. Incluye, cuando corresponda:

- reglas y contexto del proyecto;
- arquitectura;
- THREADs y MANIFESTs;
- HANDOFFs;
- conocimiento metodológico y decisiones consolidadas;
- Activity Log u otros registros persistentes;
- índices o vistas necesarias para descubrir el estado.

Una nueva conversación debe poder reconstruir desde `knowledge` la identidad y el estado de los THREADs sin recorrer arbitrariamente ramas de trabajo.

### `develop`

`develop` es la línea de integración del software. Una implementación debe registrar qué estado de `knowledge` constituye su base de conocimiento, preferentemente mediante una referencia de rama y commit en el MANIFEST o documento equivalente.

No se establece que el contenido completo de `knowledge` deba fusionarse físicamente en `develop`. Cuando el software necesite documentación técnica concreta, puede incorporarse selectivamente.

### `main`

`main` representa el software estable/desplegable. No es la fuente global del conocimiento del proyecto. Un cambio consolidado en `knowledge` no tiene que llegar a `main` si todavía no existe una implementación, si queda fuera del producto o si el ciclo de software es independiente.

La documentación técnica necesaria para desarrollar, mantener, operar o utilizar el software puede permanecer en `develop` y/o `main`. No se adopta la regla `main = develop - docs`.

### Ramas de trabajo

Las ramas `agent/*`, `feature/*` u otras ramas temporales representan trabajo en evolución. No son autoritativas por el mero hecho de existir.

Una rama de trabajo puede producir:

```text
resultado de conocimiento → consolidación en `knowledge`
resultado de software     → integración en `develop` / `main`
```

## 5. Evento de consolidación

Un **evento de consolidación** ocurre cuando un cambio deja de ser exclusivamente trabajo de una conversación o rama temporal y pasa a formar parte del estado autoritativo del proyecto.

Ejemplos de cambios que deben consolidarse en `knowledge` cuando afecten al estado autoritativo:

- creación o modificación de un documento autoritativo;
- adopción de una decisión persistente;
- creación o actualización de un MANIFEST;
- creación o actualización de un HANDOFF;
- cierre de un THREAD con estado persistente;
- registro de una actividad operativa significativa;
- incorporación de conocimiento validado;
- modificación relevante de la arquitectura.

El flujo esperado es:

```text
trabajo / análisis
      ↓
resultado persistente
      ↓
documentar
      ↓
actualizar MANIFEST / HANDOFF / ACTIVITY cuando proceda
      ↓
COMMIT
      ↓
consolidar en `knowledge`
```

No todo pensamiento, borrador o experimento requiere consolidación. El criterio es si modifica una fuente autoritativa o el estado persistente del proyecto.

## 6. La documentación es estado versionado del proyecto

Todo documento sustantivo del proyecto debe contener un identificador de versión.

Convención recomendada:

- major: cambio estructural/metodológico;
- minor: nueva capacidad documentada, decisión o sección sustancial;
- patch: aclaración, corrección o actualización editorial.

Los artefactos documentales deben estar comprometidos en GitHub. Cuando sean fuentes autoritativas de conocimiento/estructura, su commit de consolidación corresponde a `knowledge`.

El informe correspondiente debe referenciar los documentos importantes y registrar sus versiones actuales. Esto permite que hilos independientes recuperen el estado más reciente.

## 7. Informes, arquitectura y handoffs

El proyecto utiliza tipos documentales complementarios:

### Reglas maestras

`docs/PROJECT_WORKING_RULES.md`

Reglas operativas permanentes para todos los hilos.

### Arquitectura de hilos

`docs/THREAD_ARCHITECTURE.md`

Especificación del modelo operativo de los hilos: identidad, responsabilidad, estados, ciclos, dependencias, HANDOFF, autoridad documental y reincorporación de conversaciones.

### Informes de proyecto

Por ejemplo:

`docs/WATER_PIPELINE_AUDIT_REPORT.md`

Los informes registran lo que realmente se ha implementado, probado, medido, decidido y cambiado a lo largo del tiempo.

### Handoffs de hilo

Por ejemplo:

`docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md`

Los handoffs definen el alcance y el contexto de partida para un hilo especializado siguiente. Deben contener repositorio, rama de trabajo, ruta local cuando se conozca, requisitos de acceso, objetivo, estado actual, restricciones, entregables, validación y protocolo de cierre.

Un handoff debe entenderse como transferencia de responsabilidad, no como simple lista de tareas. El HANDOFF se consolida en `knowledge`; su referencia a una rama de trabajo puede continuar apuntando a una rama distinta.

## 8. Protocolo de responsabilidad y alcance

Toda conversación sustantiva debe poder identificar:

- responsabilidad;
- propietario o línea de trabajo;
- dentro de alcance;
- fuera de alcance;
- documentos principales;
- código/datos principales;
- entregables;
- validación;
- dependencias;
- siguiente handoff.

Un hilo no debe absorber silenciosamente trabajo perteneciente a otra línea. Una dependencia entre dominios no transfiere responsabilidad.

Las propuestas, hipótesis y alternativas deben distinguirse de las decisiones validadas. El historial del chat no convierte por sí mismo una propuesta en conocimiento autoritativo.

## 9. Protocolo de cierre de cada hilo sustantivo

Antes de declarar completada una tarea:

1. ejecutar los tests relevantes;
2. inspeccionar los resultados generados cuando proceda;
3. actualizar el informe correspondiente;
4. incrementar la versión documental cuando haya cambios sustantivos de documentación;
5. crear/actualizar el siguiente handoff si se necesita otro hilo;
6. hacer commit con un mensaje intencionado;
7. hacer push de la rama de trabajo acordada;
8. consolidar en `knowledge` los cambios que modifiquen conocimiento o estructura autoritativos;
9. registrar el SHA de consolidación y, cuando exista, el SHA de trabajo;
10. indicar cualquier incertidumbre o evidencia que falte.

El cierre termina un ciclo de trabajo; no elimina el conocimiento persistente. Una responsabilidad puede iniciar un ciclo posterior sin reescribir retrospectivamente el anterior.

## 10. Reglas de trazabilidad y evidencia

ClimaScope debe conservar la distinción entre hechos de las fuentes, datos derivados del proyecto, valores modelados y evidencia cualitativa.

Todo dataset o indicador derivado debe poder rastrearse hasta:

- fuente/proveedor;
- dataset o documento de origen;
- periodo de adquisición/observación;
- transformación o cálculo;
- código/versión relevante;
- estado del control de calidad.

Nunca convertir silenciosamente datos missing en cero.

Nunca presentar un valor interpolado o modelado como una observación directa de una estación.

Nunca tratar la ausencia de investigación como evidencia de ausencia de riesgo.

## 11. Datos raw / processed / derived

El proyecto debería converger progresivamente hacia una separación clara como:

```text
data/
├── raw/          # material fuente; preservado y trazable
├── processed/    # representaciones limpiadas/normalizadas
├── derived/      # indicadores, scores, capas de mapa, modelos
└── reports/      # resultados generados o destinados a publicación
```

Las rutas existentes no deben moverse únicamente por razones de estilo. Una migración requiere una decisión deliberada y documentación.

El trabajo AEMET actual está en `data/raw/aemet/`, incluyendo JSON originales, evidencia de adquisición `.NO_DATA`, resultados de QC y CSV mensuales/anuales W2. Tratarlo como estado existente del proyecto salvo que se apruebe una migración documentada.

## 12. Principios Station, Location y Evidence

El modelo de dominio debe distinguir al menos:

```text
Station -> observaciones
Location -> lugar/sitio evaluado por el usuario
Scope/Representativeness -> relevancia espacial entre estaciones y ubicaciones
Evidence -> soporte cuantitativo, derivado o documental
```

Una observación de estación no es automáticamente el valor de cualquier ubicación cercana.

Si posteriormente se introduce interpolación, debe etiquetarse explícitamente como modelada/interpolada y conservar método, trazabilidad e incertidumbre.

Los datos cuantitativos de estaciones y la evidencia cualitativa/documental son tipos de evidencia diferentes, pero ambos pueden asociarse a una ubicación.

## 13. Adquisición e investigación progresivas

No intentar descargar o investigar todas las ubicaciones posibles antes de disponer de un mecanismo de priorización.

El flujo preferido es:

```text
candidata
  -> cribada
  -> datos cuantitativos adquiridos
  -> QC superado
  -> investigación documental priorizada
  -> evaluada
  -> promovida / despriorizada / rechazada
```

El proyecto debe priorizar primero las ubicaciones/estaciones prometedoras y ampliar progresivamente.

La investigación documental también debe ser proporcional al interés y relevancia de una candidata. Una ubicación que todavía no haya sido investigada debe permanecer explícitamente como `not_assessed` o equivalente, nunca como `low risk` o `no risk`.

## 14. Principios del mapa

El futuro mapa debe poder distinguir:

- estaciones físicas;
- ubicaciones evaluadas;
- cobertura/alcance de estaciones;
- observaciones directas;
- indicadores derivados;
- valores modelados/interpolados;
- calidad de los datos;
- evidencia documental;
- trazabilidad.

El alcance espacial es una representación de relevancia, no una prueba de que una estación mida condiciones idénticas en toda el área.

La interpolación se pospone hasta diseñar el modelo Station/Location/Scope y sus requisitos de incertidumbre.

## 15. Estado documentado actual del proyecto

En la versión 1.0.0 de estas reglas:

- el pipeline de agua se ha auditado alrededor de las estaciones AEMET `8416`, `3195` y `7012D`;
- se ha implementado y probado la agregación mensual y anual W2 de precipitación;
- la agregación actual conserva los totales observados de precipitación y expone días missing, cobertura y completitud;
- la suite de tests alcanzó 13 tests después de los últimos cambios de agregación;
- la siguiente tarea especializada prevista es el modelo de dominio Station / Location / Scope / Evidence.

Para el estado detallado actual, leer el último `docs/WATER_PIPELINE_AUDIT_REPORT.md` y el handoff específico de la tarea.

## 16. Inventario documental conocido

Los siguientes documentos del proyecto constan como presentes y relevantes:

| Documento | Función | Versión conocida |
|---|---|---:|
| `docs/PROJECT_WORKING_RULES.md` | Reglas operativas permanentes | 1.2.0 |
| `docs/CHATGPT_PROJECT_CONTEXT.md` | Contexto de integración con ChatGPT | 1.2.0 |
| `docs/THREAD_ARCHITECTURE.md` | Arquitectura operativa de hilos | 0.3.0 |
| `docs/THREAD_MANIFEST_ARCHITECTURE_THREAD.md` | Manifest de este hilo | 0.1.0 |
| `docs/WATER_PIPELINE_AUDIT_REPORT.md` | Informe/auditoría del pipeline de agua | 0.3.1 |
| `docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md` | Handoff del siguiente hilo especializado | 0.1.1 |

## 17. Cómo iniciar un hilo nuevo

Un hilo nuevo debe recibir una instrucción breve como:

> Trabaja en ClimaScope desde el repositorio central de GitHub. Primero entra en `knowledge` y lee `docs/CHATGPT_PROJECT_CONTEXT.md`, `docs/PROJECT_WORKING_RULES.md` y `docs/THREAD_ARCHITECTURE.md`, después el informe de proyecto más reciente y el handoff específico de la tarea. Trata `knowledge` como fuente de verdad para el estado consolidado de conocimiento y estructura; conserva la trazabilidad; no inventes documentos de proyecto que falten; y sigue el protocolo de cierre. Informa de las versiones documentales actuales, la rama y la responsabilidad antes de realizar cambios sustantivos.

El handoff específico define el objetivo real y puede apuntar a una rama de trabajo distinta.

## 18. Cómo cerrar un hilo

El mensaje de cierre debe indicar:

- qué se ha implementado o decidido;
- tests/validación realizados;
- cambios de versión documental;
- archivos/datos afectados;
- rama y SHA del trabajo;
- SHA de consolidación en `knowledge` cuando corresponda;
- cuestiones no resueltas;
- siguiente documento de handoff, si procede.

Esto mantiene los hilos futuros independientes del histórico del chat y conserva el rastro de decisiones del proyecto en Git.
