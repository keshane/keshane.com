from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects, name="projects"),
    path("sudoku", views.sudoku, name="sudoku"),
]