from random import random
import numpy as np
from math import e

def degrau(u):
    if u>=0:
        return 1
    else:
        return 0
def degrauBipolar(u):
    if u>0:
        return 1
    elif u==0:
        return 0
    else:
        return -1
def linear(u):
    return u

def logistica(u,beta):
    return 1/(1 + e**(-beta*u))

def tangenteHiperbolica(u,beta):
    return (1 - e**(-beta*u))/(1 + e**(-beta*u))

def camadaSimples(entrada_e_peso=[],entrada_e_peso_prod=[],limiarDeAtivacao =[],funcaoDeAtivacao=[]):#entradas e pesos e limiar

    pontencialDeAtv = []#potencial de ativação de cada neuronio
    saidas = []#saídas de cada neuronio g(u)/y
    print("\nPasso 1 [u = Σ - θ]:")
    for indexEntrada,i in enumerate(entrada_e_peso_prod): 
        print("u"+str(indexEntrada+1)+" = ",end="")
        for indexCamada,j in enumerate(i):
            if indexCamada != len(i)-1:#se nao for o ultimo elemento nao dá \n
                print("x"+str(indexCamada+1)+"*w("+str(indexCamada+1)+","+str(indexEntrada+1)+") + ",end="")
                continue
            print("x"+str(indexCamada+1)+"*w("+str(indexCamada+1)+","+str(indexEntrada+1)+") - θ"+str(indexEntrada+1))#se for o ultimo elemento dá \n

    print("\nPasso 2 [u = Σ - θ]:")
    for indexEntrada,i in enumerate(entrada_e_peso_prod): 
        print("u"+str(indexEntrada+1)+" = ",end="")
        for indexCamada,j in enumerate(i):
            if indexCamada != len(i)-1:#se nao for o ultimo elemento nao dá \n
                print(str(entrada_e_peso[indexCamada][indexEntrada][0])+"*"+str(entrada_e_peso[indexCamada][indexEntrada][1])+" + ",end="")
                continue
            u = sum(i)-limiarDeAtivacao[indexEntrada]
            print(str(entrada_e_peso[indexCamada][indexEntrada][0])+"*"+str(entrada_e_peso[indexCamada][indexEntrada][1]),
                  "-",limiarDeAtivacao[indexEntrada],"=>",u)#se for o ultimo elemento dá \n
            pontencialDeAtv.append(u)

    k = 0
    print("\nPasso 3 g(u):")
    for indicePotencial,potencial in enumerate(pontencialDeAtv):
        if funcaoDeAtivacao[indicePotencial] == 1:
            k = degrau(potencial)
        elif funcaoDeAtivacao[indicePotencial] == 2:
            k = linear(potencial)
        elif funcaoDeAtivacao[indicePotencial] == 3:
            k = logistica(potencial,beta)
        elif funcaoDeAtivacao[indicePotencial] == 4:
            k = tangenteHiperbolica(potencial,beta)
        elif funcaoDeAtivacao[indicePotencial] == 5:
            k = degrauBipolar(potencial)
        saidas.append(k)
        print("g(u"+str(indicePotencial+1)+") =",k)
    return saidas



if  __name__ == '__main__':

    #amostras com seus pesos correspondentes e suas saidas d(x) desejadas
    amostras = [[0.9,0.1,1],
                [0.6,0.5,1],
                [0.2,0.8,-1],
                [0.7,0.2,1],
                [0.5,0.4,-1],
                [0.4,0.6,1],
                [0.25,0.8,-1],
                [0.1,0.9,-1],
                [0.3,0.7,-1],
                [0.0,1.0,-1]]
    
    for indexAm in range(len(amostras)):
        erro = False
        print("\n\nAmostra",indexAm+1)
        for epoca in range(1,101): #100 epocas foram adotadas
            quantidadeDeSaidas = 1 #sempre será uma saida nas amostras que foram dadas

            entrada_e_peso = []
            entrada_e_peso_prod = []#produto da entrada com o peso
            limiarDeAtivacao = [] #limiar de ativação de cada neurônio
            funcaoDeAtivacao = []#Vetor que guarda qual a função de ativacao de cada neuronio

            
            for entrada in amostras[indexAm][:2]:
                aux = []
                aux.append((entrada,random()))#entrada da amostra e peso randomico
                entrada_e_peso.append(aux)

            for linha in entrada_e_peso: #Faz o produto da entrada com o peso para cada neuronio
                entrada_e_peso_prod.append(np.prod(linha,axis=1))

            for i in range(quantidadeDeSaidas):
                limiarDeAtivacao.append(random())
                funcaoDeAtivacao.append(5)#função adotada foi a degrau bipolar para os testes randomicos
            beta = None
            if ((3 in funcaoDeAtivacao) or (4 in funcaoDeAtivacao)):
                beta = 1#valor de beta adotado foi sempre de 1
            
            entrada_e_peso = np.array(entrada_e_peso)
            entrada_e_peso_prod = np.array(entrada_e_peso_prod).transpose()
            
            y = camadaSimples(entrada_e_peso,entrada_e_peso_prod,limiarDeAtivacao,funcaoDeAtivacao)[0]

            if y != amostras[indexAm][-1]:#compara a saida obtida com a saída desejada
                continue
            print("Solução encontrada na época",epoca)
            erro = True
            break
