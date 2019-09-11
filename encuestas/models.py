from django.db import models

# Create your models here.

class pregunta(models.Model):
    pregunta_text = models.CharField(max_length=200)
    fecha_publicacion = models.DateField('Fecha de Publicación')

class respuesta(models.Model):
    pregunta = models.ForeignKey(pregunta, on_delete=models.CASCADE)
    respuesta_text = models.CharField(max_length=200)
    voto = models.IntegerField(default = 0)

class usuario(models.Model):
    nombre = models.CharField(max_length=200)
    usuario = models.CharField(max_length=100)
    clave = models.CharField(max_length=30)