#se crea un nuevo diccionario
diccionarios = { "HUEVOS": 22.50, "JAMON": 23}

print(diccionarios ["HUEVOS"])

#obtenemos UNICAMENTE las claves del diccionario
diccionarios.keys()
print("las llaves del diccionario son", diccionarios.keys())

#obtenemos UNICAMENTE los valores
diccionarios.values()
print("los valores del diccionarios", diccionarios.values())

#eliminamos un elemento en especifico
diccionario.pop("HUEVOS") #El .pop es para eliminar valores
print(diccionarios)

diccionarios.update({"LECHE":19})
print(diccionarios)

diccionarios.update({"LECHE":45})
