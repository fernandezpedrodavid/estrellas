import datetime
from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.db.models import Max, Min, Avg

from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    DetailView,
)
from django.db.models import Max, Min, Avg

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
#

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
    
    
class JugadorEdad(ListView):
    model = Jugador
    template_name = "jugador/edad-actual.html"
    context_object_name = 'jugadores'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edad_actual'] = [(jugador, jugador.edad()) for jugador in context['jugadores']]
        return context   
 
 
class JugadorSalario(ListView):
    template_name = "jugador/sueldo-jugador.html"
    context_object_name = 'salarios'
    
    def get_queryset(self):
        return Jugador.objects.all()
   
   
class SueldoBajo(ListView):
    model = Jugador
    template_name = "jugador/sueldo-bajo.html"
    context_object_name = 'menor'

    def get_queryset(self):
        sueldo_bajo = Jugador.objects.aggregate(Min('sueldo'))['sueldo__min']
        return Jugador.objects.filter(sueldo=sueldo_bajo)
        
    
    
class SueldoAlto(ListView):
    model = Jugador
    template_name = "jugador/sueldo-alto.html"
    context_object_name = 'mayor'

    def get_queryset(self):
        sueldo_alto = Jugador.objects.aggregate(Max('sueldo'))['sueldo__max']
        return Jugador.objects.filter(sueldo=sueldo_alto)
    




class SueldoAnual(ListView):
    model = Jugador
    template_name = "jugador/anual.html"
    context_object_name = 'jugadores'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jugadores= Jugador.objects.all()
        informacion_jugador = []
        for jugador in jugadores :
            informacion_jugador_temp = {
                'nombre': jugador.nombre,
                'apellido': jugador.apellido,
                'sueldo_anual': jugador.sueldo * 12,
            }
            informacion_jugador.append(informacion_jugador_temp)
        context['informacion_jugador'] = informacion_jugador
        return context


class SueldoDif(ListView):
    model = Jugador
    template_name = "jugador/diferencia.html"
    context_object_name = 'diferencia'

    def get_context_data(self, **kwargs):
        diferencia = super().get_context_data(**kwargs)
        sueldo_alto = Jugador.objects.aggregate(Max('sueldo'))['sueldo__max']
        sueldo_bajo = Jugador.objects.aggregate(Min('sueldo'))['sueldo__min']
        diferencia['diferencia'] = sueldo_alto - sueldo_bajo
        return diferencia
    
    
class SueldoPromedio(ListView):
    model = Jugador
    template_name = "jugador/sueldo-prom.html"
    context_object_name = 'jugadores'
    
    def get_context_data(self, **kwargs):
        promedio= super().get_context_data(**kwargs)
        promedio['promedio'] = Jugador.objects.aggregate(Avg('sueldo'))['sueldo__avg']
        return promedio
    
class Aumento10(UpdateView):
    model = Jugador
    template_name = "jugador/suba10.html"
    fields = [
        'sueldo',
        'id',
    ]
    success_url = reverse_lazy('jugador_app:jugadores')

    def form_valid(self, form):
        salario = form.instance.sueldo
        x = 0.10
        aumento10 = salario + (salario * x)
        form.instance.sueldo = aumento10
        form.save()

        return super().form_valid(form)
    
    
class Aumento15(UpdateView):
    model = Jugador
    template_name = "jugador/suba15.html"
    fields = [
        'sueldo',
        'id',
    ]
    success_url = reverse_lazy('jugador_app:jugadores')

    def form_valid(self, form):
        salario = form.instance.sueldo
        x = 0.15
        aumento15 = salario + (salario * x)
        form.instance.sueldo = aumento15
        form.save()

        return super().form_valid(form)
    
    
class Aumentar20(UpdateView):
    model = Jugador
    template_name = "jugador/suba20.html"
    fields = [
        'sueldo',
        'id',
    ]
    success_url = reverse_lazy('jugador_app:jugadores')

    def form_valid(self, form):
        salario = form.instance.sueldo
        x = 0.20
        aumento20 = salario + (salario * x)
        form.instance.sueldo = aumento20
        form.save()

        return super().form_valid(form)
    
    

    
class NumJugadores(ListView):
    template_name = "jugador/numero.html"
    context_object_name = 'jugadores'

    def get_context_data(self, **kwargs):
        num_jugadores = super().get_context_data(**kwargs)
        num_jugadores['num_jugadores'] = Jugador.objects.count()
        return num_jugadores

    def get_queryset(self):
        return []
        
class ListJugadorByKword(ListView):
    """lista jugadores por palabra clave"""
    template_name = 'jugador/by_kword.html'
    context_object_name = 'jugadores'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        lista = Jugador.objects.filter(
            nombre = palabra_clave
        )
        return lista

 
class JugadorDetail(DetailView):
    model = Jugador
    template_name = "jugador/detail_jugador.html"
    
    
    
    
class JugadorDeleteView(DeleteView):
    template_name = "jugador/del-jugador.html"
    model = Jugador
    success_url = 'list.jugador/' 
    
    

class Registro(ListView):
    template_name = "jugador/registro.html"
    context_object_name = 'leer'
    
    def get_queryset(self):
        with open('registro.txt', encoding='latin-1')as file_object:
            leer = file_object.read()

        return leer
    

class JugadorEdad(ListView):
    model = Jugador
    template_name = "jugador/edad-actual.html"
    context_object_name = 'jugadores'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edad_actual'] = [(jugador, jugador.edad()) for jugador in context['jugadores']]
        return context 

          

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
    template_name = "país/join.html"
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