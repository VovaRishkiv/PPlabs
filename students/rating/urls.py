from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from rating.models import Rating
"""
urlpatterns = [
    path('', views.main, name = "main"),
]
"""
urlpatterns = [
    path('', ListView.as_view(queryset=Rating.objects.all().order_by("-mark"), template_name="rating/Homes.html")),
]