def main():

	my_list = [1,4,5,6,9,13,19,21]
	
	odd = [i for i in my_list if i % 2 != 0]
	print(odd) # me muestra los impares de la lista

	odd2 = list(filter(lambda x: x%2 !=0, my_list))
	print(odd2)




if __name__ == '__main__':
	main()