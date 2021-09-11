import numpy as np
from math import e
from copy import deepcopy


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

     
