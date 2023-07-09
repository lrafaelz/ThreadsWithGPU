import numpy as np
import multiprocessing as mp
import time
import torch
import cupy as cp
import tensorflow as tf

def sortTorch(matriz):
    matriz_tensor = torch.from_numpy(matriz)
    matriz_linha, _ = torch.sort(matriz_tensor, dim=1)
    matriz_coluna, _ = torch.sort(matriz_tensor, dim=0)
    soma_linhas = torch.sum(matriz_tensor, dim=1)
    soma_colunas = torch.sum(matriz_tensor, dim=0)
    soma_total = torch.sum(matriz_tensor)
    maiores_linha, _ = torch.max(matriz_tensor, dim=1)
    maiores_coluna, _ = torch.max(matriz_tensor, dim=0)
    menores_linha, _ = torch.min(matriz_tensor, dim=1)
    menores_coluna, _ = torch.min(matriz_tensor, dim=0)
    # print(matriz_linha)
    # print(matriz_coluna)
    # print(soma_linhas)
    # print(soma_colunas)
    # print(soma_total)
    # print(maiores_linha)
    # print(maiores_coluna)
    # print(menores_linha)
    # print(menores_coluna)

def sortTorchSequential(matrizes):
    for matriz in matrizes:
        sortTorch(matriz)

def sortNumpy():
    pass

def sortCupy():
    pass

def sortTensorflow():
    pass

import os
import numpy as np
import multiprocessing
import time

def ler_arquivo_txt(arquivo_txt):
    with open(arquivo_txt, 'r') as arquivo:
        linhas = arquivo.readlines()

    matriz = np.empty((len(linhas), 1000))
    for i, linha in enumerate(linhas):
        valores = linha.split()
        matriz[i] = np.array(valores, dtype=np.float64)

    # matriz = np.loadtxt(arquivo_txt, dtype=np.float64)
    
    return matriz

def arquivos_txt():
    arquivos_txt = []
    for i in range(1, 101):
        arquivos_txt.append('Arquivos_Entrada/' + str(i) + '.txt')

    return arquivos_txt

def readMulticore():
    arquivos = arquivos_txt()
    pool = multiprocessing.Pool()
    resultados = pool.map(ler_arquivo_txt, arquivos)
    pool.close()
    pool.join()
    return resultados

if __name__ == '__main__':
    print(torch.cuda.device_count())
    # t0 = time.time()
    # matrizes = readMulticore()
    # t1 = time.time()
    # print("Tempo de execução: ", round(t1 - t0, 4), " segundos")

    # # Exemplo de uso
    # t0 = time.time()
    # sortTorchSequential(matrizes)
    # t1 = time.time()
    # print("Tempo de execução processamento: ", round(t1 - t0, 4), " segundos")



