import random

def lanzar_dado(caras):
    return random.randint(1, caras)

def lanzar_dados(cantidad, caras):
    return [lanzar_dado(caras) for _ in range(cantidad)]
def calcular_resultados(resultados):
    suma= sum(resultados)
    promedio= sum / len(resultados)
    maximo= max(resultados)
    minimo= min(resultados)
    return suma, promedio, maximo, minimo
