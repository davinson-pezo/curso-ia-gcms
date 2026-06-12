# Guia - Identificacion con NIST 17 en Python

Objetivo: entender como se propone una identidad quimica para un pico GC-MS usando Python, espectros limpios y la biblioteca NIST 17.

Esta guia complementa el pipeline GC-MS. No sustituye la validacion quimica: los resultados de NIST son candidatos de identificacion que deben revisarse con criterio analitico, bibliografia y, cuando sea posible, patrones autenticos.

## Donde encaja en el flujo

```text
archivos CDF + tabla de picos
        |
        v
extraccion del espectro del pico
        |
        v
substraccion de fondo local
        |
        v
busqueda contra NIST 17
        |
        v
candidatos con Match Factor
        |
        v
revision quimica e informe
```

## Recursos necesarios

- Cromatogramas GC-MS del curso.
- Tabla de picos exportada desde ChemStation u otra herramienta equivalente.
- Biblioteca NIST 17 descargada desde Drive.
- Base SQLite derivada de NIST 17, generada localmente.

La biblioteca y cualquier base de datos derivada son archivos pesados. No deben subirse a GitHub.

## Algoritmo usado

### 1. Leer la tabla de picos

El pipeline parte de una tabla con, al menos:

- tiempo de retencion;
- area relativa o area%;
- informacion de control si existe;
- identificacion previa si el software la propone.

### 2. Localizar el apex en el CDF

Para cada pico se abre el archivo CDF y se busca el scan cuyo tiempo esta mas cerca del tiempo de retencion objetivo.

```text
scan_apex = scan con menor distancia entre tiempo_scan y RT_objetivo
```

Ese scan contiene el espectro de masas que se va a limpiar y comparar.

### 3. Aplicar substraccion de fondo local

Para evitar que el espectro del pico este contaminado por column bleed, siloxanos, ruido o fondo instrumental, se usa una ventana local alrededor del apex:

- ventana aproximada: +/- 20 scans;
- exclusion del centro del pico: +/- 4 scans;
- fondo elegido: scan con menor TIC dentro de la ventana permitida.

Luego se resta el espectro de fondo al espectro del apex. Para cada ion del apex se busca el ion equivalente en el fondo con una tolerancia aproximada de +/- 0.5 Da.

```text
intensidad_limpia = max(0, intensidad_apex - intensidad_fondo)
```

Los iones con intensidad 0 se eliminan antes de buscar en NIST.

### 4. Buscar coincidencias en NIST 17

El espectro limpio se compara contra la biblioteca NIST 17 usando un Match Factor espectral. La idea es comparar el patron de masas e intensidades del pico experimental con los espectros de referencia.

El calculo usa una similitud tipo coseno ponderada:

- peso de masa: 1.0;
- peso de intensidad: 0.5;
- tolerancia habitual para emparejar masas: +/- 0.5 Da.

En Python, el emparejamiento de masas puede acelerarse con `numpy.searchsorted`, evitando bucles lentos sobre todas las combinaciones de masas.

### 5. Aplicar criterios de decision

El pipeline usa reglas practicas para separar coincidencias razonables de resultados debiles:

- aceptar hits cuando el Match Factor es mayor o igual a 400 en una ventana de busqueda de +/- 2.0 Da;
- si no hay hit y el pico tiene area relevante, probar una busqueda de respaldo con ventana de +/- 3.5 Da;
- si el pico es pequeno y no hay coincidencia suficiente, registrar `No match found`.

Estos umbrales son criterios operativos para el curso. En un trabajo real deben justificarse y revisarse segun matriz, instrumento, calidad espectral y objetivo analitico.

## Salidas esperadas

El pipeline puede generar:

- reportes detallados por muestra en `.txt`;
- tabla maestra consolidada en `.csv`;
- tabla simplificada con los mejores hits por pico;
- campos utiles como RT, area%, nombre candidato, formula, CAS y Match Factor.

La tabla consolidada permite conectar la identificacion tentativa con el analisis multivariado y el informe tecnico final.

## Prompt para Antigravity

```text
[ROL]
Eres un quimico analitico experto en GC-MS, espectrometria de masas e identificacion espectral.

[CONTEXTO]
Tengo cromatogramas GC-MS en CDF, una tabla de picos exportada desde ChemStation y una biblioteca NIST 17 convertida a SQLite localmente.
Quiero revisar como se propone una identidad quimica para cada pico usando Python.

[TAREA]
Explica o implementa un pipeline que:
1. Lea la tabla de picos.
2. Abra el CDF correspondiente.
3. Localice el scan del apex para cada RT.
4. Aplique substraccion de fondo local.
5. Compare el espectro limpio contra NIST 17.
6. Devuelva los mejores candidatos con Match Factor.
7. Exporte un reporte detallado y una tabla consolidada.

[CRITERIOS]
- No trates los hits de NIST como identificaciones confirmadas.
- Documenta tolerancias, umbrales y limitaciones.
- Marca como candidato cualquier compuesto no validado con patron autentico.
- No subas la base NIST ni archivos pesados al repositorio.

[FORMATO]
Devuelve:
- resumen del flujo;
- pseudocodigo o codigo Python comentado;
- estructura de la tabla de salida;
- advertencias metodologicas.
```

## Como interpretar el resultado

Una identificacion por biblioteca es una propuesta, no una prueba definitiva. Antes de usar un compuesto como biomarcador candidato, revisa:

- calidad del espectro;
- Match Factor y diferencia entre primer y segundo hit;
- coherencia con el tiempo de retencion;
- plausibilidad quimica y biologica;
- presencia del ion o fragmentos diagnosticos;
- evidencia bibliografica en NotebookLM;
- necesidad de confirmacion con estandar autentico.

La IA puede ayudar a ordenar el flujo, escribir codigo y resumir candidatos, pero la decision cientifica sigue dependiendo del analista.
