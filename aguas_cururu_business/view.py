import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

# httpRequest: Realiza periciones al servidor.
# httpResponse: Pare enviar la respuesta al servidor usando protocolo http


# Esto es una vista
def bienvenida(request):  # Se pasa objeto tipo request como primer argumento
    return HttpResponse("Bienvenido al sistema")


# Esto es una vista utilizando css
def bienvenidaRojo(request):  # Se pasa objeto tipo request como primer argumento
    return HttpResponse("<p style='color:red'>Bienvenido al sistema :) <p>")


def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "tercerda edad"
        else:
            categoria = "adultez"
    else:
        if edad < 10:
            categoria = "infancia"
        else:
            categoria = "adolescencia"
    resultado = "<h1>Categoria de la edad: %s</h1>" % categoria
    return HttpResponse(resultado)


def obtenerMomentoActual(request):
    # respuesta = "<h1>Momento actual: {0}</h1>".format(
    #     datetime.datetime.now())
    respuesta = "<h1>Momento actual: {0}</h1>".format(
        datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(respuesta)


def contenidoHTML(request, nombre, edad):
    # No es la forma adecuada de hacerlo
    contenido = """
    <html>
    <body>
    <p>Nombre %s / Edad: %s</p>
    </body>
    </html>
    """ % (nombre, edad)
    return HttpResponse(contenido)


def miPrimeraPlantilla(request):
    # Abrir el documento que contiene a la plantilla
    plantillaExterna = open(
        "C:/Users/janto/Documents/PROYECTO_AGUAS CURURU/aguas_cururu_business/templates/plantilla.html")
    # Cargar el documento en una variable de tipo plantilla
    template = Template(plantillaExterna.read())
    # Cerrar el documento externo que se ha abierto
    plantillaExterna.close()
    # Crear un contexto
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)


def plantillaParametros(request):
    nombre = "Javier Antonio Valenzuela Velasquez"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "JavaScript", "Java", "C#", "Kotlin"]
    # Abrir el documento que contiene a la plantilla (No es la mejor practica)
    plantillaExterna = open(
        "C:/Users/janto/Documents/PROYECTO_AGUAS CURURU/aguas_cururu_business/templates/plantilla_parametros.html")
    # Cargar el documento en una variable de tipo plantilla
    template = Template(plantillaExterna.read())
    # Cerrar el documento externo que se ha abierto
    plantillaExterna.close()
    # Crear un contexto
    contexto = Context(
        {"nombrePersonal": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
    documento = template.render(contexto)
    return HttpResponse(documento)


def plantillaLoader(request):
    nombre = "Javier Antonio Valenzuela Velasquez"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "JavaScript", "Java", "C#", "Kotlin", "PHP"]
    # Configurar ruta completa en  DIRS perteneciente a settings.py
    plantillaExterna = loader.get_template('plantilla_parametros.html')
    # Renderizar el documento que se va a retornar
    documento = plantillaExterna.render(
        {"nombrePersonal": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
    return HttpResponse(documento)


def plantillaShortcut(request):
    nombre = "Javier Antonio Valenzuela Velasquez"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "C++",
                 "JavaScript", "Java", "C#", "Kotlin", "PHP"]
    return render(request, 'plantilla_parametros.html', {"nombrePersonal": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})


def plantillaHija1(request):
    return render(request, "plantilla_hija1.html", {})


def plantillaHija2(request):
    return render(request, "plantilla_hija2.html", {})
