matriz = [
    [15, 8],
    [23,12]
]
#Empecemos asumiendo que el primero es el mayor
mayor = matriz[0][0]
for fila in matriz:
    for elemento in fila:
        if elemento > mayor:
            mayor = elemento
#Mostramos resultados
print("La matriz es:")
for fila in matriz:
    print(elemento, end=" ")
    print()
print(f"\nEl mayor elemento es: {mayor}")
