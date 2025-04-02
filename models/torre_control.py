#
#   Javier Barreiro Portela
#   24 - 03 - 2025
from collections import deque

from models.aeropuerto import Pista
from models.avion import Avion, Prioridad

class TorreControl:
    def __init__(self):
        # Agregar varias pistas para poder usarlas
        pista_1 = Pista(1, 8_000)
        pista_2 = Pista(2, 2_500)
        self.pistas = [pista_1, pista_2]
        self.cola_aterrizaje = deque()
        self.cola_despegue = deque()

    # Asignamos el avion a una pista donde pueda aterrizar o despegar si hay sitio
    def asignar_avion_pista(self, id_pista, avion: Avion):
        for pista in self.pistas:
            if pista.id == id_pista and pista.disponible:
                # Pista encontrada, asignamos el avion a dicha pista.
                # Metemos en cola al avion
                pista.asignar_avion(avion)
                pass

    def autorizar_aterrizaje(self, avion):
        print(f"Avion {avion.id} solicita aterrizar.")
        self.cola_aterrizaje.append(avion)
        self.gestionar_pistas()

    def autorizar_despegue(self, avion):
        # Recorre ambas pistas y comprueba si alguno
        print(f"Avion {avion.id} solicita despegar.")
        self.cola_despegue.append(avion)
        self.gestionar_pistas()

    # Aqui deberemos hacer comprobaciones de quien esta en la cola
    # y como vamos a gestionar la cola y asignar dicho avion a una pista disponible
    #
    def gestionar_pistas(self):
        for pista in self.pistas:
            if pista.disponible:
                if self.cola_aterrizaje:
                    avion = self.cola_aterrizaje.popleft()
                    avion.aterrizar()
                    pista.disponible = False
                elif self.cola_despegue:
                    avion = self.cola_despegue.popleft()
                    avion.despegar()
                    pista.disponible = False

    def gestionar_emergencia(self, avion):
        pass

    def mostrar_estado(self):
        pass
