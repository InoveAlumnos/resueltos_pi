# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio.

# Ingreso de tres palabras:
palabra_1 = str(input('Ingrese la primera palabra:').lower())
palabra_2 = str(input('Ingrese la segunda palabra:').lower())
palabra_3 = str(input('Ingrese la tercera palabra:').lower())

# Determinación de la forma de ordenamiento.
print('¿Cómo desea ordenar las palabras?')
eleccion = int(input('Si desea hacerlo alfabéticamente, ingrese 1; Si desea hacerlo por cantidad de letras, ingrese 2:'))

# Ordenamiento
if eleccion == 1:
    # Determinación del orden alfabético de la última a la primera.
    if palabra_1 > palabra_2 and palabra_1 > palabra_3:
        mayor = palabra_1
        if palabra_2 > palabra_3:
            intermedia = palabra_2
            menor = palabra_3      
        else:
            intermedia = palabra_3
            menor = palabra_2
        print(f'{mayor}, {intermedia}, {menor}.')

    elif palabra_2 > palabra_3:
        mayor = palabra_2
        if palabra_1 > palabra_3:
            intermedia = palabra_1
            menor = palabra_3
        else:
            intermedia = palabra_3
            menor = palabra_1
        print(f'{mayor}, {intermedia}, {menor}.')

    else:
        mayor = palabra_3
        if palabra_1 > palabra_2:
            intermedia = palabra_1
            menor = palabra_2
        else:
            intermedia = palabra_2
            menor = palabra_1
        print(f'{mayor}, {intermedia}, {menor}.')

elif eleccion == 2:
    # Determinación de la longitud de las palabras.
    largo_palabra_1 = len(palabra_1)
    largo_palabra_2 = len(palabra_2)
    largo_palabra_3 = len(palabra_3)

    # Ordenamiento por longitud de manera decreciente.
    # Aclaración: a igual longitud ordena de manera alfabética de la última a la primera.
    if largo_palabra_1 > largo_palabra_2 and largo_palabra_1 > largo_palabra_3:
        largo_mayor = palabra_1
        if largo_palabra_2 > largo_palabra_3:
            largo_medio = palabra_2
            largo_menor = palabra_3
        else:
            largo_medio = palabra_3
            largo_menor = palabra_2
        print(f'{largo_mayor}, {largo_medio}, {largo_menor}.')

    elif largo_palabra_2 > largo_palabra_3:
        largo_mayor = palabra_2
        if largo_palabra_1 > largo_palabra_3:
            largo_medio = palabra_1
            largo_menor = palabra_3
        else:
            largo_medio = palabra_3
            largo_menor = palabra_1
        print(f'{largo_mayor}, {largo_medio}, {largo_menor}.')

    else:
        largo_mayor = palabra_3
        if largo_palabra_1 > largo_palabra_2:
            largo_medio = palabra_1
            largo_menor = palabra_2
        else:
            largo_medio = palabra_2
            largo_menor = palabra_1
        print(f'{largo_mayor}, {largo_medio}, {largo_menor}.')

else:
    print("Elección errónea. Reinicie el programa.")
