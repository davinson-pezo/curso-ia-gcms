# Guia de configuracion: NotebookLM con Chrome y Antigravity

Esta guia prepara NotebookLM para el bloque de literatura del curso **IA en GC-MS**. El objetivo es que NotebookLM funcione como una base de conocimiento consultable sobre las referencias del curso, y que Antigravity pueda usarlo a traves de Google Chrome.

NotebookLM no sustituye el criterio cientifico: solo debe responder sobre las fuentes que subimos. Si una respuesta no esta respaldada por las fuentes, no se usa como conclusion final.

> Cambio importante: en el curso ya no usaremos una skill externa de NotebookLM. El flujo recomendado es abrir el cuaderno en Chrome, iniciar sesion manualmente y pedir a Antigravity que interactue con ese cuaderno visible.

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
5. Copia la URL del notebook. La necesitaremos para que Antigravity abra exactamente ese cuaderno.

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

## 4. Nuevo enfoque: Chrome visible + Antigravity

No instalaremos una skill externa de NotebookLM. El flujo sera:

```text
Alumno
-> Antigravity
-> Google Chrome visible
-> cuaderno de NotebookLM abierto y autenticado
-> pregunta escrita en NotebookLM
-> respuesta con citas
-> Antigravity resume y conecta con el pipeline GC-MS
```

Ventajas de este enfoque:

- evita sesiones bloqueadas por automatizaciones en segundo plano;
- permite que el alumno haga login, 2FA o CAPTCHA manualmente;
- mantiene visible lo que Antigravity esta haciendo;
- no requiere guardar cookies, perfiles ni archivos de sesion dentro del repo;
- funciona aunque NotebookLM cambie detalles internos de su interfaz.

---

## 5. Preparar Chrome

1. Abre Google Chrome.
2. Inicia sesion con tu cuenta de Google.
3. Entra en el cuaderno del curso usando la URL copiada antes.
4. Comprueba que aparecen las fuentes cargadas.
5. Deja el cuaderno abierto en una pestana visible.

Si Antigravity abre otra ventana de Chrome, no pasa nada: inicia sesion manualmente en esa ventana o pide al agente que use la ventana donde ya tienes el cuaderno abierto.

---

## 6. Prompt para Antigravity

Usa este prompt desde Antigravity 2.0 o Antigravity IDE:

```text
Abre Google Chrome y navega a este cuaderno de NotebookLM:

<pega aqui la URL del cuaderno>

Si aparece pantalla de login, 2FA, CAPTCHA o seleccion de cuenta, detente y pideme que lo resuelva manualmente.

Cuando el cuaderno este abierto, escribe esta pregunta en NotebookLM:

"Que evidencias relacionan m/z 49 y m/z 84 con aldehidos, cetonas, estres oxidativo o viabilidad embrionaria?"

Espera la respuesta. Devuelveme:
1. resumen de la respuesta;
2. citas o fuentes que NotebookLM menciona;
3. que afirmaciones son defendibles;
4. que afirmaciones siguen siendo especulativas;
5. como conectarlo con el pipeline GC-MS del curso.
```

---

## 7. Preguntas recomendadas

```text
Resume cada paper en una tabla con:
autor, ano, especie, tipo de muestra, tecnica GC-MS, biomarcadores reportados, limitaciones.
```

```text
Que evidencias relacionan VOCs, aldehidos o cetonas con estres oxidativo y viabilidad embrionaria?
```

```text
Que decisiones metodologicas del pipeline GC-MS puedo justificar con estas fuentes?
```

```text
Que conclusiones no deberia afirmar porque las fuentes no las respaldan?
```

---

## 8. Reglas de uso en el curso

- NotebookLM se usa para consultar fuentes, no para inventar bibliografia.
- Toda afirmacion importante debe estar respaldada por una cita del notebook.
- Antigravity puede navegar y escribir preguntas, pero el alumno resuelve login, contrasenas, 2FA y CAPTCHAs.
- No uses automatizaciones en segundo plano ni skills externas de NotebookLM durante el curso.
- Los cromatogramas reales no se suben a GitHub.
- Las referencias pesadas viven en Google Drive, no en el repositorio.
- Los archivos de sesion, cookies o perfiles de navegador nunca se versionan.

---

## 9. Problemas frecuentes

### Antigravity abre Chrome en segundo plano

Pide al agente que traiga Chrome al frente o abre tu mismo el cuaderno en una ventana visible. No continues si no ves que cuaderno esta usando.

### NotebookLM pide login otra vez

Es normal. Inicia sesion manualmente. El agente no debe manejar contrasenas ni 2FA.

### El agente pregunta en el cuaderno equivocado

Copia de nuevo la URL del cuaderno correcto y pide que navegue a esa URL antes de preguntar.

### La respuesta no cita fuentes

No la uses como evidencia. Pide a NotebookLM que responda indicando fuentes o reformula la pregunta.

Para el flujo pedagogico completo, continua con [Paso 3 - NotebookLM para literatura con Chrome](paso3_notebooklm.md).
