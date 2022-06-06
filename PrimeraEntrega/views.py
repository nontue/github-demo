from django.template import Template, Context
from django.template import loader
from django.http import HttpResponse
from datetime import datetime

def saludo(request):
	return HttpResponse('Hola Django - Coder')

def diaDeHoy(request):
    dia = datetime.now()
    documentoDeTexto = f'Hoy es: <br> {dia}'

    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f'Mi nombres es: <br><br> {nombre}'
    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):

    nom = 'nombre'
    ap = 'apellido'
    listaDeNotas = [2,2,3,7,2,5]
    diccionario = {'nombre':nom, 'apellido':ap, 'hoy':datetime.now(), 'notas':listaDeNotas}

  #  miHtml = open(r'C:/Users/Usuario/Documents/CoderHouse/Python/django/PrimeraEntrega/PrimeraEntrega/templates/template1.html')

   # plantilla = Template(miHtml.read())

    #miHtml.close()

    #miContexto = Context(diccionario)
    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
