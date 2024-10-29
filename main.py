#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

#Ingrese el radio: 5
#Perimetro: 31.4
#Área: 78.5

import math

# Función para calcular el perímetro y el área de un círculo
def calcular_circulo(radio):
    perimetro = 2 * math.pi * radio
    area = math.pi * (radio ** 2)
    return perimetro, area

#Ingrese el radio
radio = float(input("Ingrese el radio: "))
perimetro, area = calcular_circulo(radio)

# Mostrar los resultados
print(f"Perímetro: {perimetro:.1f}")
print(f"Área: {area:.1f}")
