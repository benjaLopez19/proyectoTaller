from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from dashboard.forms import FormularioBusqueda
from dashboard.models import Data



def home(request):

    return render(request,"home.html")

def estadisticas(request):
        
    busqueda = Data.objects.all()
    confianza = []
    suma = 0
    #=====================================================================================confianza
    i=0

    while i < 2000:
     
        confianza.append(busqueda[i].confidence) 
        print(confianza[i])

        i+=1


    #=========================================================================================calificacion 



    return render(request, "estadisticas.html",{"confianza":confianza})



def graficos(request):

    return render(request, "graficos.html")

def busqueda(request):

    if request.method=="POST":
        formulario=FormularioBusqueda(request.POST)
        if formulario.is_valid():
            infForm=formulario.cleaned_data
            if infForm["esRespuesta"] == False:
                busqueda=Data.objects.filter(mensaje_usuario__icontains=infForm["entrada"])
            else:
                busqueda=Data.objects.filter(respuesta_bot__icontains=infForm["entrada"])
            print(busqueda[30].id)
        else:
            print("error")

    else:
        formulario=FormularioBusqueda()


    return render(request, "busqueda.html", {"form":formulario}) 


# Create your views here.
