#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

#Primera nota: 55
#Segunda nota: 71
#Tercera nota: 46
#Cuarta nota: 87
#El promedio es: 64.75




# Función para calcular el promedio de 4 notas
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Lista para almacenar las notas
notas = []

# Solicitar al usuario que ingrese las notas
for i in range(1, 5):
    nota = float(input(f"Ingrese la {i}ª nota: "))
    notas.append(nota)

# Calcular el promedio
promedio = calcular_promedio(notas)

# Mostrar el resultado
print(f"El promedio es: {promedio:.2f}")
