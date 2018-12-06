from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mainpage_met(request):
    return render(request, "mainApp/Home.html")
