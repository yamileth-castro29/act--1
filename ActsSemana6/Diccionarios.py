print("Ejercicios diccionarios - martes \n")
print("\nEjercicio 1\n")
#Escribe tus datos
usuario = {
    "nombre": "Yamileth",
    "edad" : 18,
    "ciudad" : "Monterrey"
}
print("Diccionario completo:")
print(usuario)
print("\nAcceso a valores individuales:")
print("Nombre:", usuario["nombre"])
print("Edad:", usuario["edad"])
print("Ciudad:", usuario["ciudad"])


print("\nEjericio2\n")
videojuego = {
    "titulo": "Minecraft", 
    "plataforma": "PC"
}
print("Diccionario original:")
print(videojuego)
videojuego["año"] = 2019
videojuego["genero"] = "Sandbox"
videojuego["es_multiplicador"] = True

print("\nDiccionario despues de agregar datos:")
print(videojuego)
print("\nNuevos datos agregados:")
print("Año:", videojuego["año"])
print("Genero:", videojuego["genero"])
print("¿Es multiplicador?:", videojuego["es_multiplicador"])


print("\nEjericio 3\n")
perfil = {
    "usuario": "Yamileth",
    "seguidores": 750,
    "publicaciones": 4,
    "ciudad": "Monterrey"
}
print("Perfil original:")
print(perfil)
print("Seguidores antes:", perfil["seguidores"])
perfil["seguidores"] = 1500
perfil["publicaciones"] = 45,
print("\nPerfil actualizado:")
print(perfil)
print("Seguidores ahora:", perfil["seguidores"])
print("Publicaciones ahora:", perfil["publicaciones"])


print("\nEjercicio 4 - eliminar un par clave-valor\n")
cuenta = {
    "usuario": "Yam_cas29",
    "email": "castropardoyamileth@gmail.com",
    "telefono":"8115044097",
    "ciudad": "Monterrey"
}
print("Cuenta original(con telefono):")
print(cuenta)
del cuenta["telefono"]
print("\nCuenta despues de eliminar telefono:")
print(cuenta)
print("\nVerificacion - ¿existe 'telefono'?:", "telefono" in cuenta)


print("\nEjercicio 5 - len\n")
pelicula = {
    "titulo": "After",
    "director": "Jeny Gage",
    "año": 2019,
    "genero":"Romance adolescente",
    "duracion_minutos": 106,
    "calificacion": 7.0
}
print("Pelicula:")
print(pelicula)
cantidad = len(pelicula)
print("\n¿Cuantos datos tiene el diccionario?:", cantidad)
print("El diccionario tiene", cantidad,"pares clave-valor")


print("\nEjercicio 6 - obtener las keys\n")
cancion = {
    "titulo": "Heart of Gold",
    "artista": "Shawn Mendes",
    "album": "Shawn",
    "año": 2024,
    "genero": "pop",
    "duracion_segundos": 170
}
print("Diccionario de cancion:")
print(cancion)
print("\nTodas las claves o datos del diccionario:")
claves = cancion.keys()
print(claves)

print("\nMostrando claves una por una:")
for clave in claves:
    print("-", clave)

print("Ejericio 7: obtener los values")
calificaciones = {
    "Economia": 9.7,
    "Derecho de adunas": 9.5,
    "Admin de negocios": 9.3,
    "Logistica y cadena de suministro": 9.6,
    "Mercadoctenia Internacional": 9.4
}
print("Diccionario de calificaciones:")
print(calificaciones)
print("\nTodos los valores del diccionario:")
valores = calificaciones.values()
print(valores)


