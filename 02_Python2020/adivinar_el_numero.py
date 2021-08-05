import random 

def main():
	numero_aleatorio = random.randint(0, 20)
	numero_elegido = int(input('Escoge un número: '))

	while numero_elegido != numero_aleatorio:

		if numero_elegido < numero_aleatorio:
			print('el numero es más grande')
		else:
			print('el numero es más pequeño')
		
		numero_elegido = int(input('Escoge otro número: '))

	print('Ganaste!')

if __name__ == '__main__':
	main() 