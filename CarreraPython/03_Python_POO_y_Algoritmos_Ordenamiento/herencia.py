# modelamos jerarqui de clases 

class Rectangulo: 

	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	def area(self):
		return self.base * self.altura

# asi hereda o extiende de otra clase
class Cuadrado(Rectangulo):

	def __init__(self, lado):
		super().__init__(lado, lado)


if __name__ == '__main__':
	
	rectagulo = Rectangulo(base=3, altura=5) # 15
	print(rectagulo.area()) # debemos ejecutar su metodo area

	cuadrado = Cuadrado(lado=5) # 25
	print(cuadrado.area()) # debemos ejecutar su metodo area

