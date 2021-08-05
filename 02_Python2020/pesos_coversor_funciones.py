def conversor(tipo_pesos, valor_dolar):
	pesos = float(input(f"Cuantos pesos {tipo_pesos} tienes?: "))
	dolares = pesos / valor_dolar
	dolares = round(dolares, 2)
	dolares = str(dolares)
	print(f"tienes {dolares} dolares")
	

def main():
	opcion = int(input("""
	1 - Colombianos
	2 - Argentinos
	3 - Mexicanos
	"""))

	if opcion == 1:
		valorActual = int(input("precio actual: "))
		conversor("colombianos", valorActual)
	elif opcion == 2:
		valorActual = int(input("precio actual: "))
		conversor("argentinos",valorActual)
	elif opcion == 3:
		valorActual = int(input("precio actual: "))
		conversor("mexicanos",valorActual)
	else:
		print('Opcion no implementada aun')


if __name__ == '__main__':
	main()