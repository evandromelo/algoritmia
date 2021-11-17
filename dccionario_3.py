# diccionario
stock={'platano':240,
       'naranja':1000,
       'pera':400,
       'piña':150}
print('*** stock actual ***')
for fruta in stock.keys():
    clave = fruta
    cant_frutas = stock [fruta]
    print ('%d unidades de %s' %(cant_frutas, clave))




