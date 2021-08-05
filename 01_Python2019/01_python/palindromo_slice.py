import random 

def palindrome2(palabra):
	palabra_invertida = palabra[::-1]

	if palabra_invertida == palabra:
		return True

	return False


if __name__ == '__main__':
	
	palabra = str(input('introcude una palabra: '))

	resultado = palindrome2(palabra)


	if resultado is True:
		print(f'{palabra} si es un palindromo')
	else:
		print(f'{palabra} no es un palindromo')


