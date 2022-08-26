
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from turismoBahia.models import Museos, CentroHistorico, Parques
from turismoBahia.forms import MuseoFormulario, FormularioBusqueda, CentroHistorioFormulario, ParqueFormulario

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from turismoBahia.forms import CreacionUsuarios


from django.contrib.auth.mixins import LoginRequiredMixin
from  django.contrib.auth.decorators import login_required





# Create your views here.


def index(request):


    return render(request, "turismoBahia/index.html")
@login_required
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


@login_required
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

    
@login_required
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




def iniciar_sesion(request):
    if request.method =="GET":
        formulario = AuthenticationForm()

        context = {
            "form": formulario
        }
        return render(request, "turismoBahia/login.html", context)

    else:
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data

            usuario = authenticate(username=data.get("username"), password=data.get("password"))
            if usuario is not None:
                login(request,usuario)

                return redirect("inicio")
            else:
                context = {
                    "error": "Error en la autentificacion",
                    "form": formulario
                }  

                return render(request, "turismoBahia/login.html", context)
        else:
            context = {
                "error":"Datos no validos",
                "form": formulario
                } 
            return render(request,"turismoBahia/login.html", context)         

def registrar_usuario(request):
    if request.method == "GET":
        formulario = CreacionUsuarios()
        return render(request, "turismoBahia/registros.html", {"form": formulario})
    else:
        formulario = CreacionUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")

        else:
            context = {
                "error": "Datos no validos",
                "form": formulario
            }
            return render(request, "turismoBahia/registros.html", context)        
