#Programa que calcule promedio ponderado
#Se multiplicada cada calificacion por los creditos de cada materia
#El resultado anterior se suma con los resultados de cada materia
#Por separado se suman los creditos de cada materia
#se divide la suma de todas las materias por sus respectivos creditos, entre la suma de todos los creditos
# las materias son fundamentos, BD y Etica

print("-- Bienvenido a la base de datos de las calificaciones --\nIngrese los datos")

#Contador y diccionario que usamos para almacenar las materias

contador = 0
notasMaterias = {}

#Como son 3 materias, el while se establece para terminar cuando llegue a 3
#Tambien se implementa un menú para elegir la materia

while contador < 3:
  contador += 1
  materia = input("Elija la materia a editar:\n1.Fundamentos\n2.BD\n3.Ética\n(No usar acentos)\n")
  materia = materia.lower()
  
  #Establecemos condicionales que verifiquen cual materia elegimos

  if materia == "fundamentos":
    nota = float(input(f"Cual fue la nota de {materia}?: "))
    credit = float(input(f"Cuantos creditos tiene {materia}?: "))
    #Una vez obtenidos la nota y el credito, los almacenamos en un nuevo diccionario, cuya clave en el anterior diccionario será el nombre de la materia

    notasMaterias[materia] = {"nota":nota,"credito":credit}

  elif materia == "etica":
    nota = float(input(f"Cual fue la nota de {materia}?: "))
    credit = float(input(f"Cuantos creditos tiene {materia}?: "))
    notasMaterias[materia] = {"nota":nota,"credito":credit}
  
  elif materia == "bd":
    nota = float(input(f"Cual fue la nota de {materia}?: "))
    credit = float(input(f"Cuantos creditos tiene {materia}?: "))
    notasMaterias[materia] = {"nota":nota,"credito":credit}

  #Else implementado en caso de que no se escriba ninguna materia

  else:
    print("Por favor, digite correctamente la materia")
    contador -= 1

#Contadores que usaremos para las operaciones del promedio ponderado

notaTotal = 0
creditTotal = 0
mult = 0

#Calculando el promedio ponderado por medio de un bucle for, que itera los diccionarios

for i in notasMaterias:
  notaOp = notasMaterias[i]["nota"]
  creditOp= notasMaterias[i]["credito"]
  mult += notaOp * creditOp
  creditTotal += creditOp

prompond = mult/creditTotal

print(f"El promedio ponderado es de {prompond}")