import time # Para retornar o tempo de execução

# Função que transforma o arquivo em uma Matriz de caracteres

def função_matriz(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    matriz = [list(linha.strip()) for linha in linhas]
    return matriz

# Função que realiza a Busca em Profundidade

def DFS(matriz, linha, coluna, visitado, caminho_atual):
    LINHAS, COLUNAS = len(matriz), len(matriz[0])

    if (min(linha, coluna) < 0 or 
        linha == LINHAS or 
        coluna == COLUNAS or 
        (linha, coluna) in visitado or 
        matriz[linha][coluna] == '#'):
        return False

    caminho_atual.append((linha, coluna))

    if matriz[linha][coluna] == 'E':
        print("Caminho encontrado:", caminho_atual)
        return True

    visitado.add((linha, coluna))

    if (DFS(matriz, linha + 1, coluna, visitado, caminho_atual) or
        DFS(matriz, linha, coluna + 1, visitado, caminho_atual) or
        DFS(matriz, linha - 1, coluna, visitado, caminho_atual) or
        DFS(matriz, linha, coluna - 1, visitado, caminho_atual)):
        return True

    visitado.remove((linha, coluna))
    caminho_atual.pop()
    return False

# Exemplo de uso

def menu():
    while True:
        print("\nMenu:")
        print("1. Realizar busca em profundidade")
        print("2. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            caminho_arquivo = input("Digite o arquivo desejado: ")
            matriz = função_matriz(caminho_arquivo)
            for linha in matriz:
                print(linha)

            # Encontrando a posição inicial 'S'
            posicao_inicial = None
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j] == 'S':
                        posicao_inicial = (i, j)
                        break
                if posicao_inicial:
                    break

            # Calculando e imprimindo o caminho
            if posicao_inicial:
                linha_inicial, coluna_inicial = posicao_inicial
                visitado = set()
                caminho_atual = []
            # Medindo o tempo de execução
            inicio = time.time()
            if not DFS(matriz, linha_inicial, coluna_inicial, visitado, caminho_atual):
                print("Nenhum caminho encontrado do início ao fim.")
            fim = time.time()

            tempo_execucao = fim - inicio
            print(f"Tempo de execução da DFS: {tempo_execucao:.6f} segundos")
        elif escolha == '2':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

