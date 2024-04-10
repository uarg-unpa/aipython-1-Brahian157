import random

def lanzar_dado(caras):
    return random.randint(1, caras)

def main():

    print("Bienvenido al Simulador de Lanzamientos de Dados")

    cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
    tipo_dado = input("Seleccione el tipo de dado (6 para dado de 6 lados, cualquier otro número para dado personalizado): ")

    if tipo_dado == '6':
        caras_dado = 6
    else:
        caras_dado = int(input("Ingrese el número de caras de cada dado: "))

    cantidad_lanzamientos = int(input("Ingrese la cantidad de lanzamientos a realizar: "))

    lanzamiento = 0  

    while lanzamiento < cantidad_lanzamientos:  
        lanzamiento += 1  

        resultados = [lanzar_dado(caras_dado) for _ in range(cantidad_dados)]

        print(f"\nLanzamiento {lanzamiento}:")
        for i, resultado in enumerate(resultados, start=1):
            print(f"Dado {i}: {resultado}")

        suma_resultados = sum(resultados)
        promedio_resultados = suma_resultados / cantidad_dados
        maximo_resultado = max(resultados)
        minimo_resultado = min(resultados)

        print(f"Suma: {suma_resultados}")
        print(f"Promedio: {promedio_resultados}")
        print(f"Máximo: {maximo_resultado}")
        print(f"Mínimo: {minimo_resultado}")

if __name__ == "__main__":
    main()