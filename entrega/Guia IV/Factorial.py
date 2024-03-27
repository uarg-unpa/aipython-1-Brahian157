def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Ingrese un número para calcular su factorial: "))
print("El factorial de", numero, "es:", factorial(numero))
