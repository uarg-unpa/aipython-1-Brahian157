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

    
 