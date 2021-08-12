class Persona:

	def __init__(self, nombre):
		self.nombre = nombre

	def avanza(self):
		print(f"{self.nombre} anda caminando")



class Ciclista(Persona):

	def __init__(self, nombre):
		super().__init__(nombre)

	def avanza(self):
		print(f"{self.nombre} anda en bicicleta")



def main():
	
	persona = Persona('David')
	persona.avanza()

	ciclista = Ciclista('Daniela')
	ciclista.avanza()

	ciclista2 = Ciclista('Jared')
	ciclista2.avanza()
	# como ver el nombre del ciclista2?
	print(f"{ciclista2.nombre} es el ciclista 2")


if __name__ == '__main__' :
	main()