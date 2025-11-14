#Creamos las matrices que vamos a restar
matriz_a = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]
matriz_b = [
    [2, 5, 8],
    [3, 10, 15],
    [5, 20, 25]
]       
#Crear una matriz vacia para guardar el resultado
resultado = []
for i in range(3):
    fila = []
    for j in range(3):
        resta = matriz_a[i][j] - matriz_b[i][j]
        fila.append(resta)
    resultado.append(fila)