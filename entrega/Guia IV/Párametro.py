def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    cadena_invertida = cadena[::-1]
    return cadena == cadena_invertida

cadena = input("Ingrese una cadena de texto para verificar si es un palíndromo: ")
if es_palindromo(cadena):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")