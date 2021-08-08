def main():

	dicc = {}

	for i in range(1, 101):
		if i % 3 != 0:
			dicc[i] = i**3

	print(dicc)

	dicCom = {i:i**3 for i in range(1, 1000) if i % 3 != 0 }
	print('***'*10)
	print(dicCom)

if __name__ == '__main__':
	main()