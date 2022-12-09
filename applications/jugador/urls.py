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
    path(
        'del.jugador/<pk>',
        views.JugadorDeleteView.as_view(),
        name='del-jugador'
    ),
    path(
        'buscar-jugador/',
        views.ListJugadorByKword.as_view(),
        name='jugadorxnombre'
    ),
    path(
        'detail-jugador/<pk>/',
        views.JugadorDetail.as_view(),
        name='jugadordetail'
    ),
     
#urls para país
    path(
        'add-país/',
        views.AgregarPaís.as_view(),
        name='agr_país'
    ),
    path(
        'list-país/',
        views.PaísList.as_view(),
        name='list_país'
    ),
    path(
        'join-país/',
        views.PaísJoin.as_view(),
        name='join_país'
    ),
    
#urls para posición
    path(
        'add-posición/',
        views.PosiciónView.as_view(),
        name='agr_puesto'
    ),
             
]
