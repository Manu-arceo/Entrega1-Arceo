
import email
from pyexpat import model
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from turismoBahia.models import Museos, CentroHistorico, Parques, Avatar
from turismoBahia.forms import MuseoFormulario, FormularioBusqueda, CentroHistorioFormulario, ParqueFormulario, UserEditForm, AvatarForm
from django.views.generic import CreateView


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from turismoBahia.forms import CreacionUsuarios


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


def index(request):

    context = {

    }
    if not request.user.is_anonymous:

        avatar = Avatar.objects.filter(usuario = request.user.id).last()
        context.update({"avatar":avatar})
          
    return render(request, "turismoBahia/index.html", context)


@login_required
def museos(request):

    listado_museos = Museos.objects.all()

    if request.GET.get("nombre_museo"):

        formulario = FormularioBusqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_museos = Museos.objects.filter(
                nombre__icontains=data["nombre_museo"])

        return render(request, "turismoBahia/museos/museos.html", {"museos": listado_museos, "formulario": formulario})

    else:
        formulario = FormularioBusqueda()
        return render(request, "turismoBahia/museos/museos.html", {"museos": listado_museos, "formulario": formulario})


@login_required
def centroHistorico(request):

    listado_centroHistoricos = CentroHistorico.objects.all()

    if request.method == "GET":
        formulario = CentroHistorioFormulario()

        context = {
            "centroHistoricos": listado_centroHistoricos,
            "formulario": formulario
        }
        return render(request, "turismoBahia/centroHistorico/centroHistorico.html", context)

    else:

        formulario = CentroHistorioFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre = data.get("nombre")
            direccion = data.get("direccion")
            centroHistorico = CentroHistorico(
                nombre=nombre, direccion=direccion)

            centroHistorico.save()
            formulario = CentroHistorioFormulario()
            context = {
                "centroHistoricos": listado_centroHistoricos,
                "formulario": formulario
            }

        return render(request, "turismoBahia/centroHistorico/centroHistorico.html", context)


@login_required
def parques(request):

    listado_parques = Parques.objects.all()

    if request.method == "GET":
        formulario = ParqueFormulario()

        context = {
            "parques": listado_parques,
            "formulario": formulario
        }
        return render(request, "turismoBahia/parques/parques.html", context)

    else:
        formulario = ParqueFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre = data.get("nombre")
            direccion = data.get("direccion")
            parques = Parques(nombre=nombre, direccion=direccion)

            parques.save()
            formulario = ParqueFormulario()
            context = {
                "parques": listado_parques,
                "formulario": formulario
            }

        return render(request, "turismoBahia/parques/parques.html", context)

@login_required
def borrar_parque(request, id_parques):
    try:
        parques = Parques.objects.get(id = id_parques)
        parques.delete()
        return redirect("parques")

    except:
        return redirect("inicio")   

class MuseosCreate(LoginRequiredMixin, CreateView):
    model = Museos
    success_url = "/turismoBahia/museos"
    fields = ["nombre","direccion", "entrada"]
    template_name = "turismoBahia/museos/museos_form.html"
  



def iniciar_sesion(request):
    if request.method == "GET":
        formulario = AuthenticationForm()

        context = {
            "form": formulario
        }
        return render(request, "turismoBahia/autentificacion/login.html", context)

    else:
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = authenticate(username=data.get(
                "username"), password=data.get("password"))
            if usuario is not None:
                login(request, usuario)

                return redirect("inicio")
            else:
                context = {
                    "error": "Error en la autentificacion",
                    "form": formulario
                }

                return render(request, "turismoBahia/autentificacion/login.html", context)
        else:
            context = {
                "error": "Datos no validos",
                "form": formulario
            }
            return render(request, "turismoBahia/autentificacion/login.html", context)


def registrar_usuario(request):
    if request.method == "GET":
        formulario = CreacionUsuarios()
        return render(request, "turismoBahia/autentificacion/registros.html", {"form": formulario})
    else:
        formulario = CreacionUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("iniciar_sesion")

        else:
            context = {
                "error": "Datos no validos",
                "form": formulario
            }
            return render(request, "turismoBahia/autentificacion/registros.html", context)


@login_required
def actulizar_usuario(request):

    if request.method == "GET":
        form = UserEditForm(initial={"email": request.user.email,
                            "first_name": request.user.first_name, "last_name": request.user.last_name})
        return render(request, "turismoBahia/autentificacion/actualizar_user.html", {"form": form})

    else:
        form = UserEditForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = request.user

            usuario.email = data.get("email")
            usuario.password1 = data.get("password1")
            usuario.password2 = data.get("password2")
            usuario.first_name = data.get("first_name")
            usuario.last_name = data.get("last_name")

            usuario.save()
            return redirect("inicio")

        else:
            return render(request,  "turismoBahia/autentificacion/actualizar_user.html", {"form": form})

@login_required
def crear_avatar(request):

    if request.method == "GET":
        form = AvatarForm()
        contexto = {"form": form}
        return render(request, "turismoBahia/autentificacion/añadir_avatar.html", contexto)

    else:
        form = AvatarForm(request.POST, request.FILES)    
        if form.is_valid():
            data = form.cleaned_data

            usuario = User.objects.filter(username=request.user.username).first()
            avatar = Avatar(usuario=usuario,imagen=data["imagen"])

            avatar.save()
            return redirect("actualizar_usuario")

        contexto = {"form": form}
        return render(request, "turismoBahia/autentificacion/añadir_avatar.html", contexto)
            