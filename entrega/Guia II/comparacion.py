mi_edad=float(input("Ingrese su edad: "))
su_edad=float(input("Ingresa tu edad: "))
if mi_edad>su_edad:
    dif={mi_edad}-{su_edad}
    if dif==1:
       print(f"La diferencia de edad es de por {1} año")
    else:
     print(f"Eres mayor que yo por un {1} años")
elif mi_edad<su_edad:
    dif={su_edad}-{mi_edad}
    if dif==1: 
     print(f"Soy mayor que vos por {dif} años")
    else:
     print(f"Soy mayor que vos por {dif} años")
else:
  print("Tenemos la misma edad que bien")
contraseña=str(input("Ingrese la contraseña: "))
contraseña_guardada="Programador"
if contraseña.lower() == contraseña_guardada.lower():
   print("La contraseña intruducida coincide.")
else:
   print("La contraseña ingresada no coincide.")
a=float(input("Ingrese el primer número: "))
b=float(input("Ingrese el segundo número: "))
if a > b:
 print("a es mayor que b. ")
elif a < b:
   print("a es menor que b. ")
else:
   print("a es igual a b. ")





    
 