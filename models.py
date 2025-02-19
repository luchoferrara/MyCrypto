from datetime import date

import csv
import sqlite3

from . import app

RUTA_FICHERO = ''


class DBManager:
    def __init__(self, ruta):
        self.ruta = ruta

    def consultarSQL(self, consulta):

        conexion = sqlite3.connect(self.ruta)  # Conexion con la BD
        cursor = conexion.cursor()  # Abrir cursor
        cursor.execute(consulta)  # Ejecucion de la consulta
        datos = cursor.fetchall()  # Obtencion de datos
        # self.registros = []
        # nombres_columna = []
        # for columna in cursor.description:
        #   nombres_columna.append(columna[0])
        # for dato in datos:
        #   movimiento = {}
        #   indice = 0
        # for nombre in nombres_columna:
        #   movimiento[nombre] = dato[indice]
        #   indice += 1
        # self.registros.append(movimiento)
        conexion.close()  # Cerrar consulta/conexion
        # return self.registros
