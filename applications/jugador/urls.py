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
    path(
        'sueldo-jugador/',
        views.JugadorSalario.as_view(),
        name='sueldos'
    ),
    path(
        'aumento/10/<pk>/',
        views.JugadorUp10.as_view(),
        name='diez'
    ),
    path(
        'aumento/15/<pk>/',
        views.JugadorUp15.as_view(),
        name='quince'
    ),
    path(
        'aumento/20/<pk>/',
        views.JugadorUp20.as_view(),
        name='veinte'
    ),
    path(
        'sueldo/anual/',
        views.SueldoAnual.as_view(),
        name='sueldoanual'
    ),
    path(
        'sueldo/menor/',
        views.SueldoMenor.as_view(),
        name='sueldobajo'
    ),
    path(
        'sueldo/mayor/',
        views.SueldoMayor.as_view(),
        name='sueldoalto'
    ),
    path(
        'diferencia/',
        views.SueldoDif.as_view(),
        name='sueldo-dif'
    ),
    path(
        'sueldo-prom/',
        views.SueldoPromedio.as_view(),
        name='promedio'
    ),
    path(
        'num-jugadores/',
        views.NumJugadores.as_view(),
        name='cantidad'
    ),
    path(
        'leer-registro/',
        views.Registro.as_view(),
        name='leer'
    ),
    path(
        'edad-actual/',
        views.Edades.as_view(),
        name='edad'
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
    path(
        'list-posición/',
        views.PosiciónList.as_view(),
        name='posiciones'
    ),
    path(
        'del-posición/<pk>',
        views.PosiciónDelete.as_view(),
        name='del-puesto'
    ),
             
]
