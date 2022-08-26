from dataclasses import fields
from django.forms import Form, IntegerField, CharField, EmailField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MuseoFormulario(Form):

    nombre = CharField()
    direccion = CharField()
    
class CentroHistorioFormulario(Form):

    nombre = CharField()
    direccion = CharField()
    
class ParqueFormulario(Form):

    nombre = CharField()
    direccion = CharField()
    

class FormularioBusqueda(Form):
    nombre_museo = CharField(max_length=150)



class CreacionUsuarios(UserCreationForm):

    email = EmailField()
    password1 = CharField(label="Constraseña", widget=PasswordInput)
    password2 = CharField(label="Confirmar contraseña", widget=PasswordInput)

    class Meta: 
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {"username": "", "email": "", "password1": "","password2": "" }