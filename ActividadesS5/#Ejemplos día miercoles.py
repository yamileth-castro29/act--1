#Ejemplos día miercoles
print("\nEjemplo 1 mostrar el menu\n")
def mostrar_menu():
    print("=== MENU ===")
    print("1. Hamburguesa")
    print("2. Pizza")
    print("3. Tacos")

mostrar_menu()

print("\nEjemplo 2 la fav cancion\n")
def reproducir_favorita():
    print("Reproduciendo: 'Blinding Lights' de The Weeknd")

reproducir_favorita()

print("\nEjemplo 3 reglas del juego\n")
def mostrar_reglas():
    print("=== REGLAS DEL JUEGO ===")
    print(" - No hacer trampa")
    print(" - Respetar turnos")
    print(" - Divertirse")

mostrar_reglas()

#FUNCIONES CON PARAMETROS
print("\nEjemplo 4\n")

def reproducir_cancion(nombre_cancion):
    print(f"Reproduciendo: '{nombre_cancion}'")
reproducir_cancion("Bad Bunny - Tití Me Preguntó")
reproducir_cancion("Karol G - TQG")
reproducir_cancion("Taylor Swift - Anti-Hero")

def calcular_impuesto(precio):
    total = precio * 1.16 #16% de impuesto
    return total
print(calcular_impuesto(110))
print(calcular_impuesto(500))
print(calcular_impuesto(1200))
