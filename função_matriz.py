def função_matriz(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    # Removemos os espaços em branco e criamos uma matriz
    matriz = [list(linha.strip()) for linha in linhas]
    
    return matriz

# Exemplo de uso:
caminho_arquivo = "maze/maze3_blocks.txt"
matriz_do_labirinto = função_matriz(caminho_arquivo)

# Exibindo a matriz
for linha in matriz:
    print(linha)
