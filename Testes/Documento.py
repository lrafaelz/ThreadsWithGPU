import os
import numpy as np
import multiprocessing as mp
import time
import fnmatch

# print len(fnmatch.filter(os.listdir(dirpath), '*.txt'))

def ler_arquivo_txt(arquivo_txt):
    ini_time = time.time()
    matriz = np.loadtxt(arquivo_txt, dtype=float)
    end_time = time.time()
    tempo_r = end_time - ini_time
    return matriz, tempo_r

def arquivos_txt():
    arquivos_txt = []
    for i in range(1, 11):
        arquivos_txt.append('Arquivos_Entrada/' + str(i) + '.txt')
    return arquivos_txt

def readMulticore():
    arquivos = arquivos_txt()
    ini = time.time()
    pool = mp.Pool(mp.cpu_count())
    resultados = pool.map(ler_arquivo_txt, arquivos)
    pool.close()
    pool.join()
    end = time.time()
    print(end - ini)

    print(resultados[0][1])
    # for resultado in resultados:
        # print(resultado[1])

if __name__ == '__main__':
    readMulticore()
