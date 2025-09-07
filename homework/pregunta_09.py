"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    datos = open("files/input/data.csv", "r").read().splitlines()

    diccionario = {}

    for lines in datos:
        lines = lines.split("\t")
        lines = lines[4]
        lines = lines.split(",")
        for elemento in lines:
            elemento = elemento.split(":")
            if elemento[0] in diccionario:
                diccionario[elemento[0]] +=1
            else:
                diccionario[elemento[0]] =1
    diccionario = dict(sorted(diccionario.items()))
    return diccionario








