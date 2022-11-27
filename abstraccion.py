class Lavadora:
    def __init__(self):
        pass
    
    def lavar(self, temperatura="frio", nivel_agua = 4, lavado = 15, enjuague = "Normal", centrifugado = "Pre secado", programa="Normal"):
        self._configuracion(programa, lavado)
        self._llenar_tanque_de_agua(temperatura, nivel_agua)
        self._lavar()
        self._enjuague(enjuague)
        self._centrifugar(centrifugado)
        self._finalizado()
    
    def _configuracion(self, programa, lavado):
        print(f"Programado para ropa tipo {programa} y con un lavado de {lavado} minutos")
        
    def _llenar_tanque_de_agua(self, temperatura, nivel_agua):
        print(f"Llenando el tanque con un nivvel de agua {nivel_agua} y con temperatura {temperatura}")
        
    def _lavar(self):
        print("Se inicia el lavado")
    
    def _enjuague(self, enjuague):
        print(f"Se inicia el enjuague de tipo {enjuague}")
    
    def _centrifugar(self, centrifugado):
        print(f"Se inicia el centrifugando de tipo {centrifugado}")
    
    def _finalizado(self):
        print("Lavado de ropa a finalizado")

if __name__ == "__main__":
    lavadora = Lavadora()

    lavadora.lavar()
