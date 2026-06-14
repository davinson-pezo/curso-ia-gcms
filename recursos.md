# Recursos externos del curso

Antes de empezar las practicas, lee esta pagina y abre los enlaces de Google Drive indicados por el instructor.

## 1. Cromatogramas de trabajo

Carpeta Drive:

[Cromatogramas GC-MS del curso](https://drive.google.com/drive/folders/1lRc_glpeQNt-PXHD4sLunmMkT75XJl2G?usp=share_link)

Uso en el curso:

- Datos cromatograficos con los que se trabajara durante las practicas.
- Fuente para los ejercicios de lectura, exploracion y pipeline GC-MS.
- No subir estos archivos al repositorio GitHub.

## 2. Referencias para NotebookLM

Carpeta Drive:

[Referencias para NotebookLM](https://drive.google.com/drive/folders/1hHobZbc4fEVaL7YF3qN5BhDrxhqBE6wB?usp=share_link)

Uso en el curso:

- Papers y documentos que se cargaran en NotebookLM.
- NotebookLM se usara como RAG para consultas sobre las referencias.
- El flujo esperado es abrir el cuaderno en Chrome, iniciar sesion manualmente y pedir a Antigravity que consulte ese cuaderno visible.
- No se usara una skill externa de NotebookLM durante el curso.

## 3. Biblioteca NIST 17 para identificacion

Carpeta Drive:

[Biblioteca NIST 17](https://drive.google.com/drive/folders/1bMQohs3BXzdffrAm0DDlJ7EgbBPfIhb5?usp=share_link)

Uso en el curso:

- Biblioteca de espectros de masa para proponer identidades quimicas en GC-MS.
- Se usara despues de extraer y limpiar los espectros de los picos cromatograficos.
- Los resultados se interpretan como candidatos de identificacion, no como confirmacion automatica.
- No subir la biblioteca ni bases de datos derivadas al repositorio GitHub.

## Regla practica

GitHub contiene guias, scripts y material docente. Google Drive contiene los archivos pesados o externos: cromatogramas, referencias bibliograficas y bibliotecas espectrales.

Si descargas datos reales, mantenlos fuera de Git:

```text
data/raw/
```
