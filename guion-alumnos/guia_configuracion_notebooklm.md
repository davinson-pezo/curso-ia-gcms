# Guia de configuracion: NotebookLM como RAG del curso

Esta guia prepara NotebookLM para el bloque de literatura del curso **IA en GC-MS**. El objetivo es que NotebookLM funcione como una base de conocimiento consultable sobre las referencias del curso, y que despues podamos usar esas respuestas desde Antigravity IDE o desde un agente de codificacion.

NotebookLM no sustituye el criterio cientifico: solo debe responder sobre las fuentes que subimos. Si una respuesta no esta respaldada por las fuentes, no se usa como conclusion final.

---

## 1. Requisitos previos

- Python 3.10 o superior.
- Google Chrome instalado.
- Cuenta de Google con acceso a [NotebookLM](https://notebooklm.google.com/).
- Acceso al repositorio del curso.
- Acceso a las referencias del curso en Google Drive:
  [Referencias para NotebookLM](https://drive.google.com/drive/folders/1hHobZbc4fEVaL7YF3qN5BhDrxhqBE6wB?usp=share_link)

---

## 2. Crear el cuaderno en NotebookLM

1. Abre [NotebookLM](https://notebooklm.google.com/).
2. Crea un notebook nuevo con un nombre claro, por ejemplo:

   ```text
   Curso IA GC-MS - Referencias
   ```

3. Sube los PDFs y documentos de la carpeta de referencias del curso.
4. Espera a que NotebookLM termine de indexar las fuentes.
5. Copia la URL del notebook. La necesitaremos si vamos a conectarlo con un agente.

Ejemplo de URL:

```text
https://notebooklm.google.com/notebook/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

---

## 3. Consultas base para comprobar el RAG

Antes de conectarlo a un agente, comprueba manualmente que el notebook responde bien.

```text
Resume cada paper en una tabla con:
autor, ano, especie, tipo de muestra, tecnica GC-MS, biomarcadores reportados, limitaciones.
```

```text
Busca si aparecen aldehidos, cetonas, m/z 49 o m/z 84 como marcadores de estres oxidativo o viabilidad embrionaria.
```

```text
Que afirmaciones puedo defender con estas fuentes y cuales serian especulativas?
```

Si NotebookLM no cita una fuente concreta, no uses esa respuesta como evidencia.

---

## 4. Conexion opcional con un agente de IA

Esta parte es opcional. Sirve para que un agente pueda consultar NotebookLM en segundo plano mediante automatizacion de navegador.

El flujo se basa en un repositorio externo de automatizacion:

- [notebooklm-skill en GitHub](https://github.com/PleasePrompto/notebooklm-skill)

Descarga el repositorio como ZIP desde **Code -> Download ZIP** y descomprimelo.

Rutas esperadas tras descomprimir:

- macOS: `/Users/tu_usuario/Downloads/notebooklm-skill-master`
- Windows: `C:\Users\tu_usuario\Downloads\notebooklm-skill-master`

---

## 5. Reubicar la herramienta

Para no mezclar esta automatizacion con el repositorio del curso, ponla en tu carpeta de usuario y renombrala como `notebook-skill`.

macOS/Linux:

```bash
mv "$HOME/Downloads/notebooklm-skill-master" "$HOME/notebook-skill"
```

Windows PowerShell:

```powershell
Move-Item -Path "$Home\Downloads\notebooklm-skill-master" -Destination "$Home\notebook-skill"
```

---

## 6. Inicializar dependencias

macOS/Linux:

```bash
cd ~/notebook-skill
python3 scripts/run.py auth_manager.py status
```

Windows PowerShell:

```powershell
cd ~\notebook-skill
python scripts/run.py auth_manager.py status
```

Este comando suele:

1. Crear un entorno virtual `.venv`.
2. Instalar dependencias.
3. Preparar el navegador automatizado.
4. Comprobar si ya existe una sesion autenticada.

La primera vez normalmente aparecera algo como:

```text
Authenticated: No
```

---

## 7. Autenticar Google una sola vez

NotebookLM requiere una sesion real de Google. El agente no debe resolver contrasenas, 2FA ni CAPTCHAs por su cuenta.

macOS/Linux:

```bash
python3 scripts/run.py auth_manager.py setup
```

Windows:

```powershell
python scripts/run.py auth_manager.py setup
```

Proceso:

1. Se abre una ventana visible de Chrome.
2. El alumno inicia sesion con su cuenta de Google.
3. Se navega a NotebookLM si hace falta.
4. La herramienta guarda la sesion localmente.

No subas nunca al repositorio archivos de sesion, cookies ni contenido de `~/notebook-skill/data/`.

---

## 8. Registrar el notebook del curso

Sustituye la URL por la del notebook creado para el curso.

macOS/Linux:

```bash
python3 scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" \
  --name "Curso IA GC-MS - Referencias" \
  --description "Referencias del curso sobre HS-SPME-GC-MS, VOCs, embriones bovinos, quimiometria y PLS-DA" \
  --topics "GC-MS,HS-SPME,VOCs,embriones bovinos,PLS-DA,biomarcadores"
```

Windows PowerShell:

```powershell
python scripts/run.py notebook_manager.py add `
  --url "https://notebooklm.google.com/notebook/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" `
  --name "Curso IA GC-MS - Referencias" `
  --description "Referencias del curso sobre HS-SPME-GC-MS, VOCs, embriones bovinos, quimiometria y PLS-DA" `
  --topics "GC-MS,HS-SPME,VOCs,embriones bovinos,PLS-DA,biomarcadores"
```

---

## 9. Consultar NotebookLM desde el agente

Ejemplo de consulta por consola:

```bash
python3 scripts/run.py ask_question.py \
  --notebook-url "https://notebooklm.google.com/notebook/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" \
  --question "Que evidencias relacionan m/z 49 y m/z 84 con aldehidos, cetonas o estres oxidativo en embriones?"
```

Flujo esperado:

```text
Pregunta del alumno
-> Agente de IA
-> script local de NotebookLM
-> NotebookLM consulta las fuentes subidas
-> respuesta con citas
-> el agente resume y conecta con el pipeline GC-MS
```

---

## 10. Reglas de uso en el curso

- NotebookLM se usa para consultar fuentes, no para inventar bibliografia.
- Toda afirmacion importante debe estar respaldada por una cita del notebook.
- Los cromatogramas reales no se suben a GitHub.
- Las referencias pesadas viven en Google Drive, no en el repositorio.
- Los archivos de autenticacion local nunca se versionan.

Para el flujo pedagogico completo, continua con [Paso 3 - NotebookLM para literatura](paso3_notebooklm.md).
