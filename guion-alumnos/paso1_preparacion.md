# Paso 1 - Preparacion

Objetivo: dejar el repositorio listo para trabajar durante el curso.

Antes de la practica larga, instala y verifica Antigravity con la [guia de instalacion de Antigravity](guia_instalacion_antigravity.md). Para este curso es necesario tener activado **Science Skills**.

## 1. Clonar el repositorio

```bash
git clone https://github.com/davinson-pezo/curso-ia-gcms.git
cd curso-ia-gcms
```

## 2. Crear entorno Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Generar datos sinteticos

```bash
python scripts/generar_datos_sinteticos.py
```

El script crea:

```text
recursos/datos-sinteticos/gcms_features_sinteticas.csv
```

## 4. Abrir la presentacion

Abre:

```text
output/presentations/index.html
```

Controles de la presentacion:

- Flecha derecha o espacio: siguiente slide.
- Flecha izquierda: slide anterior.
- Home: primera slide.
- End: ultima slide.
