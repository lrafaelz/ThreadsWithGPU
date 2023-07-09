import numpy as np
import time
import multiprocessing as mp
import os

def execution(min, max):
    tempos_r = []
    tempos_cpu = []
    tempos_w = []
    tempos_tot = []
    for i in range(min, max):
        path_in = os.path.abspath("Arquivos_Entrada/")
        arquivo_in = path_in + '/' + str(i) + '.txt'
        path_out = os.path.abspath("Arquivos_Saida/")
        arquivo_out = path_out + '/' + str(i) + '_OUT.txt'
        
        ini_time_r = time.time()
        matriz = np.loadtxt(arquivo_in, dtype=float)
        end_time_r = time.time()
        
        ini_time_cpu = time.time()
        ordlin = np.sort(matriz, axis=1)
        ordcol = np.sort(matriz, axis=0)
        somal = np.sum(matriz, axis=1)
        somac = np.sum(matriz, axis=0)
        total = np.sum(matriz)
        maxl = np.max(matriz, axis=1)
        maxc = np.max(matriz, axis=0)
        minl = np.min(matriz, axis=1)
        minc = np.min(matriz, axis=0)
        end_time_cpu = time.time()

        ini_time_w = time.time()
        with open(arquivo_out, 'w') as file:
            np.savetxt(file, ordlin, fmt='%1.7e')
            np.savetxt(file, ordcol, fmt='%1.7e')
            np.savetxt(file, somal.reshape(1, 1000), fmt='%1.7e')
            np.savetxt(file, somac.reshape(1, 1000), fmt='%1.7e')
            np.savetxt(file, total.reshape(1, 1), fmt='%1.7e')
            np.savetxt(file, maxl.reshape(1, 1000), fmt='%1.7e')
            np.savetxt(file, maxc.reshape(1, 1000), fmt='%1.7e')
            np.savetxt(file, minl.reshape(1, 1000), fmt='%1.7e')
            np.savetxt(file, minc.reshape(1, 1000), fmt='%1.7e')
        end_time_w = time.time()

        tempos_r.append(end_time_r - ini_time_r)
        tempos_cpu.append(end_time_cpu - ini_time_cpu)
        tempos_w.append(end_time_w - ini_time_w)
        tempos_tot.append(end_time_w - ini_time_r)

    # print(tempos_r)
    # print(tempos_cpu)
    # print(tempos_w)
    print(tempos_tot)
    # print(*tempos_tot, sep='\n')

if __name__ == "__main__":
    ini_time_program = time.time()

    min = 1
    max = 11
    processos = []
    for i in range(min, max):
        processo = mp.Process(target=execution, args=(min, max))
        processo.start()
        processos.append(processo)
    for processo in processos:
        processo.join()
    
    end_time_program = time.time()
    print(end_time_program - ini_time_program)
