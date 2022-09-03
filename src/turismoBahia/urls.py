from django.urls import path
from turismoBahia.views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", index, name="inicio"),
    path("museos", museos, name="museos"),
    path("centroHistorico", centroHistorico, name="centroHistorico"),
    path("parques", parques, name="parques"),
    path("parques/borrar/<id_parques>", borrar_parque, name="borrar_parque"),
    path("museos/crear", MuseosCreate.as_view(), name = "museos_create"),
 

    path("login/", iniciar_sesion, name="iniciar_sesion"),
    path("register/",registrar_usuario, name="registrarse" ),
    path("logout/", LogoutView.as_view(template_name="turismoBahia/autentificacion/logout.html"), name="logout" ),
    path("edit/", actulizar_usuario, name="actualizar_usuario"),
    path("avatar/", crear_avatar, name="añadir_avatar")
]