from django.urls import path, include
from .views import homepage_blog

urlpatterns = [
    path('', homepage_blog , name="home page blog"),
]
