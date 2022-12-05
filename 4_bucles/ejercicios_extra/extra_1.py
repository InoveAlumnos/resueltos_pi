# CODE:41
# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Objetivo:
Realizar un programa que ordenes las letras de una palabra según el siguiente criterio:

La nueva palabra se debe componer de
- Primero todas las letras minúsculas ordenadas de menor a meyor.
- Luego todas las letras mayúsculas ordenadas de menor a meyor.
- Todos los dígitos impares ordenados de menor a meyor.
- Todos los dígitos pares ordenados de menor a meyor.

La palabra OrDenar1234 debería formar la siguiente nueva palabra según el criterior anterior:
--> aenrrDO1324

IMPORTANTE: Los métodos que le serán útil para deterinar si un
caracter es una letra minúscula, mayúscula o si es un dígito/número
los debe investigar por su cuenta.


Alumno:
- Comience por crear una variable llamada resultado
  para almacenar la palabra final que usted arme
  segun el criterio establecido en el enunciado.

- Deberá proveer por consola la palabra objetivo a ordenar
  la cual se almacenará en la variable llmada objetivo
- Deberá utilizar bucles para recorrer la palabra objetivo
  y deberá usar listas y todo método de strings a su disposición
  que lo ayude a resolver este desafio.
'''

print("Ordenar caracteres")
objetivo = input("Ingrese palabra de entrada:\n")
# Empezar aquí la resolución del ejercicio

print("Palabra de entrada:", objetivo)

minusculas = []
mayusculas = []
impares = []
pares = []

for letra in objetivo:
    if letra.isdigit():
        digito = int(letra)
        if (digito % 2) == 0:
            pares.append(letra)
        else:
            impares.append(letra)
    else:
        if letra.islower() == True:
            minusculas.append(letra)
        else:
            mayusculas.append(letra)

minusculas = sorted(minusculas)
mayusculas = sorted(mayusculas)
impares = sorted(impares)
pares = sorted(pares)

resultado = minusculas + mayusculas + impares + pares
resultado = "".join(resultado)
print("Palabra de salida:", resultado)