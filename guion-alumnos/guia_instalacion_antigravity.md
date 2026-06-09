# Guia de instalacion: Antigravity 2.0, IDE, CLI y Science Skills

Esta guia deja preparadas las herramientas que usaremos durante el curso:

- **Antigravity 2.0**: superficie principal para orquestar agentes.
- **Antigravity IDE**: editor para trabajar con el repositorio.
- **Antigravity CLI**: interfaz de terminal para ejecutar tareas agenticas.
- **Science Skills**: plugin/skill necesario para flujos cientificos.

Verificado el 8 de junio de 2026 contra documentacion oficial de Google Antigravity y el repositorio `google-deepmind/science-skills`.

---

## 1. Requisitos previos

- Cuenta de Google.
- Google Chrome instalado.
- Python 3.10 o superior para las practicas del repo.
- Git instalado.
- Acceso a este repositorio:

```bash
git clone https://github.com/davinson-pezo/curso-ia-gcms.git
cd curso-ia-gcms
```

Requisitos de sistema indicados por Google:

- macOS: version con soporte de seguridad de Apple; minimo macOS 12 Monterey. X86 no soportado.
- Windows: Windows 10 de 64 bits o superior.
- Linux: `glibc >= 2.28` y `glibcxx >= 3.4.25`.

---

## 2. Instalar Antigravity 2.0

