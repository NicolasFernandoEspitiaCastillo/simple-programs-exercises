#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

#Ingrese un numero: 4.5
#0.5
#Ingrese un numero: -1.19
#0.19



# Función para obtener la parte decimal
def parte_decimal(numero):
    # Separamos la parte entera de la parte decimal
    parte_entera = int(numero)
    parte_decimales = abs(numero - parte_entera)  # Usar abs para manejar números negativos
    return parte_decimales

# Solicitar al usuario que ingrese un número
numero_ingresado = float(input("Ingrese un número: "))

# Calcular y mostrar la parte decimal
resultado = parte_decimal(numero_ingresado)
print(resultado)
