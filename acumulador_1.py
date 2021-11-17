#                                      comando while
# Calcular la media de 5 valores, 
# que seran informados por el usuario
n = 1
suma = 0
while n<=5:
    # entrada de datos
    print('\nNúmero..................... ', n)
    x = float(input('Informe el valor: '))
    suma = suma + x
    n = n + 1
# fin while
med = suma/5
print('La media de los 5 numeros = ', med)