class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def set_region(self, region):
        if region in self._pais:
            self._region = region 

        raise ValueError(f"la region {region} no es valida en {self._pais}")

casilla = CasillaDeVotacion(123,['Ciudad de Mexico','morelos'])
casilla.region

casilla.region = 'Ciudad de Mexico'
casilla.region
