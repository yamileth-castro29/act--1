edad = int(input("¿Cual es tu edad? "))
genero -= input("¿Cual es tu genero favorito? (accion, comedia, terror): ").lower()

if edad < 13:
    print("Te recomendamos peliculas infantiles.")
elif edad >= 13 and edad <= 17 and genero == "accion":
    print("Te recomendamos Spider-Man (PG-13)")
elif edad >= 13 and edad <= 17 and genero == "comedia":
    print("Te recomedamos: Shrek (PG-13)")
elif edad >= 13 and edad <= 17 and genero == "terror":
    print("Te recomendamos: Scary Stories (PG-13)")
elif edad >= 18 and genero == "accion":
    print("Te recomendamos: John Wick ")
elif edad >= 18 and genero == "comedia":
    print("Te recomendamos: Superbad ")
elif edad >= 18 and genero == "terror":
    print("Te recomendamos: The Conjuring ")
