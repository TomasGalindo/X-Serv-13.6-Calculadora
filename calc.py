#!/usr/bin/python3
import sys
# para asegurarnos que tiene solo 4 argumentos
if len(sys.argv) != 4:
    sys.exit("Usage: python3 calculadora.py operacion operando1 operando2")

# asigno los valores de la lista
_, operacion, operando1, operando2 = sys.argv
# el guion bajo es para la variable [0] que no necesito

try:
    # si no pones la conversion te va a concatenar
    # los valores porque son string
    operando1 = float(operando1)
    operando2 = float(operando2)
except ValueError:
    sys.exit("operandos deben ser floats")

# empezamos con las operaciones

if operacion == "suma":
    print (operando1 + operando2)
elif operacion == "resta":
    print (operando1 - operando2)
elif operacion == "div":
    try:
        print(operando1 / operando2)
    except ZeroDivisionError:
        print ("Es una division por cero")
elif operacion == "mult":
    print (operando1 * operando2)
else:
    print ("solo podemos hacer 4 operaciones: suma, resta, mult y div")
