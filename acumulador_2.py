#                                   comando for in range
# Calcular la media de 5 valores, 
# que seran informados por el usuario
suma = 0
for n in range (1,6):
    # entrada de datos
    # print('\nNúmero..................... ', n)
    x = float(input('Informe el valor: '))
    # Procesamiento 1
    suma = suma + x
    n=n+1
# fin for
#Procesamiento 2
med = suma/n
# Resultados
print('La media de los 5 numeros = ', med)
