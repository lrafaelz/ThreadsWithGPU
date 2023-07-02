import h5py
import numpy as np

def ordenar_e_adicionar_soma_hdf5(nome_arquivo_entrada, nome_arquivo_saida):
    # Abre o arquivo HDF5 de entrada em modo de leitura
    arquivo_entrada = h5py.File('Arquivos_H5/' + nome_arquivo_entrada, 'r')
    
    # Obtém o conjunto de dados do arquivo HDF5
    dataset = arquivo_entrada['dados']
    
    # Verifica a dimensão da matriz
    if len(dataset.shape) != 2:
        raise ValueError("O conjunto de dados não possui a dimensão correta (2D).")
    
    # Converte o conjunto de dados em uma matriz NumPy
    matriz = np.array(dataset)
    
    # Ordena as linhas e colunas da matriz
    matriz_ordenada_linha = np.sort(matriz, axis=1)
    matriz_ordenada_coluna = np.sort(matriz, axis=0)
    
    # Calcula a soma de cada linha e coluna
    soma_linhas = np.sum(matriz_ordenada_linha, axis=1)
    soma_colunas = np.sum(matriz_ordenada_coluna, axis=0)
    
    # Fecha o arquivo de entrada
    arquivo_entrada.close()
    
    # Abre um novo arquivo HDF5 de saída em modo de escrita
    arquivo_saida = h5py.File('teste/' + nome_arquivo_saida, 'w')
    
    # Cria um novo conjunto de dados no arquivo de saída e escreve a matriz ordenada
    dataset_saida = arquivo_saida.create_dataset('dados', data=matriz_ordenada_linha)
    
    # Adiciona as duas linhas extras contendo as somas das linhas e colunas
    dataset_saida.resize((dataset_saida.shape[0] + 2, dataset_saida.shape[1]))
    dataset_saida[-2, :] = soma_linhas
    dataset_saida[-1, :] = soma_colunas
    
    # Fecha o arquivo de saída
    arquivo_saida.close()


# Exemplo de uso
arquivo_entrada = '1.h5'
arquivo_saida = '1_teste.h5'
ordenar_e_adicionar_soma_hdf5(arquivo_entrada, arquivo_saida)


# # Exemplo de uso
# arquivo_hdf5 = '1.h5'
# t1 = time.time()
# ordenar_valores_por_linha_otimizado(arquivo_hdf5)
# t2 = time.time()
# print('Tempo de execução: ', t2 - t1)