from itertools import combinations
import numpy as np
from sklearn.cluster import KMeans #para usar o KMeans
import matplotlib.pyplot as plt


def somaDasDistanciasQuadraticas(x1,y1,x2,y2):#retorna a soma de todas distancias euclidianas
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


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

    cidades2 = np.array([[0.7605,0.0169],
                     [0.2555,0.2611],
                     [0.2319,0.8008],
                     [0.7839,0.4733],
                     [0.4574,0.4338],
                     [0.7147,0.9070],
                     [0.6824,0.0601],
                     [0.7235,0.8626],
                     [0.0884,0.4301],
                     [0.4081,0.0820],
                     [0.4131,0.2990],
                     [0.4189,0.0912],
                     [0.6036,0.3158],
                     [0.1081,0.5184],
                     [0.7450,0.7358],
                     [0.6903,0.4751],
                     [0.4842,0.7605],
                     [0.0273,0.0825],
                     [0.2158,0.2395],
                     [0.1477,0.1995],
                     [0.0829,0.4828],
                     [0.3193,0.7692],
                     [0.0214,0.5659],
                     [0.7875,0.1432],
                     [0.2065,0.4865],
                     [0.5481,0.5796],
                     [0.8191,0.2116],
                     [0.4931,0.4160],
                     [0.0674,0.3336],
                     [0.6253,0.4608],
                     [0.6685,0.7183],
                     [0.6575,0.5209],
                     [0.3320,0.6996],
                     [0.9127,0.5230],
                     [0.1594,0.2272],
                     [0.6779,0.7671],
                     [0.7863,0.2465],
                     [0.2318,0.2045],
                     [0.1298,0.1180],
                     [0.4898,0.7731]])

kmeans = KMeans(n_clusters=len(cidades),init = 'k-means++').fit(cidades)
#print(kmeans.cluster_centers_)
eixo_x = []
eixo_y = []

print()
for i in range(1,301):
    kmeans.n_iter_=i
    eixo_x.append(kmeans.n_iter_)#iterações
    eixo_y.append(kmeans.inertia_)#distancias p iteração

fig, ax = plt.subplots()
ax.plot(eixo_x,eixo_y,label="distancias quadraticas em relacao a iteração")
ax.set_xlabel('Iterações')
ax.set_ylabel('Soma das distâncias quadráticas')
ax.legend()
plt.show()
