class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print("Estoy caminando")


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print("Estoy pedaleando")


def main():
    persona = Persona("Seba")
    persona.avanza()

    ciclista = Ciclista("Tomas")
    ciclista.avanza()


if __name__ == "__main__":
    main()

