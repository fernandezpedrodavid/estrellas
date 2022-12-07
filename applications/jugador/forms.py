from django import forms

from .models import Jugador


class JugadorRegisterForm(forms.ModelForm):
    
    class Meta:
        model = Jugador
        fields = (
            '__all__'
        )
