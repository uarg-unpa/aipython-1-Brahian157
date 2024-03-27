edad = int(input("Ingrese su edad: "))
ingresos_mensuales = float(input("Ingrese sus ingresos mensuales en dólares: "))
if edad > 18 and ingresos_mensuales >= 100000:
    print("Usted debe pagar el impuesto.")
else:
    print("Usted no tiene que pagar el impuesto.")