print("\nEjercicio 1\n")
canciones = ["As It Was", "Flowers","Vampire", "Cruel Summer", "Calm Down"]
print("MIS CANCIONES FAVORITAS:")
print(canciones[0])
print(canciones[1])
print(canciones[2])
print(canciones[3])
print(canciones[4])

print("\nEjercicio 2\n")
amigos = []
print("Lista inicial:", amigos)
amigos.append("Andrea")
print("Después de agregar Andrea:", amigos)
amigos.append("Meli")
print("Después de agregar Meli:", amigos)
amigos.append("Xime")
print("Después de agregar Xime:", amigos)
print (f"\nTotal de amigos {len(amigos)}")

print("\nEjercicio 3\n")
calificaciones = [98, 90, 88, 92, 89]
print("Tus calificaciones:", calificaciones)
suma = sum(calificaciones)
promedio = suma / len(calificaciones)
print(f"Tu promedio es: {promedio}")
mejor = max(calificaciones)
peor = min(calificaciones)
print(f"Mejor calificación: {mejor}")
print(f"Peor calificación: {peor}")

print("\nEjercicio 4\n")
carrito = []
print("Agregando productos al carrito.....")
carrito.append("Iphone 15")
carrito.append("AirPods")
carrito.append("Funda")
carrito.append("Cargador")
print("Carrito actual:", carrito)
print("Productos en el carrito:{len(carrito)}")
print("\n Eliminando funda....")
carrito.remove("Funda")
print("Carrito final:", carrito)
print(f"Total de productos: {len(carrito)}")

print("\nEjercicio 5\n")
videojuegos = ["Minecraft", "Fortnite", 
               "Valorant", "Roblox","GTA V"]
print("MI TOP 5 DE VIDEOJUEGOS:")
print(videojuegos)
print(f"\nMi favorito (posicion 0){videojuegos[0]}")
print(f"El de la posicion 5 (ultimo){videojuegos[-1]}")
print("\nCambio de opinion...")
videojuegos[0] = "Apex Legends"
print("Top 5 actualizado:")
print(videojuegos)

print("\nEjercicio 6\n")
series = ["Stranger Things", "Wednesday","The last of us",]
print("Series para ver:", series)
print("Agregaste One Piece:", series)
if "wednesday" in series:
    print("\n Si tienes Wednesday en tu lista.")
if "Breaking Bad" in series:
    print("Tienes Breaking Bad")
else:
    print("No tienes Breaking Bad en tu lista.")

print(f"\n¡Terminaste de ver series! {series[0]}")
series.pop(0)
print("Series restantes:", series)