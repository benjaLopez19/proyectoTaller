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

    #-- variables confianza --
    confianza =0
    suma = 0
    contador=0
    #-- variables palabras --
    palabras = []
    masrepetidas = [6]
    aux = []
    auxPalabras=[]

    for i in range(1000):
        
        #== confianza ==
        confianza = busqueda[i].confidence              #-- 
        if isinstance(confianza,float):
            suma = suma + confianza                     #-- 
            contador+=1
        
        #== palabras mas usadas ==
        buffer = busqueda[i].mensaje_usuario
        aux = buffer.split()
        aux = removePalabras(aux)
        
        if aux is None :                     #-- si el intent vuelve vacio, pasa al siguiente
            continue
        
        if len(palabras)==0  :                  #-- si la lista esta vacia, ingresa el primer dato
            for j in aux:
                dict={'palabra':j,'numero':1}
                palabras.append(dict)
                auxPalabras.append(j)           #--auxpalabras se usa ya que palabras es un diccionario y es mas facil de buscar en una list
            continue
        
        for k in aux:
            if k in auxPalabras:                  #-- si la lista ya tiene un dato ingresado con el mismo intent, suma a la cantidad del intent
                index=auxPalabras.index(k)
                num=palabras[index].get("numero") +1
                palabras[index].update({"numero":num})
            else :                                  #-- si la lista no tiene un dato con este intent, se agrega a la lista
                dict={'palabra':k,'numero':1}
                palabras.append(dict)
                auxPalabras.append(k)
    #-- calcula promedio confianza --
    promedio = suma/contador
    promedio =promedio*100
    promedio = int(promedio)
    #--------------------------------
    

    #=========================================================================================PALABRAS MAS BUSCADAS
    print("----FINAL----")
    print(palabras)
    return render(request, "estadisticas.html",{"confianza":promedio,"palabras":palabras})

#=========================================================================================
#==============================GRAFICOS===================================================
#=========================================================================================
def graficos(request):

    busqueda = Data.objects.all()               #-- saco los datos de la DB

    palabras=[]                                 #--lista nombre intent
    numeros=[]                                  #--lista cantidad intent

    palabrasF=[]                                #-- lista nombre fecha
    numerosF=[]                                 #-- lista cantidad fecha

    for i in range(1000):

    #== intent ==
        intent=busqueda[i].intent               #-- asigna el intent a una variable

        if intent is None :                     #-- si el intent vuelve vacio, pasa al siguiente
            continue

        if len(palabras)==0  :                  #-- si la lista esta vacia, ingresa el primer dato
            palabras.append(intent)
            numeros.append(1)
            continue
        
        if intent in palabras:                  #-- si la lista ya tiene un dato ingresado con el mismo intent, suma a la cantidad del intent
            index=palabras.index(intent)
            numeros[index]=numeros[index] +1
        else :                                  #-- si la lista no tiene un dato con este intent, se agrega a la lista
            palabras.append(intent)
            numeros.append(1)

    #== FECHA ==
        date=busqueda[i].fecha.strftime("%d-%m-%Y")     #-- asigna la fecha a una variable

        if date is None :                       #si la fecha vuelve vacio, pasa al siguiente
            continue

        if len(palabrasF)==0  :                 #si la lista esta vacia, ingresa el primer dato
            palabrasF.append(date)
            numerosF.append(1)
            continue
        
        if date in palabrasF:                   #si la lista ya tiene un dato ingresado con la misma fecha, suma a la cantidad de la fecha
            index=palabrasF.index(date)
            numerosF[index]=numerosF[index] +1
        else :                                   #si la lista no tiene un dato con esta fecha, se agrega a la lista
            palabrasF.append(date)
            numerosF.append(1)


    #== Browser ==
        browser=busqueda[i].navegador
        
        print(browser)

    
    print("------------ LISTA -----------")
    print("largo intents:",len(palabras))
    print("largo fechas:",len(palabrasF))

    #== preparacion datos ==
    #-- se transforman las listas a json para que puedan ser leidas en javascript  --

    js_data1 = json.dumps(palabras)     #--json nombre intent
    js_data2 = json.dumps(numeros)      #--json cantidad intent

    js_dataF1 = json.dumps(palabrasF)   #--json nombre fecha
    js_dataF2 = json.dumps(numerosF)    #--json cantidad fecha

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

#=========================================================================================
#==============================CONVERSACION===============================================
#=========================================================================================

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

#=========================================================================================
#==============================FUNCIONES==================================================
#=========================================================================================

def removePalabras(aux):
    palabras=["en","con","si","la","y"]

    aux=[word for word in aux if word not in palabras]

    return aux