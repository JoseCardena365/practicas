# ACTIVIDAD
#
# REALIZAR UN PRIGRAMA
# QUE PIDA EL NOMBRE DE 3 PERSONAS
# A CADA PERSONA SE LE PEDIRA QUE INGRESE SUS CALIFICACIONES(5 CALIFICACIONES)
# SACAR EL PROMEDIO DE LAS CALIFICACIONES DE CADA PERSONA
# DESPLEGAR UN MENSAJE CON EL NOMBRE DE LA PERSONA Y SU PROMEDIO
#
# METODOS:
# len(lista) --> obtiene el tamaño de la lista(cantidad de elementos)
# lista.append(elemento) --> afregar elemento a lista
# lista.pop() ---> elimina el ultimo elemento agregado a la lista

lista = []

listaNombres = []
for nombres in range(0,3):
    listaNombres.append(input("ingrese su nombre completo"))
# Quitar el print
    print(listaNombres)

#     variable = 0
# #Pasar la lista
#     listaCalificaciones = []
#
#     len(listaCalificaciones)
#     for calificaciones in range(0, 5):
#         #listaCalificaciones.append(input("ingrese sus calificaciones"))
#         variable += float(input("ingrese sus calificaciones"))
#
#     print(listaCalificaciones)
