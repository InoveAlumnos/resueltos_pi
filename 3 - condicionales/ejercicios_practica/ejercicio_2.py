# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n').lower())

texto_2 = str(input('Ingrese la segunda palabra:\n').lower())

'''
Al final del input agregué el método lower porque sin hacer
esa modificación, al comparar la misma palabra escrita una
vez con mayúscula inicial y la otra toda en minúscula (ej.
Argentina y argentina) se ordenaba alfabéticamente poniendo
primero la escrita con mayúscula.
Algo similar ocurría con dos palabras distintas que comenzaran
con la misma letra, pero una de ellas con mayúscula inicial y
la otra con minúscula (ej. Rumbo y rumba). sin el método lower
el programa ordenaba "Rumbo" y después "rumba", siendo que van
al revés.
'''

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 < texto_2:
   print(f'{texto_1} precede en el orden alfabético a {texto_2}.')
elif texto_1 > texto_2:
    print(f'{texto_2} precede en el orden alfabético a {texto_1}.')
else:
    print(f'Ingresó dos veces la misma palabra.')

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) > len(texto_2):
    print(f'{texto_1} tiene más letras que {texto_2}.')
elif len(texto_1) < len(texto_2):
    print(f'{texto_2} tiene más letras que {texto_1}.')
else:
    print(f'{texto_1} y {texto_2} tienen la misma cantidad de letras.')

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

# Las siguientes variables toman como valor la primera letra de cada palabra.
inicial_texto_1 = texto_1[0] 
inicial_texto_2 = texto_2[0]

if inicial_texto_1 > inicial_texto_2:
    print(f'La primera letra de {texto_1} es mayor que la primera letra de {texto_2}.')
elif inicial_texto_1 < inicial_texto_2:
    print(f'La primera letra de {texto_2} es mayor que la primera letra de {texto_1}.')
else:
    print(f'Las iniciales de {texto_1} y {texto_2} son la misma letra.')

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_1:
    print(f'Se verifica que {copia_texto_1} es igual a {texto_1}.')

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 != texto_2:
    print(f'Se verifica que {copia_texto_1} es distinto a {texto_2}.')
else:
    print(f'{copia_texto_1} es igual a {texto_2}.')
    