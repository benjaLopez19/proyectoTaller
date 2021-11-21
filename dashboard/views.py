from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from dashboard.forms import FormularioBusqueda
from dashboard.models import Data
from django.utils.html import strip_tags
import json
from datetime import datetime


def home(request):

    return render(request,"home.html")

#=========================================================================================
#==============================ESTADISTICAS===============================================
#=========================================================================================

def estadisticas(request):
        
    busqueda = Data.objects.all()
    confianza = [6]
    suma = 0
    #=====================================================================================confianza
    i=0
    contador=0
    #=========================================================================================PALABRAS MAS BUSCADAS VARIABLES
    palabras = [{"0":0}]
    masrepetidas = [6]
    aux = []

    while i < 10:
     
        confianza.append(busqueda[i].confidence)            #agregar elementos al arreglo
        if isinstance(confianza[i],float):
            suma = suma + confianza[i]              #promedio
            contador+=1
        i+=1
        
        buffer = busqueda[i].mensaje_usuario
        aux = buffer.split()                                        #arreglo donde estan todas las palabras
    
        """     
        j=0   
        while j < len(aux):
            
            if palabras.__contains__(aux[j]):
                palabras[aux[j]] += 1   
            else:
                palabras[aux[j]] = 0
            
        j+=1

    print(palabras)
        """ 
    promedio = suma/contador
    

    #=========================================================================================PALABRAS MAS BUSCADAS


    return render(request, "estadisticas.html",{"confianza":promedio})

#=========================================================================================
#==============================GRAFICOS===================================================
#=========================================================================================
def graficos(request):

    busqueda = Data.objects.all()

    #==  INTENT  ==
    palabras=[]
    numeros=[]

    for i in range(500):
        intent=busqueda[i].intent

        if intent is None :
            continue

        if len(palabras)==0  :
            palabras.append(intent)
            numeros.append(1)
            continue
        
        if intent in palabras:
            index=palabras.index(intent)
            numeros[index]=numeros[index] +1
        else :
            palabras.append(intent)
            numeros.append(1)
        
    print("------------ LISTA -----------")
    print("largo intents:",len(palabras))

    js_data1 = json.dumps(palabras)
    js_data2 = json.dumps(numeros)

    #== FECHA ==
    fechas =[]
    palabrasF=[]
    numerosF=[]
    i=0
    k=0

    for i in range(500):
        date=busqueda[i].fecha.strftime("%d-%m-%Y")

        if date is None :
            continue

        if len(palabrasF)==0  :
            palabrasF.append(date)
            numerosF.append(1)
            continue
        
        if date in palabrasF:
            index=palabrasF.index(date)
            numerosF[index]=numerosF[index] +1
        else :
            palabrasF.append(date)
            numerosF.append(1)


    print("------------ LISTA -----------")
    print("largo fechas:",len(palabrasF))

    js_dataF1 = json.dumps(palabrasF)
    js_dataF2 = json.dumps(numerosF)

    #== RETURN ==
    return render(request, "graficos.html", {"data1": js_data1,"data2": js_data2,"dataF1": js_dataF1,"dataF2": js_dataF2})

#=========================================================================================
#==============================BUSQUEDA===================================================
#=========================================================================================
def busqueda(request):

    if request.method=="POST":
        formulario=FormularioBusqueda(request.POST)
        if formulario.is_valid():
            infForm=formulario.cleaned_data
            if infForm["esRespuesta"] == False:
                busqueda=Data.objects.filter(mensaje_usuario__icontains=infForm["entrada"])[:100]
            else:
                busqueda=Data.objects.filter(respuesta_bot__icontains=infForm["entrada"])[:50]
            if not busqueda:
                return render(request, "busqueda.html", {"form":formulario,"noHayResultados":"No se encontraron resultados"})
            else:
                return render(request, "busqueda.html", {"form":formulario,"busqueda":busqueda})
    else:
        formulario=FormularioBusqueda()
        return render(request, "busqueda.html", {"form":formulario})

def convContext(request, id):
    if id:
        print('if')
        busqueda=Data.objects.filter(conversation_id__icontains=id).order_by("fecha")
        print(busqueda)
        if not busqueda:
            return render(request,"conversacion.html",{"error":"No hubo resultados"})
        else:
            return render(request, "conversacion.html", {"busqueda": busqueda})

    

    return render(request, "busqueda.html", {"form":formulario}) 


# Create your views here.
