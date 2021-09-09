from itertools import combinations
import numpy as np

def somaDasDistanciasQuadraticas(cidades):#retorna a soma de todas distancias euclidianas
    somatorio = 0
    for arr1,arr2 in combinations(cidades,2):
        somatorio += ((arr1[0] - arr2[0])**2 + (arr1[1] - arr2[1])**2)**0.5
    return somatorio


if __name__ == "__main__":
    cidades = np.array([[0.1990,0.9442],
                        [0.6743,0.8386],
                        [0.9271,0.2584],
                        [0.3438,0.0429],
                        [0.5945,0.0059],
                        [0.6155,0.5744],
                        [0.0034,0.7439],
                        [0.9820,0.8068],
                        [0.8995,0.6376],
                        [0.6928,0.2513],
                        [0.4397,0.1443],
                        [0.7010,0.6516],
                        [0.6097,0.9461],
                        [0.2999,0.8159],
                        [0.8560,0.9302],
                        [0.1121,0.3099],
                        [0.2916,0.2688],
                        [0.0974,0.5365],
                        [0.3974,0.1633],
                        [0.3333,0.2110]])

