import numpy as np
import time

min = 1
max = 11
tempos = []
for i in range(min, max):
    arquivo  = 'Arquivos_Entrada/'+str(i)+'.txt'
    ini_time = time.time()
    a        = np.loadtxt(arquivo, dtype=float)
    ordlin   = np.sort(a, axis=1)
    ordcol   = np.sort(a, axis=0)
    somal    = np.sum(a, axis=1)
    somac    = np.sum(a, axis=0)
    tot      = np.sum(a)
    maxl     = np.max(a, axis=1)
    maxc     = np.max(a, axis=0)
    minl     = np.min(a, axis=1)
    minc     = np.min(a, axis=0)
    end_time = time.time()
    tempos.append(end_time - ini_time)
print(tempos)
# tempos2 = []
# # salvando o array em um arquivo txt
# for i in range(min, max):
#     arquivo = str(i)+'_out2.txt'
#     ini_time = time.time()
#     with open('/content/drive/MyDrive/SO/SO FINAL/OUT/'+arquivo, 'w') as file:
#         np.savetxt(file, lins, fmt='%1.7e')
#         np.savetxt(file, cols, fmt='%1.7e')
#         np.savetxt(file, somaL.reshape(1, 1000), fmt='%1.7e')
#         np.savetxt(file, somaC.reshape(1, 1000), fmt='%1.7e')
#         np.savetxt(file, total.reshape(1, 1), fmt='%1.7e')
#         np.savetxt(file, maiorL.reshape(1, 1000), fmt='%1.7e')
#         np.savetxt(file, maiorC.reshape(1, 1000), fmt='%1.7e')
#         np.savetxt(file, menorL.reshape(1, 1000), fmt='%1.7e')
#         np.savetxt(file, menorC.reshape(1, 1000), fmt='%1.7e')
#         end_time = time.time()
#         tempos2.append(end_time - ini_time)

# with open('/content/drive/MyDrive/SO/SO FINAL/OUT/tempos.txt', 'w') as file:
#     np.savetxt(file, tempos)
#     np.savetxt(file, tempos2)
# # print(tempos2)