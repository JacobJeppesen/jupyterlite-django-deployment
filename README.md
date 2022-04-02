# Minimal JupyterLite deployment with Django
A minimal example of deploying Jupyter Lite with Django.

## Installation
Navitate to the root of the project and run the following commands:
```bash
conda create -n jupyterlite-django python=3.10 --yes
conda activate jupyterlite-django
pip install -r requirements.txt
python mysite/manage.py runserver  
```

Then open the browser and go to http://localhost:8000/. If it does not work, and you want to make sure Django is running properly, check that http://localhost:8000/admin/ works.

## Re-build the JupyterLite static files 
Run the following commands to rebuild the JupyterLite static files:

```bash
cd mysite/jupy/static/assets
jupyter lite build --output-dir jupydist
```