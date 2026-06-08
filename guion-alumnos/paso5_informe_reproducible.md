# Paso 5 - Informe reproducible

Objetivo: convertir el analisis en un informe que otra persona pueda auditar.

El informe de referencia del curso es:

```text
informe_dataquorum_v3_final.md
```

Ese archivo esta en la raiz del repositorio junto con su carpeta de imagenes:

```text
informe_dataquorum_v3_final_images/
```

Durante el bloque practico de 90 minutos, la meta no es solo obtener una tabla de biomarcadores: la meta es entender como pasar de cromatogramas, referencias y resultados quimiometricos a un informe tecnico comparable en estructura, trazabilidad y nivel de cautela cientifica.

## Estructura minima

```text
1. Pregunta cientifica
2. Datos usados
3. Preprocesado
4. Modelo exploratorio
5. Resultados
6. Validacion
7. Limitaciones
8. Proximos pasos
```

## Checklist

- El informe distingue datos reales, sinteticos y resultados simulados.
- Cada tabla indica de donde viene.
- Cada grafica tiene una interpretacion y una limitacion.
- No se presentan identificaciones NIST tentativas como confirmadas.
- Las conclusiones separan evidencia, hipotesis y especulacion.
- Las imagenes del informe se guardan con rutas relativas para que abran en GitHub.
- El informe final declara limitaciones como n pequeno, validacion externa pendiente e identificacion tentativa.

## Prompt sugerido

```text
Redacta un informe tecnico breve con estructura IMRaD a partir de los resultados en resultados/.
Marca explicitamente que los datos son sinteticos.
Incluye una seccion de limitaciones y una lista de validaciones necesarias antes de publicar.
```