1. Abre la pagina oficial:

   [https://antigravity.google/download](https://antigravity.google/download)

2. Descarga el instalador correspondiente a tu sistema operativo.
3. Instala la aplicacion.
4. Si aparece una opcion tipo **Keep Both** o **Replace**, elige **Replace** para actualizar la instalacion principal.
5. Inicia sesion con tu cuenta de Google.

Antigravity 2.0 trabaja con **Projects**. Para este curso:

1. Crea un proyecto nuevo.
2. Anade la carpeta local del repositorio `curso-ia-gcms`.
3. Usa permisos conservadores al inicio.
4. Concede permisos adicionales solo cuando entiendas que accion va a ejecutar el agente.

---

## 3. Instalar o abrir Antigravity IDE

Antigravity IDE es el editor donde trabajaremos sobre archivos del repositorio. Puede instalarse desde el mismo centro de descargas:

[https://antigravity.google/download](https://antigravity.google/download)

Tambien esta la pagina de producto:

[https://www.antigravity.google/product/antigravity-ide](https://www.antigravity.google/product/antigravity-ide)

Durante la instalacion o actualizacion de Antigravity 2.0 puede aparecer una opcion para reinstalar o conservar el IDE. Para este curso conviene tener ambos:

- Antigravity 2.0 para gestionar agentes y tareas largas.
- Antigravity IDE para editar, revisar y ejecutar el repositorio.

Comprobacion rapida:

1. Abre Antigravity IDE.
2. Abre la carpeta `curso-ia-gcms`.
3. Verifica que puedes ver `README.md`, `guion-alumnos/` y `output/presentations/index.html`.
4. Abre una terminal integrada y ejecuta:

```bash
python --version
git status
```

---

## 4. Instalar Antigravity CLI

La CLI se instala con los comandos oficiales de Google.

macOS/Linux:

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://antigravity.google/cli/install.ps1 | iex
```

Windows CMD:

```cmd
curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Despues de instalar, abre una terminal nueva y comprueba:

```bash
antigravity --version
```

Si el comando no existe, cierra y vuelve a abrir la terminal. En macOS/Linux tambien puede hacer falta recargar la shell:

```bash
source ~/.zshrc
```

o

```bash
source ~/.bashrc
```

---

## 5. Autenticacion de la CLI

La CLI intenta usar una sesion segura del sistema. Si no encuentra una, abrira el navegador para iniciar sesion con Google.

Prueba desde la raiz del repositorio:

```bash
antigravity
```

En sesiones remotas por SSH, la CLI puede mostrar una URL de autorizacion. Copiala en tu navegador local, inicia sesion y pega el codigo de vuelta en la terminal.

Para cerrar sesion dentro de la CLI:

```text
/logout
```

---

## 6. Activar Science Skills

Para este curso es **obligatorio activar Science**. Lo usaremos para consultas cientificas, referencias, bases de datos, quimioinformatica y razonamiento sobre literatura.

### Opcion A: usuario nuevo de Antigravity

1. Abre Antigravity.
2. Durante el onboarding busca el paso **Build with Google**.
3. Marca la opcion **Science**.
4. Finaliza el onboarding.
5. Reinicia Antigravity si lo solicita.

### Opcion B: usuario que ya tenia Antigravity

1. Actualiza Antigravity a la ultima version.
2. Abre **Settings**.
3. Ve a **Customizations**.
4. Entra en **Build with Google Plugins**.
5. Pulsa **Customize**.
6. Descarga/activa el plugin **Science**.
7. Reinicia Antigravity.

### Opcion C: instalacion manual del bundle

Si el instructor lo pide o si el plugin no aparece en la interfaz:

```bash
npx skills add google-deepmind/science-skills/
```

Notas:

- La primera vez que uses una Science Skill, Antigravity puede pedir permiso para instalar dependencias.
- El bundle usa `uv` para gestionar dependencias.
- Algunas skills pueden requerir claves API. Si una skill lo necesita, el agente debe pedir la clave y explicar donde guardarla.
- No guardes claves API dentro del repositorio.

---

## 7. Comprobacion para el curso

Desde Antigravity IDE o CLI, abre el repositorio y comprueba que el agente entiende el contexto:

```text
Lee README.md, recursos.md y guion-alumnos/paso3_notebooklm.md.
Resume en 5 puntos que herramientas se usaran en el curso y que datos no deben subirse a GitHub.
```

Despues comprueba Science Skills con una pregunta cientifica sencilla:

```text
Usando Science Skills, explica que son VOCs en el contexto de HS-SPME-GC-MS y por que pueden ser utiles para evaluar viabilidad embrionaria.
```

La respuesta debe:

- Ser cientifica y prudente.
- No inventar referencias.
- Distinguir entre evidencia, hipotesis y limitaciones.

---

## 8. Problemas frecuentes

### El comando `antigravity` no aparece

- Cierra y abre la terminal.
- Revisa que el instalador haya anadido la CLI al `PATH`.
- En macOS/Linux prueba `source ~/.zshrc` o `source ~/.bashrc`.

### No aparece Science

- Actualiza Antigravity.
- Revisa Settings -> Customizations -> Build with Google Plugins.
- Si sigue sin aparecer, usa la instalacion manual con `npx skills add google-deepmind/science-skills/`.

### El agente pide permisos para instalar `uv`

Es esperado la primera vez que se usa Science Skills. Acepta solo si estas dentro de una sesion del curso y entiendes la accion.

### La CLI abre el navegador para iniciar sesion

Es normal. Inicia sesion con tu cuenta de Google y vuelve a la terminal.

---

## 9. Fuentes oficiales

- Antigravity 2.0: [https://antigravity.google/docs/overview?app=antigravity](https://antigravity.google/docs/overview?app=antigravity)
- Descargas: [https://antigravity.google/download](https://antigravity.google/download)
- Antigravity IDE: [https://www.antigravity.google/product/antigravity-ide](https://www.antigravity.google/product/antigravity-ide)
- Antigravity CLI: [https://www.antigravity.google/docs/cli-getting-started](https://www.antigravity.google/docs/cli-getting-started)
- Science Skills: [https://github.com/google-deepmind/science-skills](https://github.com/google-deepmind/science-skills)
- Build with Google Plugins: [https://antigravity.google/docs/build-with-google?app=antigravity](https://antigravity.google/docs/build-with-google?app=antigravity)
