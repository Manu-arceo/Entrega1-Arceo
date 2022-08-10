from django.urls import path
from turismoBahia.views import *

urlpatterns = [
    path("", index, name="inicio"),
    path("museos", museos, name="museos"),
    path("centroHistorico", centroHistorico, name="centroHistorico"),
    path("parques", parques, name="parques"),
    path("museos/crear/", crear_museo, name="crear_museo"),

]