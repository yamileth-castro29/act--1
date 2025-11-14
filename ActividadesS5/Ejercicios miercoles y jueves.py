#Ejercicios miercoles
def mostar_perfil():
    print("Usuario: @TaylorSwift")
    print("Seguidores: 1.2b")
    print("Bio: Cantante")

mostrar_perfil()
print()
mostrar_perfil()

#Ejericio 2
def calcular_horas_tiktok(minutos_por_dia):
    minutos_totales = minutos_por_dia * 7
    horas_totales = minutos_totales / 60
    return horas_totales    
horas = calcular_horas_tiktok(30)
print(f"Ves {horas} horas de Tiktok a la semana")
horas2 = calcular_horas_tiktok(60)
print(f"Ves {horas2} horas de Tiktok a la semana")

#Ejercicio 3
def puedo_comprar(dinero_que_tengo, precio_producto):
    if dinero_que_tengo >= precio_producto:
        return "Si puedes comprarlo"
    else:
        return "No te alcanza"
resultado1 = puedo_comprar(500, 300)
print(f"Tenis nuevos: {resultado1}")
resultado2 = puedo_comprar(150, 800)
print(f"Celular nuevo: {resultado2}")
resultado3 = puedo_comprar(100, 100)
print(f"Audifonos: {resultado3}")

#Ejercicio 4
print("\nEjercicio 4")
def calcular_likes_totales(likes_foto1, likes_foto2, likes_foto3):
    total = likes_foto1 + likes_foto2 + likes_foto3
    return total
total = calcular_likes_totales(150, 230, 89)
print(f"Tienes {total} likes en total")
total2 = calcular_likes_totales(800, 420, 300)
print(f"Tienes {total2} likes en total")

#Ejercicio 5
print("\nEjercicio 5")
def aplicar_descuento(precio_original, porcentaje_descuento):
    descuento = precio_original * porcentaje_descuento / 100
    precio_final = precio_original - descuento
    return precio_final
precio_final1 = aplicar_descuento(1000, 20)
print(f"El precio final: $ {precio_final1}")
precio_final2 = aplicar_descuento(500, 10)
print(f"El precio final: $ {precio_final2}")

#Ejercicio 6
print("\nEjercicio 6")
def calcular_promedio(cal1, cal2, cal3):
    suma = cal1 + cal2 + cal3
    promedio = suma / 3
    return promedio
promedio = calcular_promedio(85, 90, 78)
print(f"Tu promedio es: {promedio}")

promedio2 = calcular_promedio(100, 95, 88)
print(f"Tu promedio es: {promedio2}")