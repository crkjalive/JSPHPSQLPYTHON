# Leer el archivo 
# cuento EL ALEPH
def run():
	letra = 'e'
	counter = 0
	with open('aleph.txt') as f:
		for line in f:
			counter += line.count(letra)

	print(f"la {letra} se encontro {counter} veces en el texto")


if __name__ == '__main__':
	run()



