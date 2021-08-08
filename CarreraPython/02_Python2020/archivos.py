# lee el archivo, lo recorre con el for, los inserta al array y los imprime
def read_numbers():
	numbers = []
	with open('./numbers.txt','r', encoding="utf-8") as f:
		for line in f:
			numbers.append(int(line))
	print(numbers) 


def read_names():
	names = []
	with open('./names.txt','r', encoding="utf-8") as f:
		for line in f:
			names.append(line)
	print(names) 


# crea names.txt, recorremos en array, escribimos el archivo names, y un salto de linea
def sobre_write():
	names = ["Jared", "Linda", "Cristian", "Kenneth", "Rodrigo", "Rocío"] 
	with open('./names.txt','w', encoding="utf-8") as f:
		for name in names:
			f.write(name+",")
			f.write("\n")


# agregamos al archivo con a, los nombres del array, al final de las lineas del archivo
def add_write():
	names = ["Mateo", "Marcos", "Lucas", "Juan", "Juana", "Milena"] 
	with open('./names.txt','a', encoding="utf-8") as f:
		for name in names:
			f.write(name+",")
			f.write("\n")


def run():
	add_write()
	#sobre_write()
	#read_numbers()
	#read_names()


if __name__ == '__main__':
	run()