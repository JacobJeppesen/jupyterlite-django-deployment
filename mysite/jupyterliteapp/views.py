from django.shortcuts import render


def index(request):
    template_path = "index.html"
    context = {}
    return render(request, template_path, context)
