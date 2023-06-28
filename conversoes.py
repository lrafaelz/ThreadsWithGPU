# Leitura de arquivo com dados de entrada será em pandas ou conversão do txt para hdf5 para leitura através de h5py

# ordenação dos dados de entrada usando o numpy com counting sort


import h5py
import time
import multiprocessing as mp
# leitura do arquivo txt

# Funções para conversão de um único arquivo (txt ou hdf5)
def txtToHdf5(arquivo_txt, arquivo_hdf5):
    with open('Arquivos_Entrada/' + str(arquivo_txt), 'r') as arquivo_txt:
        # Lê o conteúdo do arquivo de texto
        conteudo = arquivo_txt.read()

    # Cria um arquivo HDF5
    saida_hdf5 = h5py.File("Arquivos_h5/" + str(arquivo_hdf5), 'w')

    # Cria um conjunto de dados no arquivo HDF5
    dataset = saida_hdf5.create_dataset('dados', data=conteudo)

    # Fecha o arquivo HDF5
    saida_hdf5.close()

def hdf5ToTxt(arquivo_txt, arquivo_hdf5):
    entrada_hdf5 = h5py.File("Arquivos_h5/" + str(arquivo_hdf5), 'r')

    # Obtém o conjunto de dados do arquivo HDF5
    dataset = entrada_hdf5['dados']

    # Obtém os dados do conjunto de dados
    dados = str(dataset[()])

    # Remove o caractere b' no início e o \n' no final do conteúdo
    dados = dados.strip("b").strip("'")

    # Escreve os dados em um arquivo de texto
    with open('Arquivos_Saida/' + str(arquivo_txt), 'w') as saida_txt:
        saida_txt.write(dados)

    # Fecha o arquivo HDF5
    entrada_hdf5.close()


# Funções para conversão de um range de arquivos (txt ou hdf5), utilizado para multiprocessamento
def txtToHdf5Loop(start, end):
    for i in range(start, end):
        i += 1
        arquivo_txt = str(i) + '.txt'
        arquivo_hdf5 = str(i) + '.h5'
        txtToHdf5(arquivo_txt, arquivo_hdf5)

def hdf5ToTxtLoop(start, end):
    for i in range(start, end):
        i += 1
        arquivo_txt = str(i) + '_out.txt'
        arquivo_hdf5 = str(i) + '.h5'
        hdf5ToTxt(arquivo_txt, arquivo_hdf5)

# Função para multiprocessamento
def multicore(func):
    max = 100 
    nThreads = mp.cpu_count()
    jobs = []
    # print('Número de threads: ', nThreads)
    t1 = time.time()
    for i in range(nThreads):
        # definindo intervalos de atuação a cada thread
        
        min_ = int(i*(max/nThreads))
        max_ = int((i+1)*(max/nThreads))
        if func == 1:
            p = mp.Process(target=txtToHdf5Loop, args=(min_, max_))
        elif func == 2:
            p = mp.Process(target=hdf5ToTxtLoop, args=(min_, max_))
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
    t2 = time.time()
    return t2-t1


if __name__ == '__main__':
    # Exemplo de uso
    # arquivo_txt = '1.txt'
    # arquivo_hdf5 = '1.h5'
    # # txtToHdf5(arquivo_txt, arquivo_hdf5)
    # hdf5ToTxt(arquivo_txt, arquivo_hdf5)

    print('Singlecore: ')
    t1 = time.time()
    txtToHdf5Loop(1, 100)
    t2 = time.time()
    print('Tempo de conversão de txt para hdf5: ', t2-t1)
    t3 = time.time()
    hdf5ToTxtLoop(1, 100)
    t4 = time.time()
    print('Tempo de conversão de hdf5 para txt: ', t4-t3)
    print('----------------------------------------------------')
    print('Tempo total de conversão singleThread: ', t4-t1)
    print('\n----------------------------------------------------\n')

    print('Multicore: ')
    tmp = multicore(1)
    
    print('Tempo de conversão de txt para hdf5: ', tmp)
    tmp1 = multicore(2)
    print('Tempo de conversão de hdf5 para txt: ', tmp1)
    print('----------------------------------------------------')
    print('Tempo total de conversão multiThread: ', tmp + tmp1)
    print('----------------------------------------------------')





    

