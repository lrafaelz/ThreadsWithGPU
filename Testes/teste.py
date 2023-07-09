import torch
import time

if __name__ == '__main__':
    matriz = torch.randn(1000, 1000)
    if torch.cuda.is_available():
        print ('GPU disponível', torch.cuda.get_device_name(torch.cuda.current_device()))
        matriz = matriz.cuda()
    ti = time.time()
    matriz_linha, _ = torch.sort(matriz, dim=1)
    matriz_coluna, _ = torch.sort(matriz, dim=0)
    tf = time.time()
    print('-----------------------------------')
    print('O tempo total = ', (tf - ti))
    print(matriz_linha)
    print('-----------------------------------')
    print(matriz_coluna)