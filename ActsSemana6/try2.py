print("Ejercicios try except - Jueves 20 de nov\n")
print("Ejercicio 2: Division entre numeros\n")

try:
    numero1 = int (input("Escribe el primer numero: "))
    numero2 = int (input("Escribe el segundo numero: "))
    resultado = numero1/numero2
    print(f"El resultado de {numero1} + {numero2} = {resultado}")
except ZeroDivisionError:
    print("ERROR: No puedes dividir entre dos cero")
except ValueError: 
    print("EROR: Debes escribir numeros, no texto")
    
