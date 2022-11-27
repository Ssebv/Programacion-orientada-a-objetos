import random
class Hotel:
    def __init__(self, nombre, cantidad_habitaciones, pisos, estacionamientos):
        self.nombre = nombre
        self.cantidad_habitaciones = cantidad_habitaciones
        self.pisos = pisos
        self.estacionamientos = estacionamientos
        self._habitaciones_utilizadas = 0
        self._huespedes = 0

 
        if self._habitaciones_utilizadas == cantidad_habitaciones:
            print("El hotel se encuentra al tope de su capacidad")
 
    def reserva(self,nombre, apellido, dia_inicio, dia_termino, mes):
        dia_reserva = dia_inicio, mes
        dia_fin_reserva = dia_termino, mes
        
        rand = random.randint(0, self.cantidad_habitaciones)
        print (f"Su reserva es desde el dia {dia_reserva} hasta el dia {dia_fin_reserva} señor {nombre+ ' ' + apellido}")
        habitacion = rand    
        codigo_reserva = random.randint(0,10000)   
        print(f"Su habitacion es la {habitacion}")
        print(f"Su codigo de reserva es {codigo_reserva}")
        
    def checkin(self, codigo_reserva, cantidad_huespedes, habitacion): 
        codigo_reserva = codigo_reserva
        self._habitacion = Habitacion(cantidad_huespedes, habitacion)
        self._huespedes += cantidad_huespedes
        return habitacion, cantidad_huespedes
    
    def checkout(self, cantidad_huespedes):
        self._huespedes -= cantidad_huespedes
    
    def ocupacion_total(self):
        return self._huespedes   

        

class Habitacion:
    def __init__(self,cantidad_usuarios, numero_habitacion):
        self.cantidad_usuarios = cantidad_usuarios
        self.numero_habitacion = numero_habitacion

        
if __name__ == '__main__':
    hotel1 = Hotel('Mar', 23, 3, 23)


    hotel1.reserva("Juan", "Carlos", 12, 24, 3)
    hotel1.reserva("Juan1", "Carlos", 12, 22, 3)
    hotel1.reserva("Juan2", "Carlos", 12, 26, 3)
    hotel1.checkin(23,2,12)

    print("--------")
    print(hotel1.ocupacion_total())