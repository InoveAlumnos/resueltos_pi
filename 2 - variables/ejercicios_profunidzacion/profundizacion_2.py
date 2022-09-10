# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que consulte por consola:
- El nombre completo de la persona
- El DNI de la persona
- La edad de la persona
- La altura de la persona

Finalmente el programa debe imprimir dos líneas de texto por separado
- En una línea imprimir el nombre completo y el DNI, aclarando de que
  campo se trata cada uno
        Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
- En la segunda línea se debe imprimir el nombre completo, edad y
  altura de la persona
  Nuevamente debe aclarar el campo de cada uno, para el que lo lea
  entienda de que se está hablando.
'''

print('Sistema de ingreso de datos')
# Empezar aquí la resolución del ejercicio
# Solicitud de nombre, apellido, DNI, edad y altura.
nombre = str(input ("Ingrese su nombre/s:"))
apellido = str(input ("Ingrese su apellido/s:"))
nombre_completo = nombre + " " + apellido
dni = str(input ("Ingrese el número de DNI:"))
edad = int(input ("¿Qué edad tiene?:"))
altura = float(input ("¿Cuál es su altura en metros (use punto como separador decimal)?:"))

# Impresión de nombre completo y DNI
print ("Nombre completo:", nombre_completo, "; DNI nº", dni)

# Impresión de nombre completo, edad y altura.
print ("Nombre completo:", nombre_completo, "; Edad", edad, "años; Estatura", altura, "metros")