# Leitura de arquivo com dados de entrada será em pandas ou conversão do txt para hdf5 para leitura através de h5py

# ordenação dos dados de entrada usando o numpy com counting sort

# conversor txt to hdf5
# https://stackoverflow.com/questions/56999923/to-convert-hdf5-to-txt-file

import h5py
import sys
# leitura do arquivo txt



def txtToHdf5(arquivo_txt, arquivo_hdf5):
    with open('Arquivos_Entrada/' + arquivo_txt, 'r') as arquivo_txt:
        # Lê o conteúdo do arquivo de texto
        conteudo = arquivo_txt.read()

    # Cria um arquivo HDF5
    saida_hdf5 = h5py.File("Arquivos_h5/" + arquivo_hdf5, 'w')

    # Cria um conjunto de dados no arquivo HDF5
    dataset = saida_hdf5.create_dataset('dados', data=conteudo)

    # Fecha o arquivo HDF5
    saida_hdf5.close()

def Hdf5ToTxt(arquivo_txt, arquivo_hdf5):
    entrada_hdf5 = h5py.File("Arquivos_h5/" + arquivo_hdf5, 'r')

    # Obtém o conjunto de dados do arquivo HDF5
    dataset = entrada_hdf5['dados']

    # Obtém os dados do conjunto de dados
    dados = dataset[()]


    # Escreve os dados em um arquivo de texto
    with open('Arquivos_Saida/' + arquivo_txt, 'w') as saida_txt:
        saida_txt.write(str(dados))

    # Fecha o arquivo HDF5
    entrada_hdf5.close()

# rode o programa com $ python main.py 1 1.txt 1.h5
# 1º argumento:
# 1 para converter de txt para hdf5
# 2 para converter de hdf5 para txt

if __name__ == '__main__':
    # Exemplo de uso
    arquivo_txt = '1.txt'
    arquivo_hdf5 = '1.h5'
    # txtToHdf5(arquivo_txt, arquivo_hdf5)
    Hdf5ToTxt(arquivo_txt, arquivo_hdf5)
