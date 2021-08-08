class Coordenada():

  # metodo constructor inicializa la clase
  def __init__(self, x, y):

    self.x = x
    self.y = y


  # metodo distancia
  def distancia(self, otra_cordenada):

    x_diff = (self.x - otra_cordenada.x)**2
    y_diff = (self.y - otra_cordenada.y)**2

    return (x_diff + y_diff)**0.5


def run():
  # instancias de la clase
  cordenada_1 = Coordenada(3, 30)
  cordenada_2 = Coordenada(4, 8)

  # 22.02271554554524
  # print(cordenada_1.distancia(cordenada_2)) 

  # para ver si una instancia pertenece a una clase
  print( isinstance(cordenada_2, Coordenada) ) # True


if __name__ == '__main__':
  run()