import random 

def main():
	numero_real = False
	numero_random = random.randint(0, 20)

	while not numero_real:
		numero_usuario = int(input('Intenta un numero: '))

		if numero_usuario == numero_random:
			print('Felicitaciones, encontraste el numero')
			numero_real = True
		elif numero_usuario > numero_random:
			print('el numero es menor')
		else:
			print('el numero es mayor')


if __name__ == '__main__':
	main()