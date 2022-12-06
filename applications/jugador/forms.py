from django import forms

from .models import Jugador


class JugadorRegisterForm(forms.ModelForm):
    
    class Meta:
        model = Jugador
        fields = (
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'dni',
            'sueldo',
        )
