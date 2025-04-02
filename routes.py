from flask import render_template, request, redirect, url_for
from models.torre_control import TorreControl
from models.aeropuerto import Aeropuerto, Pista
from models.avion import Avion, Prioridad

def init_routes(app):
    madrid = Aeropuerto("Madrid", [Pista(1, 8500), Pista(2, 2300)])
    torre = TorreControl()

    # Agregar un par de aviones de inicio
    avion_1 = Avion(1, "Airbus 340", Prioridad.NORMAL)
    avion_2 = Avion(2, "Boeing 737", Prioridad.VIP)
    avion_3 = Avion(3, "Airbus 330", Prioridad.NORMAL)
    avion_4 = Avion(4, "Airbus 319", Prioridad.NORMAL)


    @app.route('/')
    def index():
        return render_template('index.html')

    # Podemos crear una funcion o algo que nos permite agregar más aviones.

    # Funcion que podamos consultar los aviones en cola y sus caracteristicas
    # Esto igual podemos ir haciendolo en tiempo real? Segun la cola se actualiza, entran y salen aviones
    # y asi conseguir que sea mas visual y util.
