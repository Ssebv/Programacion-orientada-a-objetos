class Mesa:
    def __init__(self, patas, meson):
        self.__patas = patas
        self.__meson = meson

    @property
    def obtener_patas(self):
        print(self.__patas)
        return self.__patas

    @obtener_patas.setter
    def modificar_patas(self, patas):
        if patas > 0.0:
            print("Vas a modificar el numero de patas")
            self.__patas = patas
            print(f"Has modificado el numero de patas a {self.__patas}")
        else:
            ValueError("No construimos mesas aereas")

    @property
    def obtener_menson(self):
        print(self.__meson)
        return self.__meson

    @obtener_menson.setter
    def modificar_meson(self, meson):
        if meson > 0:
            print("Vas a modificar el meson")
            self.__meson = meson
            print(f"Has modificado el meson a {self.__meson}")
        else:
            raise ValueError("No existe un meson con 0 centimetros y/o metros")

if __name__ == "__main__":
    mesa_casa = Mesa(4, 100)
    mesa_casa.obtener_patas
    mesa_casa.modificar_patas = 10
    mesa_casa.obtener_menson
    mesa_casa.modificar_meson = 50
    mesa_casa.obtener_patas
    mesa_casa.modificar_meson = -1
    mesa_casa.obtener_patas