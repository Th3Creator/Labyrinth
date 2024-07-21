def arquivo_matriz(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    matriz = [list(linha.strip()) for linha in linhas]
    return matriz

# Exemplo de uso
caminho_arquivo = 'maze/toy.txt'
matriz = arquivo_matriz(caminho_arquivo)

# Exibindo a matriz
for linha in matriz:
    print(linha)
    
print(matriz[1][0])  # Isso deve retornar 'S'