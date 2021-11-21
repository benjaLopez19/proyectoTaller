from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from dashboard.forms import FormularioBusqueda
from dashboard.models import Data
from django.utils.html import strip_tags
import json


def home(request):

    return render(request,"home.html")

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



def graficos(request):
    #=========================================================================================INTENT
    busqueda = Data.objects.all()
    intents =[]
    palabras=[]
    numeros=[]

    i=0
    k=0
    while i < 200:
        if busqueda[i].intent==None :
            next

        if i==0 : 
            diccionario ={"intent":busqueda[i].intent,"cantidad":1}
            intents.append(diccionario) #agregar primer elemento al arreglo

        res = next((sub for sub in intents if sub['intent'] == busqueda[i].intent), None)
        if res == None:
            diccionario ={"intent":busqueda[i].intent,"cantidad":1}
            intents.append(diccionario)
        else   :
            index = next((index for (index, d) in enumerate(intents) if d["intent"] == busqueda[i].intent), None)
            num=res.get("cantidad")
            num+=1
            intents[index].update({"cantidad":num})

        i+=1

    print("------------ LISTA -----------")
    while k<len(intents):
        print(intents)
        palabras.append(intents[k].get("intent"))
        numeros.append(intents[k].get("cantidad"))
        k+=1

    print("largo",len(intents))


    #=========================================================================================FECHA
    

    js_data1 = json.dumps(palabras)
    js_data2 = json.dumps(numeros)
    return render(request, "graficos.html", {"data1": js_data1,"data2": js_data2})


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
