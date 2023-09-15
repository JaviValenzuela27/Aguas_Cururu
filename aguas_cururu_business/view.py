from django.http import HttpResponse
import datetime

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
