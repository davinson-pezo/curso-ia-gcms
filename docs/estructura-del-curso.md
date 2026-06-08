# Estructura del curso

Este documento fija la estructura del repositorio para que sea comprensible en GitHub y util durante la clase.

## Principios

- La presentacion debe poder abrirse sin construir nada.
- Los alumnos no deben necesitar datos reales ni confidenciales.
- Los comandos mostrados en slides deben apuntar a archivos existentes.
- Las salidas generadas localmente no deben subirse al repositorio.
- Las imagenes usadas por la presentacion deben mantener rutas estables.

## Mapa de carpetas

```text
curso-ia-gcms/
├── README.md
├── LICENSE
├── LICENSE-MIT.md
├── requirements.txt
├── index.html
├── output/presentations/
│   ├── index.html
│   ├── images/
│   └── markdown/
├── images/
├── markdown/
├── guion-alumnos/
├── recursos/
│   ├── datos-sinteticos/
│   ├── lecturas/
│   └── prompts/
├── scripts/
├── resultados/
└── docs/
```

## Convencion de nombres

- Guias de alumnos: `pasoN_tema.md`.
- Prompts reutilizables: `nombre_descriptivo.md`.
- Scripts: verbo + objeto, por ejemplo `generar_datos_sinteticos.py`.
- Resultados: no versionar salvo ejemplos pequenos y anonimizados.

## Pendientes recomendados

- Exportar una version PDF de la presentacion para backup.
- Decidir si `output/presentations/` sera el entregable final o si se generara desde una fuente editable.
- Anadir notebooks de practica cuando el pipeline real este reconstruido.
- Separar datos sinteticos pequenos versionados de datos generados por cada alumno.

