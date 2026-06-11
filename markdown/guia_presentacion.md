# Guia de seguimiento de la presentacion

> Material para alumnos. No es un guion literal del profesor: resume que vamos a ver, que conviene preparar y que deberias poder hacer al terminar cada bloque.

## Como usar esta guia

- Tenla abierta junto con la presentacion.
- Usa cada bloque como mapa de estudio, no como transcripcion de la clase.
- Marca dudas durante la sesion y vuelve a los enlaces del repositorio al final.
- Para la parte practica, trabaja siempre desde el repositorio clonado y revisa primero `README.md` y `recursos.md`.

## Objetivo del curso

Al final del seminario deberias entender como combinar IA agent-first, Antigravity, NotebookLM, MCP y Python para transformar datos GC-MS en un flujo de trabajo reproducible:

- preparar datos y recursos cientificos;
- escribir prompts auditables para analisis;
- conectar herramientas externas o datos propios;
- ejecutar un pipeline GC-MS guiado por IA;
- interpretar resultados con criterio cientifico;
- convertir el analisis en un informe tecnico comparable al ejemplo DataQuorum.

## Bloques de la presentacion

### 1. Apertura y contexto

Veremos por que la IA es relevante para cromatografia y que significa trabajar con agentes en investigacion cientifica.

Al terminar este bloque deberias poder explicar:

- que puede acelerar la IA en un flujo GC-MS;
- que no debe delegarse sin supervision humana;
- por que el criterio cientifico sigue siendo central;
- cual sera el caso practico del curso.

### 2. Stack moderno de IA para ciencia

Revisaremos las capas que aparecen en un flujo moderno:

- modelos LLM;
- herramientas y agentes;
- conectores MCP;
- datos propios y bases externas.

La idea clave es separar el modelo de las herramientas y de los datos. Si algo falla, hay que saber en que capa se produjo el problema.

### 3. Antigravity 2.0, IDE y CLI

Veremos las diferencias practicas entre:

- Antigravity 2.0 como entorno agent-first;
- Antigravity IDE para trabajo interactivo con codigo;
- Antigravity CLI para tareas reproducibles o por lotes.

El objetivo no es memorizar comandos, sino entender cuando usar cada superficie.

### 4. Science Skills y herramientas cientificas

Veremos como un agente puede consultar herramientas cientificas especializadas en lugar de limitarse a generar texto.

Presta atencion a:

- trazabilidad de las respuestas;
- limites de cada herramienta;
- diferencia entre buscar informacion y validar evidencia.

### 5. Prompt engineering cientifico

Trabajaremos con una plantilla reusable para prompts cientificos:

- rol;
- contexto;
- tarea;
- formato;
- validacion.

Resultado esperado: poder escribir un prompt que otro cientifico podria revisar y ejecutar sin pedir aclaraciones.

### 6. MCP y conexion con datos externos

Veremos MCP como una forma estandarizada de conectar la IA con archivos, bases de datos o herramientas externas.

Al terminar este bloque deberias entender:

- que problema resuelve MCP;
- por que no es lo mismo que copiar y pegar datos;
- que riesgos hay al conectar agentes a informacion real;
- como documentar que herramientas se han usado.

### 7. NotebookLM como RAG cientifico

NotebookLM se usara como base de consulta sobre referencias y protocolos del curso.

Lo importante es entender:

- que NotebookLM responde sobre las fuentes que le damos;
- por que ayuda a reducir respuestas inventadas;
- como usarlo para contrastar decisiones metodologicas;
- que limitaciones tiene aunque cite fuentes.

### 8. Antigravity + NotebookLM

Veremos el flujo combinado:

- NotebookLM como memoria bibliografica;
- Antigravity como entorno de ejecucion;
- el alumno como responsable de validar decisiones.

La idea es no usar una sola herramienta para todo: cada herramienta cumple una funcion distinta.

### 9. Caso practico GC-MS: embriones bovinos

Este es el bloque central. Trabajaremos con un caso de analisis GC-MS orientado a biomarcadores de viabilidad embrionaria.

Veremos el flujo completo:

- lectura de archivos CDF;
- correccion de linea base;
- deteccion de picos;
- alineamiento entre muestras;
- PLS-DA y VIP scores;
- validacion quimica de senales;
- interpretacion biologica;
- limitaciones del analisis.

Resultado esperado: comprender como se pasa de cromatogramas crudos a una tabla de biomarcadores candidatos y que partes del resultado son exploratorias.

### 10. Referencias bibliograficas

Veremos como construir una bibliografia verificable usando IA sin perder control sobre las fuentes.

Puntos clave:

- verificar DOI y metadatos;
- distinguir resumen de evidencia;
- usar NotebookLM para consultar fuentes;
- evitar citas no comprobadas.

### 11. Maquetado del paper

Veremos como convertir un informe tecnico en un borrador de manuscrito con estructura IMRyD.

El objetivo es entender el flujo:

- informe tecnico reproducible;
- secciones del paper;
- figuras y tablas;
- formato de revista;
- carta al editor.

### 12. Cierre

Recapitularemos que parte del trabajo hizo la IA y que parte depende del cientifico.

La pregunta final no es "que herramienta uso", sino "como construyo un flujo reproducible, auditable y cientificamente defendible".

## Practica durante el curso

### Antes de empezar

- Clona el repositorio.
- Lee `README.md`.
- Lee `recursos.md`.
- Revisa las guias en `guion-alumnos/`.
- Ten acceso a los cromatogramas y a las referencias indicadas en recursos.

### Durante la sesion practica

Trabajaremos en torno a cinco acciones:

- preparar el entorno;
- escribir un prompt cientifico;
- consultar referencias con NotebookLM;
- ejecutar o revisar el pipeline GC-MS;
- comparar el resultado con el informe de ejemplo.

### Despues de la sesion

Deberias poder continuar con:

- adaptar el prompt a tus propios datos;
- repetir el pipeline con datos sinteticos o propios;
- documentar parametros y decisiones;
- generar una tabla de resultados;
- redactar un informe reproducible.

## Preguntas que deberias poder responder

- Que parte del flujo depende de los datos y que parte depende del modelo?
- Que evidencia necesito para confiar en un biomarcador?
- Como detecto si la IA esta inventando una conclusion?
- Que informacion debe incluir un prompt cientifico auditable?
- Cuando conviene usar NotebookLM y cuando Antigravity?
- Que limitaciones debo declarar antes de convertir resultados en paper?

## Checklist final

- [ ] Entiendo la diferencia entre LLM, agente, herramienta y datos.
- [ ] Tengo localizada la carpeta de recursos del curso.
- [ ] Se donde estan los cromatogramas y las referencias.
- [ ] Puedo explicar el pipeline GC-MS de principio a fin.
- [ ] Puedo escribir un prompt con rol, contexto, tarea, formato y validacion.
- [ ] Se que resultados son exploratorios y cuales requieren validacion externa.
- [ ] Puedo usar el informe DataQuorum como referencia de entregable final.
