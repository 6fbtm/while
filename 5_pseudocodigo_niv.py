#Programa que lea la nota de 40 estudiantes y decida quienes nivelan y quienes no

print("--- Bienvenido a la base de datos ---") # Establecer los valores del minimo para pasar y para nivelar. Establecer listas vacias donde se pondrán los que pasan, nivelan y pierden, y un diccionario vacío donde se pondrán los estudiantes con sus notas
min = 70
niv = 50
notasLista = []

pasan = []
nivelan = []
pierden = []

dic_est = {}

# Bucle que primero valida la variable start

while True:
  print("Escriba un nombre, y para salir, digite 'salir'") 
  start = input("")
  if start == "salir":
    for i in dic_est:
      if dic_est[i] >= min:
        pasan.append(i)
      elif dic_est[i] >= niv:
        niv.append(i)
      else:
        pierden.append(i)
    break
  elif start.isnumeric() == False:
    name = start
    nota1 = float(input("Nota 1 del estudiante: ")) #Pedimos las 5 notas
    nota2 = float(input("Nota 2 del estudiante: "))
    nota3 = float(input("Nota 3 del estudiante: "))
    nota4 = float(input("Nota 4 del estudiante: "))
    nota5 = float(input("Nota 5 del estudiante: "))
    prom = (nota1+nota2+nota3+nota4+nota5)/5 #Le sacamos el promedio
    dic_est[name] = prom #Las almacenamos en un diccionario que contenga el nombre
  else:
    print("Escriba un nombre valido")

print(f"Los estudiantes que pasaron fueron {pasan}")
print(f"Los estudiantes que pueden nivelar son {nivelan}")
print(f"Los estudiantes que perdieron totalmente fueron {pierden}")