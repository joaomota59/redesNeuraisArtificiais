def degrau(u):
    if u>=0:
        return 1
    else:
        return 0


if  __name__ == '__main__':
    quantAmostras = int(input("Quantidade de amostras que possui o conjunto de treinamento -> "))
    precisaoRequerida = float(input("Precisão Requerida(ε) -> "))
    numMaxEpocas = float(input("Número máximo de épocas -> "))
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

    vetPotAtv = []
    for indiceAmostra in range(quantAmostras):
        entradas = [-1] + amostras[indiceAmostra][:-1]#wo = -1 no perceptron ...trocar dps o 0 aqui

        u = 0

        #print("Época:",epoca+1)
        print("u = ",end="")
        for i in range(len(entradas)):
            u+= entradas[i]*w[i]
            if(i!=len(entradas) - 1):
                print(entradas[i],"*",w[i],"+",end="")
                continue
            print(entradas[i],"*",w[i],"=",u,end="\n")

        #epoca += 1
        
        vetPotAtv.append(u)

    print("E(w) = ",end="")

    equacao = "1/2*("
    
    for index,potencial in enumerate(vetPotAtv):
        if(index != len(vetPotAtv) - 1):
            equacao += "("+str(amostras[index][-1])+"-"+str(potencial)+")**2 + "
            continue
        equacao += "("+str(amostras[index][-1])+"-"+str(potencial)+")**2 )"
    print(equacao)
