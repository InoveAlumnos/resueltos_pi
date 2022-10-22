# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos condicionales y operador incremento

# Objetico
# Verificar cuanta veces (contar) el usuario
# ingresa por consola un número mayor a cero
cantidad_numeros_positivos = 0

# Alumno:
# Deberá solicitar tres números enteros por consola,
# cada nuḿero entero lo debe almacenar en variables llamadas:
# numero_1
# numero_2
# numero_3
numero_1 = int(input("Ingrese el número 1:\n"))
numero_2 = int(input("Ingrese el número 2:\n"))
numero_3 = int(input("Ingrese el número 3:\n"))

# Deberá realizar un tres condicionales separados,
# en cada condicional deberá averiguar si cada número
# es mayor a cero.

# Por cada número mayor a cero (cada condicional que se cumpla)
# deberá incrementar en 1 (+= 1) la "variable cantidad_numeros_positivos"
if numero_1 > 0:
    print(f"{numero_1} es positivo")
    cantidad_numeros_positivos += 1

if numero_2 > 0:
    print(f"{numero_2} es positivo")
    cantidad_numeros_positivos += 1

if numero_3 > 0:
    print(f"{numero_3} es positivo")
    cantidad_numeros_positivos += 1

# Al finalizar, imprimir en pantalla la variable cantidad_numeros_positivos
print(cantidad_numeros_positivos)


