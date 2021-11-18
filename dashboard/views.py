from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from dashboard.forms import FormularioBusqueda
from dashboard.models import Data

def home(request):

    return render(request,"home.html")

def estadisticas(request):
        
    busqueda = Data.objects.all()[:5]
    print(busqueda[0].navegador)
    
    return render(request, "estadisticas.html",busqueda[0].navegador)



def graficos(request):

    return render(request, "graficos.html")

def busqueda(request):

    if request.method=="POST":
        formulario=FormularioBusqueda(request.POST)
        if formulario.is_valid():
            infForm=formulario.cleaned_data
            busqueda=Data.objects.filter(mensaje_usuario__icontains=infForm["entrada"])
            print(busqueda)
        else:
            print("error")

    else:
        formulario=FormularioBusqueda()


    return render(request, "busqueda.html", {"form":formulario}) 


# Create your views here.
