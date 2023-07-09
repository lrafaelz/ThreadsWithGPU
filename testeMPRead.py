import numpy as np
import cupy as cp
import multiprocessing as mp
import numba as nb
from numba import cuda
import time

def ler_arquivo_txt(arquivo_txt):
    with open('Arquivos_Entrada/' + arquivo_txt + '.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    matriz = np.empty((len(linhas), 1000))
    for i, linha in enumerate(linhas):
        valores = linha.split()
        matriz[i] = np.array(valores, dtype=np.float64)

    return matriz

def multicore():
    max = 11
    nThreads = mp.cpu_count()
    # result = 0
    # adicionando a fila de execução (FIFO)
    # q = mp.Queue()
    processes = []  # Lista para armazenar os processos
    for i in range(1, nThreads):
        # definindo intervalos de atuação a cada thread
        min_ = int (i*max / nThreads)
        max_ = int ( (i+1)*max / nThreads)
        p = mp.Process(target=executar_todos_arquivos, args=(min_, max_))
        p.start()
        processes.append(p)  # Adiciona o processo à lista de processos

    # Aguarda a conclusão de todos os processos
    for p in processes:
        p.join()


def executar_todos_arquivos(min, max):
    for i in range(min, max):
        arquivo_txt = str(i)
        matriz = ler_arquivo_txt(arquivo_txt)
        # print(matriz)
              

if __name__ == '__main__':

    # Exemplo de uso
    t0 = time.time()
    multicore()
    t1 = time.time()
    print("Tempo de execução: ", round(t1 - t0, 4), " segundos")

    # Exemplo de uso
    t0 = time.time()
    executar_todos_arquivos(1, 101)
    t1 = time.time()
    print("Tempo de execução: ", round(t1 - t0, 4), " segundos")

