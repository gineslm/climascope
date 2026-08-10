# Climate Refuge — AEMET benchmark pipeline v0.4

## Cambio principal de esta versión

La descarga ahora es **reanudable por bloques**.

Cada bloque de hasta 180 días se guarda inmediatamente en:

`data/raw/aemet/`

Ejemplo:

`8416_2015-12-06_2016-06-02.json`

Si vuelves a ejecutar el programa y ese archivo ya existe y contiene datos, el programa muestra:

`[YA DESCARGADO, reutilizando]`

y NO hace ninguna petición a AEMET para ese periodo.

Al final se genera además un archivo consolidado:

`8416_2011-01-01_2025-12-31.json`

## Importante sobre las descargas anteriores

Las versiones anteriores del programa no guardaban cada bloque individual inmediatamente.
Guardaban el consolidado solamente cuando terminaba toda la estación.

Por eso, los bloques que viste en pantalla durante una ejecución anterior **pueden no existir como archivos recuperables** si el proceso se interrumpió antes de finalizar.

La v0.4 evita precisamente ese problema.

## Ejecución

1. Copia `.env.example` a `.env`.
2. Añade una NUEVA API key de AEMET.
3. `pip install -r requirements.txt`
4. `python src/pipeline.py`

Puedes interrumpir y volver a ejecutar. Los bloques ya descargados se reutilizarán.

## Ubicación de los datos

Desde la carpeta raíz del proyecto:

`data/raw/aemet/`

La ruta completa en Windows será aproximadamente:

`C:\Users\User\Downloads\climate_refuge_aemet_v0_1\data\raw\aemet\`

o la carpeta equivalente donde hayas descomprimido el proyecto.

## Seguridad

La clave API compartida anteriormente debe considerarse expuesta. Revócala/regénérala y usa la nueva solamente en `.env`.
