puntuacion = float(input("Ingrese la puntuación del estudiante: "))

if 80 <= puntuacion <= 100:
    clasificacion = "A"
elif 70 <= puntuacion <= 79:
    clasificacion = "B"
elif 60 <= puntuacion <= 69:
    clasificacion = "C"
elif 50 <= puntuacion <= 59:
    clasificacion = "D"
elif 0 <= puntuacion <= 49:
    clasificacion = "F"
else:
    clasificacion = "Puntuación inválida"
print(f"La clasificación del estudiante es: {clasificacion}")