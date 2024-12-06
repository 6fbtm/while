#Programa que elija al ganador de las elecciones, candidatos A, B y C
#Como minimo el ganador debe tener el 51% de votos a favor
#En caso de un empate, van a segunda vuelta los dos que mas tengan votos
#La eleccion se anula si hay empate por el segundo lugar, o empate triple

print("-- Bienvenido, administrador --")

#Bucle que pide el numero de votos

while True:
  canA = int(input("Votos del candidato A: "))
  canB = int(input("Votos del candidato B: "))
  canC = int(input("Votos del candidato C: "))
  break

totalVotos = canA+canB+canC

#Sacando el porcentaje de los votos respecto al total de votos

porcA = canA/totalVotos*100
porcB = canB/totalVotos*100
porcC = canC/totalVotos*100

#Condicionales que validan si ganan, empatan o anulan

if porcA > 0.5:
  print("el candidato A gana las elecciones")
elif porcB > 0.5:
  print("El candidato B gana las elecciones")
elif porcC > 0.5:
  print("El candidato C gana las elecciones")
elif porcA == porcB and porcB == porcC or porcB == porcC or porcC == porcA:
  print("Elecciones anuladas")
elif porcA == porcB or porcA == porcC or porcC == porcB:
  print("Empate. Van a segunda vuelta")

