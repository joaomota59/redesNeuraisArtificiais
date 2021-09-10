import numpy as np #para manipular os vetores
from matplotlib import pyplot as plt #para plotar os gráficos
from sklearn.cluster import KMeans #para usar o KMeans
from sklearn.decomposition import PCA


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


    if int(input("Entre [1 - 20 Cidades] [2 - 40 Cidades]\n->")) == 1:
        cidades = cidades
    else:
        cidades = cidades2
    
    print("Quantidade de Cidades",len(cidades),"\n")

    for i in range(5):
        reduced_data = PCA(n_components=2).fit_transform(cidades)
        kmeans = KMeans(init="k-means++", n_clusters=len(cidades)).fit(reduced_data)

        # Step size of the mesh. Decrease to increase the quality of the VQ.
        h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].

        # Plot the decision boundary. For that, we will assign a color to each
        x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
        y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

        # Obtain labels for each point in mesh. Use last trained model.
        Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.figure(1)
        plt.clf()
        plt.imshow(Z, interpolation="nearest",
                   extent=(xx.min(), xx.max(), yy.min(), yy.max()),
                   cmap=plt.cm.Paired, aspect="auto", origin="lower")

        plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
        # Plot the centroids as a white X
        centroids = kmeans.cluster_centers_
        plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=169, linewidths=3,
                    color="w", zorder=10)
        plt.title("K-means Clusters formados com as cidades\n"
                  "Centroides estão marcados com um X")
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        plt.xticks(())
        plt.yticks(())
        plt.show()
