#EJERCICIO 1
#PARTE1
print("Empezando a trabajar con Python")
print("Realizado por: 'David Mateo López Bulla")  

# Consultando los tipos de valores
print("El tipo de dato de 875 es:")
print(type(875))

print("El tipo de dato de 4.89 es:")
print(type(4.89))

print("El tipo de dato del texto: Now is better than never. es:")
print(type("Now is better than never."))

print("El tipo de dato de 1.32 es:")
print(type(1.32))

print("¿El valor 5 + 8i corresponde a un valor entero?")
print(type(5 + 8j))

print("¿El valor 8.2 corresponde a un valor entero?")
print(type(8.2))

print("¿El texto: Readability counts. corresponde a un string?")
print(type("Readability counts.\n"))

#PARTE2

print("Programa que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones:")

# Ciclo para realizar 5 interacciones
for i in range(5):
    # Pidiendo al usuario que ingrese un valor
    valor = input("Interacción " + str(i+1) + ", ingrese un valor cualquiera: ")
            
    
    # Mostrando el tipo de dato del valor ingresado
    print("Este tipo de dato en Python es: ", type(valor))

# Mensaje final
print("¡YA NO SE HARÁN MÁS INTERACCIONES!")