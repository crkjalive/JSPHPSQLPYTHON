# para poder medir el tiempo en Python
import time

# implementacion factorial iterativa

def factorial(n):
	respuesta = 1

	while n > 1:
		respuesta *= n 
		n -= 1

# implementacion factorial recursiva

def factorial_r(n):
	if n == 1:
		return 1

	return n * factorial(n-1)


if __name__ == '__main__':
	
	n = 1000

	# podemos medir nuestro algoritmo

	comienzo = time.time()
	factorial(n)
	final = time.time()
	print(final - comienzo)

	comienzo = time.time()
	factorial_r(n)
	final = time.time()
	print(final - comienzo)

# Codigo en la funcion recursiva me da error, no se que es?

# en el curso la complejidad por tiempo no es lo mas preciso,
# ya que hace primero un computo y luego el otro