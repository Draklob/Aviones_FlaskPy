#
#   Javier Barreiro Portela
#   24 - 03 - 2025
import time
from enum import Enum

class Prioridad(Enum):
    EMERGENCIA = 1    # Emergencia: Vuelos con problemas críticos
    VIP = 2   # VIP: Vuelos prioritarios (oficiales, medicos)
    NORMAL = 3    # NORMAL: Vuelos comerciales regulares

# Estos destinos usan una distancia simbolica y totalmente aleatoria
class Destino(Enum):
    CHICAGO = 320
    NEW_YORK = 280
    CALIFORNIA = 420
    TEXAS = 450
    MIAMI = 230

MAX_COMBUSTIBLE = 203_057

class Avion:
    def __init__(self, id, modelo, prioridad, combustible=MAX_COMBUSTIBLE):
        """
        Inicializa el objeto con los atributos especificados

        Args:
            id (int): Identificador único de avión
            modelo (str): Modelo del avión
            prioridad (Prioridad): Nivel de prioridad (1 = alta, 2 media y 3 baja )
            combustible (float): Cantidad de combustible en litros
        """
        self.id = id
        self.modelo = modelo
        if not isinstance(prioridad, Prioridad):
            self.prioridad = Prioridad.NORMAL
            raise ValueError("La prioridad debe ser un valor del ENUM. Por defecto le ponemos en normal.")
        self.prioridad = prioridad
        self.combustible = min(combustible, MAX_COMBUSTIBLE)
        self.is_volando = False  # Estado inicial en tierra
        self.is_recargando_combustible = False  # Estado de si el avion está o no recargando combustible

    def despegar(self, destino: Destino):
        # Aqui deberiamos comprobar el combustible necesario para hacer x vuelo y comprobar que tiene de sobra
        # En principio vamos a hacer una comprobación de que el avión esté al 45% de su limite maximo para poder despegar
        if self.puede_volar(destino):
            # Comprobar que la torre de control nos da permiso para poder volar
            print(f"El avión {self.modelo} {self.id} solicita despegar a {destino.name}.")
            self.torre_control.solicitar_despegue(self)
            self.is_volando = True
        else:
            print("El avion no puede volar. Necesita recargar combustible")
            # Pone el avion a PRIORIDAD EMERGENCIA
            self.cargar_combustible()

    def aterrizar(self):
        if not self.is_volando:
            print(f"El avión está en tierra.")
        else:
            self.is_volando = False
            ## Le quitamos un poco de combustible
            self.combustible -= 45_000

    def puede_volar(self, destino: Destino):
        percen_combustible_actual = self.calcular_combustible()

        if self.is_volando:
            print(f"El avión {self.id} ({self.modelo}) ya está en vuelo.")
            return False
        elif percen_combustible_actual < 25:
            print(f"El avión {self.id} ({self.modelo}) tiene muy poco combustible para despegar.")
            return False
        elif self.calcular_combustible_viaje(destino) < percen_combustible_actual:
            return True

    def calcular_combustible(self):
        # Calculamos el % del combustible del avion
         return  self.combustible * 100 / MAX_COMBUSTIBLE

    def calcular_combustible_viaje(self, destino: Destino):
        combustible_vuelo= destino.value * 2.4 * 2      # Multiplicamos por 2, por ida y vuelta del avion
        return combustible_vuelo * 100 / MAX_COMBUSTIBLE

    def cargar_combustible(self):
        if not self.is_recargando_combustible:
            self.is_recargando_combustible = True
            litros_restantes = MAX_COMBUSTIBLE - self.combustible
            tiempo_total_recarga = litros_restantes / 25 # 25 litros por segundo
            print(f"Tiempo estimado de recarga del avion: {tiempo_total_recarga} segundos.")
            while self.combustible >= MAX_COMBUSTIBLE:
                print(f"Recargando avion...Combustible actual: {self.combustible:.2f} litros.")
                self.combustible = min(self.combustible + 25, MAX_COMBUSTIBLE)
                time.sleep(1)

            print(f"Recarga cmopletada. El avión {self.id} {self.modelo} está listo.")
            self.is_recargando_combustible = False

    def get_prioridad(self):
        return self.prioridad

    def set_prioridad(self, prioridad):
        if not isinstance(prioridad, Prioridad):
            raise ValueError("La prioridad debe ser un valor del ENUM")
        self.prioridad = prioridad

    def solicitar_despegue(self):
        pass

    def soliticar_aterrizaje(self):
        pass