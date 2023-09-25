import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix

class Mag:
    def __init__(self):
        pass
    def calcular_menor_arvore_geradora(self, XY_Points, nodesName):
        # Calculando as distâncias entre os pontos usando a função distance_matrix
        # Isso cria uma matriz onde o elemento (i, j) é a distância euclidiana entre o ponto i e o ponto j
        # A distância euclidiana entre dois pontos (x1, y1) e (x2, y2) é calculada como:
        # sqrt((x2 - x1)^2 + (y2 - y1)^2)
        # Por exemplo, a distância entre os pontos (1, 2) e (4, 6) é 5.
        Adj_ndir = distance_matrix(XY_Points, XY_Points)

        # Criando um grafo não dirigido a partir da matriz de adjacência (matriz de distâncias)
        # A função from_numpy_matrix converte uma matriz numpy em um grafo
        G = nx.convert_matrix.from_numpy_array(Adj_ndir)

        # Renomeando os nós para usar os nomes fornecidos em nodesName
        # Isso cria um mapeamento de índices para nomes e aplica esse mapeamento ao grafo
        mapping = {i: nodesName[i] for i in range(len(nodesName))}
        G = nx.relabel_nodes(G, mapping)

        # Aplicando o algoritmo de Prim para encontrar a Menor Árvore Geradora (MAG)
        # A função minimum_spanning_tree retorna um novo grafo que é a MAG do grafo original
        T = nx.minimum_spanning_tree(G)

        # Definindo as posições dos nós para plotagem usando um dicionário
        # As chaves são os nomes dos nós e os valores são as coordenadas (x, y)
        pos = {nodesName[i]: XY_Points[i] for i in range(len(nodesName))}

        # Plotando o grafo
        plt.figure(figsize=(8, 6))

        # Desenhando o grafo original
        # Os parâmetros definem características visuais, como cor dos nós, tamanho, cor das arestas, etc.
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=15, width=2, edge_color='gray')

        # Desenhando as arestas da MAG em verde e com uma largura maior
        nx.draw_networkx_edges(T, pos, edge_color='g', width=3)

        # Adicionando um título ao gráfico
        plt.title('Grafo com Menor Árvore Geradora')
        plt.savefig(f"MAG_com_{len(nodesName)}_nos")
        print(f'Grafo salvo como {f"MAG_com_{len(nodesName)}_nos"}')