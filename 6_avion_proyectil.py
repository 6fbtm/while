#Programa que calcule la distancia que separa a un avion de un proyectil que disparó
#En el momento del disparo el avion va a 800km/h giró a 90° y acelera a 20m/s**2
#El proyectil acelera a 10m/s**2
#El codigo debe calcular la distancia a la que se separa hasta que esté a 10000m o mas

#Asumiendo que el proyectil tambien va a 800km/h

import math

#Las medidas de la velocidad y aceleracion del avion, y de la velocidad y aceleración del proyectil respectivamente

plnSpdKmh = 800
plnAcc = 20
prctlSpdKmh = 800
prctlAcc = 10

#Contadores que usaremos en el bucle

dist = 0
sec = 0

#Conversiones. Para realizar las operaciones tenemos que hacer que las unidades sean equivalentes. Cambiamos los kmh por ms

plnSpdMs = plnSpdKmh/3.6
prctlSpdMs = prctlSpdKmh/3.6

#Calculando distancia por segundo


while dist < 10000:
  sec += 1
  plnDistS = plnSpdMs+(plnAcc*sec)
  prctlDistS = prctlSpdMs+(prctlAcc*sec)
  dist += math.sqrt(math.pow(plnDistS,2)+math.pow(prctlDistS,2))
  print(f"Han pasado {sec} segundos, y la distancia entre el avion y el proyectil es de {dist}m")