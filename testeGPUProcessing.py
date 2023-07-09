import numpy as np
import multiprocessing as mp
import time
import torch
import cupy as cp
import tensorflow as tf

max = 11
vetor = [] * max

def sortTorch(matriz):
    matriz_linha, _ = torch.sort(matriz, dim=1)
    matriz_coluna, _ = torch.sort(matriz, dim=0)
    print(matriz_linha)
    print(matriz_coluna)

def sortNumpy():
    pass

def sortCupy():
    pass

def sortTensorflow():
    pass

def multicore():
    global max
    nThreads = mp.cpu_count()
    # result = 0
    # adicionando a fila de execução (FIFO)
    q = mp.Queue()
    processes = []  # Lista para armazenar os processos
    for i in range(1, nThreads):
        print("Thread: ", i)
        # definindo intervalos de atuação a cada thread
        min_ = int (i*max / nThreads)
        max_ = int ( (i+1)*max / nThreads)
        p = mp.Process(target=executar_todos_arquivos, args=(q, min_, max_))
        p.start()
        # p.join()
        processes.append(p)  # Adiciona o processo à lista de processos

    # Aguarda a conclusão de todos os processos
    for p in processes:
        p.join()
        print("Processo: ", p)
    
    for i in range(0, max):
        print(q.get())
        print()
        

    # for i in range(max):
    #     # matriz = q.get() # desempilha os resultados
    #     print(q.get()) # desempilha os resultados
    #     print()
        # print("Matriz: ", i, " - ", matriz)
        # sortTorch(q.get())
    

def ler_arquivo_txt(arquivo_txt):
    # with open('Arquivos_Entrada/' + arquivo_txt + '.txt', 'r') as arquivo:
    #     linhas = arquivo.readlines()

    # matriz = np.empty((len(linhas), 1000))
    # for i, linha in enumerate(linhas):
    #     valores = linha.split()
    #     matriz[i] = np.array(valores, dtype=np.float64)

    matriz = np.loadtxt('Arquivos_Entrada/' + arquivo_txt + '.txt', dtype=np.float64)
    
    return matriz

def executar_todos_arquivos(q, min, max):
    vetor = [] * (max - min)
    for i in range(min, max):
        arquivo_txt = str(i)
        matriz = ler_arquivo_txt(arquivo_txt)
    q.put(vetor)
        
        

if __name__ == '__main__':

    # Exemplo de uso
    t0 = time.time()
    multicore()
    t1 = time.time()
    print("Tempo de execução: ", round(t1 - t0, 4), " segundos")

    # Exemplo de uso
    t0 = time.time()
    # executar_todos_arquivos(None, 1, 101)
    t1 = time.time()
    print("Tempo de execução: ", round(t1 - t0, 4), " segundos")
