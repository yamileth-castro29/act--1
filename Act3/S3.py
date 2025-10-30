print("="*22)
print("Ejercicio 1\n")

edad = int(16)

if edad >= 16:
    print("Podes jugar \n")
else: 
    print("No podes jugar \n")

print("="*18)
print("Ejercicio 2\n")

calificacion = int(input("Ingresa tu calificacion(0-100):"))

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Ay!, no aprobado")


#Ejercicio 2 con AND
print("Ejercicio 2 con AND\n")

calificacion = int(input("Ingresa tu calificacion(0-100):"))

if calificacion >= 90 and calificacion <= 100:
    print("Excelente")
elif calificacion >= 70 and calificacion < 90:
    print("Aprobado")
elif calificacion >= 0 and calificacion < 70:
    print("Ay!, no aprobado")
else:
    print("Calificacion invalida")



