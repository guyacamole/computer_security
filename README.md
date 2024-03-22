## Project Setup

This project requires Python 3.6 or later. Here are the steps to set up the project:

1. Create a virtual environment:

```bash
python3 -m venv .venv
```

2. Activate the virtual environment:

On Linux or MacOS:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.\venv\Scripts\activate
```

3. Install the required libraries:

```bash
pip install python-docx openpyxl PyPDF2
```

4. Run the proyect

On Linux or MacOS:

```bash
python3 main.py
```

On Windows:

```bash
py main.py
```

## Code Explanation

El script `main.py` esta disenado para extraer metadatos de archivos en una ruta especificada. Los archivos objetivo son: `.docx`, `.xlsx`, y `.pdf`.

La funcion `extract_metadata(file_path)` es la que se encarga de extraer la metadata e imprimirla. primero obtiene la extension del los archivos  y despues usa la libreria adecuada para ectraer la metadata de cada tipo de archivo.

La funcion  `main()` pregunta a el usuario el path o directorio de de donde se obtendran los archivos, despues busca todos los archivos contenidos en el y llama a la funcion `extract_metadata(file_path)` para cada archivo.
