#
#   Javier Barreiro Portela
#   24 - 03 - 2025
from collections import deque

from pista import Pista
from avion import Avion, Prioridad

class TorreControl:
    def __init__(self):
        # Agregar varias pistas para poder usarlas
        pista_1 = Pista(1, 8_000)
        pista_2 = Pista(2, 2_500)
        self.pistas = [pista_1, pista_2]
        # Agregar un par de aviones de inicio
        avion_1 = Avion(1, "Airbus 340", self, Prioridad.NORMAL)
        avion_2 = Avion(2, "Boeing 737", self, Prioridad.VIP)
        avion_3 = Avion(3, "Airbus 330", self, Prioridad.NORMAL)
        avion_4 = Avion(4, "Airbus 319", self, Prioridad.NORMAL)

        self.cola_aterrizaje = deque()
        self.cola_despegue = deque()

        # Asignamos de forma automatica a estos aviones a las pistas
        self.asignar_pista(1, avion_1)
        self.asignar_pista(1, avion_2)
        self.asignar_pista(2, avion_3)
        self.asignar_pista(2, avion_4)

    def asignar_pista(self, id_pista, avion: Avion):
        for pista in self.pistas:
            if pista.id == id_pista:
                # Pista encontrada, asignamos el avion a dicha pista.
                # Metemos en cola al avion
                pista.asignar_avion(avion)
                pass

    def solicitar_aterrizaje(self, avion):
        print(f"Avion {avion.id} solicita aterrizar.")
        self.cola_aterrizaje.append(avion)
        self.gestionar_pistas()

    def solicitar_despegue(self, avion):
        # Recorre ambas pistas y comprueba si alguno
        print(f"Avion {avion.id} solicita despegar.")
        self.cola_despegue.append(avion)
        self.gestionar_pistas()

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

    def mostrar_estado(self):
        pass

ME QUEDA GESTIOAR LAS PISTAS PARA ATERRIZAR Y DESPEGAR LOS AVIONES