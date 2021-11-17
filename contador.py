"""
Problema: Crear un programa que imprima de 1 hasta un número informado 
por el usuario.
"""
#                       Contador
fin = int(input('Informe hasta que numero imprimir? '))
# fin es la condición de parada
x = 1   
# valor inicial de la variable
while x <= fin:
    print(x)
    x = x + 1 # x es el contador
print ('fin del programa')