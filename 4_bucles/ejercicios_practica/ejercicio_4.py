# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con bucles "while"

x = 0
# Realizar un bucle "while" cuya condición de continuidad
# sea que <x sea menor a 10> y que <x sea distinto de 6>
# Colocar ambas condiciones como condicion del "while" realizando
# una condición compuesta (utilice el operador "and" o "or" según corresponda)
# En cada iteracion del bucle debe incrementar el valor de "x" en "2"
# e imprimir en pantalla el resultado de X (antes de incrementar) con print
while x < 10 and x != 6:
    print("El valor de x es", x)
    x = x + 2

print("terminamos!")
