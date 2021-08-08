def divisors(num):
	divisors = []

	for i in range(1, num + 1):
		if num % i == 1:
			divisors.append(i)

	return divisors


def run():

	try:
		num = int(input("ingresa un número: "))
		print(divisors(num))
		print('Termino el programa')
	except ValueError:
		print("Debes ingresar un Número")



if __name__ == '__main__':
	run()

# El error esta en que esta comparando la variable i y 
# no es entero en 0, por eso no encuentra el error y ejecuta 
# el programa como si nada aunque este dando mal el resultado