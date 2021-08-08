# Diccionarios
# mi_dict =  {
#   'llave':'valor',
# }

# iteracion en diccionarios

# mi_dict = dict()
# print(type(mi_dict))

dicc = {}
dicc['primer_dato'] = 'Hola'
dicc['segundo_dato'] = 'Mundo'

print(dicc['primer_dato'])
print(dicc['segundo_dato'])

# iterar un diccionario
calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 10
calificaciones['web'] = 8
calificaciones['bases_de_datos'] = 10

# iterar por keys
for key in calificaciones:
	print(key)

# iterar por values
for value in calificaciones.values():
	print(value)

# iterar key y value
for key, value in calificaciones.items():
	print(f"llave: {key}, valor: {value}")


# promedio de calificaciones















