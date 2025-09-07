"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    datos = open("files/input/data.csv", "r").read().splitlines()

    meses = {}

    for lines in datos:
        lines = lines.split("\t")
        fecha = lines[2].split("-")
        fecha = fecha[1]
        if fecha in meses:
            meses[fecha] += 1
        else:
            meses[fecha] = 1
    lista = list(meses.items())
    lista.sort()
    return lista