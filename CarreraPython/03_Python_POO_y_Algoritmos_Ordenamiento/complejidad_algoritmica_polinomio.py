def f(x):

	respuesta = 0

	for i in range(1000): # 1000
		respuesta += 1

	for i in range(x): # x
		respuesta += x

	for i in range(x): 
		for j in range(x):
			respuesta += 1 # 2 x*x=x2 = 2x2 
			respuesta += 1 #

	return respuesta

print(f(1000))

# funcion polinominial
# lo importante es ver los datos grandes para determinar 
# que tan alto es el alcanze de nuestra ecuacion
