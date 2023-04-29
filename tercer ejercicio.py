ed1,titulo1=int(input("ingrese su edad: "))
if ed1>=18:
    print("Usted es mayor de edad")
    input("Tiene titulo de bachiller: ").upper()
    if titulo1=="SI":
        print("Usted es apto para sacar la licencia")
    else:
        print("Usted no es apto para la licencia por su titulo")
else:
    print("Usted no es mayor de edad")
    if ed1>=16:
        print("Existe la posibilidad de un permiso de aprendizaje")
    else:
        print("Usted no es apto para sacar la licencia")
    