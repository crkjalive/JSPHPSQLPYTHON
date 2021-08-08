opcion = int(input("""
	1 - Colombianos
	2 - Argentinos
	3 - Mexicanos
	"""))


if opcion == 1:
	pesos = float(input("Cuantos pesos colombianos tienes?: "))
	valor_dolar = 3900
	dolares = pesos / valor_dolar
	dolares = round(dolares, 2)
	dolares = str(dolares)
	print(f"tienes {dolares} dolares")
elif opcion == 2:
	pesos = float(input("Cuantos pesos argentinos tienes?: "))
	valor_dolar = 64
	dolares = pesos / valor_dolar
	dolares = round(dolares, 2)
	dolares = str(dolares)
	print(f"tienes {dolares} dolares")
elif opcion == 3:
	pesos = float(input("Cuantos pesos mexicanos tienes?: "))
	valor_dolar = 24
	dolares = pesos / valor_dolar
	dolares = round(dolares, 2)
	dolares = str(dolares)
	print(f"tienes {dolares} dolares")
else:
	print('Opcion no implementada aun')