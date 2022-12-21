from django.db import models

from .managers import SueldoManager

# Create your models here.
class Jugador(models.Model):
    """Model definition for Jugador."""

    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30, blank=True)
    fecha_nacimiento = models.DateField()
    dni = models.PositiveIntegerField()  
    sueldo = models.PositiveIntegerField()
    
    objects = SueldoManager()
    
    class Meta:       

        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'

    def __str__(self):
        return str(self.id)+ '-' + self.nombre + '-' + self.apellido + '-' + str(self.fecha_nacimiento)


class País(models.Model):
    """Model definition for País."""
    
    país = models.CharField('País', max_length=30, null=True)
    club = models.CharField('Club', max_length=50, null=True)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, null=True)

    class Meta:
        """Meta definition for País."""

        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def __str__(self):
        return self.país + '-'+ self.club + '-' + self.jugador.nombre + '-' + self.jugador.apellido
    
    
class Posición(models.Model):
    '''Modelo para tabla Posición'''
    
    PUESTO_CHOICES = (
        ('0', 'Arquero'),
        ('1', 'Defensor'),
        ('2', 'Medio campo'),
        ('3', 'Delantero'),
    )
    
    posición = models.CharField('Posición', max_length=1, choices=PUESTO_CHOICES)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for Posición."""

        verbose_name = 'Posición'
        verbose_name_plural = 'Posiciónes'

    def __str__(self):
        return self.posición + '-' + self.jugador.nombre + '-' + self.jugador.apellido


