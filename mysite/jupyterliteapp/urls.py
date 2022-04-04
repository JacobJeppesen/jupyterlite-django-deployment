from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

# From https://docs.djangoproject.com/en/4.0/howto/static-files/#serving-static-files-during-development
urlpatterns = [
    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
