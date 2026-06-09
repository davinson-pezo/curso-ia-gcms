# Roadmap de reconstruccion

Este archivo resume por donde continuar despues de recuperar la estructura minima del repositorio.

## Fase 1 - Repositorio usable

- README general.
- Guias basicas de alumno.
- Presentacion HTML accesible.
- Script minimo de datos sinteticos.
- `.gitignore` para evitar subir datos reales, `.DS_Store`, entornos y resultados locales.

Estado: completado como base inicial.

## Fase 2 - Material de practicas

- Crear un notebook de exploracion de datos sinteticos.
- Anadir una practica de PCA/PLS-DA con graficos.
- Crear una plantilla de informe tecnico.
- Completar `recursos/lecturas/README.md` con papers reales y enlaces.

## Fase 3 - Pipeline cientifico

- Reconstruir scripts del pipeline real en version docente.
- Separar codigo generico de codigo dependiente de datos privados.
- Documentar parametros: baseline ASLS, deteccion de picos, alignment, validacion.
- Anadir tests simples para scripts criticos.

## Fase 4 - Entrega para GitHub

- Revisar licencias y autoria de imagenes.
- Exportar una version PDF de backup.
- Crear primer commit.
- Conectar remoto de GitHub.
- Activar GitHub Pages si se quiere publicar la presentacion como web.

## Riesgos abiertos

- La carpeta canonica de imagenes de la presentacion es `images/` en la raiz del repositorio.
- El pipeline real no debe mezclarse con datos confidenciales del proyecto Milton.

## Cambios recientes

- Presentacion auditada y alineada con `informe_dataquorum_v3_final.md`: parametros ASLS, metricas PLS-DA, tabla VIP top 10 y validacion de m/z 49/84 corregidos.
- Notas del orador y guion de alumnos revisados y consistentes con el informe.
- Dataset sintetico regenerado a 22 muestras (8 Good, 7 Bad, 7 Culture).
