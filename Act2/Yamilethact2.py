def calcular_precio_visita(edad, tipo_visitante):
    # definir descuentos
    descuentos = {
        "adulto mayor": 0.12,
        "profesor": 0.10,
        "estudiante": 0.10
    }
    # precio base
    if edad < 3:
        return 0.0
    elif edad < 18:
        precio = 30.0
    else:
        precio = 45.0

    descuento = descuentos.get(tipo_visitante, 0.0)
    return precio * (1 - descuento)

def main():
    total = 0.0
    try:
        n = int(input("Ingrese el número de visitantes que pagarán boleto: "))
        if n <= 0:
            print("El número de visitantes debe ser mayor que cero.")
            return
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        return

    for i in range(1, n + 1):
        print(f"\nVisitante {i}:")
        # edad válida
        try:
            edad = int(input("  Ingrese la edad del visitante: "))
        except ValueError:
            print("  Edad inválida. Se omite este visitante.")
            continue  # mejor que break, continuar con el siguiente

        if edad < 0:
            print("  Edad negativa no permitida. Se omite este visitante.")
            continue

        # tipo de visitante
        tipo = input("  Tipo de visitante (adulto mayor / profesor / estudiante / otro): ")
        tipo = tipo.strip().lower()

        if tipo not in ("adulto mayor", "profesor", "estudiante", "otro"):
            print("  Tipo de visitante no reconocido. Se considerará sin descuento.")
            tipo = "otro"

        precio_visita = calcular_precio_visita(edad, tipo)
        print(f"  Precio para este visitante: ${precio_visita:.2f}")
        total += precio_visita

        # ejemplo de break: si total superara cierto valor (opción extra)
        if total > 1000:
            print("  Se alcanzó el monto máximo permitido. Finalizando registros.")
            break

    print(f"\nTotal a pagar por todos los visitantes registrados: ${total:.2f}")

if __name__ == "__main__":
    main()
