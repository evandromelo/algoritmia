while True:
    # Inicio de mi programa
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
    # Fin de mi programa
    #
    # Ejecutar de nuevo o parar?
    op=int(input('\n¿Desea continuar? 1 para SÍ y 2 para NO ==> '))
    if op!=1:
       break
# fin while
#
print ('¡FIN del programa a petición del usuario!')

