# README

## Descrição

Este programa implementa duas técnicas de busca em um labirinto representado por uma matriz: Busca em Profundidade (DFS) e Busca em Largura (BFS), nos quais as funções foram baseadas e adaptadas a partir deste blog sobre [Métodos de Buscas em Grafos](https://medium.com/@anwarhermuche/métodos-de-busca-em-grafos-bfs-dfs-cf17761a0dd9). O labirinto é carregado a partir de um arquivo de texto, onde 'S' representa a posição inicial, 'E' a posição final, ' ' (espaço) representa caminhos livres e '#' ou '█' representam obstáculos. O usuário pode escolher qual técnica de busca utilizar através de um menu interativo.

## Funcionalidades

1. **Busca em Profundidade (DFS)**: Explora o labirinto tentando ir o mais profundo possível antes de retroceder.
2. **Busca em Largura (BFS)**: Explora o labirinto camada por camada, garantindo que o caminho mais curto é encontrado.

## Estrutura do Código

- **CriaMatriz(caminho_arquivo)**: Carrega o labirinto a partir de um arquivo de texto.
- **BuscaEmProfundidade(matriz, linha, coluna, visitado, caminhoAtual)**: Implementa a busca em profundidade.
- **BuscaEmLargura(matriz, linha, coluna, visitados, caminhos)**: Implementa a busca em largura.
- **Menu()**: Exibe um menu interativo para o usuário escolher entre as buscas ou sair do programa.

## Instruções de Uso

1. Execute o script.
2. Escolha a busca desejada no menu.
3. Insira o arquivo de texto, seguindo o modelo "maze/nome_arquivo.txt".
4. O resultado da busca e o tempo de execução serão exibidos.

## Autores

Felipe Fialho e Christian Daniel 

---
