from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage_met, name = "mainpage_met"),
]