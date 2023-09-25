import matplotlib.pyplot as plt
import networkx
import numpy as np

class Dijkstra:
    def __init__(self, matriz):
        # Matriz de adjacência que representa o grafo
        self.matriz = matriz
        #Verifica se a matriz é direcionada ou não
    def is_directed(self):
        for i in range(len(self.matriz)):
                for j in range(len(self.matriz)):
                    if self.matriz[i][j] != self.matriz[j][i]:
                        print("A matriz é direcionada")
                        return networkx.DiGraph  # A matriz é direcionada
        print("A matriz é não direcionada")
        return networkx.Graph  # A matriz é não direcionada
    def plotar_grafo_circulo(self, nome_arquivo='grafico_grafo.png'):
        """
        Plota um grafo usando o layout 'círculo' e salva em um arquivo.
        
        Parâmetros:
        - matriz: Uma matriz de adjacência que representa o grafo.
        - nome_arquivo: Nome do arquivo onde a imagem do grafo será salva.
        """
        # Criar um grafo utilizando a função from_numpy_array, a partir da matriz de adjacência
        # Converte uma lista de listas em um array numpy para ser usado como entrada da função from_numpy_array
        # Create_using é o tipo de grafo que será criado, no caso um grafo direcionado (DiGraph), Se não especificasse isso, o padrão seria criar um grafo não direcionado (Graph)
        G = networkx.convert_matrix.from_numpy_array(np.array(self.matriz), create_using=self.is_directed())
        
        # Definir o layout 'círculo'
        posicao = networkx.circular_layout(G)
        
        # Desenhar o grafo com os rótulos dos nós, tamanho e cor específicos
        networkx.draw(G, posicao, with_labels=True, node_size=700, node_color='skyblue', font_size=15, width=2, edge_color='gray')
        
        # Salvar o grafo em um arquivo
        plt.title('Grafo com Layout Círculo')
        plt.savefig(nome_arquivo)
        print(f'Grafo salvo como {nome_arquivo}')

    def calcular_caminhos(self, inicio):
        n = len(self.matriz)
        # Lista para armazenar a menor distância de 'inicio' para cada vértice
        menor_caminho = [float('inf')] * n
        # Lista para armazenar o vértice anterior no caminho mínimo
        antecessor = [-1] * n
        # Lista para marcar vértices já visitados
        visitados = [False] * n
        menor_caminho[inicio] = 0  # A distância do vértice inicial para ele mesmo é 0
        
        for _ in range(n):
            # Encontrar o vértice com a menor distância dentre os não visitados
            minimo = float('inf')
            u = -1
            for i in range(n):
                if not visitados[i] and menor_caminho[i] < minimo:
                    minimo = menor_caminho[i]
                    u = i
            visitados[u] = True  # Marcar o vértice 'u' como visitado
            
            # Atualizar as distâncias dos vértices adjacentes a 'u'
            for v in range(n):
                if self.matriz[u][v] and not visitados[v] and menor_caminho[u] + self.matriz[u][v] < menor_caminho[v]:
                    menor_caminho[v] = menor_caminho[u] + self.matriz[u][v]
                    antecessor[v] = u
        
        # Construir os caminhos a partir da lista de antecessores
        caminhos = {}
        for i in range(n):
            caminho = []
            atual = i
            while atual != -1:
                caminho.append(chr(65 + atual))  # Convertendo índices para letras, o 65 é o 'A' na tabela ASCII, A + 1 = B, A + 2 = C, ...
                atual = antecessor[atual]
            caminho.reverse() # Inverter a lista para que o caminho comece em 'inicio', exemplo: ['A', 'B', 'C', 'D']
            caminhos[chr(65 + i)] = ' -> '.join(caminho)  
        
        return caminhos