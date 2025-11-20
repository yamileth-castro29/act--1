print("Ejericio 5: Multiplicar numero por texto")
try:
    numero = int(input("¿Cuantas veces quieres ver el mensaje?"))
    mensaje = input("¿Cual es el mensaje?")
    print(mensaje * numero)
except ValueError:
    print("ERROR: Debes escribir un numero entero")
except TypeError:
    print("ERROR: No se puede hacer esa operacion")
    
