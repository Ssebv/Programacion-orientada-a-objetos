class Vehiculos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.en_marcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f" Marca: {self.marca} \n Modelo: {self.modelo} \n En Marcha: {self.en_marcha} \n "
              f"Acelerando: {self.acelera}  \n Frenando: {self.frena}")


class Moto(Vehiculos):
    pass


if __name__ == "__main__":
    vehiculo = Vehiculos("Nissan", "360z")
    vehiculo.estado()
    print("-----------")
    moto = Moto("Suzuki", "Yamaha")

    moto.arrancar()
    moto.acelerar()
    moto.estado()
