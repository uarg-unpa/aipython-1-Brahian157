def maximo_de_tres(num1, num2, num3):
    return max(num1, num2, num3)

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

resultado = maximo_de_tres(numero1, numero2, numero3)
print("El máximo entre", numero1, ",", numero2, "y", numero3, "es:", resultado)