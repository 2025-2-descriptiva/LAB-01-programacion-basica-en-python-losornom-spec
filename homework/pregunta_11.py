"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """


    datos = open("files/input/data.csv", "r").read().splitlines()

    diccionario = {}

    for lines in datos:
        lines = lines.split("\t")
        valor = int(lines[1])
        columna4 = lines[3]
        columna4 = columna4.split(",")

        for elemento in columna4:
            if elemento in diccionario:
                diccionario[elemento] = diccionario[elemento] + valor
            else:
                diccionario[elemento] = valor
    diccionario = dict(sorted(diccionario.items()))
    return(diccionario)
