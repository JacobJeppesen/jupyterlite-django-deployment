# Minimal JupyterLite deployment with Django
A minimal example of deploying Jupyter Lite with Django.

## Installation
```bash
conda create -n jupyterlite-django python=3.10
conda activate jupyterlite-django
pip install -r requirements.txt

```

## Re-build the JupyterLite static files 
Run the following commands to rebuild the JupyterLite static files:

```bash
cd mysite/jupy/static/assets
jupyter lite build --output-dir dist 
```