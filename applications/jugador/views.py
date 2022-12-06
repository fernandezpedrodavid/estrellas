from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    UpdateView,
    ListView,
)

from django.views.generic.edit import(
    FormView
)

from .forms import (
    JugadorRegisterForm,
)
#

from .models import Jugador

"""views de jugador"""

class RegistrarJugador(FormView):
    template_name = 'jugador/registrar.html'
    form_class =  JugadorRegisterForm
    #success_url = reverse_lazy('jugador_app:lista-jugador')
    
    def form_valid(self, form):
        
        Jugador.objects.create_user(
            form.cleaned_data['fecha_nacimiento'],
            form.cleaned_data['dni'],
            form.cleaned_data['sueldo'],
            nombre=form.cleaned_data['nombre'],
            apellido=form.cleaned_data['apellido'],
            
        )  
        return super(RegistrarJugador, self).form_valid(form)

class JugadorUpView(UpdateView):
    template_name = "jugador/mod-jugador.html"
    model = Jugador
    fields = [
        'nombre',
        'apellido',
        'fecha_nacimiento',
        'dni',
        'sueldo',
    ]
    #success_url = '/lista/jugador/'

class JugadorListView(ListView):
    template_name = "jugador/list-jugador.html"
    context_object_name = 'jugadores'
    
    def get_queryset(self):
        return Jugador.objects.all()    

"""views de país"""    
    
#class PaísView(TemplateView):
    #template_name = "país/país.html"

"""views de posición"""    
    
#class PosiciónView(TemplateView):
    #template_name = "posición/puesto.html"       


