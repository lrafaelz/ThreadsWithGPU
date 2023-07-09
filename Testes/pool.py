from multiprocessing import Pool
import time
import numpy as np

def process_line(line):
    return "FOO: %s" % line

if __name__ == "__main__":
    ini_time_r = time.time()

    pool = Pool(4)
    with open('Arquivos_Entrada/1.txt') as source_file:
        # chunk the work into batches of 4 lines at a time
        results = pool.map(process_line, source_file, 4)
    
    end_time_r = time.time()

    print(end_time_r - ini_time_r)

    ini_time_r = time.time()

    matriz = np.loadtxt('Arquivos_Entrada/1.txt', dtype=float)
    
    end_time_r = time.time()

    print(end_time_r - ini_time_r)

        
    # print(results)
