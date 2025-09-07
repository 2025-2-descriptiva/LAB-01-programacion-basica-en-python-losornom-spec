"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    datos = open("files/input/data.csv", "r").read().splitlines()

    diccionario = {}

    for lineas in datos:
        lineas = lineas.split()
        clave = int(lineas[1])
        letra = str(lineas[0])
        if clave in diccionario.keys():
                diccionario[clave].append(letra)
        else:
            diccionario[clave] = list(letra)
    diccionario2 = {}
    for clave, valor in diccionario.items():
        newvalue = []
        for i in valor:
            if i not in newvalue:
                newvalue.append(i)
        newvalue.sort()
        diccionario2[clave] = newvalue
    lista = list(diccionario2.items())
    lista.sort()
    return lista

print(pregunta_08())