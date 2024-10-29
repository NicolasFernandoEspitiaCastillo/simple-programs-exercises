#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.

#El promedio del ramo se calcula con la siguiente formula.

#NC=(C1+C2+C3)3
#NF=NC⋅0.7+NL⋅0.3
#Donde NC
#es el promedio de certámenes, NL
#el promedio de laboratorio y NF
#la nota final.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#Ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3




# Función para calcular la nota necesaria en el tercer certamen
def nota_necesaria(c1, c2, nl, nf_deseada):
    # Calculamos la nota del tercer certamen necesaria
    for c3 in range(0, 101):  # Buscamos entre 0 y 100
        nc = (c1 + c2 + c3) / 3  # Promedio de certámenes
        nf = nc * 0.7 + nl * 0.3  # Nota final
        if nf >= nf_deseada:
            return c3
    return None  # Si no se encuentra una nota válida

# Solicitar las notas al usuario
c1 = float(input("Ingrese nota certamen 1: "))
c2 = float(input("Ingrese nota certamen 2: "))
nl = float(input("Ingrese nota laboratorio: "))

# Nota final deseada para aprobar
nf_deseada = 60

# Calcular la nota necesaria
nota_necesaria_c3 = nota_necesaria(c1, c2, nl, nf_deseada)

# Mostrar el resultado
if nota_necesaria_c3 is not None:
    print(f"Necesita nota {nota_necesaria_c3} en el certamen 3.")
else:
    print("No es posible aprobar el ramo con las notas ingresadas.")
