# Datos sinteticos

Los datos de esta carpeta se generan con:

```bash
python scripts/generar_datos_sinteticos.py
```

El archivo esperado es:

```text
gcms_features_sinteticas.csv
```

## Diseno del dataset

- 22 muestras (8 Good, 7 Bad, 7 Culture).
- 3 grupos: `Good`, `Bad`, `Culture`.
- 213 features numericas.
- Algunas features tienen senal diferencial simulada para que el ejercicio sea interpretable.

## Importante

Estos datos no representan mediciones reales. Sirven para practicar:

- carga de datos;
- control de calidad;
- normalizacion;
- modelos exploratorios;
- interpretacion responsable.

