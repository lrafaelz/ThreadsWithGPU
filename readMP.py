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


import numpy as np
# from numba import jit, prange, cuda
import time

# Função para ordenar uma matriz por linha
# @jit(nopython=True, parallel=True)
def ordenar_matriz_por_linha(matriz):
    matriz_ordenada = np.sort(matriz, axis=1)
    return matriz_ordenada

# Função para ordenar uma matriz por coluna
# @jit(nopython=True, parallel=True)
def ordenar_matriz_por_coluna(matriz):
    matriz_ordenada = np.sort(matriz, axis=0)
    return matriz_ordenada

# Função para calcular a soma das linhas
# @jit(nopython=True, parallel=True)
def calcular_soma_das_linhas(matriz):
    soma_linhas = np.sum(matriz, axis=1)
    return soma_linhas

# Função para calcular a soma das colunas
# @jit(nopython=True, parallel=True)
def calcular_soma_das_colunas(matriz):
    soma_colunas = np.sum(matriz, axis=0)
    return soma_colunas

# Função para calcular a soma total da matriz
# @jit(nopython=True, parallel=True)
def calcular_soma_total(matriz):
    soma_total = np.sum(matriz)
    return soma_total

# Função para obter o maior valor de cada linha
# @jit(nopython=True, parallel=True)
def obter_maiores_de_cada_linha(matriz):
    maiores_linha = np.max(matriz, axis=1)
    return maiores_linha

# Função para obter o maior valor de cada coluna
# @jit(nopython=True, parallel=True)
def obter_maiores_de_cada_coluna(matriz):
    maiores_coluna = np.max(matriz, axis=0)
    return maiores_coluna

# Função para obter o menor valor de cada linha
# @jit(nopython=True, parallel=True)
def obter_menores_de_cada_linha(matriz):
    menores_linha = np.min(matriz, axis=1)
    return menores_linha

# Função para obter o menor valor de cada coluna
# @jit(nopython=True, parallel=True)
def obter_menores_de_cada_coluna(matriz):
    menores_coluna = np.min(matriz, axis=0)
    return menores_coluna

def escrever_arquivo_saida(matriz_completa, arquivo_saida):
    for matriz in matriz_completa:
        arquivo_saida += 1
            # Ordenação por linha
        matriz_ordenada_linha = ordenar_matriz_por_linha(matriz)

        # Ordenação por coluna
        matriz_ordenada_coluna = ordenar_matriz_por_coluna(matriz)

        # Soma das linhas
        soma_linhas = calcular_soma_das_linhas(matriz)

        # Soma das colunas
        soma_colunas = calcular_soma_das_colunas(matriz)

        # Soma total da matriz
        soma_total= calcular_soma_total(matriz)
        # print("Soma total: ", soma_total)

        # Maiores de cada linha
        maiores_linha = obter_maiores_de_cada_linha(matriz)

        # Maiores de cada coluna
        maiores_coluna = obter_maiores_de_cada_coluna(matriz)

        # Menores de cada linha
        menores_linha = obter_menores_de_cada_linha(matriz)

        # Menores de cada coluna
        menores_coluna = obter_menores_de_cada_coluna(matriz)

        with open('arquivos_saida/' + str(arquivo_saida) + '_out.txt', 'w') as file:
            np.savetxt(file, matriz_ordenada_linha, fmt='%1.7e')
            np.savetxt(file, matriz_ordenada_coluna, fmt='%1.7e')
            np.savetxt(file, soma_linhas.reshape(1,1000), fmt='%1.7e')
            np.savetxt(file, soma_colunas.reshape(1,1000), fmt='%1.7e')
            np.savetxt(file, maiores_linha.reshape(1,1000), fmt='%1.7e')
            np.savetxt(file, maiores_coluna.reshape(1,1000), fmt='%1.7e')
            np.savetxt(file, menores_linha.reshape(1,1000), fmt='%1.7e')
            np.savetxt(file, menores_coluna.reshape(1,1000), fmt='%1.7e')
            np.savetxt(file, soma_total.reshape(1,1), fmt='%1.7e')

def arquivos_txt_entrada():
    arquivos_txt = []
    for i in range(1, 101):
        arquivos_txt.append('Arquivos_Entrada/' + str(i) + '.txt')

    return arquivos_txt

def readMulticore():
    arquivos = arquivos_txt_entrada()
    pool = multiprocessing.Pool()
    resultados = pool.map(ler_arquivo_txt, arquivos)
    pool.close()
    pool.join()
    return resultados


def writeMulticore():
    arquivos = escrever_arquivo_saida()
    pool = multiprocessing.Pool()
    resultados = pool.map(ler_arquivo_txt, arquivos)
    pool.close()
    pool.join()
    return resultados

if __name__ == '__main__':

    t0 = time.time()
    matrizes = readMulticore()
    t1 = time.time()
    print("Tempo de leitura: ", round(t1 - t0, 4), " segundos")
    t0 = time.time()
    escrever_arquivo_saida(matrizes, 0)
    t1 = time.time()
    print("Tempo de execução (calculo + escrita): ", round(t1 - t0, 4), " segundos")


