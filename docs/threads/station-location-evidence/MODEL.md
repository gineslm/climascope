# ClimaScope — Modelo Station / Location / Scope / Evidence

**Versión:** 1.0.0  
**Estado:** En definición  
**Idioma:** español (España)  
**THREAD responsable:** `thread-station-location-evidence`

## 1. Propósito

Definir el modelo de dominio que permite relacionar observaciones de estaciones con ubicaciones evaluadas, su representatividad espacial y la evidencia utilizada por ClimaScope.

El núcleo conceptual es:

```text
Station → Location → Scope/Representativeness → Evidence
```

Este documento describe conocimiento vigente del dominio. El estado operativo del THREAD vive en su MANIFEST y sus propuestas pendientes en su HANDOFF.

## 2. Principios consolidados

1. Una observación de estación no equivale automáticamente al valor de una ubicación cercana.
2. La representatividad espacial debe ser explícita.
3. Deben distinguirse semánticamente:
   - observado en estación;
   - relevante para una ubicación;
   - modelado/interpolado para una ubicación.
4. La interpolación queda aplazada hasta disponer de método, trazabilidad e incertidumbre explícitos.
5. La adquisición y la investigación son progresivas.
6. `not_assessed` nunca significa ausencia de riesgo.
7. Los datos cuantitativos de estaciones y la evidencia cualitativa/documental son tipos de evidencia diferentes que pueden asociarse a una ubicación.
8. Los datos AEMET raw/W2 y su trazabilidad deben preservarse salvo migración deliberada.

## 3. Entidades conceptuales

### Station

Representa una estación física de observación y constituye el origen de observaciones cuantitativas directas.

Debe preservar, como mínimo, identidad, localización, procedencia, periodo disponible y estado/calidad de sus observaciones cuando esa información exista.

### Location

Representa el lugar o sitio que se desea evaluar. No debe confundirse con una estación ni heredar automáticamente sus valores.

Una Location puede relacionarse con varias fuentes de evidencia y con una o más estaciones cuya relevancia debe justificarse.

### Scope / Representativeness

Expresa la relación de relevancia espacial entre una Station y una Location.

No afirma que las condiciones sean idénticas dentro de un área. Debe permitir distinguir entre observación directa y uso de esa observación como evidencia relevante para otro lugar.

### Evidence

Abstracción para el soporte utilizado en la evaluación de una Location.

Puede incluir, al menos:

- observaciones cuantitativas de estaciones;
- indicadores derivados;
- evidencia documental/cualitativa;
- en el futuro, valores modelados explícitamente etiquetados como tales.

La procedencia y el tipo de evidencia deben permanecer visibles.

## 4. Relaciones y restricciones

```text
Station
   │
   │ observaciones
   ▼
Evidence cuantitativa
   │
   ├──────────────► Location
   │                  ▲
   │                  │
   └─ Scope / Representativeness

Evidence documental ───────────► Location
```

Restricciones vigentes:

- ninguna Station representa automáticamente una Location;
- toda relación de representatividad debe ser explícita;
- un valor modelado no puede presentarse como observado;
- la falta de evidencia no puede convertirse en evidencia negativa;
- cualquier transformación debe conservar trazabilidad suficiente para reconstruir fuente y método.

## 5. Estados de investigación/adquisición

La investigación es progresiva. Para evidencia documental se consideran útiles estados como:

```text
not_assessed
in_research
assessed
insufficient_evidence
```

La nomenclatura final puede evolucionar, pero debe conservar la diferencia entre “no investigado” y “investigado sin evidencia suficiente”.

## 6. Relación con el mapa

El mapa debe ser una capa de navegación sobre la evidencia, no un sustituto de ella.

Debe poder distinguir visual y semánticamente:

- estaciones físicas;
- ubicaciones evaluadas;
- relaciones de Scope/Representativeness;
- observaciones directas;
- indicadores derivados;
- valores modelados/interpolados;
- evidencia documental;
- calidad y trazabilidad.

## 7. Interpolación

No existe todavía una interpolación de producción aprobada.

Antes de introducirla deben definirse, como mínimo:

- método;
- variables de entrada;
- criterios de aplicabilidad espacial;
- incertidumbre;
- procedencia;
- forma de distinguir el resultado modelado de una observación directa.

## 8. Compatibilidad con el pipeline existente

El modelo debe ser compatible con los datos AEMET/W2 existentes y no exige reinterpretarlos ni moverlos de forma prematura.

El pipeline de agua conserva su propia autoridad sobre adquisición, QC y agregación. Este modelo consume ese conocimiento como dependencia y gobierna únicamente la semántica de Station/Location/Scope/Evidence.

## 9. Cuestiones abiertas de dominio

- cardinalidades finales entre Station, Location y Evidence;
- esquema de datos concreto para Scope/Representativeness;
- metadatos mínimos obligatorios de Evidence;
- máquina de estados final de adquisición/investigación;
- estrategia de implementación/migración cuando el modelo conceptual esté suficientemente cerrado.

Estas cuestiones pertenecen al estado actual del problema y no deben resolverse mediante supuestos silenciosos.

## 10. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 2026-09-08 | `MODEL.md` deja de actuar como handoff/bootstrap y pasa a contener exclusivamente conocimiento vigente del dominio Station/Location/Scope/Evidence. |
