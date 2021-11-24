from scipy import signal
import numpy as np

def convolucao (entrada,filtro,stride=1,modo="valid"):
    filtro = np.array(filtro,np.float32)
    entrada = np.array(entrada,np.float32)

    saida = signal.convolve2d(entrada, filtro[::-1, ::-1], mode=modo)[::stride, ::stride]
    print(saida)


if __name__ == "__main__":
    filtro = [[0.1,0.2,0.6],
          [0.6,0.8,0.7],
          [0.5,0.4,0.3]]
    entrada = [
                [0.0,0.0,0.0,0.0,0.0],
                [0.0,0.2,0.4,0.3,0.0],
                [0.0,0.3,0.9,0.6,0.0],
                [0.0,0.9,0.1,0.2,0.0],
                [0.0,0.0,0.0,0.0,0.0]
              ]
    stride = 1
    modo = "valid"
    #entrada = np.pad(entrada, (1, 1), 'constant', constant_values=(0, 0))#caso tenha padding ao arredor da matriz, descomentar aqui
    convolucao(entrada=entrada,filtro=filtro,stride=stride,modo=modo)
