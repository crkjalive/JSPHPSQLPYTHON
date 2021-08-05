def main():

	diccionario = {
		'llave1' : 1,
		'llave2' : 2,
		'llave3' : 3,
	}
	# print(diccionario['llave1'])
	# print(diccionario['llave2'])
	# print(diccionario['llave3'])

	poblacion_paises = {
		'Argentina':44938712,
		'Brasil':210147125,
		'Colombia':50372424,
	}

	# print(poblacion_paises['Colombia'], "Colombia")
	# print(poblacion_paises['Brasil'], "Brasil")
	# print(poblacion_paises['Argentina'], "Argentina")

	for pais in poblacion_paises:
		print(pais)

	for pais in poblacion_paises.values():
		print(pais)

	for pais in poblacion_paises.items():
		print(pais)

	for pais, poblacion in poblacion_paises.items():
		print(pais, poblacion)

if __name__ == '__main__':
	main()