print("Ejercicio 3: Acceder a elementos de una lista")
try:
    amigos =["Juan", " Maria", "Carlos", "Sofia"]
    posicion = int (input("¿Cual es el numero de amigo que queires ver?(1-4):"))
    amigo = amigos[posicion - 1]
    print(f"Tu amigo es: {amigo}")
except IndexError:
    print("ERROR: Ese numero no existe en la lista")
except ValueError:
    print("ERROR: Debes escribir un numero")
    