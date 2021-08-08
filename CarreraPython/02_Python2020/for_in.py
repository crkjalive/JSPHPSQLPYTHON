def main():
	
	for x in range(50):
		print(f"range hasta el 50 - {x}")

	for impares in range(20):
		if impares % 2 != 0:
			print(f"impares {impares}")
		elif impares % 2 == 0:
			print(f"pares {impares}")

	lista = list(range(1, 11))
	print(len(lista))
	print(lista)

	for item in lista:
		if item == 5:
			continue
		elif item == 9:
			break
		else:
			print(f"continue item 5 {item} break en 9 {item * 5} ")


if __name__ == '__main__':
	main()
