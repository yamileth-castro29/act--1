print("Ejercicios try except - Jueves 20 de nov\n")
print("Ejercicio 1: Convertir texto a numero\n")
try:
    edad = int (input("¿Cuantos años tienes? "))
    print(f"El proximo año tendras {edad + 1}")
except ValueError:
    print("EROR: Debes escribir un numero, no texto")