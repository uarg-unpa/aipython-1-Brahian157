palabra=str(input("Ingrese una palabra: "))
palabra_modificada = palabra.replace("a", "😃")
print(palabra_modificada)
frase="El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio"
palabras=frase.split()
primeras_dos_palabras= " ".join(palabras[:2])
print(primeras_dos_palabras)
frase_2= " La ciencia es una ecuación diferencial. La religión es una condición de frontera. "
frase_sin_espacios=frase_2.strip()
print(frase_sin_espacios)
frase_3="El razonamiento matemático puedeconsiderarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones.\n Que podemos llamar la intuición y el ingenio."
print(frase_3)
print("Nombre\tEdad\tPais\tCiudad\nAlexa\t250\tUSA\tCapeCod")
