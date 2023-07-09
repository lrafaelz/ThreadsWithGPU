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

    t0 = time.time()
    matrizes = readMulticore()
    t1 = time.time()
    print("Tempo de execução: ", round(t1 - t0, 4), " segundos")

