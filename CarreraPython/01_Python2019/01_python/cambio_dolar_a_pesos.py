def cambioHoy(dolar,valor):
	operacion = dolar * valor
	return operacion

def main():
	print(f"Calculadora de divisas a pesos")
	print(f"Cuantos pesos tengo")
	print('')
	monto = float(input('cantidad de dolares: '))
	dolar = float(input('precio del dolar: '))
	result = cambioHoy(monto,dolar)

	#print(f"{monto} dolares a pesos son {result} pesos en colombia ")

	print("${} dolares a pesos son ${} pesos en colombia ".format(monto, result))

if __name__ == '__main__':
	main()