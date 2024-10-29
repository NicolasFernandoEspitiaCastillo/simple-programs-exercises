#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.

#Ingrese longitud: 45
#45 cm = 17.7165 in
#Ingrese longitud: 13
#13 cm = 5.1181 in



# Función para convertir centímetros a pulgadas
def cm_a_pulgadas(centimetros):
    return centimetros / 2.54

# Solicitar al usuario que ingrese la longitud en centímetros
longitud_cm = float(input("Ingrese longitud: "))

# Realizar la conversión
longitud_in = cm_a_pulgadas(longitud_cm)

# Mostrar el resultado
print(f"{longitud_cm} cm = {longitud_in:.4f} in")
