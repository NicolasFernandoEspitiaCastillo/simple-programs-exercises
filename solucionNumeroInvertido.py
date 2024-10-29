#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

#Ingrese numero: 345
#543
#Ingrese numero: 241
#142

# Solicitar al usuario que ingrese un número de tres dígitos
numero = input("Ingrese un número de tres dígitos: ")

# Verificar que el número tenga exactamente tres dígitos
if len(numero) == 3 and numero.isdigit():
    # Invertir los dígitos del número
    numero_invertido = numero[::-1]
    # Mostrar el resultado
    print(numero_invertido)
else:
    print("Por favor, ingrese un número válido de tres dígitos.")
