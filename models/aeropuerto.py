#
#   Javier Barreiro Portela
#   24 - 03 - 2025
from collections import deque
from models.avion import Avion

class Pista():
    def __init__(self, id: int, longitud, disponible: bool = True):
        """
                Inicializa la pista para los aviones

                Args:
                    id (int): identificador de la pista
                    longitud (float): Metros de longitud de la pista para permitir varios aviones en ella
                    disponibilidad (boolean): Si está ocupada o no la pista
                """
        self.id = id
        self.longitud = longitud
        self.disponible = disponible

        # Puede ser util en caso de que la torre decida por el motivo que sea, cerrar la pista y no esté disponible
        # Valido para abrir o cerrar la pista
        def set_disponible(self, value: bool) -> None:
            if not isinstance(value, int):
                raise "Error! Valor no aceptable."
            self.disponible = value

        # Conocer la disponibilidad de la pista
        def get_disponible(self) -> bool:
            return self.disponible

class Aeropuerto:
    def __init__(self, nombre: str, pistas: list[Pista] = None) -> None:
        self.nombre = nombre
        self.pistas = []
        if pistas is None:
            self.pistas = [Pista(1, 8000)]
        if not pistas:
            raise ValueError("Debe haber al menos una pista para agregar")
        for pista in pistas:
            self.pistas.append(pista)
        self.aviones_estacionados = deque()
        self.vuelos_programados = {}

    def asignar_avion_a_pista(self, avion: Avion):
        # Simplemente asigna el avion a dicha pista cuando esta en tierra
        # Cuando asignamos al avion ya puede solicitar el despegue
        pass

    def estacionar_avion(self, avion:Avion):
        pass

    # Administrar el estado del avion
    def administrar_aviones(self):
        pass

    # ejemplo {"ID_VUELO" : "DESTINO"}
    #         { "VY124" : "Madrid" }
    def registrar_vuelo(self, ): # Aqui podria agrear un argumento Vuelo y crear una clase para registrar vuelos
        # Aqui se registraria el vuelo y en que pista va el avion
        # Asignaria el avion a dicha pista
        pass

    def gestionar_vuelos(self):
        pass

# -----------********** PENDIENTE DE COMPROBAR     ************---------------
    # No se aun si vamos a usar esto o si vamos a gestionar algun tipo de colas
    # def asignar_avion(self, avion: Avion):
    #     if len(self.aviones_parados) < 1:
    #         # Asigna el avion y pone la pista a no disponible
    #         self.aviones_parados.append(avion)
    #         self.disponibilidad = False
    #     else:
    #         print("La pista está siendo usada. Intentalo más tarde.")
    #
    #     if not self.aviones_parados:
    #         self.disponible = True
    #
    # # No se aun si usaremos o trataremos de alguna forma los aviones parados en la pista
    # def remover_avion(self):
    #     # quita el primer avion que entro
    #     avion =self.aviones_parados.pop()
    #     print(f"")
    #     pass