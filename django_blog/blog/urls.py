from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name = 'index'),
    path('critica/',critica, name = 'critica'),
    path('estrenos/',estrenos, name = 'estrenos'),
    path('internacional/',internacional, name = 'internacional'),
    path('animacion/',animacion, name = 'animacion'),
    path('clasico/',clasico, name = 'clasico'),
    path('<slug:slug>/',detallePost, name = 'detalle_post'),
    ]