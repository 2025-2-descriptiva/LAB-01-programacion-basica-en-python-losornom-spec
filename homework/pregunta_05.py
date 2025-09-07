"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """






    datos = open("files/input/data.csv", "r").read().splitlines()

    diccionario={}
    for line in datos:
        line = line.split("\t")
        if line[0] in diccionario:
            diccionario[line[0]] +=line[1]
        else:
            diccionario[line[0]] = line[1]

    lista = []

    for clave, element in diccionario.items():
        cadena = [int(digito) for digito in element]
        maximo = max(cadena)
        minimo = min(cadena)
        lista.append((clave, maximo, minimo))
        lista.sort()
    
    return lista