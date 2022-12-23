import datetime
from datetime import date

hoy = datetime.date.today()

añonac =int(input('\n Su año de nacimiento: '))
mesnac =int(input(' Su mes de nacimiento: '))
dianac =int(input(' Su día de nacimiento: '))
d = date.today()

Calculando = (d.year) - (añonac)
Calculando2 = Calculando - 1

if mesnac > d.month:
    print("su edad es" +str(Calculando2))

if dianac > d.day:
    print("su edad es" +str(Calculando2))
    
if mesnac < d.month:
    print("su edad es" +str(Calculando))
    
if dianac < d.day:
    print("su edad es" +str(Calculando))