from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bienvenidos a Django")

def consulta(request):
    return HttpResponse("Estás en el módulo de consulta")