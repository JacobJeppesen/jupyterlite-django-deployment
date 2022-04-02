from django.conf import settings
from django.conf.urls.static import static

# From https://docs.djangoproject.com/en/4.0/howto/static-files/#serving-static-files-during-development
urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
