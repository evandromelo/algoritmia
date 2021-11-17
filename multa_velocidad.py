"""
COMANDO if   -    sí

programa multa por exceso de velocidad
"""
# Entrada de Datos
vel = int (input('Velocidad del coche (km/h): '))
# Procesamiento
if vel > 110:
    # Resultados
    print('Te ha tocado una multa')
    valor_multa= (vel-110) * 5
    print ("valor de la multa (Euros): ", valor_multa)
    
    