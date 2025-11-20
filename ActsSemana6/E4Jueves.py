print("Ejercicio 4: Busqueda en un diccionario")
try:
    telefonos = {
        "Yami": "555-1234",
        "Allision": "555-5678",
        "Saul": "555-9012"
    }
    nombre = input("¿De quien quieres el telefono?")
    telefono = telefonos[nombre]
    print(f"El telefono de{nombre} es: {telefono}")
except KeyError:
    print("ERROR: Ese nombre no esta en la agenda")
