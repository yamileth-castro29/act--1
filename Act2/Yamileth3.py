print("Ejercicio 7. Operadores de comparación")

print ("¿He aprobado o no la materia?")
calificacion = 70
resultado5 = calificacion >= 70
print("¿Aprobé?:", resultado5)

resultado6 = calificacion > 70
print("¿Aprobé?:", resultado6)

mi_edad = 17
edad_minima = 18

resultado1 = mi_edad == 15
print ("\n¿Soy mayor de edad?(==):", resultado1)

resultado2 = mi_edad != 20
print("¿Tengo 18 años?(!=):", resultado2)

resultado3 = mi_edad < 18
print("¿Mi edad es menor que 18?(<):", resultado3)

resultado4 = mi_edad <= 10
print("¿Mi edad es menor o igual a 10?(<=):", resultado4)




print("Ejercicio 8. Operadores lógicos")
tengo_internet = True
tengo_cuenta = True

puedo_jugar = tengo_internet and tengo_cuenta
print("\n¿Puedo jugar? (ambas True):", puedo_jugar)

tengo_internet2 = True
tengo_cuenta2 = False
puedo_jugar2 = tengo_internet2 and tengo_cuenta2
print("¿Puedo jugar? (una es False):", puedo_jugar2)

tengo_celular = True
tengo_tablet = False
tengo_dispositivo = tengo_celular or tengo_tablet
print("\n¿Tengo dispositivo? (al menos una True):", tengo_dispositivo)

esta_lloviendo = False
puedo_salir = not esta_lloviendo
print("¿Puedo salir? (NOT False = True):", puedo_salir)