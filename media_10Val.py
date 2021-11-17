# Calcular la media de 10 valores enteros 
# que serán informados por el usuario
cont = 1
suma = 0
while cont<=10:
    # entrada de datos
    print ('Contando los números... ',cont,'\n')
    cont = int (input('Informe un número: '))
    suma = suma + cont
    cont = cont + 1
# fin while
med = suma/10
print('La media de los 10 numeros = ', med)