from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def home(request):

    return render(request,"home.html")

def estadisticas(request):

    return render(request, "estadisticas.html")

def graficos(request):

    return render(request, "graficos.html")

def busqueda(request):

    return render(request, "busqueda.html")


# Create your views here.
