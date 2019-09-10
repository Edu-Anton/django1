from django.db import models

# Create your models here.

class pregunta(models.Model):
    pregunta_text = models.CharField(max_length=200)
    fecha_publicacion = models.DateField('Fecha de Publicación')

class respuesta(models.Model):
    pregunta = models.ForeignKey(pregunta, on_delete=models.CASCADE)
    respuesta_text = models.CharField(max_length=200)
    voto = models.IntegerField(default = 0)