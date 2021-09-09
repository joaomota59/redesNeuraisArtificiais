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

    #X = np.array([[1, 2], [1, 4], [1, 0],
    #               [10, 2], [10, 4], [10, 0]])

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
