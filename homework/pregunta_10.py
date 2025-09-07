"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]

    """

    datos = open("files/input/data.csv", "r").read().splitlines()

    lista = []

    for lines in datos:
        lines = lines.split("\t")

        columna4 = lines[3]
        columna4 = columna4.split(",")
        columna5 = lines[4]
        columna5 = columna5.split(",")
        columna4 = len(columna4)
        columna5 = len(columna5)
        lista.append((lines[0], columna4, columna5))
    return lista

