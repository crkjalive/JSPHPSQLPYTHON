def main():
	LIMITE = 10000

	contador = 0 
	potencia = 2**contador

	while potencia < LIMITE:
		print(f" 2 a la {contador} es {potencia}")
		contador = contador + 1
		potencia = 2**contador


if __name__ == '__main__':
	main()