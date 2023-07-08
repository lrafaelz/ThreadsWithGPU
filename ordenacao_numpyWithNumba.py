import  os
import numpy as np
from numba import jit, prange
import time

# Função para ordenar uma matriz por linha
@jit(nopython=True)
def ordenar_matriz_por_linha(matriz):
    matriz_ordenada = []
    for i in range(1000):
        matriz_ordenada.append(np.sort(matriz[i]))
    return matriz_ordenada

# Função para ordenar uma matriz por coluna
@jit(nopython=True, parallel=True)
def ordenar_matriz_por_coluna(matriz):
    matriz_ordenada = []
    for i in prange(1000):
        matriz_ordenada.append(np.sort(matriz[:,i]))
    return matriz_ordenada

# Função para calcular a soma das linhas
@jit(nopython=True)
def calcular_soma_das_linhas(matriz):
    soma_linhas = np.sum(matriz, axis=1)
    return soma_linhas

# Função para calcular a soma das colunas
@jit(nopython=True)
def calcular_soma_das_colunas(matriz):
    soma_colunas = np.sum(matriz, axis=0)
    return soma_colunas

# Função para calcular a soma total da matriz
@jit(nopython=True)
def calcular_soma_total(matriz):
    soma_total = []
    soma_total.append(np.sum(matriz))
    return soma_total

# Função para obter o maior valor de cada linha
@jit(nopython=True)
def obter_maiores_de_cada_linha(matriz):
    maiores_linha =[]
    for i in range(1000):
        maiores_linha.append(np.max(matriz[i]))
    return maiores_linha

# Função para obter o maior valor de cada coluna
@jit(nopython=True)
def obter_maiores_de_cada_coluna(matriz):
    maiores_coluna = []
    for i in range(1000):
        maiores_coluna.append(np.max(matriz[:,i]))
    return maiores_coluna

# Função para obter o menor valor de cada linha
@jit(nopython=True)
def obter_menores_de_cada_linha(matriz):
    menores_linha = []
    for i in range(1000):
        menores_linha.append(np.min(matriz[i]))
    return menores_linha

# Função para obter o menor valor de cada coluna
@jit(nopython=True)
def obter_menores_de_cada_coluna(matriz):
    menores_coluna = []
    for i in range(1000):
        menores_coluna.append(np.min(matriz[:,i]))
    return menores_coluna

def escrever_arquivo_saida(matriz, arquivo_saida):
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
    print("Soma total: ", soma_total)

    # Maiores de cada linha
    maiores_linha = obter_maiores_de_cada_linha(matriz)

    # Maiores de cada coluna
    maiores_coluna = obter_maiores_de_cada_coluna(matriz)

    # Menores de cada linha
    menores_linha = obter_menores_de_cada_linha(matriz)

    # Menores de cada coluna
    menores_coluna = obter_menores_de_cada_coluna(matriz)

    file_path = os.path.abspath("Arquivos_Saida/")
    with open(file_path + arquivo_saida + '.txt', 'w') as file:
        np.savetxt(file, matriz_ordenada_linha, fmt='%1.7e')
        np.savetxt(file, matriz_ordenada_coluna, fmt='%1.7e')
        np.savetxt(file, soma_linhas.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, soma_colunas.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, maiores_linha, fmt='%1.7e')
        np.savetxt(file, maiores_coluna, fmt='%1.7e')
        np.savetxt(file, menores_linha, fmt='%1.7e')
        np.savetxt(file, menores_coluna, fmt='%1.7e')
        np.savetxt(file, soma_total, fmt='%1.7e')

# Função para ler o arquivo txt e converter para uma matriz
def ler_arquivo_txt(arquivo_txt):
    file_path = os.path.abspath("Arquivos_Entrada/")
    with open(file_path +  "/" + str(arquivo_txt) + '.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    
    matriz = np.zeros((len(linhas), len(linhas[0].split())), dtype=np.int32)
    # matriz = np.zeros((len(linhas), len(linhas[0].split())), dtype=np.float64)

    for i, linha in enumerate(linhas):
        valores = linha.split()
        for j, valor in enumerate(valores):
            matriz[i, j] = float(valor)
    
    return matriz

def executar_todos_arquivos():
    for i in range(1, 31):
        arquivo_txt = str(i)
        matriz = ler_arquivo_txt(arquivo_txt)
        escrever_arquivo_saida(matriz, arquivo_txt)
    

if __name__ == '__main__':
    # Exemplo de uso
    t0 = time.time()
    arquivo_txt = '1'
    matriz = ler_arquivo_txt(arquivo_txt)
    # escrever_arquivo_saida(matriz, str(arquivo_txt))
    executar_todos_arquivos()
    t1 = time.time()
    print("Tempo de execução com numba: ", round(t1-t0, 3), " segundos")