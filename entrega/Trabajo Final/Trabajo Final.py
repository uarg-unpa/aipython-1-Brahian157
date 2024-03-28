import random

def lanzar_dado(caras):
    return random.randint(1, caras)

def main():
    print("Bienvenido al Simulador de Lanzamientos de Dados")

    cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
    caras_dado = int(input("Ingrese el número de caras de cada dado: "))
    cantidad_lanzamientos = int(input("Ingrese la cantidad de lanzamientos a realizar: "))

    

        