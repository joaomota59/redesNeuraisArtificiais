import numpy as np
from math import e

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


def camadaSimples(entrada_e_peso=[],entrada_e_peso_prod=[],limiarDeAtivacao =[],funcaoDeAtivacao=[]):#entradas e pesos e limiar

    pontencialDeAtv = []#potencial de ativação de cada camada
    saidas = []#saídas de cada camada g(u)/y
    
    print("\nPasso 1 [u = Σ - θ]:")
    for indexEntrada,i in enumerate(entrada_e_peso_prod): 
        print("u"+str(indexEntrada+1)+" = ",end="")
        for indexCamada,j in enumerate(i):
            if j != i[-1]:#se nao for o ultimo elemento nao dá \n
                print("x"+str(indexCamada+1)+"*w("+str(indexCamada+1)+","+str(indexEntrada+1)+") + ",end="")
                continue
            print("x"+str(indexCamada+1)+"*w("+str(indexCamada+1)+","+str(indexEntrada+1)+") - θ"+str(indexEntrada+1))#se for o ultimo elemento dá \n

    print("\nPasso 2 [u = Σ - θ]:")
    for indexEntrada,i in enumerate(entrada_e_peso_prod): 
        print("u"+str(indexEntrada+1)+" = ",end="")
        for indexCamada,j in enumerate(i):
            if j != i[-1]:#se nao for o ultimo elemento nao dá \n
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
        saidas.append(k)
        print("g(u"+str(indicePotencial+1)+") =",k)
    return saidas

def camadasMultiplas(entrada_e_peso=[],entrada_e_peso_prod=[],limiarDeAtivacao =[],funcaoDeAtivacao=1):
    pass


if  __name__ == '__main__':

    entrada_e_peso = []
    aux = []
    entrada_e_peso_prod = []#produto da entrada com o peso
    limiarDeAtivacao = [] #limiar de ativação de cada neurônio
    funcaoDeAtivacao = []#Vetor que guarda qual a função de ativacao de cada neuronio
    
    simplesOuMultipla = int(input("Entre com 1-[Algoritmo de Camada Simples] ou 2-[Algoritmo de Múltiplas Camadas]\n->"))
    quantidadeDeEntradas = int(input("Quantidade de entradas que o neurônio possui:\n->"))
    beta = None
    if (funcaoDeAtivacao == 3 or funcaoDeAtivacao == 4):
        beta = float(input("Valor de Beta:\n->"))
    numeroCamadas = 0
    quantidadePorCamada = []#quantidade de neurônio por camada <-> Usado no algoritmo de Múltiplas Camadas
    quantidadeDeSaidas = 0
    if simplesOuMultipla == 1:
        quantidadeDeSaidas = int(input("Quantidade de neurônios da camada:\n->"))
        
        for i in range(quantidadeDeEntradas):
            aux = []
            entrada = float(input("Digite a entrada x"+str(i+1)+":"))
            for j in range(quantidadeDeSaidas):
                aux.append((entrada,float(input("Digite o peso (w"+str(i+1)+","+str(j+1)+"):"))))
            entrada_e_peso.append(aux)

        for linha in entrada_e_peso: #Faz o produto da entrada com o peso para cada camada
            entrada_e_peso_prod.append(np.prod(linha,axis=1))

        for i in range(quantidadeDeSaidas):
            limiarDeAtivacao.append(float(input("Digite o limiar(θ"+str(i+1)+"):")))
            funcaoDeAtivacao.append(int(input("Tipo g(u"+str(i+1)+") 1-[Degrau] 2-[linear] 3-[logistica] 4-[tangenteHiperbolica]\n->")))
        
        entrada_e_peso = np.array(entrada_e_peso)
        entrada_e_peso_prod = np.array(entrada_e_peso_prod).transpose()
        camadaSimples(entrada_e_peso,entrada_e_peso_prod,limiarDeAtivacao,funcaoDeAtivacao)
    elif simplesOuMultipla == 2:
        numeroCamadas = int(input("Quantidade de camadas que o neurônio possui:\n->"))
        for i in range(numeroCamadas):
            quantidadePorCamada.append(int(input("Quantidade de neurônios da camada "+str(i+1)+":\n->")))
        for i in range(quantidadeDeEntradas):
            aux = []
            entrada = float(input("Digite a entrada x"+str(i+1)+":"))
            for j in range(quantidadePorCamada[0]):#Quantidade de neurônios da primeira camada
                aux.append((entrada,float(input("Digite o peso (w"+str(i+1)+","+str(j+1)+"):"))))
            entrada_e_peso.append(aux)
        for linha in entrada_e_peso: #Faz o produto da entrada com o peso para cada camada
            entrada_e_peso_prod.append(np.prod(linha,axis=1))
        entrada_e_peso_prod = np.array(entrada_e_peso_prod).transpose()
            
    
    
        
    

        
