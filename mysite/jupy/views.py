from django.shortcuts import render


def index(request):
    template_path = "index.html"
    return render(request, template_path, {})
