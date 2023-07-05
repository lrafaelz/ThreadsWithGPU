import tensorflow as tf
import time

physical_devices = tf.config.list_physical_devices('GPU')

# Verificar se a GPU está disponível e habilitar o uso da GPU no Colab
if tf.config.list_physical_devices('GPU'):
    tf.config.experimental.set_memory_growth(tf.config.list_physical_devices('GPU')[0], True)

# Criar a matriz de entrada
matriz = tf.random.normal((1000, 1000))

ti = time.time()
# Ordenar cada linha separadamente
matriz_linha = tf.sort(matriz, axis=1)
matriz_coluna = tf.sort(matriz, axis=0)
tf = time.time()

if physical_devices:
    for device in physical_devices:
        print(f"GPU disponível: {device}")
else:
    print("Nenhuma GPU disponível.")
# Imprimir o tempo total
print('Tempo total = ', (tf -ti))
# Imprimir a matriz ordenada
print(matriz_linha)
print(matriz_coluna)