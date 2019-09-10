from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import pregunta, respuesta

admin.site.register(pregunta)
admin.site.register(respuesta)