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
    contador=0
    while i < 2000:
     
        confianza.append(busqueda[i].confidence)            #agregar elementos al arreglo
        if isinstance(confianza[i],float):
            suma = suma + confianza[i]              #promedio
            contador+=1
        i+=1

    promedio = suma/contador
    print(promedio)

    #=========================================================================================calificacion 

    


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

        palabras.append(intents[k].get("intent"))
        numeros.append(intents[k].get("cantidad"))
        k+=1

    print("largo",len(intents))


    #=========================================================================================FECHA
    

    return render(request, "graficos.html",{"intents":palabras, "cantidad":numeros})

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
