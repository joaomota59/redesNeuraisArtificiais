import numpy as np
from math import e
from copy import deepcopy
from random import random


def degrau(u):
    if u>=0:
        return 1
    else:
        return 0

def linear(u):
    return u

def logistica(u,beta):
    return 1/(1 + e**(-beta*u))

def tangenteHiperbolica(u,beta):
    return (1 - e**(-beta*u))/(1 + e**(-beta*u))

def camadasMultiplas(entrada_e_peso=[],limiarDeAtivacao =[],funcaoDeAtivacao=[],numeroCamadas=2,camadaAtual = 1,quantCamadaAnterior=2,pesosCamadas=[]):
    potencialDeAtvGlobal = []#lista que irá conter o potencial de ativação de todos neuronios
    pontencialDeAtv = []#potencial de ativação dos neuronios da camada atual que está sendo analisada
    saidasGlobal = []#saídas de todos neurônios g(u)/y
    global saidas
    saidas = []#saídas de cada neuronio da camada atual g(u)/y

    '''
    print("\nPasso 1 [u = Σ - θ]:")
    for indexEntrada in range(quantidadePorCamada[camadaAtual-1]): 
        print("u"+str(indexEntrada+1)+" = ",end="")
        for indexCamada in range(quantCamadaAnterior):
            if indexCamada != quantCamadaAnterior-1:#se nao for o ultimo elemento nao dá \n
                print("x"+str(indexCamada+1)+"*w("+str(indexCamada+1)+","+str(indexEntrada+1)+") + ",end="")
                continue
            print("x"+str(indexCamada+1)+"*w("+str(indexCamada+1)+","+str(indexEntrada+1)+") - θ"+str(indexEntrada+1))#se for o ultimo elemento dá \n
    print("\nPasso 2 [u = Σ - θ]:")
    '''
    

    for indexEntrada in range(quantidadePorCamada[camadaAtual-1]):
        expressao = ""
        #print("u"+str(indexEntrada+1)+" = ",end="")
        for indexCamada in range(quantCamadaAnterior):
            if indexCamada != quantCamadaAnterior-1:#se nao for o ultimo elemento nao dá \n
                expressao += str(entrada_e_peso[indexCamada][indexEntrada][0])+"*"+str(entrada_e_peso[indexCamada][indexEntrada][1])+" + "
                #print(str(entrada_e_peso[indexCamada][indexEntrada][0])+"*"+str(entrada_e_peso[indexCamada][indexEntrada][1])+" + ",end="")
                continue
            
            expressao+= str(entrada_e_peso[indexCamada][indexEntrada][0])+"*"+str(entrada_e_peso[indexCamada][indexEntrada][1])+" - "+str(limiarDeAtivacao[indexEntrada])
            u = eval(expressao)
            #print(str(entrada_e_peso[indexCamada][indexEntrada][0])+"*"+str(entrada_e_peso[indexCamada][indexEntrada][1]),
                  #"-",limiarDeAtivacao[indexEntrada],"=>",u)#se for o ultimo elemento dá \n
            pontencialDeAtv.append(u)
            
    potencialDeAtvGlobal = deepcopy(pontencialDeAtv) #potencial de atv global recebe todos potenciais de ativação da camada 1
    
    k = 0
    #print("\nPasso 3 g(u):")
    for indicePotencial,potencial in enumerate(pontencialDeAtv):
        if funcaoDeAtivacao[indicePotencial] == 2:
            k = logistica(potencial,beta)
        elif funcaoDeAtivacao[indicePotencial] == 1:
            k = tangenteHiperbolica(potencial,beta)
        elif funcaoDeAtivacao[indicePotencial] == 3:
            k = linear(potencial)
        saidas.append(k)
        #print("x"+str(indicePotencial+1)+" = g(u"+str(indicePotencial+1)+") =",k)

    
    if camadaAtual==numeroCamadas:#caso tenha chegado na ultima camada
        return saidas

    saidasGlobal = deepcopy(saidas)
    auxLimiarDeAtivacao = deepcopy(limiarDeAtivacao[quantidadePorCamada[camadaAtual-1]:])#desconsidera os limiares já processados
    auxFuncaoDeAtivacao = deepcopy(funcaoDeAtivacao[quantidadePorCamada[camadaAtual-1]:])#desconsidera o tipo das funcoes de ativacao já processadas
    auxentrada_e_peso = []
    
    #print("\nCamada "+str(camadaAtual+1)+"\n")
    for i in range(len(saidas)):
        aux = []
        for j in range(quantidadePorCamada[camadaAtual]):#Quantidade de neurônios da enesima - camada
            aux.append((saidas[i],pesosCamadas[j]))
        auxentrada_e_peso.append(aux)#pega o peso randomico e entrada de cada neuronio da n- camada interna
    saidas = []#reseta a lista de saidas
    pontencialDeAtv = []#reseta a lista de potetencial de ativacao
    camadaAtual+=1
    #print(camadaAtual,numeroCamadas)
    if camadaAtual<=numeroCamadas:
        return camadasMultiplas(auxentrada_e_peso,auxLimiarDeAtivacao,auxFuncaoDeAtivacao,numeroCamadas,camadaAtual,quantidadePorCamada[camadaAtual-2],pesosCamadas[j:])

