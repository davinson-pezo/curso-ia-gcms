# Paso 4 - Pipeline GC-MS

Objetivo: reproducir de forma simplificada el flujo del caso de embriones con datos sinteticos.

## Punto de partida

Genera el dataset:

```bash
python scripts/generar_datos_sinteticos.py
```

Archivo generado:

```text
recursos/datos-sinteticos/gcms_features_sinteticas.csv
```

## Prompt para Antigravity o un agente equivalente

```text
[ROL]
Eres un quimico analitico experto en HS-SPME-GC-MS, metabolomica y quimiometria.

[CONTEXTO]
Tengo una matriz sintetica de features GC-MS en recursos/datos-sinteticos/gcms_features_sinteticas.csv.
Cada fila es una muestra y cada columna feature_* representa una senal cromatografica agregada.
La columna grupo contiene Good, Bad o Culture.

[TAREA]
Analiza el dataset:
1. Carga el CSV.
2. Revisa dimensiones, grupos y valores faltantes.
3. Normaliza las features.
4. Ajusta un modelo exploratorio PLS-DA o PCA + clasificador simple.
5. Extrae las 10 features que mejor separan los grupos.
6. Exporta una tabla de resultados en resultados/biomarcadores_top10.csv.

[FORMATO]
Devuelve:
- resumen de dimensiones;
- tabla top 10 con feature, grupo_asociado, importancia;
- advertencias metodologicas;
- rutas de archivos generados.

[VALIDACION]
No afirmes biomarcadores reales. Marca todo como ejercicio con datos sinteticos.
Comprueba que los grupos Good, Bad y Culture estan representados.
```

## Que deberias obtener

- Un dataset de 22 muestras (igual que el caso real del informe).
- 213 features numericas.
- Tres grupos: `Good`, `Bad`, `Culture`.
- Una tabla top 10 generada en `resultados/`.

## Interpretacion correcta

Este ejercicio sirve para practicar estructura de analisis, no para concluir biologia real. En el curso, el caso de embriones se usa como narrativa cientifica; el repositorio publico debe proteger los datos confidenciales.

## Siguiente paso

Cuando se trabaja con cromatogramas reales, la tabla de features debe conectarse con identificaciones quimicas tentativas. Para esa parte usa la [guia de identificacion con NIST 17](guia_identificacion_nist17.md), donde se resume el flujo Python: CDF, apex, substraccion de fondo local, busqueda espectral y candidatos con Match Factor.
