from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.newPage, name="newpage"),
    path("random", views.random, name="random"),
    path("edit", views.edit, name="edit"),
    path("<str:title>", views.greet, name="greet"),
    
]
