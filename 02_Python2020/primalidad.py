# el numero primo solo es divisible por si mismo y el 1

def es_primo(numero):

	contador = 0

	for i in range(1, numero + 1):
		if i == 1 or i == numero:
			continue
		if numero % i == 0:
			contador += 1

	if contador == 0:
			return True
	else:
			return False
			
def run():
	numero = int(input('escribe el numero: '))
	
	if es_primo(numero):
		print(f'Tu numero {numero} es primo')
	else:
		print(f'Tu numero {numero} NO es primo')


if __name__ == '__main__':
	run()