from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    DetailView,
    View,
)

from .forms import (
    JugadorRegisterForm,
)
#

from .models import (
    Jugador,
    País,
    Posición,
)

"""views de jugador"""

class RegistrarJugador(CreateView):
    template_name = 'jugador/registrar.html'
    model = Jugador
    form_class = JugadorRegisterForm
    success_url = reverse_lazy('jugador_app:jugadores')
    
     
    

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
    success_url = reverse_lazy('jugador_app:jugadores')


class JugadorListView(ListView):
    template_name = "jugador/list-jugador.html"
    context_object_name = 'jugadores'
    
    def get_queryset(self):
        return Jugador.objects.all()    
 
 
class JugadorSalario(ListView):
    template_name = "jugador/sueldo-jugador.html"
    context_object_name = 'salarios'
    
    def get_queryset(self):
        return Jugador.objects.all()
   
   
class SueldoBajo(ListView):
    template_name = "jugador/sueldo-menor.html"
    context_object_name = 'jugadores'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Jugador.objects.sueldobajo(palabra_clave)
    
    
class SueldoAlto(ListView):
    template_name = "jugador/sueldo-alto.html"
    context_object_name = 'jugadores'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Jugador.objects.sueldoalto(palabra_clave)
    

class SueldoDif(ListView):
    template_name = "jugador/diferencia.html"
    context_object_name = 'jugadores'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Jugador.objects.Diferencia(palabra_clave)
        

class ListJugadorByKword(ListView):
    """lista jugadores por palabra clave"""
    template_name = 'jugador/by_kword.html'
    context_object_name = 'jugadores'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        lista = Jugador.objects.filter(
            sueldo = palabra_clave
        )
        return lista

 
class JugadorDetail(DetailView):
    model = Jugador
    template_name = "jugador/detail_jugador.html"
 
    
class JugadorDeleteView(DeleteView):
    template_name = "jugador/del-jugador.html"
    model = Jugador
    success_url = 'list.jugador/' 

       

"""views de país"""    
    
class AgregarPaís(CreateView):
    template_name = 'país/regist-país.html'
    model = País
    fields = ('__all__')
    success_url = 'list-país/'    
    
    
class PaísList(ListView):
    template_name = "país/list-país.html"
    context_object_name = 'país'
    
    def get_queryset(self):
        return País.objects.all()   
    
class PaísJoin(ListView):
    template_name = "país/join-país.html"
    context_object_name = 'países'
    
    def get_queryset(self):
        país_join = País.objects.select_related().all()
        return país_join    

"""views de posición"""    
    
class PosiciónView(CreateView):
    template_name = "posición/puesto.html" 
    model = Posición      
    fields = ('__all__')
    success_url = reverse_lazy('jugador_app:posiciones')
    
    
class PosiciónList(ListView):
    template_name = "posición/list-posición.html"
    context_object_name = 'posiciones'
    
    def get_queryset(self):
        return Posición.objects.all() 
     
     
class PosiciónDelete(DeleteView):
    template_name = "posición/del-puesto.html"
    model = Jugador
    success_url = 'list.jugador/'