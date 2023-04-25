from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("teachers/", views.teachers, name="teachers"),
    path("generate-teachers/", views.generate_teachers, name="generate_teachers"),
]
