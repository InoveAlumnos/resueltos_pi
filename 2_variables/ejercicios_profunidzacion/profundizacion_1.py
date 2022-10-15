# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
- El objetivo será realizar un calculadora,
- Se ingresará por consola dos números decimales (float)
- Se deberá calcular todas las operaciones entre ellos:
A) Suma  --> primero número más el segundo    
B) Resta --> primero número menos el segundo
C) Multiplicación --> primero número por el segundo
D) División --> primero número dividido el segundo
E) Exponente/Potencia --> primero número exponente el segundo

- Para todos los casos se debe imprimir en pantalla
  el resultado de la operación realizada

Alumno:
- Crear una una variable llamada numero_1
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada numero_2
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Almacenar el valor de cada operación realizada en las
  variables que usted creará con los siguientes nombres:
  suma, resta, multiplicacion, division, potencia

- Al final imprimir todos los resultados almacenados
  en esas variables
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

# Solicitud de dos números.
numero_1 = float(input("Ingrese el primer número:"))

numero_2 = float(input("Ingrese el segundo número:"))

# Cálculo de todas las operaciones indicadas
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2
potencia = numero_1 ** numero_2

# Imprimir todos los resultados:
print ("La suma entre", numero_1, "y", numero_2, "es:", suma)
print ("La resta entre", numero_1, "y", numero_2, "es:", resta)
print ("El producto entre", numero_1, "y", numero_2, "es:", multiplicacion)
print ("El cociente entre", numero_1, "y", numero_2, "es:", division)
print (numero_1, "elevado a", numero_2, "es:", potencia)