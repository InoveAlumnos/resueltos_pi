# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios con funciones y módulos
import random

'''
Enunciado:
Crear la función "contar"
Utilizar la función "lista_aleatoria" creada antes 
para generar una lista de 5 números en
un rango de 1 a 6 inclusive

lista_numeros = lista_aleatoria(inicio, fin, cantidad)

Alumno:
- Generar una una nueva funcion que se llame "contar",
que cuente la cantidad de veces que un número (pasado
por parámetro a la función) se repite en la lista
(también pasada por parámetro)
- Primer parámetro --> número a buscar y contar
- Segundo parámetro --> la lista de números
Para saber cuantas veces se repiten el elemento pasado
en la lista pueden usar el método nativo de list "count"
'''

# --------------------------------
# Aquí copiar la función "lista_aleatoria"
# ya elaborada en el ejercicio anterior
def lista_aleatoria(inicial, final, cantidad):
    lista = []
    for _ in range(cantidad):
        numero = random.randint(inicial, final)
        lista.append(numero)

    return lista 
# --------------------------------


# --------------------------------
# Aquí dentro definir la función contar
def contar(lista, buscado):
    tres = lista.count(buscado)
    return tres


# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    inicio = 0
    fin = 10
    cantidad = 5

    # Alumno: Utilizar la función "lista_aleatoria"
    # para que genere una lista de 5 números que esten comprendidos
    # entre los números 1 al 6 inclusive

    # lista_numeros = lista_aleatoria()
    lista_numeros = lista_aleatoria(inicio, fin, cantidad)

    # Imprimir en pantalla "lista_numeros" que tendrá
    # los valores retornado por la función "lista_aleatoria":

    # print(lista_numeros)
    print('Mi lista aleatoria es:', lista_numeros)

    # Luego quiero averiguar cuantas veces se repite el numero 3
    # en la lista aleatoria creada
    #buscado = 3
    # cantidad_tres = contar(lista_numeros, 3)
    cantidad_tres = contar(lista_numeros, 3)

    # print(cantidad_tres)
    print('El 3 aparece', cantidad_tres, 'veces')
    print("terminamos")
