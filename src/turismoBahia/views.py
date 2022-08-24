from ast import For
from django.shortcuts import render
from django.http import HttpResponse
from turismoBahia.models import Museos, CentroHistorico, Parques
from turismoBahia.forms import MuseoFormulario, FormularioBusqueda, CentroHistorioFormulario, ParqueFormulario
# Create your views here.

def index(request):


    return render(request, "turismoBahia/index.html")

def museos(request):
   
    listado_museos = Museos.objects.all()

    if request.GET.get("nombre_museo"):

        formulario =FormularioBusqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_museos = Museos.objects.filter(nombre__icontains = data["nombre_museo"])

        return render(request, "turismoBahia/museos.html", {"museos": listado_museos, "formulario": formulario})
   
    else:  
         formulario = FormularioBusqueda() 
         return render(request, "turismoBahia/museos.html", {"museos": listado_museos, "formulario": formulario} )    



def centroHistorico(request):

    listado_centroHistoricos = CentroHistorico.objects.all()

    if request.method == "GET":
        formulario = CentroHistorioFormulario()

        context = {
            "centroHistoricos": listado_centroHistoricos,
            "formulario": formulario
        }
        return render(request,"turismoBahia/centroHistorico.html", context ) 

    else:
        
        formulario = CentroHistorioFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre = data.get("nombre")
            direccion = data.get("direccion")
            centroHistorico= CentroHistorico(nombre=nombre, direccion=direccion)

            centroHistorico.save()
            formulario = CentroHistorioFormulario()
            context = {
            "centroHistoricos": listado_centroHistoricos,
            "formulario": formulario
        }  

        return render(request,"turismoBahia/centroHistorico.html", context )

    

def parques(request):

    listado_parques = Parques.objects.all()

    if request.method == "GET":
        formulario = ParqueFormulario()

        context = {
            "parques":listado_parques,
            "formulario": formulario
        }
        return render(request, "turismoBahia/parques.html", context)

    else:
        formulario = ParqueFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre = data.get("nombre")
            direccion = data.get("direccion")
            parques= Parques(nombre=nombre, direccion=direccion)

            parques.save()
            formulario = ParqueFormulario()
            context = {
            "parques": listado_parques,
            "formulario": formulario
        }  

        return render(request,"turismoBahia/parques.html", context )

            



     



def crear_museo(request):
   
     if request.method == "GET":
        formulario = MuseoFormulario()
        return render(request, "turismoBahia/formulario.html", {"formulario": formulario})

     else:

        formulario = MuseoFormulario(request.POST)

        if formulario.is_valid(): 
            
            data = formulario.cleaned_data 
  
            nombre = data.get("nombre")
            direccion = data.get("direccion")
            museos = Museos(nombre=nombre, direccion=direccion)

            museos.save()
            formulario = MuseoFormulario()
            return render(request, "turismoBahia/index.html") 

        else: 
            return HttpResponse("El formulario no es valido")