class CasillaDeVotacion:
    __regiones_Mexico = {  # Mapa de regiones de México
        'region1': "Ciudad de México",
        'region2': "Morelos"
    }

    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__regiones_Mexico.values():
            self.__region = region
            print(f"La region {region} de encuentra en {self.__pais}. La región se cambió correctamente")
        else:
            print(f"La region {region} no es válida en {self.__pais}")


if __name__ == '__main__':
    casilla = CasillaDeVotacion(123, "México")
    print(casilla.region)  # Imprime None porque no tiene region asignada
    casilla.region = "Ciudad de México"
    print(casilla.region)

    casilla2 = CasillaDeVotacion(124, "México", )
    casilla2.region = "Washington"  # Aquí arroja mensaje de que no es válida en México (así se definió en el setter)
    print(casilla2.region)  # Imprime None porque no se le pudo asignar Washington, por lo que sigue sin asignarse region
    casilla2.region = "Morelos"  # Verifica en los valores del mapa y encuentra morelos, por lo que lo asigna y crea la casilla
    print(casilla2.region)  # Imprime la nueva región (Morelos, en este caso)

