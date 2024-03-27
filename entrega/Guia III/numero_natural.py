N = int(input("Introduce un número natural N: "))
suma = 0
for i in range(1, N + 1):
    suma += i
    if i == N:
        print(f"{i}", end=" ")
    else:
        print(f"{i} +", end=" ")
print(f"= {suma}")

N = int(input("Introduce un número natural N: "))
suma = 0
numero = 2 

for _ in range(N):
    suma += numero
    numero += 2 
print(f"La suma de los primeros {N} números pares es: {suma}")