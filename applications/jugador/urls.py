from django.contrib import admin
from django.urls import path

from . import views
    
app_name = 'jugador_app'

#urls para jugador
urlpatterns = [
    path(
        'add.jugador/',
        views.RegistrarJugador.as_view(),
        name='registrar'
    ),
    path(
        'mod.jugador/<pk>/',
        views.JugadorUpView.as_view(),
        name='modificar'
    ),
    path(
        'list.jugador/',
        views.JugadorListView.as_view(),
        name='jugadores'
    ),
     
#urls para país
    
    
#urls para posición
          
]
