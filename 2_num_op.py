#Programa que calcule la suma, resta, multiplicacion y division de dos numeros dados por el usuario

contador = 0 #Contador que registre cuantos procesos se han llevado a cabo

while contador >= 10: #Bucle que hace repetir el proceso hasta llegar a 10 proceso hechos
  n1 = int(input("Ingrese el primer numero: "))
  n2 = int(input("Ingrese el segundo numero: "))
  suma = n1+n2
  resta = n1-n2
  multi = n1*n2
  div = n1/n2
  print(f"La suma de los numeros da {suma}. La resta da {resta}. La multiplicación da {multi}. La división da {div}.")
  contador += 1

