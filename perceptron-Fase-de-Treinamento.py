
def degrau(u):
    if u>=0:
        return 1
    else:
        return 0


if  __name__ == '__main__':
    quantAmostras = int(input("Quantidade de amostras que possui o conjunto de treinamento -> "))
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


    while(True):
        errosInexisteCont = 0
        for indiceAmostra in range(quantAmostras):
            erro = "inexiste"

            entradas = [-1] + amostras[indiceAmostra][:-1]#wo = -1 no perceptron ...trocar dps o 0 aqui
            
            u = 0
            print("\n\nAmostra:",indiceAmostra+1)
            print("Época:",epoca+1)
            print("u = ",end="")
            for i in range(len(entradas)):
                u+= entradas[i]*w[i]
                if(i!=len(entradas) - 1):
                    print(entradas[i],"*",w[i],"+",end="")
                    continue
                print(entradas[i],"*",w[i],"=",u,end="\n")

            saida = degrau(u)

            print("g(u) =",saida)#Função degrau foi adotada como função de ativação

            if saida != amostras[indiceAmostra][-1]:#se y != d(k)
                for i in range(len(entradas)):
                    w[i] = w[i] + taxaDeAprendizagem*(amostras[indiceAmostra][-1]-saida)*entradas[i]
                erro = "existe"
            print("Erro:",erro)
            print("W =",w)

            if (erro == "inexiste"):
                errosInexisteCont+=1

        epoca+=1
        if errosInexisteCont == quantAmostras:#se todas amostras possuem o status inexiste
            break


