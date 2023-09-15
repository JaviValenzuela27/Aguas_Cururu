from django.http import HttpResponse

# httpRequest: Realiza periciones al servidor.
# httpResponse: Pare enviar la respuesta al servidor usando protocolo http


# Esto es una vista
def bienvenida(request):  # Se pasa objeto tipo request como primer argumento
    return HttpResponse("Bienvenido al sistema")


# Esto es una vista utilizando css
def bienvenidaRojo(request):  # Se pasa objeto tipo request como primer argumento
    return HttpResponse("<p style='color:red'>Bienvenido al sistema :) <p>")
