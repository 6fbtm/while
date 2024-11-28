#Programa que calcule el precio de venta por kilo de huevo. Precio se determina por a traves de la calidad de las N gallinas que hay en la granja.
#Calidad de huevos = (peso gallina * altura gallinas)/ numero de huevos

while True: #Bucle que repite las consultas
  start = input("Comenzar o salir | ") 
  if start == "salir": #Si el usuario escribe "salir", entonces el bucle para
    break

  print("-- Ingrese las especificaciones de la gallina en cuestión --")

  peso = float(input("Ingrese el peso en KG: "))
  altura = float(input("Ingrese la altura en CM: "))
  eggs = int(input("Ingrese la cantidad de huevos por kilo: "))
  cal = (peso*altura)/eggs
  print(f"El precio de venta por kilo de huevo es de ${cal}")


