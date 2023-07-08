import numpy as np
import time

# Criando um array 1000x1000 com numeros aleatorios
#a = np.random.randint(low=-100, high=101, size=(1000,1000))
min = 1
max = 5
tempos = []
for i in range(min, max):
    arquivo = str(i)+'.txt'
    start = time.time()
    a = np.loadtxt('Arquivos_Entrada/'+arquivo, dtype=float)   
    # Ordenando cada linha separadamente
    ordlin = np.sort(a, axis=1)
    ordcol = np.sort(a, axis=0)
    somal = np.sum(a, axis=1)
    somac = np.sum(a, axis=0)
    tot = np.sum(a)
    maxl = np.max(a, axis=1)
    maxc = np.max(a, axis=0)
    minl = np.min(a, axis=1)
    minc = np.min(a, axis=0)
    end = time.time()
    tempos.append(end - start)
print(tempos)
tempos2 = []
# salvando o array em um arquivo txt
for i in range(min, max):
    arquivo = str(i)+'_out.txt'
    start = time.time()
    with open('OUT/'+ arquivo, 'w') as file:
        np.savetxt(file, ordlin, fmt='%1.7e')
        np.savetxt(file, ordcol, fmt='%1.7e')
        np.savetxt(file, somal.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, somac.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, tot.reshape(1,1), fmt='%1.7e')
        np.savetxt(file, maxl.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, maxc.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, minl.reshape(1,1000), fmt='%1.7e')
        np.savetxt(file, minc.reshape(1,1000), fmt='%1.7e')
        end = time.time()
        tempos2.append(end - start)
print(tempos2)