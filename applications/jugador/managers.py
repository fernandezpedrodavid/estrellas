from django.db import models
from django.db.models import Count, Avg, Sum

class SueldoManager(models.Manager):
    """Model definition for SueldoManager."""

    def sueldobajo(self,kword):
        sueldobajo = self.filter(
            sueldo__gt=0,
            sueldo__lt=160000  
        ).order_by('apellido', 'nombre', 'sueldo')
        return sueldobajo
      
    def sueldoalto(self,kword):
        sueldoalto = self.filter(
            sueldo__gt=300000, 
        ).order_by('apellido', 'nombre', 'sueldo')
        return sueldoalto
    
    
    def num_jugadores(self):
        resultado = self.values(
            'nombre'    
        ).annotate(
            num_jugadores=Count('nombre'),
            
        )
        
        for r in resultado:
            print('========')
            print(r, r['num_jugadores'])
            
        return resultado    
    