#Suma de matrices de 3x3
matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

#Crear la matriz resultado
resultado = []
print("\Ejercicio 2: Cambia los numeros\n")
numeros_ej2 = [10, 33, 74, 11, 9, 22]
print("Lista original:", numeros_ej2)

n = len(numeros_ej2)
for i in range(n):
    for j in range(0, n-i-1):
        if numeros_ej2[j] > numeros_ej2[j+1]:
            numeros_ej2[j], numeros_ej2[j+1] = numeros_ej2[j+1], numeros_ej2[j]
print("Lista ordenada:", numeros_ej2)