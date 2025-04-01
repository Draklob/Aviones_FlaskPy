#
#   Javier Barreiro Portela
#   24 - 03 - 2025
from collections import deque
from avion import Avion


class Pista:
    def __init__(self, id: int, longitud, disponibilidad: bool = True):
        """
        Inicializa la pista para los aviones

        Args:
            id (int): identificador de la pista
            longitud (float): Metros de longitud de la pista para permitir varios aviones en ella
            disponibilidad (boolean): Si está ocupada o no la pista
        """
        self.id = id
        self.longitud = longitud
        self.disponibilidad = disponibilidad
        self.aviones_en_cola = deque()

    # Puede ser util en caso de que la torre decida por el motivo que sea, cerrar la pista y no esté disponible
    # Valido para abrir o cerrar la pista
    def set_disponibilidad(self, value: bool):
        if not isinstance(value, int):
            raise "Error! Valor no aceptable."
        self.disponibilidad = value

    # Conocer la disponibilidad de la pista
    def get_disponibilidad(self):
        return self.disponibilidad

    def asignar_avion(self, avion: Avion):
        if len(self.aviones_en_cola) < 1:
            # Asigna el avion y pone la pista a no disponible
            self.aviones_en_cola.append(avion)
            self.disponibilidad = False
        else:
            print("La pista está siendo usada. Intentalo más tarde.")

        if not self.aviones_en_cola:
            self.disponibilidad = True

    def remover_avion(self):
        # quita el primer avion que entro
        avion =self.aviones_en_cola.pop()
        print(f"")
        pass