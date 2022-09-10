# Python Inicial [Python]
# Proyecto integrador

# Autor: Inove Coding School
# Version: 2.0

# Importamos módulos y librerías necesarias.
import interfaz
import random
import csv


def leer_palabra_secreta(csvfilename):
    '''
    Lee las palabras secretas presentes
    en un archivo csv y retonar una 
    de manera aleatoria
    '''
    palabras = []
    with open(csvfilename, 'r') as csvfile:
        data = list(csv.DictReader(csvfile))
        for row in data:
            palabras.append(row["palabras"])
    return random.choice(palabras)


def pedir_letra(letras_usadas):
    '''
    Función que permite ingresar una letra
    por consola y la retorna.
    '''
    while True:
        letra = str(input('Ingresar una letra: ')).lower()
        # Compruebo que la letra ya no se ha ingresado anteriormente.
        # En caso de no estar la appendeo en la lista de letras_usadas.
        if letra in letras_usadas:
            print(f'Usted ya ingresó la letra "{letra}".')
        elif len(letra) > 1:
            print(f'Debe ingresar una sola letra, usted ingreso "{letra}".')
        else:
            print(f'Letra ingresada "{letra}"')
            break

    # Agregamos la letra
    letras_usadas.append(letra)
    return letra


def verificar_letra(letra, palabra_secreta):
    '''
    Función que verifica si la letra
    pertenece a la palabra a adivinar.
    '''
    if letra in palabra_secreta:
        return True
    else:
        return False


def validar_palabra(letras_usadas, palabra_secreta):
    '''
    Retorna si la palabra oculta ha sido descubierta
    '''
    validar = True
    for letra in palabra_secreta:
        if letra not in letras_usadas:
            validar = False
            break
    
    return validar


if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta('palabras.csv')
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')

