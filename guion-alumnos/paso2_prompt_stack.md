# Paso 2 - Scientific Prompt Stack

Objetivo: escribir instrucciones que produzcan resultados verificables, no respuestas bonitas.

## Estructura

Usa siempre cinco bloques:

```text
[ROL]
Quien debe ser la IA.

[CONTEXTO]
Datos disponibles, instrumento, tecnica, restricciones y objetivo biologico.

[TAREA]
Accion concreta y pasos esperados.

[FORMATO]
Formato de salida: tabla, CSV, lista de checks, codigo, informe.

[VALIDACION]
Como debe comprobarse que el resultado es correcto.
```

## Practica

Toma el caso de embriones y escribe un prompt para:

- Leer datos de GC-MS.
- Aplicar correccion de baseline.
- Detectar picos.
- Alinear features entre muestras.
- Ajustar un modelo PLS-DA.
- Reportar los 10 biomarcadores principales.

Compara tu prompt con:

```text
recursos/prompts/scientific_prompt_stack.md
```

## Criterio de calidad

Un buen prompt cientifico permite auditar:

- Que datos se usaron.
- Que pasos se ejecutaron.
- Que parametros se eligieron.
- Que salidas se generaron.
- Que validaciones se hicieron.

