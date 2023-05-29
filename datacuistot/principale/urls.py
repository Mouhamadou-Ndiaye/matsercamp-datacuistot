from . import views
from django.urls import path

urlpatterns = [
    path("", views.findyourfood),
    path("connexion/", views.connexion),
    path("inscription/",views.inscription),
    path("apropos", views.apropos)
]
