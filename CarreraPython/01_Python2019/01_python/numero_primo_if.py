# el numero primo solo es divisible por si mismo y el 1

def esPrimo(num):
	if num < 2:
		return False
	elif num == 2:
		return True
	elif num > 2 and num % 2 == 0:
		return False
	else:
		for i in range(3, num):
			if num % i == 0:
				return False
			
	return True

def run():
	numero = int(input('escribe el numero: '))
	result = esPrimo(numero)

	if result is True:
		print(f'Tu numero {numero} es primo')
	else:
		print(f'Tu numero {numero} NO es primo')

if __name__ == '__main__':
	run()