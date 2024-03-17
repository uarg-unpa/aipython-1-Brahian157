mi_edad=int(input("Ingrese su edad: "))
su_edad=int(input("Ingresa tu edad: "))
if mi_edad>su_edad:
    dif=mi_edad-su_edad
    if dif==1:
       print("La diferencia de edad es de año")
if mi_edad<su_edad:
    dif=su_edad-mi_edad
    if dif==1: 
     print("La diferencia de edad es de año")
else:
 print("La diferencia de edad es de años")
contraseña=str(input("Ingrese la contraseña: "))
contraseña_guardada="Programador"
if contraseña.lower() == contraseña_guardada.lower():
   print("La contraseña intruducida coincide.")
else:
   print("La contraseña ingresada no coincide.")
print("La contraseña ingresada no coincide.")
a=float(input("Ingrese el primer número: "))
b=float(input("Ingrese el segundo número: "))
if a > b:
 print("a es mayor que b. ")
elif a < b:
   print("a es menor que b. ")
else:
   print("a es igual a b. ")





    
 