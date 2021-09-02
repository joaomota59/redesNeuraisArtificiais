import sys

def tangHiperbolica(vet = [(0.3,0.4),(0.7,0.5)],theta = 0.2,beta = 1):
    e = sys.float_info.epsilon
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
def degrau(vet = [(0.3,0.4),(0.7,0.5)],theta = 0.2):
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
    if u>=0:
        saida = 1
    else:
        saida = 0
    print("g(u) =",saida)
    
if  __name__ == '__main__':
    quantidadeDeEntradas = int(input("Digite a quantidade de entradas que o neurônio possui\n->"))
    entrada_e_peso = []
    for i in range(quantidadeDeEntradas):
        entrada_e_peso.append((float(input("Digite o x"+str(i+1)+":")),float(input("Digite o w"+str(i+1)+":"))))
    _theta = float(input("Digite o limiar de ativação(θ):"))


    choice = int(input("Digite 1-[Função Degrau] 2-[Função Tangente Hiperbólica]\n->"))

    if choice == 1:
        degrau(entrada_e_peso,_theta)
    elif choice == 2:
        _beta = float(input("Digite o limiar de beta(β):"))
        tangHiperbolica(entrada_e_peso,_theta,_beta)
