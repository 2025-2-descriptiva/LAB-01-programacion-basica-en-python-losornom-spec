"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    datos = open("files/input/data.csv", "r").read().splitlines()

    conteos = {}




    for line in datos:
        line = line.split("\t")

        if line[0] in conteos:
            elemento = int(line[1])
            conteos[line[0]] = conteos[line[0]]+elemento
        else:
            conteos[line[0]] = int(line[1])
    lista = list(conteos.items())

    lista.sort()
    return lista