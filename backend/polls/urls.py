"""URLs for the app."""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("greet", views.greet, name="greet"),
    path("logging", views.test_logs, name="test_logs")
]
