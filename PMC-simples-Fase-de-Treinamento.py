from math import e
import numpy as np

def tangenteHiperbolica(u,beta):
    return (1 - e**(-beta*u))/(1 + e**(-beta*u))


quantidadePorCamada = []
entrada = int(input("Quantidade de entradas que o neuronio possui -> "))
numeroCamadas = int(input("Quantidade de camadas neurais que o neurônio possui -> "))
for i in range(numeroCamadas):
    quantidadePorCamada.append(int(input("Quantidade de neurônios da camada "+str(i+1)+" -> ")))
funcaoDeAtv = int(input("Função de ativação[1-Tagente Hiperbólica] -> "))#Função de atv para todos neurônios
beta = float(input("Valor de Beta -> "))

entradas = [-1]
W = []#matriz de matrizes guarda os pesos de todas camadas
I = [] #matriz de saidas

for i in range(entrada):
    entradas.append(float(input("x"+str(i+1)+" -> ")))

indicesPesosDeTodasCamadas = [[quantidadePorCamada[0],entrada+1]]

for quantidade in range(1,numeroCamadas):
    indicesPesosDeTodasCamadas.append([quantidadePorCamada[quantidade],quantidadePorCamada[quantidade-1]+1])#+1 pq conta entrada -1 em cada

aux = []
aux2 = []
for x in range(numeroCamadas):
    j = indicesPesosDeTodasCamadas[x][0]
    i = indicesPesosDeTodasCamadas[x][1]
    aux2 = []
    for linha in range(j):
        aux = []
        for coluna in range(i):
            aux.append(float(input("Camada "+str(x+1)+" W"+str(linha+1)+","+str(coluna)+" -> ")))
        aux2.append(aux)
    W.append(aux2)

for index,matriz in enumerate(W): print("Camada-"+str(index+1)+" Wij\n",np.array(matriz),end="\n\n")#exibe a matriz de pesos

camadaAtual = 0

while camadaAtual<numeroCamadas:

    for linha in W[camadaAtual]:#SAIDA Ij(1)
        saida = ""
        for coluna in range(len(W[camadaAtual][0])):
            if coluna != len(W[camadaAtual][0]) - 1:
                saida += str(entradas[coluna])+" * "+str(linha[coluna])+" + "
                continue
            saida += str(entradas[coluna])+" * "+str(linha[coluna])
        I.append(saida)

    print("Camada "+str(camadaAtual+1)+" -> I(j) =")
    for i in I: print(i)#calculo
    print()


    print("Camada "+str(camadaAtual+1)+" -> I(j) =")
    I = [eval(i) for i in I]
    for i in I: print(i)#valor do calculo
    print()




    Y = [tangenteHiperbolica(i,beta) for i in I]
    if camadaAtual != numeroCamadas -1:
        Y.insert(0,-1)

    print("Camada "+str(camadaAtual+1)+" -> Y(j) =")
    for i in Y: print(i)#valor da funcao de atv
    print()

    entradas = Y
    I = []
    camadaAtual+=1
