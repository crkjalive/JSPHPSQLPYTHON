# factorial de un número
# consiste en tomar un nuemro y irlo multiplicando con el numero anterior a su valor
'''
5 * 4 * 3 * 2 * 1 = 120
'''

# implementacion de la funcion factorial

def factorial(numero):
	if numero == 0: # caso base
		return 1

	return numero * factorial(numero - 1 )



if __name__ == '__main__':
	numero = int(input('Escribe un número: '))

	resultado =  factorial(numero)

	print(resultado)


# caso base, permite darle un tope a la funcion recursiva
# que evita entrar al infinity loop 
# infinity loop, en python solo permite hacer 1000 veces
