class Millas:
    def __init__(self):
        self._distancia = 0
    
    @property
    def obtener_distancia(self):
        print("Llamada al metodo getter")
        return self._distancia

    @obtener_distancia.setter
    def obtener_distancia(self, valor):
        print("Llamada al metodo setter")
        if valor <= 0:
            raise ValueError("No es posible convertir distancias menores a 0")

        self._distancia = valor


if __name__ == "__main__":

    avion = Millas()
    avion._distancia = 200
    print(avion.obtener_distancia)

    avion._distancia = 100
    print(avion.obtener_distancia)

