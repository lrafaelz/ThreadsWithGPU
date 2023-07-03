import numpy as np
# from numba import jit, prange, cuda

# Função para ordenar uma matriz por linha
# @jit(nopython=True, parallel=True)
def ordenar_matriz_por_linha(matriz):
    matriz_ordenada = np.sort(matriz, axis=1, kind='heapsort')
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

# Função para executar todas as operações em sequência
def executar_operacoes_arquivo(matriz):
    # Ordenação por linha
    matriz_ordenada_linha = ordenar_matriz_por_linha(matriz)

    # Ordenação por coluna
    matriz_ordenada_coluna = ordenar_matriz_por_coluna(matriz)

    # Soma das linhas
    soma_linhas = calcular_soma_das_linhas(matriz)

    # Soma das colunas
    soma_colunas = calcular_soma_das_colunas(matriz)

    # Soma total da matriz
    soma_total = calcular_soma_total(matriz)

    # Maiores de cada linha
    maiores_linha = obter_maiores_de_cada_linha(matriz)

    # Maiores de cada coluna
    maiores_coluna = obter_maiores_de_cada_coluna(matriz)

    # Menores de cada linha
    menores_linha = obter_menores_de_cada_linha(matriz)

    # Menores de cada coluna
    menores_coluna = obter_menores_de_cada_coluna(matriz)

    # Concatena todas as informações em um único array
    resposta = np.concatenate((matriz_ordenada_linha,
                               matriz_ordenada_coluna,
                               soma_linhas.reshape(1, 1000),
                               soma_colunas.reshape(1, 1000),
                               soma_total,
                               maiores_linha.reshape(1, 1000),
                               maiores_coluna.reshape(1, 1000),
                               menores_linha.reshape(1, 1000),
                               menores_coluna.reshape(1, 1000)),
                               axis=0)

    return resposta

def escrever_arquivo_saida_2(matriz, arquivo_saida):
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

    # Maiores de cada linha
    maiores_linha = obter_maiores_de_cada_linha(matriz)

    # Maiores de cada coluna
    maiores_coluna = obter_maiores_de_cada_coluna(matriz)

    # Menores de cada linha
    menores_linha = obter_menores_de_cada_linha(matriz)

    # Menores de cada coluna
    menores_coluna = obter_menores_de_cada_coluna(matriz)

    with open('arquivos_saida/' + arquivo_saida + '.txt', 'w') as file:
        np.savetxt(file, matriz_ordenada_linha, fmt='%1.7e')
        np.savetxt(file, matriz_ordenada_coluna, fmt='%1.7e')
        np.savetxt(file, soma_linhas.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, soma_colunas.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, maiores_linha.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, maiores_coluna.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, menores_linha.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, menores_coluna.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, soma_total.reshape(1,1), fmt='%1.7e')


# Função para ler o arquivo txt e converter para uma matriz
def ler_arquivo_txt(arquivo_txt):
    with open('Arquivos_Entrada/' + str(arquivo_txt) + '.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    
    matriz = np.zeros((len(linhas), len(linhas[0].split())), dtype=np.int32)
    
    for i, linha in enumerate(linhas):
        valores = linha.split()
        for j, valor in enumerate(valores):
            matriz[i, j] = float(valor)
    
    return matriz

# Função para escrever a resposta em um arquivo de saída
def escrever_arquivo_saida(resposta, arquivo_saida):
    with open(arquivo_saida, 'w') as arquivo:
        for linha in resposta:
            arquivo.write(' '.join(map(str, linha)) + '\n')

# Função para executar todas as operações em sequência nos arquivos de entrada
def executar_operacoes_sequencia_arquivos(arquivos_entrada, arquivo_saida):
    resposta_total = []
    
    for arquivo_entrada in arquivos_entrada:
        matriz = ler_arquivo_txt(arquivo_entrada)
        resposta = executar_operacoes_arquivo(matriz)
        resposta_total.append(resposta)
    
    resposta_total = np.concatenate(resposta_total, axis=1)
    
    escrever_arquivo_saida(resposta_total, arquivo_saida)


if __name__ == '__main__':
    # Exemplo de uso
    arquivo_txt = '1'
    matriz = ler_arquivo_txt(arquivo_txt)
    # resposta = executar_operacoes_arquivo(matriz)
    # escrever_arquivo_saida(resposta, 'Arquivos_Saida/' + str(arquivo_txt) + '.txt')
    escrever_arquivo_saida_2(matriz, str(arquivo_txt))
    