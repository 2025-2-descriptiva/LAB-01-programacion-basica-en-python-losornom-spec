"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    datos = open("files/input/data.csv", "r").read().splitlines()

    diccionario = {}

    for renglon in datos:
        renglon = renglon.split("\t")

        if renglon[0] in diccionario:
            diccionario[renglon[0]] += 1
        else: 
            diccionario[renglon[0]] = 1

    lista = list(diccionario.items())
    lista.sort()
    return lista

