# list comprehensions, Dictionary comprehentions

# sugar sintatica

### listado de pares hasta el 100
pares = [x for x in range(10) if x % 2 == 0]
print("sugar",pares) 

# esto es lo mismo que decir
lista_pares = []
for i in range(0,10):
	if i % 2 == 0:
		lista_pares.append(i)
print(lista_pares)


### listado de impares hasta el 99
nones = [x for x in range(10) if x % 2 != 0]
print("sugar",nones)

# esto es lo mismo que decir
lista_impares = []
for i in range(0,10):
	if i % 2 != 0:
		lista_impares.append(i)
print(lista_impares)

# cuadrados
cuadrados = {num: num**2 for num in range(10)}
print("sugar",cuadrados) 


cuadrados_dict = {}
for x in range(10):
	cuadrados_dict[x] = x**2
print(cuadrados_dict)


squares = {numero: numero**2 for numero in range(0,10)}
print(squares)




