def mensaje_creativo(nombre):
    mensaje = f"¡Hola {nombre}! Bienvenido a nuestro sistema!."
    return mensaje

nombre = input("Por favor, ingresa tu nombre: ")
print(mensaje_creativo(nombre))