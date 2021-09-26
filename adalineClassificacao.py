import pandas as pd

def degrauBipolar(u):#Adaptacao para classificao de padroes
    if u>=0:
        return 1
    else:
        return -1

if  __name__ == '__main__':

    df = pd.read_excel('Treinamento_Adaline_PPA.xls')
    amostras = df.values.tolist()
    
    print('''\nDigite os valores do vetor contendo limiar e os pesos,
          separados por vírgula!
          exemplo: θ,w1,w2,w3
          exemplo: 0.5,0.4,0.3,0.1
          ''')
    w = [float(i) for i in input("-> ").split(",")]

    for index,(x1,x2,x3,x4,d) in enumerate(amostras):
        u = -1*w[0]+x1*w[1]+x2*w[2]+x3*w[3]+x4*w[4]
        y = degrauBipolar(u)
        if y == -1:
            print("Amostra",index+1,"∈ a Classe A <-> y =",y)
        else:
            print("Amostra",index+1,"∈ a Classe B <-> y =",y)
