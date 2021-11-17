# Técnica centinela
#
cont=0            #contador de notas
suma=0            #acumulador que suma las notas
centinela=-1
print(' .... Para finalizar entrada de datos informe nota=-1  ....')
nota=float(input('Informe nota del alumno (entre 0 y 100): '))

while (nota!=centinela):
         cont = cont+1
         suma= suma+nota
         nota=float(input('Informe nota del alumno (entre 0 e 100): '))
if (cont>0):
         media = suma/cont
         print ('La media de %d alumnos = %4.2f' % (cont, media))
# FIN