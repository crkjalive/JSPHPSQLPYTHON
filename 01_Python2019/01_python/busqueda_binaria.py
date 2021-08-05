# -*- coding: utf-8 -*-

def binary_search(numbers, number_to_find, low, high):

	if low > high:
		return False

	mid = round((low + high) / 2)
	print("estamos por aqui ", mid)

	if numbers[mid] == number_to_find:
		return True
	elif numbers[mid] > number_to_find:

		print("low", low)
		print("mid", mid)
		print("high", high)
		return binary_search(numbers, number_to_find, low, mid - 1)
	else:
		print("low", low)
		print("mid", mid)
		print("high", high)
		return binary_search(numbers, number_to_find, mid + 1, high)


if __name__ == '__main__':
	
	numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
	16,17,18,19,20,21,22,23,24,25,26,27,28,29]

	number_to_find = int(input('buscar un numero de la lista: '))

	result = binary_search(numbers, number_to_find, 0, len(numbers)-1)

	if result is True:
		print(f"el numero {number_to_find} si esta en la lista")
	else:
		print(f"el numero {number_to_find} No esta en la lista")