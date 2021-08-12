class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura="caliente"):
        self._llenar_de_agua(temperatura)
        self._agregar_jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_de_agua(self, temperatura):
        print(f"llenando el tanque de agua {temperatura}")

    def _agregar_jabon(self):
        print(f"agregando el jabon")

    def _lavar(self):
        print(f"lavando la ropa")

    def _centrifugar(self):
        print(f"centrifugando la ropa")

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
