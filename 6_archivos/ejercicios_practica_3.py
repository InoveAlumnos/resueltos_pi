# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def desafio():
    print('Ejercicio de archivos')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Al final de esta función retornar (return) el stock total de tornillos
    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open (archivo, 'r')
    busca_tornillos = list(csv.DictReader(csvfile))
    
    suma_tornillos = 0
    for articulo in busca_tornillos:
        suma_tornillos += int(articulo['tornillos'])
    
    print('El stock de tornillos es:', suma_tornillos)
    csvfile.close()

    return suma_tornillos


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio()
