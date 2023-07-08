import numpy as np
import cupy as cp
import pandas as pd
import time

# https://docs.cupy.dev/en/stable/install.html

# Função para ordenar uma matriz por linha
def ordenar_matriz_por_linha(matriz):
    return cp.sort(matriz, axis=1)

# Função para ordenar uma matriz por coluna
def ordenar_matriz_por_coluna(matriz):
    return cp.sort(matriz, axis=0)

# Função para calcular a soma das linhas
def calcular_soma_das_linhas(matriz):
    return cp.sum(matriz, axis=1)

# Função para calcular a soma das colunas
def calcular_soma_das_colunas(matriz):
    return cp.sum(matriz, axis=0)

# Função para calcular a soma total da matriz
def calcular_soma_total(matriz):
    return cp.sum(matriz)

# Função para obter o maior valor de cada linha
def obter_maiores_de_cada_linha(matriz):
    return cp.max(matriz, axis=1)

# Função para obter o maior valor de cada coluna
def obter_maiores_de_cada_coluna(matriz):
    return cp.max(matriz, axis=0)

# Função para obter o menor valor de cada linha
def obter_menores_de_cada_linha(matriz):
    return cp.min(matriz, axis=1)

# Função para obter o menor valor de cada coluna
def obter_menores_de_cada_coluna(matriz):
    return cp.min(matriz, axis=0)

# Função para escrever o arquivo de saída
def escrever_arquivo_saida(matriz, arquivo_saida):
    matriz_ordenada_linha = ordenar_matriz_por_linha(matriz)
    matriz_ordenada_coluna = ordenar_matriz_por_coluna(matriz)
    soma_linhas = calcular_soma_das_linhas(matriz)
    soma_colunas = calcular_soma_das_colunas(matriz)
    soma_total = calcular_soma_total(matriz)
    maiores_linha = obter_maiores_de_cada_linha(matriz)
    maiores_coluna = obter_maiores_de_cada_coluna(matriz)
    menores_linha = obter_menores_de_cada_linha(matriz)
    menores_coluna = obter_menores_de_cada_coluna(matriz)

   with open(f'arquivos_saida/{arquivo_saida}.txt', 'w') as file:
        cp.savetxt(file, matriz_ordenada_linha.get(), fmt='%1.7e')
        cp.savetxt(file, matriz_ordenada_coluna.get(), fmt='%1.7e')
        cp.savetxt(file, soma_linhas.reshape(1, -1), fmt='%1.7e')
        cp.savetxt(file, soma_colunas.reshape(1, -1), fmt='%1.7e')
        cp.savetxt(file, maiores_linha.get(), fmt='%1.7e')
        cp.savetxt(file, maiores_coluna.get(), fmt='%1.7e')
        cp.savetxt(file, menores_linha.get(), fmt='%1.7e')
        cp.savetxt(file, menores_coluna.get(), fmt='%1.7e')
        cp.savetxt(file, [soma_total.get()], fmt='%1.7e')

# Função para ler o arquivo txt e converter para uma matriz
def ler_arquivo_txt(arquivo_txt):
    df = pd.read_csv(f'Arquivos_Entrada/{arquivo_txt}.txt', delimiter=' ', header=None)
    matriz = cp.asarray(df.values)
    return matriz

def executar_todos_arquivos():
    for i in range(1, 31):
        arquivo_txt = str(i)
        matriz = ler_arquivo_txt(arquivo_txt)
        escrever_arquivo_saida(matriz, arquivo_txt)

if __name__ == '__main__':
    # Configurar o uso da GPU
    cp.cuda.Device(0).use()

    # Exemplo de uso
    t0 = time.time()
    executar_todos_arquivos()
    t1 = time.time()
    print("Tempo de execução com GPU: ", round(t1 - t0, 3), " segundos")
