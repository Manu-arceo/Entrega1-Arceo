from django.forms import Form, IntegerField, CharField, EmailField


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