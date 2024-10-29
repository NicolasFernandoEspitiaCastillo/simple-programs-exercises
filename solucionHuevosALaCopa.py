#Cuando un huevo es hervido en agua, las proteínas comienzan a coagularse cuando la temperatura sobrepasa un punto crítico. 
#A medida que la temperatura aumenta, las reacciones se aceleran.

#En la clara, las proteínas comienzan a coagularse para temperaturas sobre 63°C, mientras que en la yema lo hacen para temperaturas 
#sobre 70°C. Para hacer un huevo a la copa, la clara debe haber sido calentada lo suficiente para coagularse a más de 63°C, pero la 
#yema no debe sobrepasar los 70°C para evitar obtener un huevo duro.

#El tiempo en segundos que toma al centro de la yema alcanzar Ty
#°C está dado por la fórmula:

#t=M2/3cρ1/3Kπ2(4π/3)2/3ln[0.76To−TwTy−Tw],
#donde M
 #es la masa del huevo, ρ
 #su densidad, c
 #su capacidad calorífica específica y K
 #su conductividad térmica. Algunos valores típicos son:

#M=47[g]
 #para un huevo pequeño y M=67[g]
 #para uno grande,
#ρ=1.038[gcm−3],
#c=3.7[Jg−1K−1], y
#K=5.4⋅10−3[Wcm−1K−1].
#Tw
#es la temperatura de ebullición del agua y To
#la temperatura original del huevo antes de meterlo al agua, ambos en grados Celsius.

#Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo en segundos 
#que le toma alcanzar la temperatura máxima para prepararlo a la copa.


import math

def tiempo_hervido(To, M):
    # Constantes
    ρ = 1.038  # [g/cm³]
    c = 3.7    # [J/g·K]
    K = 5.4e-3 # [W/cm·K]
    Tw = 100   # [°C] (temperatura de ebullición del agua)
    Ty = 70    # [°C] (temperatura de coagulación de la yema)

    # Convertir la masa a gramos y calcular la fórmula
    t = (M ** (2/3) * c * ρ ** (1/3) * K * math.pi ** 2 * (4 * math.pi / 3) ** (2/3) *
         math.log((0.76 * To - Tw) / (Ty - Tw)))
    
    return t

# Solicitar la temperatura original del huevo
To = float(input("Ingrese la temperatura original del huevo (°C): "))

# Masa del huevo (se puede ajustar según el tamaño)
# Cambia M entre 47 y 67 según el tamaño del huevo
M = 47  # Para un huevo pequeño
# M = 67  # Para un huevo grande

# Calcular el tiempo
tiempo = tiempo_hervido(To, M)

# Mostrar el resultado
print(f"El tiempo que toma al huevo alcanzar la temperatura máxima para prepararlo a la copa es: {tiempo:.2f} segundos.")
