import pandas as pd
from random import random

def degrauBipolar(u):#Adaptacao para classificao de padroes
    if u>=0:
        return 1
    else:
        return -1

def perceptron(amostras=[[]],w=[],taxaDeAprendizagem=0.05):
    quantAmostras = len(amostras)

    epoca = 0
    
    while(True):
        errosInexisteCont = 0
        for indiceAmostra in range(quantAmostras):
            erro = "inexiste"

            entradas = [-1] + amostras[indiceAmostra][:-1]#wo = -1 no perceptron ...trocar dps o 0 aqui
            
            u = 0
            #print("\n\nAmostra:",indiceAmostra+1)
            #print("Época:",epoca+1)
            #print("u = ",end="")
            for i in range(len(entradas)):
                u+= entradas[i]*w[i]
                if(i!=len(entradas) - 1):
                    #print(entradas[i],"*",w[i],"+",end="")
                    continue
                #print(entradas[i],"*",w[i],"=",u,end="\n")

            saida = degrauBipolar(u)

            #print("g(u) =",saida)#Função degrau Bipolar foi adotada como função de ativação

            if saida != amostras[indiceAmostra][-1]:#se y != d(k)
                for i in range(len(entradas)):
                    w[i] = w[i] + taxaDeAprendizagem*(amostras[indiceAmostra][-1]-saida)*entradas[i]
                erro = "existe"
            #print("Erro:",erro)
            #print("W =",w)

            if (erro == "inexiste"):
                errosInexisteCont+=1

        epoca+=1
        if errosInexisteCont == quantAmostras:#se todas amostras possuem o status inexiste
            print("Valores Finais W =",w)
            print("Época:",epoca+1)
            return w

def perceptronOperacao(amostrasTP = [[]],w = []):

    quantAmostras = len(amostrasTP)

    for indiceAmostra in range(quantAmostras):
        entradas = [-1] + amostrasTP[indiceAmostra]
        u = 0
        for j in range(len(entradas)):
            u+= entradas[j]*w[j]

        saida = degrauBipolar(u) 
        if saida == -1:
            print("A amostra:",amostrasTP[indiceAmostra],"pertence a classe com saída:",saida)
        else:
            print("A amostra:",amostrasTP[indiceAmostra],"pertence a classe com saída:",saida)
    return


if  __name__ == '__main__':

    df = pd.read_excel('Treinamento_Perceptron.xls')

    df2 = pd.read_excel('Teste_Perceptron.xls')

    quantidade_de_treinamentos = int(input("Entre com a quantidade de treinamentos que deseja realizar -> "))

    usarEntradaNormalizada = int(input("Usar Entradas normalizadas [1-Sim] [2-Não] -> "))

    if usarEntradaNormalizada == 1:#Normaliza os valores de entrada dividindo cada valor de entrada pelo maior valor
        for coluna in list(df.columns)[:-1]:#-1 pq nao faz alterações na coluna de valor desejado (d)
            df[coluna] = df[coluna]/max(df[coluna])

    amostras = df.values.tolist()
    
    for quantidadeT in range(quantidade_de_treinamentos):
        w = []
        
        for i in range(len(amostras[0])):#atribui valores randomicos entre 0 e 1 para o vetor w
            w.append(random())

        _taxaDeAprendizagem = 0.01

        print("Taxa de Aprendizagem adotada:",_taxaDeAprendizagem)
        print("Valores Iniciais w =",w,end="\n")

        w = perceptron(amostras,w,taxaDeAprendizagem = 0.01)#taxa de aprendizagem adotada foi de 0.01

        print("\nTreinamento",quantidadeT+1,"finalizado!")

        #apos o treinamento entao faz a classificação de cada amostra
        perceptronOperacao(df2.values.tolist(),w)
        
        if quantidadeT != quantidade_de_treinamentos - 1:
            input("Aperte Enter para realizar o próximo treinamento!\n")
        print("\n\n")
