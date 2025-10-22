print("Ejercicio 9. Operadores de asignacion\n")

puntos = 0
print("Puntos iniciales:", puntos)

puntos += 10
print("Ganaste 10 puntos (+=):", puntos)

puntos -= 5
print("Perdiste 5 puntos (-=):", puntos)

puntos *= 2
print ("¡Puntos x2! (*=)")

puntos /= 2
print("Dividir puntos (/=):", puntos)


print("Ejercicio 10. Operadores de identidad\n")
print ("=== ¿SON LA MISMA COSA? ===")
lista1 = ["manzana", "pera"]
lista2 = ["manzana", "pera"]
lista3 = lista1

print ("¿lista1 es lista2? (is):", lista1 is lista2)
print ("¿lista1 es lista3? (is):", lista1 is lista3)
print ("¿lista1 NO es lista2? (is not):", lista1 is not lista2)