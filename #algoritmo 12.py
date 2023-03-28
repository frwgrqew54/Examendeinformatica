#algoritmo 12
# Definimos una función para cada operación

def suma(n):
    resultado = 0
    for i in range(n):
        num = float(input("Introduce el número {}: ".format(i+1)))
        resultado += num
    return resultado

def resta(n):
    resultado = float(input("Introduce el número 1: "))
    for i in range(1, n):
        num = float(input("Introduce el número {}: ".format(i+1)))
        resultado -= num
    return resultado

def multiplicacion(n):
    resultado = 1
    for i in range(n):
        num = float(input("Introduce el número {}: ".format(i+1)))
        resultado *= num
    return resultado

def division(n):
    resultado = float(input("Introduce el número 1: "))
    for i in range(1, n):
        num = float(input("Introduce el número {}: ".format(i+1)))
        resultado /= num
    return resultado

# Pedimos al usuario que elija la operación que desea realizar

operacion = input("Introduce la operación que quieres realizar (suma, resta, multiplicacion, division): ")

# Pedimos al usuario que introduzca la cantidad de números que desea utilizar para la operación

n = int(input("¿Cuántos números quieres {}? ".format(operacion)))

# Realizamos la operación correspondiente

if operacion == "suma":
    resultado = suma(n)
elif operacion == "resta":
    resultado = resta(n)
elif operacion == "multiplicacion":
    resultado = multiplicacion(n)
elif operacion == "division":
    resultado = division(n)
else:
    print("Operación no válida")

# Mostramos el resultado

print("El resultado de la {} es {}".format(operacion, resultado))