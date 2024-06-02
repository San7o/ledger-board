"""URL Configuration for the greet app."""
from django.urls import path
from sender.views.greet import greet
from sender.views.send_data import send_data

urlpatterns = [
    path("greet", greet, name="greet"),
    path("send", send_data, name="send_data"),
]
