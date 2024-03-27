numero = int(input("Introduce un número entero positivo mayor a 3: "))

while numero <= 3:
    numero = int(input("El número debe ser mayor a 3. Por favor, inténtalo de nuevo: "))

print("Números impares hasta", numero, ":")

for i in range(1, numero + 1, 2):
    print(i)