from math import e
import matplotlib.pyplot as plt
#from itertools import permutations


def tangHiperbolica(vet = [(0.3,0.4),(0.7,0.5)],theta = 0.2,beta = 1):
    somatorio = 0
    print("Σ = ",end="")
    for i in range(len(vet)):
        somatorio += vet[i][0]*vet[i][1]
        if(i!=len(vet) - 1):
            print(vet[i][0],"*",vet[i][1],"+",end="")
            continue
        print(vet[i][0],"*",vet[i][1]," =",somatorio,end="")
        
    u = somatorio - theta
    print("\nu =",somatorio,"-",theta,"=",u)
    saida = (1 - e**(-beta*u))/(1 + e**(-beta*u))
    print("g(u) =",saida)
    return saida

def logistica(vet = [(0.3,0.4),(0.7,0.5)],theta = 0.2,beta = 1):
    somatorio = 0
    print("Σ = ",end="")
    for i in range(len(vet)):
        somatorio += vet[i][0]*vet[i][1]
        if(i!=len(vet) - 1):
            print(vet[i][0],"*",vet[i][1],"+",end="")
            continue
        print(vet[i][0],"*",vet[i][1]," =",somatorio,end="")
        
    u = somatorio - theta
    print("\nu =",somatorio,"-",theta,"=",u)
    saida = 1/(1 + e**(-beta*u))
    print("g(u) =",saida)
    return saida

def graficoFuncaoLogistica2(dominioEntrada = [-3,3], w = [0.1,0.2] , theta = 0.0,beta = 1, pontosDeDiscretizacao = 50):#com dois pesos
    global vetorGU, vetorEntradas
    vetorEntradas = []
    vetorGU = []
    razaoPA = (dominioEntrada[1] - dominioEntrada[0])/(pontosDeDiscretizacao - 1)
    for i in range(1,51):
        x = dominioEntrada[0] + (i-1)*razaoPA
        vetorEntradas.append(x)
        vetorGU.append(logistica([(x,w[0]),(x,w[1])],theta,beta))
    #perm = permutations(vetorEntradas,2)
    #for i in perm:
    #    print(logistica([(i[0],w[0]),(i[1],w[1])], theta, beta))


def graficoFuncaoLogistica(dominioEntrada = [-3,3], w1 = 0.1 , theta = 0.0,beta = 1, pontosDeDiscretizacao = 50):#com somente um peso
    global vetorGU, vetorEntradas
    razaoPA = (dominioEntrada[1] - dominioEntrada[0])/(pontosDeDiscretizacao - 1)
    vetorEntradas = []
    vetorGU = []
    for i in range(1,51):
        x = dominioEntrada[0] + (i-1)*razaoPA
        vetorEntradas.append(x)
        vetorGU.append(logistica([(x,w1)],theta,beta))

def graficoFuncaoTangenteHiperbolica(dominioEntrada = [-3,3], w1 = 0.1 , theta = 0.0,beta = 1, pontosDeDiscretizacao = 50):#com somente um peso
    global vetorGU, vetorEntradas
    razaoPA = (dominioEntrada[1] - dominioEntrada[0])/(pontosDeDiscretizacao - 1)
    vetorEntradas = []
    vetorGU = []
    for i in range(1,51):
        x = dominioEntrada[0] + (i-1)*razaoPA
        vetorEntradas.append(x)
        vetorGU.append(tangHiperbolica([(x,w1)],theta,beta))


if  __name__ == '__main__':
    fig, ax = plt.subplots()
    entrada = int(input("Digite 1-[Gerar Gráfico da Função TangenteHiperbolica] ou 2-[Gerar Gráfico da Função Logística] \n->"))
    dominio = [float(input("Valor Inicial do Dominio: ")),float(input("Valor Final do Dominio: "))]
    quantEntrada = int(input("Digite 1-[Possui somente uma entrada] 2-[Possui duas entradas] \n->"))
    _beta = float(input("Digite o valor de beta: "))
    _theta = float(input("Digite o valor de theta: "))
    _pontosDeDiscretizacao = int(input("Quantidade de pontos de discretização: "))
    tipoFuncao=''
    if(quantEntrada == 1):
        ent = [float(input("Digite o valor do peso: "))]
    elif (quantEntrada == 2):
        ent = [float(input("Digite o valor do 1° peso: ")),float(input("Digite o valor do 2° peso: "))]
    else:
        raise Exception
    if entrada == 1 and quantEntrada == 1:
        tipoFuncao = 'Função Tangente Hiperbolica'
        graficoFuncaoTangenteHiperbolica()#usar para gerar o gráfico da função
        ax.set_title('Gráfico entrada x1 em relação a saída g(u)/y')
    elif entrada == 2:
        tipoFuncao = 'Função Logística'
        if quantEntrada == 1:
            graficoFuncaoLogistica(dominioEntrada = dominio, w1 = ent[0] , theta = _theta,beta = _beta, pontosDeDiscretizacao = _pontosDeDiscretizacao)
            ax.set_title('Gráfico entrada x1 em relação a saída g(u)/y')
        else:
            graficoFuncaoLogistica2(dominioEntrada = dominio, w = ent , theta = _theta,beta = _beta, pontosDeDiscretizacao = _pontosDeDiscretizacao)
            ax.set_title('Gráfico entrada (x1,x2) em relação a saída g(u)/y, sendo x1 = x2')
    
    ax.plot(vetorEntradas,vetorGU,label = tipoFuncao)
    ax.set_xlabel('Entrada x')
    ax.set_ylabel('Saída y/g(u)')
    ax.legend()
    plt.show()
    #tangHiperbolica()#vet = [(x1,w1),(x2,w2),...],theta = valorT , beta = valorB
