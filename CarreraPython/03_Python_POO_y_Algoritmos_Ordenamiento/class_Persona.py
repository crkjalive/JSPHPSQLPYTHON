class Persona():

	# metodo constructor inicializa la clase
	def __init__(self, nombre, edad):

		self.nombre = nombre
		self.edad = edad


	# metodo saludar
	def saluda (self, otra_persona):
		return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'


def run():
	# instancias de la clase
	david = Persona('David', 35)
	erika = Persona('Erika', 25)

	print(david.saluda(erika))
	print(erika.saluda(david))

if __name__ == '__main__':
			run()		