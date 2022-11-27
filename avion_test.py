class Millas:
    def __init__(self, distancia = 0):
        self.distancia = distancia
        
    def convertir_a_kilometros(self):
        return (self.distancia * 1.609344)
    # Metodo getter
    def obtener_distancia(self):
        return self._distancia
    # Metodo setter
    def definir_distancia(self):
        if self.distancia < 0:
            raise ValueError ("No es posible convertir distancias menores a 0.")
        
        self._distancia = self.distancia
        

avion = Millas(100000)
avion.definir_distancia()

print(avion.obtener_distancia())
print(avion.convertir_a_kilometros())