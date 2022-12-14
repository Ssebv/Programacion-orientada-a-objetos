
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self._libros = []

    def consultar_nombre_biblioteca(self):
        return self.nombre

    def agregar_libro(self, libro):
        self._libros.append({
            libro.titulo,
            libro.autor,
            libro.cantidad_de_paginas,
            libro.genero,
            libro.sinopsis
        })

    def consultar_libros(self):
        return self._libros

    def consultar_libro(self, id):
        return self._libros[id]

    def quitar_libro(self, id):
        self._libros.pop(id)
        
class Libro:
    def __init__(self, titulo, autor, cantidad_de_paginas, genero, sinopsis):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_de_paginas = cantidad_de_paginas
        self.genero = genero
        self.sinopsis = sinopsis
        
if __name__ == '__main__':
    ejecutar = True
    
    while(ejecutar):
        print("- - - B I B L I O T E C A S - - -")
        opcion = int(input("¿Qué vas a hacer?:\n1-Crear Biblioteca\n2-Agregar libro\n3-Ver catalogo\n4-Quitar Libro\n5-Salir\n:"))
        
        if opcion == 1:
            nombre = input("Nombre de la biblioteca: ")
            biblioteca = Biblioteca(nombre)

            print(f"Se creo la biblioteca: {biblioteca.consultar_nombre_biblioteca()}")

        elif opcion == 2:
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            cantidad_de_paginas = input("Paginas: ")
            genero = input("Genero: ")
            sinopsis = input("Sinopsis: ")

            libro = Libro(titulo, autor, cantidad_de_paginas, genero, sinopsis)
            biblioteca.agregar_libro(libro)
        
        elif opcion == 3:
            print("Catalogo de libros: ")
            
            for i in biblioteca.consultar_libros():
                print(i)

        elif opcion == 4:
            indice = int(input("Id del libro a eliminar: "))
            biblioteca.quitar_libro(indice)

        elif opcion == 5:
            ejecutar = False

        else:
            print("Opcion incorrecta")
