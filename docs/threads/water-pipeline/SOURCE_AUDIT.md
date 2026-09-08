# ClimaScope — Auditoría inicial de fuentes de agua (W0/W1)

**Versión:** 1.0.0  
**Estado:** Activo  
**Idioma:** español (España)  
**THREAD responsable:** `thread-water-pipeline`

## 1. Alcance

Este documento registra la auditoría inicial de fuentes para el pipeline de agua. No define un Water Score ni aprueba ningún indicador CRS.

La auditoría sigue la regla del proyecto de mantener separadas adquisición, QC, transformación y diseño de indicadores. Los datos missing no se convierten en cero y no se introduce interpolación en esta fase.

## 2. Familias de fuentes verificadas

| source_id | proveedor | variable | acceso | estado actual | limitación principal |
|---|---|---|---|---|---|
| `aemet_precipitation` | AEMET | precipitación | API REST OpenData | fuente verificada; adquisición pendiente | debe medirse cobertura estación/periodo; requiere API key |
| `snczi_flood` | MITECO | exposición a inundación | visor + descargas/WMS | fuente verificada; descarga reproducible pendiente | la cobertura cartografiada varía y no todas las áreas inundables están mapeadas |
| `water_bodies_surface` | MITECO | aguas superficiales | descargas GIS/WMS | fuente verificada; descarga reproducible pendiente | el inventario no es una medida de seguridad de suministro |
| `water_bodies_groundwater` | MITECO | aguas subterráneas | descargas GIS/WMS | fuente verificada; descarga reproducible pendiente | la presencia no implica recurso explotable o suministro seguro |
| `drought` | MITECO / organismos de cuenca | sequía/escasez | planes oficiales y servicios de cuenca | familia verificada; auditoría de indicador pendiente | sequía y escasez son conceptos distintos |
| `reservoirs` | MITECO / organismos de cuenca | regulación/almacenamiento | GIS + datos operativos de cuenca | fuente verificada; auditoría de series pendiente | contar embalses no debe convertirse en un score CRS |
| `supply_systems` | proveedores competentes | sistema de abastecimiento | caso por caso | no automatizado | los límites de sistema y la disponibilidad pública varían |

## 3. Ámbito benchmark

Territorios iniciales:

- Valencia — estación AEMET `8416`;
- Cartagena — estación AEMET `7012D`;
- Madrid-Retiro — estación AEMET `3195`.

Son las ubicaciones benchmark ya utilizadas por el pipeline climático.

## 4. Hallazgos por fuente

### AEMET — precipitación

AEMET OpenData proporciona una API REST adecuada para acceso programático al catálogo publicado. El repositorio ya dispone de un descargador de climatología diaria, por lo que el pipeline de agua no debe duplicar ni modificar innecesariamente el pipeline térmico.

La tarea W1 inmediata es adquirir/inspeccionar precipitación de las tres estaciones benchmark y reportar:

- cobertura temporal;
- número de registros;
- nulos;
- ceros explícitos;
- valores positivos;
- totales mensuales;
- totales anuales;
- controles básicos de plausibilidad.

Un valor de precipitación missing permanece missing. Nunca se interpreta como `0`.

### SNCZI

MITECO proporciona el sistema nacional de cartografía de zonas inundables y descargas oficiales. El catálogo incluye zonas para periodos de retorno T=10, T=50, T=100 y T=500, además de ARPSIs.

La primera implementación debe verificar una ruta reproducible de descarga y registrar metadatos de capa/versión antes de calcular exposición.

MITECO advierte que no todas las zonas potencialmente inundables de España están actualmente cartografiadas. La ausencia de polígono no puede tratarse como prueba de ausencia de peligro.

### Masas de agua superficiales y subterráneas

MITECO publica cartografía del ciclo de planificación hidrológica 2022–2027, incluyendo masas superficiales y subterráneas y capas de estado.

Son evidencia útil de contexto de recurso/sistema, pero la mera presencia de una masa de agua no constituye un indicador de seguridad hídrica.

### Sequía y escasez

La documentación vigente de MITECO distingue gestión de sequía y escasez y proporciona Planes Especiales de Sequía por cuenca. La implementación debe conservar esta distinción. Esta auditoría no aprueba un indicador compuesto de sequía/escasez.

### Embalses

El catálogo de servicios de agua de MITECO expone capas nacionales de inventario/GIS de embalses y presas. Las series operativas de almacenamiento requieren una auditoría separada por cuenca/fuente. Contar embalses no es un proxy aceptado de seguridad hídrica.

### Sistemas de abastecimiento

Esta capa permanece intencionadamente no automatizada. El trabajo benchmark debe mapear para cada territorio el sistema real de suministro, fuentes, infraestructura y recursos externos antes de proponer cualquier métrica de dependencia.

## 5. Procedencia

Todo dataset adquirido debe poder conservar al menos:

```text
source_id
provider
dataset
retrieval_date
source_url
access_method
raw_file
transformation
quality_status
limitations
```

Linaje previsto:

```text
raw → clean → derived
```

Ningún indicador CRS derivado pertenece a esta fase.

## 6. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 2026-09-08 | Normalización al castellano y al formato documental vigente, sin cambiar hallazgos ni decisiones de la auditoría. |
