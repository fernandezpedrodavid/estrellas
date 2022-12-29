import datetime
from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.db.models import Count
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    DetailView,
    TemplateView,
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
 
 
class JugadorSalario(ListView):
    template_name = "jugador/sueldo-jugador.html"
    context_object_name = 'salarios'
    
    def get_queryset(self):
        return Jugador.objects.all()
   
   
class SueldoMenor(ListView):
    model = Jugador
    template_name = "jugador/sueldo-menor.html"
    context_object_name = 'menor'
    
    def get_queryset(self):
        min_sueldo = Jugador.objects.aggregate(Min('sueldo'))['sueldo__min']
        return Jugador.objects.filter(sueldo=min_sueldo)
    

class SueldoMayor(ListView):
    model = Jugador
    template_name = "jugador/sueldo-mayor.html"
    context_object_name = 'mayor'
    
    def get_queryset(self):
        max_sueldo= Jugador.objects.aggregate(Max('sueldo'))['sueldo__max']
        return Jugador.objects.filter(sueldo=max_sueldo)


class SueldoAnual(ListView):
    model = Jugador
    template_name = "jugador/anual.html"
    context_object_name = 'jugadores'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jugadores = Jugador.objects.all()
        informacion_anual = []
        for jugador in jugadores:
            informacion_anual.append({
                'nombre': jugador.nombre,
                'apellido': jugador.apellido,
                'sueldo_anual': jugador.sueldo * 12,
            })
        context['informacion_anual'] = informacion_anual
        return context


class SueldoDif(ListView):
    model = Jugador
    template_name = "jugador/diferencia.html"
    context_object_name = 'jugadores'
    
    def get_context_data(self, **kwargs):
        diferencia = super().get_context_data(**kwargs)
        max_sueldo= Jugador.objects.aggregate(Max('sueldo'))['sueldo__max']
        min_sueldo = Jugador.objects.aggregate(Min('sueldo'))['sueldo__min']
        diferencia ['diferencia'] = max_sueldo - min_sueldo 
        return diferencia
    
    
class JugadorUp10(UpdateView):
    model = Jugador
    template_name = "jugador/up10.html"
    fields = [
        'sueldo',
        'id'
    ]
    success_url = reverse_lazy('jugador_app:sueldos')
    
    def form_valid(self, form):
        salario = form.instance.sueldo
        aumento = 0.10
        aumento10 = salario + (salario*aumento)
        form.instance.sueldo = aumento10
        form.save
        return super().form_valid(form)


class JugadorUp15(UpdateView):
    model = Jugador
    template_name = "jugador/up15.html"
    fields = [
        'sueldo',
        'id'
    ]
    success_url = reverse_lazy('jugador_app:sueldos')
    
    def form_valid(self, form):
        salario = form.instance.sueldo
        aumento = 0.15
        aumento15 = salario + (salario*aumento)
        form.instance.sueldo = aumento15
        form.save
        return super().form_valid(form)
    

class JugadorUp20(UpdateView):
    model = Jugador
    template_name = "jugador/up20.html"
    fields = [
        'sueldo',
        'id'
    ]
    success_url = reverse_lazy('jugador_app:sueldos')
    
    def form_valid(self, form):
        salario = form.instance.sueldo
        aumento = 0.20
        aumento20 = salario + (salario*aumento)
        form.instance.sueldo = aumento20
        form.save
        return super().form_valid(form)
    
    


    
class SueldoPromedio(ListView):
    model = Jugador
    template_name = "jugador/sueldo-prom.html"
    context_object_name = 'sueldos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['media_sueldo'] = Jugador.objects.aggregate(Avg('sueldo'))['sueldo__avg']
        return context
    
    
class NumJugadores(ListView):
    model = Jugador
    template_name = "jugador/numero.html"
    context_object_name = 'jugadores'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_jugadores'] = Jugador.objects.count()
        return context
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
    

class Edades(ListView):
    template_name = "jugador/edad-actual.html"
    model = Jugador
    fields = [
        'nombre',
        'apellido',
        'fecha_nacimiento'
    ]
    context_object_name = 'edades' 

    def calculate_age(self, born):
        today = datetime.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        edades = []
        for jugador in context['edades']:
            born = jugador.fecha_nacimiento
            age = self.calculate_age(born)
            edades.append((jugador.nombre, jugador.apellido, age))
        context['edades'] = edades
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