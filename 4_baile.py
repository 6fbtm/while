#Programa que encuentre cuantas damas habian en un baile
#En la fiesta habian 42 personas, una dama bailó con 7 caballeros, una segunda con 8, y asi sucesivamente. La ultima bailó con todos los caballeros.
total = 0
dama = 1
caballero = 7 #Contadores que establecen los numeros por donde se empieza

while total < 42: #El bucle sigue hasta que total sea mayor que 42
  dama += 1
  caballero += 1 #Por cada vez que se repite el bucle, a dama se le suma 1 y a caballero tambien
  total = dama + caballero

print(f"Hay {dama} damas, {caballero} caballeros y {total} personas en total") #El resultado es la cantidad de damas y caballeros. Tambien el total de personas
