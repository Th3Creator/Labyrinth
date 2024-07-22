# Labyrinth

### 1. Importar o módulo `time`

- **`import time`**: Importa o módulo `time`, que permite medir o tempo de execução do código.

### 2. Ler o arquivo e criar a matriz

- **`open(caminho_arquivo, 'r')`**: Abre o arquivo no modo de leitura.
- **`linhas = arquivo.readlines()`**: Lê todas as linhas do arquivo e as armazena em uma lista.
- **`list(linha.strip())`**: Converte cada linha em uma lista de caracteres, removendo espaços em branco no início e no fim.
- **`matriz`**: A matriz resultante onde cada linha do arquivo é uma lista de caracteres.

### 3. Função DFS (Busca em Profundidade) - fonte: https://medium.com/@anwarhermuche/métodos-de-busca-em-grafos-bfs-dfs-cf17761a0dd9

- **`LINHAS, COLUNAS = len(matriz), len(matriz[0])`**: Obtém o número de linhas e colunas da matriz.
- **Condições de parada**:
  - **`min(linha, coluna) < 0`**: Verifica se a posição está fora dos limites da matriz.
  - **`linha == LINHAS or coluna == COLUNAS`**: Verifica se a posição está fora dos limites da matriz.
  - **`(linha, coluna) in visitado`**: Verifica se a posição já foi visitada.
  - **`matriz[linha][coluna] == '#'`**: Verifica se a posição é uma parede.
- **`caminho_atual.append((linha, coluna))`**: Adiciona a coordenada atual ao caminho.
- **Condição de sucesso**:
  - **`matriz[linha][coluna] == 'E'`**: Verifica se a posição atual é o fim. Se for, imprime o caminho e retorna `True`.
- **`visitado.add((linha, coluna))`**: Marca a posição atual como visitada.
- **Recursão**:
  - Tenta mover para baixo, direita, cima e esquerda, chamando a função DFS recursivamente.
  - Se qualquer uma das chamadas recursivas retornar `True`, a função retorna `True`.
- **Backtracking**:
  - **`visitado.remove((linha, coluna))`**: Desmarca a posição atual como visitada.
  - **`caminho_atual.pop()`**: Remove a coordenada atual do caminho se não levar ao fim.

### 4. Uso do código

- **`caminho_arquivo = 'maze/toy.txt'`**: Define o caminho do arquivo.
- **`matriz = ler_arquivo_como_matriz(caminho_arquivo)`**: Lê o arquivo e cria a matriz.
- **Encontrando a posição inicial 'S'**:
  - Percorre a matriz para encontrar a posição inicial marcada com 'S'.
- **Calculando e imprimindo o caminho com tempo de execução**:
  - Se a posição inicial for encontrada, chama a função DFS para encontrar e imprimir o caminho do início ao fim.
  - **Medindo o tempo de execução**:
    - **`inicio = time.time()`**: Marca o tempo de início antes da execução da DFS.
    - **`fim = time.time()`**: Marca o tempo de fim após a execução da DFS.
    - **`tempo_execucao = fim - inicio`**: Calcula o tempo de execução subtraindo o tempo de início do tempo de fim.
    - **Impressão do tempo de execução**: Imprime o tempo de execução da DFS em segundos.
  - Se não houver caminho, imprime uma mensagem indicando isso.