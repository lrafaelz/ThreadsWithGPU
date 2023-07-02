# ThreadsWithGPU
**Carregar arquivos texto** (use múltiplas threads para IO_Bound)

**Operações matemáticas:** (use múltiplas threads para CPU_Bound)
- Matriz ordenada por linha
- Matriz ordenada por coluna
- Soma das linhas
- Soma das colunas
- Soma total da matriz
- Maiores de cada linha
- Maiores de cada coluna
- Menores de cada linha
- Menores de cada coluna

## Requisitos

**Criar estratégia de otimização de IO** (variar nº de threads de IO)

**Criar estratégia de otimização de CPU** (variar nº de threads de CPU)

Espera-se:
- Interface definindo o diretório de entrada, número de threads e etc (20%)
- Separação das threads (IO_Bound(R/W) das de CPU_Bound) (10%)
- Coleta dos tempos de leitura (Threads de IO) (5%)
- Coleta dos tempos de execução (Threads de CPU) (5%)
- Coleta dos tempos de escrita (Threads de IO) (5%)
- Coleta do tempo total para cada arquivo concluído (5%)
- Coleta do tempo TOTAL de execução de software (10%)
- Gerar bons gráficos dos resultados (15%)
- Criar relatório, analisar resultados e concluir a respeito da solução proposta (25%)

## Resultados

**Espera-se como saída:**
Para cada arquivo de entrada <NÚMERO>.TXT um arquivo <NÚMERO>_OUT.TXT contendo:
- Matriz ordenada por linha (1000 x 1000 elementos [1000 linhas com 1000 elementos cada])
- Matriz ordenada por coluna (1000 x 1000 elementos [1000 linhas com 1000 elementos cada])
- Soma das linhas (1 linha do arquivo com 1000 elementos)
- Soma das colunas (1 linha do arquivo com 1000 elementos)
- Soma total da matriz (1 linha do arquivo com 1 elemento)
- Maiores de cada linha (1 linha do arquivo com 1000 elementos)
- Maiores de cada coluna (1 linha do arquivo com 1000 elementos)
- Menores de cada linha (1 linha do arquivo com 1000 elementos)
- Menores de cada coluna (1 linha do arquivo com 1000 elementos)
TOTAL DE LINHAS DO ARQUIVO DE RESPOSTA (2007 linhas)

## Avaliação

Escrever um relatório técnico contendo:
- Descrever a máquina onde foram executadas as operações;
- Serão avaliadas as soluções multi-thread para (IO e CPU) bound;
- Espera-se um gráfico de tempo mostrando os resultados (variando o tempo (eixo Y) vs o número de threads (eixo X) para as operações IO_bound);
- Espera-se um gráfico de tempo mostrando os resultados (variando o tempo (eixo Y) vs o número de threads (eixo X) para as operações CPU_bound);
- Espera-se uma conclusão perante a solução ótima encontrada para o problema;
OBS:
- O trabalho precisa ser apresentado pelos integrantes para o professor.
- Não respeitar os requisitos implica em sérios descontos.
- Se o programa rodar paralelo e otimizado em GPU (o grupo ganha 1 ponto extras na média final)
- O software mais rápido ganhará 0,5 na média final
