def degrau(u):
    if u>=0:
        return 1
    else:
        return 0


if  __name__ == '__main__':
    quantAmostras = int(input("Quantidade de amostras que possui o conjunto de treinamento -> "))
    precisaoRequerida = float(input("Precisão Requerida(ε) -> "))
    numMaxEpocas = int(input("Número máximo de épocas -> "))
    amostras = []

    for i in range(quantAmostras):
        print("\nAmostra "+str(i+1))
        x1 = float(input("x1: "))
        x2 = float(input("x2: "))
        dk = float(input("d(k): "))
        amostras.append([x1,x2,dk])

    print('''\nDigite os valores do vetor contendo limiar e os pesos,
          separados por vírgula!
          exemplo: θ,w1,w2,w3
          exemplo: 0.5,0.4,0.3,0.1
          ''')
    w = [float(i) for i in input("-> ").split(",")]

    taxaDeAprendizagem = float(input("Taxa de aprendizagem(η) -> "))

    epoca = 0

    while True:
        vetPotAtv = []
        print("\nÉpoca:",epoca+1)
        for indiceAmostra in range(quantAmostras):
            entradas = [-1] + amostras[indiceAmostra][:-1]#wo = -1 no perceptron ...trocar dps o 0 aqui

            u = 0
            print("u = ",end="")
            for i in range(len(entradas)):
                u+= entradas[i]*w[i]
                if(i!=len(entradas) - 1):
                    print(entradas[i],"*",w[i],"+",end="")
                    continue
                print(entradas[i],"*",w[i],"=",u,end="\n")

            #epoca += 1
            
            vetPotAtv.append(u)
        print("W =",w)
        print("Eqm_Anterior(w) = ",end="")

        equacao = "1/"+str(len(vetPotAtv))+"*("
        
        for index,potencial in enumerate(vetPotAtv):#Eqm Anterior
            if(index != len(vetPotAtv) - 1):
                equacao += "("+str(amostras[index][-1])+"-"+str(potencial)+")**2 + "
                continue
            equacao += "("+str(amostras[index][-1])+"-"+str(potencial)+")**2 )"
        print(equacao,"=",eval(equacao))

        vetPotAtv = []

        for indiceAmostra in range(quantAmostras):
            u = 0

            #print("Época:",epoca+1)
            print("u = ",end="")
            for i in range(len(entradas)):
                u+= entradas[i]*w[i]
                if(i!=len(entradas) - 1):
                    print(entradas[i],"*",w[i],"+",end="")
                    continue
                print(entradas[i],"*",w[i],"=",u,end="\n")

            for i in range(len(w)):
                w[i] = w[i] + taxaDeAprendizagem*(amostras[indiceAmostra][-1]-u)*entradas[i]

            vetPotAtv.append(u)


        print("Eqm_Atual(w) = ",end="")

        equacao2 = "1/"+str(len(vetPotAtv))+"*("
        for index,potencial in enumerate(vetPotAtv):#Eqm Atual
            if(index != len(vetPotAtv) - 1):
                equacao2 += "("+str(amostras[index][-1])+"-"+str(potencial)+")**2 + "
                continue
            equacao2 += "("+str(amostras[index][-1])+"-"+str(potencial)+")**2 )"
        print(equacao2,"=",eval(equacao2))
        print("W =",w)

        epoca+=1

        diferencaAtualeAnterior = abs(eval(equacao) - eval(equacao2))

        print("|Eqm_Atual(w) - Eqm_Anterior(w)| =",diferencaAtualeAnterior)

        if diferencaAtualeAnterior <= precisaoRequerida or numMaxEpocas == epoca:
            break
    
    


        
