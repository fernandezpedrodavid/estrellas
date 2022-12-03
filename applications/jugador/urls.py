from django.contrib import admin
from django.urls import path

from . import views
    
app_name = 'jugador_app'

#urls para jugador
urlpatterns = [
    path(
        'jugador/',
        views.JugadorView.as_view(),
        name='jugador'
    ),
     
#urls para país
    path(
        'país/',
        views.PaísView.as_view(),
        name='país'
    ),  
    
#urls para posición
    path(
        'puesto/',
        views.PosiciónView.as_view(),
        name='posición'
    ),       
]
