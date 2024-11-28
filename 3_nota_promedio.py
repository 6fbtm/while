#Programa que solicite nombre, apellido, edad y nota promedio de 5 estudiantes de un curso de computación

estudiantes_dict = {}

for i in range(5):
  name = input("Digite el nombre del estudiante: ")
  ape = input("Digite el apellido del estudiante: ")
  edad = input("Digite la edad del estudiante: ")
  nota = input("Digite la nota promedio del estudiante: ")
  
  est = {
    "Nombre":name,
    "Apellido":ape,
    "Edad":edad,
    "Nota promedio":nota
  }

  estudiantes_dict[name] = est

print(estudiantes_dict)