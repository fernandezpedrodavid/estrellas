from django.shortcuts import render

from django.views.generic import (
    TemplateView,
)

"""views de jugador"""

class JugadorView(TemplateView):
    template_name = "jugador/juego.html"

"""views de país"""    
    
class PaísView(TemplateView):
    template_name = "país/país.html"

"""views de posición"""    
    
class PosiciónView(TemplateView):
    template_name = "posición/puesto.html"       


