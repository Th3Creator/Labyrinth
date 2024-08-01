import time 
from collections import deque

def CriaMatriz(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    matriz = [list(linha.strip()) for linha in linhas]
    
    return matriz

def BuscaEmProfundidade(matriz, linha, coluna, visitado, caminhoAtual):
    LINHAS, COLUNAS = len(matriz), len(matriz[0])

    if (min(linha, coluna) < 0 or 
        linha == LINHAS or 
        coluna == COLUNAS or 
        (linha, coluna) in visitado or
        matriz[linha][coluna] == '#' or 
        matriz[linha][coluna] == '█'):
        return False

    caminhoAtual.append((linha, coluna))

    if matriz[linha][coluna] == 'E':
        print("Caminho encontrado:", sorted(caminhoAtual))
        return True

    visitado.add((linha, coluna))

    if (BuscaEmProfundidade(matriz, linha + 1, coluna, visitado, caminhoAtual) or
        BuscaEmProfundidade(matriz, linha, coluna + 1, visitado, caminhoAtual) or
        BuscaEmProfundidade(matriz, linha - 1, coluna, visitado, caminhoAtual) or
        BuscaEmProfundidade(matriz, linha, coluna - 1, visitado, caminhoAtual)):
        return True

    visitado.remove((linha, coluna))
    caminhoAtual.pop()

    return False

def BuscaEmLargura(matriz, linha, coluna, visitados):
    LINHAS, COLUNAS = len(matriz), len(matriz[0])
    
    fila = deque([((linha, coluna), [(linha, coluna)])])
   
    visitados.add((linha, coluna))
    
    while fila:
        (linha, coluna), caminho = fila.popleft()
        
        if matriz[linha][coluna] == 'E':
            print("Caminho encontrado:", caminho)
            return True
        
        vizinhos = [(linha+1, coluna), (linha-1, coluna), (linha, coluna+1), (linha, coluna-1)]
        
        for newLinha, newColuna in vizinhos:
            if (0 <= newLinha < LINHAS and 
                0 <= newColuna < COLUNAS and 
                matriz[newLinha][newColuna] != '#' and
                matriz[newLinha][newColuna] != '█' and  
                (newLinha, newColuna) not in visitados):
                
                fila.append(((newLinha, newColuna), caminho + [(newLinha, newColuna)]))
                visitados.add((newLinha, newColuna))
    
    return False

def Menu():
    while True:  
        print("\n\n ▄█          ▄████████ ▀█████████▄  ▄██   ▄      ▄████████  ▄█  ███▄▄▄▄       ███        ▄█    █▄\n"    + 
              "███         ███    ███   ███    ███ ███   ██▄   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄   ███    ███\n" + 
              "███         ███    ███   ███    ███ ███▄▄▄███   ███    ███ ███▌ ███   ███    ▀███▀▀██   ███    ███\n"    + 
              "███         ███    ███  ▄███▄▄▄██▀  ▀▀▀▀▀▀███  ▄███▄▄▄▄██▀ ███▌ ███   ███     ███   ▀  ▄███▄▄▄▄███▄▄\n"  + 
              "███       ▀███████████ ▀▀███▀▀▀██▄  ▄██   ███ ▀▀███▀▀▀▀▀   ███▌ ███   ███     ███     ▀▀███▀▀▀▀███▀\n"   + 
              "███         ███    ███   ███    ██▄ ███   ███ ▀███████████ ███  ███   ███     ███       ███    ███\n"    + 
              "███▌    ▄   ███    ███   ███    ███ ███   ███   ███    ███ ███  ███   ███     ███       ███    ███\n"    + 
              "█████▄▄██   ███    █▀  ▄█████████▀   ▀█████▀    ███    ███ █▀    ▀█   █▀     ▄████▀     ███    █▀")
        print("\n\n1. Realizar busca em profundidade")
        print("2. Realizar busca em largura")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            caminhoArquivo = input("Digite o arquivo desejado:")
           
            matriz = CriaMatriz(caminhoArquivo)
           
            for linha in matriz:
                print(linha)

            posicaoInicial = None
            
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j] == 'S':
                        posicaoInicial = (i, j)
                        break
                if posicaoInicial:
                    break

            if posicaoInicial:
                linhaInicial, colunaInicial = posicaoInicial
                visitado = set()
                caminhoAtual = []

            inicio = time.time()
            if not BuscaEmProfundidade(matriz, linhaInicial, colunaInicial, visitado, caminhoAtual):
                print("Nenhum caminho encontrado do início ao fim.")           
            fim = time.time()

            tempoDeExecucao = fim - inicio
           
            print(f"Tempo de execução da busca em profundidade: {tempoDeExecucao:.6f} segundos")
        elif escolha == '2':
            caminhoArquivo = input("Digite o arquivo desejado:")
           
            matriz = CriaMatriz(caminhoArquivo)
           
            for linha in matriz:
                print(linha)

            posicaoInicial = None
            
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j] == 'S':
                        posicaoInicial = (i, j)
                        break
                if posicaoInicial:
                    break

            if posicaoInicial:
                linhaInicial, colunaInicial = posicaoInicial
                visitado = set()
                caminhos = []

            inicializaCronometro = time.time()
            if not BuscaEmLargura(matriz, linhaInicial, colunaInicial, visitado):
                print("Nenhum caminho encontrado do início ao fim.")
            finalizaCronometro = time.time()

            print(f"Tempo de execução da busca em largura: {(finalizaCronometro - inicializaCronometro):.6f} segundos")
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

Menu()