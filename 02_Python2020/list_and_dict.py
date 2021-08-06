
def main():

	lista = [1,"hello",True,5.7]
	dicc = {"firstname":"Google", "lastname":"Covid"}

	lista_diccs = [
		{"firstname":"Bart", "lastname":"Simpson"},
		{"firstname":"Lisa", "lastname":"Simpson"},
		{"firstname":"Margie", "lastname":"Simpson"},
		{"firstname":"Homero", "lastname":"Simpson"},
		{"firstname":"March", "lastname":"Bobie"},
	]

	dicc_lista = {
		"numeros_naturales" : [1,2,3,4,5],
		"numeros_enteros" : [-2,-1,0,1,2],
		"numeros_flotantes" : [1.2,4.5,2.43,6.29],
	}

	for key, value in dicc_lista.items():
		print(key, value)

	print(dicc_lista["numeros_naturales"])
	print(dicc_lista["numeros_enteros"])
	print(dicc_lista["numeros_flotantes"])

	for key in lista_diccs:
		print(key)

	print("mostrando array por indice",lista_diccs[0])
	print("mostrando array por indice",lista_diccs[1])
	print("mostrando array por indice",lista_diccs[2])
	print("mostrando array por indice",lista_diccs[3])


if __name__ == '__main__':
	main()