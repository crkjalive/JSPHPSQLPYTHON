def palindromo(palabra):
	palabra = palabra.replace(' ', '') # remplaza espacio por nada
	palabra = palabra.lower()
	palabra_invertida = palabra[::-1] # invierte la palabra

	if palabra == palabra_invertida:
		return True
	else:
		return False


def main():
	palabra = input('escribe la palabra: ')
	es_palindromo = palindromo(palabra)

	if es_palindromo == True:
		print(f"{palabra} es un palindromo")
	else:
		print(f"{palabra} no es un palindromo")


if __name__ == '__main__':
	main()