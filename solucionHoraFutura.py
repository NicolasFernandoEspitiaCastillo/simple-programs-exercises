#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, 
#que indique qué hora marcará el reloj dentro de h horas:

#Hora actual: 3
#Cantidad de horas: 5
#En 5 horas, el reloj marcara las 8
#Hora actual: 11
#Cantidad de horas: 43
#En 43 horas, el reloj marcara las 6



# Función para calcular la hora futura
def hora_futura(hora_actual, horas_a_sumar):
    # Calcular la nueva hora
    nueva_hora = (hora_actual + horas_a_sumar) % 12
    return nueva_hora if nueva_hora != 0 else 12  # Si es 0, significa que son las 12

# Solicitar la hora actual y la cantidad de horas a sumar
hora_actual = int(input("Hora actual (1-12): "))
horas_a_sumar = int(input("Cantidad de horas: "))

# Calcular y mostrar la nueva hora
nueva_hora = hora_futura(hora_actual, horas_a_sumar)
print(f"En {horas_a_sumar} horas, el reloj marcará las {nueva_hora}.")