if  __name__ == '__main__':
    numeroCamadas = 2 #possui uma camada escondida e uma camada de saida
    quantidadePorCamada = [3,1]#3 neuronios na camada escondida e 1 na camada de saida
    entrada_e_peso = []

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


    
    pesosCamadas = []#vetor que guarda o peso randomico dos neuronios de cada camada
    limiarDeAtivacao = [] #limiar de ativação randomico para cada configuracao
    funcaoDeAtivacao = [] #Funcao de ativação para cada neurônio
    
    eixo_x = []#valores do eixo x
    eixo_y = []#valores do eixo y
    eixo_z = []#valores do eixo z
        
    for i in range(int(sum(quantidadePorCamada))):#percorre em todos neurônios para atribuir o limiar para cada um
        limiarDeAtivacao.append(random())#Limiar de ativacao randomico para cada neuronio
        if i<=2:
            funcaoDeAtivacao.append(1)#Funcao de ativacao tag hiperbolica para os neuronios da camada escondida
        else:
            funcaoDeAtivacao.append(3)#Funcao de ativicao linear para os neuronios da camada de saida

    numeroDePesos = sum([quantidadePorCamada[i]*quantidadePorCamada[i+1] for i in range(len(quantidadePorCamada)-1)])#numero total de pesos das camadas internas

    for i in range(int(2*quantidadePorCamada[0]+numeroDePesos)):#numero de pesos da primeira camada + numero de pesos das camadas internas
        pesosCamadas.append(random())#peso randomico gerado para cada neuronio


    for x1,x2,y in amostras:
        contadorAux = 0
        for i in range(2):#sempre sera duas entradas nas questoes pedidas
            aux = []
            if i == 0:
                entrada = x1
            else:
                entrada = x2
            for j in range(quantidadePorCamada[0]):#Quantidade de neurônios da primeira camada
                aux.append((entrada,pesosCamadas[contadorAux]))
            
            contadorAux+=1
            entrada_e_peso.append(aux)
    
                
        resultado = camadasMultiplas(entrada_e_peso,limiarDeAtivacao,funcaoDeAtivacao,numeroCamadas,quantCamadaAnterior=2,pesosCamadas=pesosCamadas[contadorAux:])[0]#quantCamadaAnterior = 2 pois sempre será duas entradas nos problemas que foram solicitados graficos
        eixo_x.append(x1)
        eixo_y.append(x2)
        eixo_z.append(resultado)
        break#DEPOIS REMOVER O BREAK

