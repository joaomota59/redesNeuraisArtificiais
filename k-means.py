import numpy as np #para manipular os vetores
from matplotlib import pyplot as plt #para plotar os gráficos
from sklearn.cluster import KMeans #para usar o KMeans

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

    #X = np.array([[1, 2], [1, 4], [1, 0],
    #               [10, 2], [10, 4], [10, 0]])

    print("Quantidade de Cidades",len(cidades),"\n")

    for i in range(5):
        kmeans = KMeans(n_clusters=len(cidades),init = 'k-means++').fit(cidades)#define numero randomico de clusters e numero randomico de centroides
        print("Iteração:",str(i+1))
        print("Quantidade de centroides:",len(kmeans.cluster_centers_))
        print("Coordenadas dos centroides de cada cluster:\n",kmeans.cluster_centers_)
        print("\n\n")
