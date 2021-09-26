from random import random
import pandas as pd
import matplotlib.pyplot as plt



def degrau(u):
    if u>=0:
        return 1
    else:
        return 0


if  __name__ == '__main__':


    df = pd.read_excel('Treinamento_Adaline_PPA.xls')
    amostras = df.values.tolist()
    quantAmostras = len(amostras)
    precisaoRequerida = 0.000001 #10^-6
    print('''\nDigite os valores do vetor contendo limiar e os pesos,
          separados por vírgula!
          exemplo: θ,w1,w2,w3
          exemplo: 0.5,0.4,0.3,0.1
          ''')
    w = [float(i) for i in input("-> ").split(",")]
    print("Pesos iniciais -> W =",w,end="\n\n")
    taxaDeAprendizagem = 0.0025
    errosQuadraticosM = []

    epoca = 0
    vetPotAtv = []#lista que guarda os valores do potencial de ativacao
    
    while True:
        #print("\nÉpoca:",epoca+1)
        if epoca == 0:
            for indiceAmostra in range(quantAmostras):
                entradas = [-1] + amostras[indiceAmostra][:-1]#wo = -1 no perceptron ...trocar dps o 0 aqui

                u = 0
                #print("u = ",end="")
                for i in range(len(entradas)):
                    u+= entradas[i]*w[i]
                    if(i!=len(entradas) - 1):
                        #print(entradas[i],"*",w[i],"+",end="")
                        continue
                    #print(entradas[i],"*",w[i],"=",u,end="\n")

                #epoca += 1
                
                vetPotAtv.append(u)

        #print("W =",w)
        #print("Eqm_Anterior(w) = ",end="")

        equacao = "1/"+str(len(vetPotAtv))+"*("
        
        for index,potencial in enumerate(vetPotAtv):#Eqm Anterior
            if(index != len(vetPotAtv) - 1):
                equacao += "("+str(amostras[index][-1])+"-"+str(potencial)+")**2 + "
                continue
            equacao += "("+str(amostras[index][-1])+"-"+str(potencial)+")**2 )"
        #print(equacao,"=",eval(equacao))
            
        errosQuadraticosM.append(eval(equacao))
        
        vetPotAtv = []

        for indiceAmostra in range(quantAmostras):
            entradas = [-1] + amostras[indiceAmostra][:-1]#wo = -1 no perceptron ...trocar dps o 0 aqui
            u = 0

            #print("Época:",epoca+1)
            #print("u = ",end="")
            for i in range(len(entradas)):
                u+= entradas[i]*w[i]
                if(i!=len(entradas) - 1):
                    #print(entradas[i],"*",w[i],"+",end="")
                    continue
                #print(entradas[i],"*",w[i],"=",u,end="\n")

            for i in range(len(w)):
                w[i] = w[i] + taxaDeAprendizagem*(amostras[indiceAmostra][-1]-u)*entradas[i]

            vetPotAtv.append(u)


        #print("Eqm_Atual(w) = ",end="")

        equacao2 = "1/"+str(len(vetPotAtv))+"*("
        for index,potencial in enumerate(vetPotAtv):#Eqm Atual
            if(index != len(vetPotAtv) - 1):
                equacao2 += "("+str(amostras[index][-1])+"-"+str(potencial)+")**2 + "
                continue
            equacao2 += "("+str(amostras[index][-1])+"-"+str(potencial)+")**2 )"
        #print(equacao2,"=",eval(equacao2))
        #print("W =",w)

        diferencaAtualeAnterior = abs(eval(equacao) - eval(equacao2))

        #print("|Eqm_Atual(w) - Eqm_Anterior(w)| =",diferencaAtualeAnterior)

        if diferencaAtualeAnterior <= precisaoRequerida:
            print("\nÉpoca:",epoca+1)
            print("Pesos Finais -> W =",w)
            break
        
        epoca+=1

    ###Grafico
    fig, ax = plt.subplots()
    ax.plot([i+1 for i in range(epoca+1)],errosQuadraticosM)
    ax.set_xlabel('Época')
    ax.set_ylabel('Erro Quadrático médio')
    plt.show()
    
