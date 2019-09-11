from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bienvenidos a Django")

def consulta(request):
    return HttpResponse("Estás en el módulo de consulta")

def proveedores(request):
    return HttpResponse("Bienvenido al mundo de proveedores")

def detalles(request, detalle_id):
    return HttpResponse("El detalle es %s" % detalle_id)

def respuestas(request, pregunta_id):
    response = "El Detalle es %s"
    return HttpResponse(response % pregunta_id)

def respuestas2(request, pregunta_id):
    response = "El Detalle es %s"
    return HttpResponse(response % pregunta_id)

def preguntas(request):
    lista_preguntas=pregunta.objects.order_by('-fecha_publicacion')[:3]
    template = loader.get_template('index.html')
    context = {'lista_preguntas_ct': lista_preguntas}
    return HttpResponse(template.render(context, request))