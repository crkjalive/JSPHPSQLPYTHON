import random 


def palindrome(palabra):
	letras_palabra = []

	for letras in palabra:
		letras_palabra.insert(0, letras)

	palabra_invertida = ''.join(letras_palabra)

	if palabra_invertida == palabra:
		return True

	return False


if __name__ == '__main__':
	
	palabra = str(input('introcude una palabra: '))

	resultado = palindrome(palabra)


	if resultado is True:
		print(f'{palabra} si es un palindromo')
	else:
		print(f'{palabra} no es un palindromo')


