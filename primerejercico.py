ed1,titulo1=int(input("ingrese su edad: ")),input("Tiene titulo de bachiller: ").upper()
if ed1>=18:
    print("Usted es mayor de edad")
    if titulo1=="SI":
        print("Usted es apto para sacar la licencia")
    else:
        print("Usted no es apto para la licencia por su titulo")
else:
    print("Usted es menor de edad no puede tener licencia")