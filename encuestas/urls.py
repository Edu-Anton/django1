from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('consulta/', views.consulta),
    path('proveedores/', views.proveedores),
    path('<int: pregunta_id>/', views.respuestas, name="respuestas"),
    path('<int:pregunta_id>/ruta2/', views.respuestas2, name="respuestas2")
]