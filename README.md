# Minimal JupyterLite deployment with Django
This is a minimal deployment of JupyterLite with Django. It contains a Django app, named `jupyterliteapp`, with examples and the static files needed to run JupyterLite. The URL to the collected static files in Django has been re-named to `public/`, such that the URL to JupyterLite is `/public/jupyter/index.html`. The important paths in the project are: 
```
└── mysite                          
    ├── manage.py                   <- Django management script
    ├── mysite                      
    │   └── settings.py             <- Settings for the Django project
    └── jupyterliteapp              
        ├── urls.py                 <- URL configuration for the JupyterLite app
        ├── contents                <- Contents for the JupyterLite app (i.e., sample noteoboks)
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

Then open the browser and go to http://localhost:8000/public/jupyter/index.html. If it does not work, and you want to make sure Django is running properly, check that http://localhost:8000/admin/ works.

## Rebuild the JupyterLite static files 
Run the following commands to rebuild the JupyterLite static files:

```bash
cd mysite/jupyterliteapp
jupyter lite build --output-dir static/jupyter --contents contents
```