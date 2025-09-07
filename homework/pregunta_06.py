"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    datos = open("files/input/data.csv", "r").read().splitlines()
    diccionariomax = {}
    diccionariomin = {}
    for lines in datos:
        lines = lines.split("\t")
        columna = lines[4]
        columna = columna.split(",")
        for elemento in columna:
            elemento = elemento.split(":")
            unidad = int(elemento[1])
            if elemento[0] in diccionariomax:
                diccionariomax[elemento[0]] = max(diccionariomax[elemento[0]], unidad)
            else:
                diccionariomax[elemento[0]] = unidad
            if elemento[0] in diccionariomin:
                diccionariomin[elemento[0]] = min(diccionariomin[elemento[0]], unidad)
            else:
                diccionariomin[elemento[0]] = unidad
    lista1 = list(diccionariomin.items())
    lista1.sort()
    lista2 = diccionariomax
    tupla = []
    for letra in lista1:
        letra = list(letra)
        letra.append(lista2[letra[0]])
        tupla.append(tuple(letra))
    return tupla









