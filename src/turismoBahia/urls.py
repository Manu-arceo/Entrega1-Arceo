from django.urls import path
from turismoBahia.views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", index, name="inicio"),
    path("museos", museos, name="museos"),
    path("centroHistorico", centroHistorico, name="centroHistorico"),
    path("parques", parques, name="parques"),
    path("museos/crear/", crear_museo, name="crear_museo"),

    path("login/", iniciar_sesion, name="iniciar_sesion"),
    path("register/",registrar_usuario, name="registrarse" ),
    path("logout/", LogoutView.as_view(template_name="turismoBahia/logout.html"), name="logout" )

]