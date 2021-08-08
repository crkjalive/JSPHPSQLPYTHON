
def main():

	squares = []
	squares2 = []
	squares3 = []
	for i in range(1,101):
		squares.append(i**2)

	print(squares)

	squares2 = []
	for i in range(1,101):
		if i % 3 != 0:
				squares2.append(i**2)

	print("***"*20)
	print(squares2)

	# list comprehencions

	squares3 = [i**2 for i in range(1,101) if i % 3 != 0]
	print('***---'*10)
	print(squares3)


if __name__ == '__main__':
	main()