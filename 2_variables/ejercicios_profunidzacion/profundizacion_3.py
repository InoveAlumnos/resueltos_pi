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

# Ejercicios de práctica con cadenas
'''
Enunciado:
Realice un programa que reciba por consola su nombre completo
e imprima en pantalla su nombre en los siguientes formatos:
- Todas las letras en minúsculas
- Todas las letras en mayúsculas
- Solo la primera letra del nombre en mayúscula

NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
de strings:
- lower
- upper
- capitalize

Puede buscar en internet como usar en Python estos métodos.
Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

Link de referencia:
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

Cualquier duda con estos métodos pueden consultarla por el campus
'''

print('Ahora si! buena suerte')
# Empezar aquí la resolución del ejercicio
# Solicitud de nombre completo (nombre y apellido).
nombre_completo = str(input ("Escriba aquí su nombre completo (nombre y apellido):"))

# Aplicación del método lower e impresión del resultado.
# Se aplica el método lower directamente sobre la variable nombre_completo.
print (nombre_completo.lower())

# Aplicación del método upper e impresión del resultado.
# Se crea una variable en la que se aplica el método upper a la variable nombre_completo.
# Se imprime la variable creada.
nombre_completo_upper = nombre_completo.upper()
print (nombre_completo_upper)

# Aplicación del método capitalize e impresión del resultado.
print (nombre_completo.capitalize())