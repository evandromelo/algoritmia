# Comando while
op=1
while op==1:
         # Definição das funções

        def CparaF(C):
                F=1.8*C+32
                return F

        def FparaC(F):
                C=5/9*(F-32)
                return C

        def CparaK(C):
            K=C+273
            return K

        def KparaC(K):
            C=K-273
            return C
        # fim definição funções

        # inicio programa
        # apresentação via print do programa
        print('Esse programa oferece 4 opções')
        print('de transformção de temperatura:')
        print('        1.ºC para °F')
        print('        2.ºF para °C')
        print('        3. K para °C')
        print('        4.ºC para  K')
        # entrada de dados 0
        tipo=int(input('Digite o numero da transformação desejada: '))
        # processamento
        if tipo == 1:
            gC=float(input('Digite a temperatura em °C: ')) # entrada de dados 1
            gF=CparaF(gC)  # chamada da função
            # Resultado 1
            print (gC,'°C =',gF,'°F')
        elif tipo==2:
            gF=float(input('Digite a temperatura em °F: ')) # entrada de dados 2
            gC=FparaC(gF)  # chamada da função
            # Resultado 2
            print (gF,'°F =',gC,'°C')
        elif tipo==3:
            gK=float(input('Digite a temperatura em K: ')) # entrada de dados 3
            gC=KparaC(gK)  # chamada da função
            # Resultado 3
            print (gK,'K =',gC,'°C')
        elif tipo==4:
            gC=float(input('Digite a temperatura em °C: ')) # entrada de dados 4
            gK=CparaK(gC)  # chamada da função
            # Resultado 4
            print (gC,'°C =',gK,'K')
        else:
            print('Opção inválida. BURRO......')
            print ("executando o programa")

op=int(input("Deseja continuar?  Sim=1  Não=2 ? "))
# fim while
print("Fim a pedido do usuário")


      
