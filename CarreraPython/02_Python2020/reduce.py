from functools import reduce

def main():

	my_list = [2,2,2,2,2]
	my_list2 = [3,3,3,3,3]
	
	all_multiplied2 = reduce(lambda a, b: a * b, my_list2)
	print(all_multiplied2) # 243


	all_multiplied = 1
	for i in my_list:
		all_multiplied = all_multiplied * i
	print(all_multiplied) # 32






if __name__ == '__main__':
	main()