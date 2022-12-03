from django.contrib import admin
 
from .models import (
    Jugador,
    País,
    Posición
)     

# Register your models here.
admin.site.register(Jugador)
admin.site.register(País)
admin.site.register(Posición)