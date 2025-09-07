"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    datos = open("files/input/data.csv", "r").read().splitlines()

    diccionario = {}

    for lines in datos:
        lines = lines.split("\t")
        columna5 = lines[4]
        columna5 = columna5.split(",")
        contador = 0
        for elemento in columna5:
            elemento = elemento.split(":")
            elemento1 = int(elemento[1])
            contador += elemento1
        if lines[0] in diccionario:
            diccionario[lines[0]] += contador
        else:
            diccionario[lines[0]] = contador
    diccionario = dict(sorted(diccionario.items()))
    return diccionario
