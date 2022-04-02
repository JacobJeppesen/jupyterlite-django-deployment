# Minimal JupyterLite deployment with Django
A minimal example of deploying Jupyter Lite with Django.

The important paths in the projects are: 
```
└── mysite                          
    ├── manage.py                   <- Django management script
    ├── mysite                      
    │   └── settings.py             <- Settings for the Django project
    └── jupyterliteapp              
        ├── urls.py                 <- URL configuration for the Jupyter Lite app
        ├── content                 <- Contents for the JupyterLite app
        └── static                  
            └── jupyter             <- The static files for the JupyterLite app
```

## Installation
Navigate to the root of the project and run the following commands:
```bash
conda create -n jupyterlite-django python=3.10 --yes
conda activate jupyterlite-django
pip install -r requirements.txt
python mysite/manage.py collectstatic
python mysite/manage.py runserver  
```

Then open the browser and go to http://localhost:8000/static/jupyter/index.html. If it does not work, and you want to make sure Django is running properly, check that http://localhost:8000/admin/ works.

## Re-build the JupyterLite static files 
Run the following commands to rebuild the JupyterLite static files:

```bash
cd mysite/jupyterliteapp
jupyter lite build --output-dir static/jupyter --contents content && rm .jupyterlite.doit.db
```