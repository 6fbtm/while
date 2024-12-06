#Una empresa contrata n vendedores, cada uno tiene que hacer tres ventas y gana una comsión del 10%
#Programa que calcule el dinero que obtendrá un empleado por tres ventas con comisiones y sueldo base

print("-- Bienvenido a la base de datos --\n Porfavor ingrese los datos: ")

sueldo = float(input("Sueldo base de los empleados: "))

nVendedores = int(input("Ingrese la cantidad de vendedores a calcular: "))

#Contador que calculará las veces que se repite el bucle
contador = 0

while contador < nVendedores:
  contador += 1
  print(f"** Procesando los datos del vendedor {contador}")
  venta1 = int(input("Ingrese el precio de la venta 1: "))
  venta2 = int(input("Ingrese el precio de la venta 2: "))
  venta3 = int(input("Ingrese el precio de la venta 3: "))
  venta1com,venta2com,venta3com = venta1*0.1,venta2*0.1,venta3*0.1

  dinero = sueldo + venta1com+venta2com+venta3com
  print(f"El dinero que este vendedor ganó son ${dinero}")


