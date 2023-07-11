import numpy as np
import time

ini_time_program = time.time()
min = 1
max = 4
tempos_r = []
tempos_cpu = []
tempos_w = []
tempos_tot = []
for i in range(min, max):
    arquivo_in = 'Arquivos_Entrada/'+str(i)+'.txt'
    arquivo_out = 'Arquivos_Saida/'+str(i)+'_OUT.txt'
    
    ini_time_r = time.time()
    matriz = np.loadtxt(arquivo_in, dtype=float)
    print(matriz)
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
    print(end_time_w - ini_time_w)

print(tempos_r)
print(tempos_cpu)
print(tempos_w)
print(tempos_tot)
# print(*tempos_tot, sep='\n')

end_time_program = time.time()
print(end_time_program - ini_time_program)
