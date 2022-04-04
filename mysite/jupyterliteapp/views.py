from django.http import HttpResponse


def index(request):
    message = "You're at the main page. Go to <a href='http://localhost:8000/public/jupyter/index.html'>" \
              "http://localhost:8000/public/jupyter/index.html</a> to test JupyterLite."
    return HttpResponse(message)
