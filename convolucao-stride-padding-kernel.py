from scipy import signal
import numpy as np

def convolucao (entrada,filtro,stride=1,modo="valid"):
    filtro = np.array(filtro,np.uint8)
    entrada = np.array(entrada,np.uint8)

    saida = signal.convolve2d(entrada, filtro[::-1, ::-1], mode=modo)[::stride, ::stride]
    print(saida)


if __name__ == "__main__":
    filtro = [[1,0,1],
          [1,0,0],
          [0,0,2]]
    entrada = [
                [6,3,4,4,5,0,3],
                [4,7,4,0,4,0,4],
                [7,0,2,3,4,5,2],
                [0,0,1,1,0,0,0],
                [0,1,1,0,0,0,0]
              ]
    stride = 1
    modo = "valid"
    #entrada = np.pad(entrada, (1, 1), 'constant', constant_values=(0, 0))#caso tenha padding ao arredor da matriz, descomentar aqui
    convolucao(entrada=entrada,filtro=filtro,stride=stride,modo=modo)
