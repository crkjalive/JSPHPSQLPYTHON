# habitantes por pais en millones
countries = {
	'mexico' : 122,
	'colombia' : 49,
	'argentina' : 43,
	'chile' : 18,
	'peru' : 31,
}
print(countries)

# loop infinito
while True:
	country = str(input('Escribe el nombre de un país: ')).lower()
	try:
		print(f'La poblacion de {country} es de {countries[country]} millones')
	except KeyError:
		print(f'aun No tenemos registros de {country}')

