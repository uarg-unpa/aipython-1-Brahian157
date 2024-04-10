def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

temperatura_fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
print("La temperatura en Celsius es:", temperatura_celsius)