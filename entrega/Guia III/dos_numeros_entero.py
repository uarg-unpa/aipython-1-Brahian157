numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print(f"Números pares entre {numero1} y {numero2}:")

for numero in range(numero1, numero2 + 1):
    if numero % 2 == 0:
        print(numero)
