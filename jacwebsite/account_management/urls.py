from django.urls import path, include

from .views import connectionpage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', connectionpage, name="connection page"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
