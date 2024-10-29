#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b
#de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
#del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.

#Ingrese cateto a: 7
#Ingrese cateto b: 5
#La hipotenusa es 8.6023252670426267

import math

# Solicitar al usuario que ingrese las longitudes de los catetos
cateto_a = float(input("Ingrese cateto a: "))
cateto_b = float(input("Ingrese cateto b: "))

# Calcular la hipotenusa usando el teorema de Pitágoras
hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)

# Mostrar el resultado
print(f"La hipotenusa es {hipotenusa}")
