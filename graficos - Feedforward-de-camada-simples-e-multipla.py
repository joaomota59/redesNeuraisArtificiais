from itertools import permutations
from random import random
import numpy as np
from math import e
import matplotlib.pyplot as plt


def logistica(u,beta):
    return 1/(1 + e**(-beta*u))

def tangenteHiperbolica(u,beta):
    return (1 - e**(-beta*u))/(1 + e**(-beta*u))


def camadaSimples(entrada_e_peso=[],entrada_e_peso_prod=[],limiarDeAtivacao =[],funcaoDeAtivacao=[]):#entradas e pesos e limiar

    pontencialDeAtv = []#potencial de ativação de cada neuronio
    saidas = []#saídas de cada neuronio g(u)/y
    #print("\nPasso 1 [u = Σ - θ]:")
    for indexEntrada,i in enumerate(entrada_e_peso_prod): 
        #print("u"+str(indexEntrada+1)+" = ",end="")
        for indexCamada,j in enumerate(i):
            if indexCamada != len(i)-1:#se nao for o ultimo elemento nao dá \n
                #print("x"+str(indexCamada+1)+"*w("+str(indexCamada+1)+","+str(indexEntrada+1)+") + ",end="")
                continue
            #print("x"+str(indexCamada+1)+"*w("+str(indexCamada+1)+","+str(indexEntrada+1)+") - θ"+str(indexEntrada+1))#se for o ultimo elemento dá \n

    #print("\nPasso 2 [u = Σ - θ]:")
    for indexEntrada,i in enumerate(entrada_e_peso_prod): 
        #print("u"+str(indexEntrada+1)+" = ",end="")
        for indexCamada,j in enumerate(i):
            if indexCamada != len(i)-1:#se nao for o ultimo elemento nao dá \n
                #print(str(entrada_e_peso[indexCamada][indexEntrada][0])+"*"+str(entrada_e_peso[indexCamada][indexEntrada][1])+" + ",end="")
                continue
            u = sum(i)-limiarDeAtivacao[indexEntrada]
            #print(str(entrada_e_peso[indexCamada][indexEntrada][0])+"*"+str(entrada_e_peso[indexCamada][indexEntrada][1]),
                  #"-",limiarDeAtivacao[indexEntrada],"=>",u)#se for o ultimo elemento dá \n
            pontencialDeAtv.append(u)

    k = 0
    #print("\nPasso 3 g(u):")
    for indicePotencial,potencial in enumerate(pontencialDeAtv):
        if funcaoDeAtivacao[indicePotencial] == 2:
            k = logistica(potencial,beta)
        elif funcaoDeAtivacao[indicePotencial] == 1:
            k = tangenteHiperbolica(potencial,beta)
        saidas.append(k)
        #print("g(u"+str(indicePotencial+1)+") =",k)
    return saidas



def valoresPA(a1,an,n=20):
    r = (an -a1)/(n-1)
    valores = []
    for i in range(1,n+1):
        valores.append(a1 + (i-1)*r)
    return valores

if  __name__ == '__main__':
    entrada = int(input("Digite 1-[Gerar Gráfico da Função TangenteHiperbolica] ou 2-[Gerar Gráfico da Função Logística] \n->"))
    dominio = [float(input("Valor Inicial do Dominio: ")),float(input("Valor Final do Dominio: "))]
    beta = float(input("Digite o valor de beta: "))
    _pontosDeDiscretizacao = int(input("Quantidade de pontos de discretização: "))
    numeroDeConfiguracoes = 5#numero de configurações adotada
    entrada_e_peso = []
    entrada_e_peso_prod = []#produto da entrada com o peso
    
    valoresDeEntrada = valoresPA(dominio[0],dominio[1],_pontosDeDiscretizacao)

    vezes = []#guardará o resultado de cada vez que foi rodado o script
    informacoes = []#guarda os pesos e limiar randomico adotado

    fig, axs1 = plt.subplots(nrows=2, ncols=2,figsize=(13, 6),subplot_kw=dict(projection="3d"))
    tipoFuncao = ""
    if entrada == 1:
        tipoFuncao = "Tangente Hiperbólica"
    elif entrada == 2:
        tipoFuncao = "Logística"
    
    for i in range(numeroDeConfiguracoes):
        w1 = random()#gera o peso w1 randomico para cada configuracao
        w2 = random()#gera o peso w2 randomico para cada configuracao
        limiarDeAtivacao = [random()] #limiar de ativação randomico para cada configuracao
        informacoes.append([w1,w2,limiarDeAtivacao[0]])
        #print(w1,w2,limiarDeAtivacao)
        eixo_x = []
        eixo_y = []
        eixo_z = []
        for x1,x2 in permutations(valoresDeEntrada,2):
            entrada_e_peso.append([[x1,w1]])
            entrada_e_peso.append([[x2,w2]])
            
            for linha in entrada_e_peso: #Faz o produto da entrada com o peso para cada neuronio
                entrada_e_peso_prod.append(np.prod(linha,axis=1))
            
            entrada_e_peso = np.array(entrada_e_peso)
            entrada_e_peso_prod = np.array(entrada_e_peso_prod).transpose()

            resultado = camadaSimples(entrada_e_peso,entrada_e_peso_prod,limiarDeAtivacao,funcaoDeAtivacao = [entrada,entrada])[0]


            eixo_x.append(x1)
            eixo_y.append(x2)
            eixo_z.append(resultado)
            
            entrada_e_peso = []
            entrada_e_peso_prod = []
        vezes.append([eixo_x,eixo_y,eixo_z])#guarda o resultado para cada configuração

    cont = 0
    for i in range(2):
        for j in range(2):
            axs1[i,j].set_title('Gráfico com w1 = '+str(round(informacoes[cont][0],2))+', w2 = '+
                                str(round(informacoes[cont][1],2))+
                                ', limiar(θ) = '+str(round(informacoes[cont][2],2)))
            axs1[i, j].plot(vezes[cont][0],vezes[cont][1],vezes[cont][2],label = tipoFuncao)
            axs1[i,j].set_xlabel("x1")
            axs1[i,j].set_ylabel("x2")
            axs1[i,j].set_zlabel("g(u)")
            axs1[i,j].legend()
            cont+=1


    #ax = fig.add_subplot(projection='3d')
    #ax.set_title('Gráfico com w1 = '+str(round(w1,2))+', w2 = '+str(round(w2,2))+', limiar(θ) = '+str(round(limiarDeAtivacao[0],2)))


    
    fig2, axs2 = plt.subplots(subplot_kw=dict(projection="3d"))
    axs2.set_title('Gráfico com w1 = '+str(round(informacoes[4][0],2))+', w2 = '+
              str(round(informacoes[4][1],2))+
              ', limiar(θ) = '+str(round(informacoes[4][2],2)))
    axs2.plot(eixo_x,eixo_y,eixo_z,label = tipoFuncao)

    axs2.set_xlabel("x1")
    axs2.set_ylabel("x2")
    axs2.set_zlabel("g(u)")
    axs2.legend()
    
    plt.show()

    
