# -*- coding: utf-8 -*-
"""
UVa - Curso Python 

@author: Evandro
"""
print('....... TIPO DE TRIANGULO .......')
a=int(input('Informe lado A:'))
b=int(input('Informe lado B:'))
c=int(input('Informe lado C:'))

if (a<(b+c) and b<(a+c) and c<(b+c)): # si forman un tringulo
    if (a==b and a==c):
        print('Equilatero')
    elif (a==b or a==c or b==c):
        print('Isosceles')
    else:
        print('Escaleno')
else: 
    print('Los lados informados no forman un triangulo')


