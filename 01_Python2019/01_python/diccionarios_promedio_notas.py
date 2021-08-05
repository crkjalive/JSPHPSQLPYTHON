# promedio de calificaciones

calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 7
calificaciones['web'] = 8
calificaciones['bases_de_datos'] = 10

promedio_total = 0

for value in calificaciones.values():
	promedio_total += value

print(promedio_total / len(calificaciones.values()))

print(calificaciones) # muestra key y values
print(calificaciones.values()) # muestra values
print(calificaciones.keys()) # muestra las keys

print(calificaciones['matematicas']) # mostrar especifico






