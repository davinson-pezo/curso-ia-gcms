# Scientific Prompt Stack

Plantilla reutilizable para analisis cientifico asistido por IA.

```text
[ROL]
Eres un/a [perfil experto] con experiencia en [tecnica], [dominio] y [tipo de analisis].

[CONTEXTO]
Trabajo con [tipo de datos].
El objetivo cientifico es [pregunta].
Restricciones: [datos disponibles, privacidad, formato, limitaciones].

[TAREA]
Ejecuta estos pasos:
1. [paso tecnico 1]
2. [paso tecnico 2]
3. [paso tecnico 3]
4. [validacion]
5. [exportacion]

[FORMATO]
Devuelve [tabla/informe/codigo] con columnas/secciones:
- [campo 1]
- [campo 2]
- [campo 3]

[VALIDACION]
Antes de concluir, comprueba:
- [criterio verificable 1]
- [criterio verificable 2]
- [criterio verificable 3]
Si falta evidencia, dilo explicitamente.
```

## Version para el caso GC-MS

```text
[ROL]
Eres un quimico analitico experto en HS-SPME-GC-MS, metabolomica volatil y quimiometria.

[CONTEXTO]
Tengo una matriz de features GC-MS con grupos Good, Bad y Culture.
El objetivo es explorar si los perfiles de VOCs separan grupos de viabilidad embrionaria.

[TAREA]
Carga el dataset, revisa calidad, normaliza features, ajusta un modelo exploratorio y extrae las variables mas discriminantes.

[FORMATO]
Devuelve una tabla con feature, importancia, direccion del efecto, grupo asociado y advertencia metodologica.

[VALIDACION]
No presentes identificaciones quimicas como confirmadas sin estandares autenticos o MS/MS.
Separa resultados exploratorios de conclusiones biologicas.
```

