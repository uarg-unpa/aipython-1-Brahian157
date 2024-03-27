def invertir_string(cadena):
    return cadena[::-1]

cadena = input("Ingrese una cadena de texto: ")
resultado = invertir_string(cadena)
print("El string invertido es:", resultado)