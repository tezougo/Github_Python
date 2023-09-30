# import osmnx as ox
# import networkx as nx
# import pandas as pd
# import matplotlib.pyplot as plt

# # Função para calcular a distância entre duas cidades
# def calcular_distancia(cidade1, cidade2):
#     origem = ox.geocode(cidade1 + ", SC")
#     destino = ox.geocode(cidade2 + ", SC")
#     origem_node = ox.distance.nearest_nodes(G, origem[1], origem[0])
#     destino_node = ox.distance.nearest_nodes(G, destino[1], destino[0])
#     distancia = nx.shortest_path_length(G, origem_node, destino_node, weight='length')
#     return distancia / 1000  # Convertendo para km

# # Ler a lista de cidades de Santa Catarina de um arquivo Excel
# df_cidades = pd.read_excel('C:\\Users\\wagne\\OneDrive\\Documentos\\Github_Repos\\Github_Python\\Modelagem_analise_avaliacao_de_Desempenho_de_Sistemas_Automatizados\\Grafo_1_em_grupo\\DistanciasRodoviarias\\cidades_sc.xlsx')
# cidades_sc = df_cidades['Cidade'].tolist()

# # Obtenha o grafo de estradas de Santa Catarina
# G = ox.graph_from_place('Santa Catarina, Brazil', network_type='drive')

# # Criar um grafo completo com as cidades e as distâncias em relação a Blumenau
# grafo_completo = nx.Graph()
# for cidade in cidades_sc:
#     distancia = calcular_distancia(cidade, 'Blumenau')
#     grafo_completo.add_edge('Blumenau', cidade, weight=distancia)

# # Usar o algoritmo de Kruskal para encontrar a árvore geradora mínima
# arvore_geradora_minima = nx.minimum_spanning_tree(grafo_completo)

# # Plotar o grafo completo
# plt.figure(figsize=(12, 8))
# pos = nx.spring_layout(grafo_completo)
# nx.draw(grafo_completo, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=15)
# plt.title('Grafo Completo das Cidades em relação a Blumenau')
# plt.savefig('grafo_completo.png')
# plt.show()

# # Plotar a árvore geradora mínima
# plt.figure(figsize=(12, 8))
# nx.draw(arvore_geradora_minima, pos, with_labels=True, node_color='lightgreen', node_size=1000, font_size=15)
# plt.title('Árvore Geradora Mínima')
# plt.savefig('arvore_geradora_minima.png')
# plt.show()

import itertools
import matplotlib.pyplot as plt
import networkx as nx
import osmnx as ox
import random

# Representação das cidades de SC
cidades = ['Abdon Batista', 'Abelardo Luz', 'Agrolândia', 'Agronômica', 'Água Doce', 'Águas de Chapecó', 'Águas Frias', 'Águas Mornas', 'Alfredo Wagner', 'Alto Bela Vista']

class Arvore_alcancabilidade_kruskal:
    def __init__(self, cidades):
        # Obtenha o grafo de estradas de Santa Catarina
        self.G = ox.graph_from_place('Florianópolis, Brazil', network_type='drive')
        self.cidades = set(cidades)
        self.grafo_completo = nx.Graph()
        self.conjuntos = {cidade: {cidade} for cidade in cidades}
        self.arvore = nx.Graph()
        self.distancias = {}
        for cidade1, cidade2 in itertools.combinations(cidades, 2):
            self.distancias[(cidade1, cidade2)] = random.randint(10, 200)
        
        self.arestas = sorted(self.distancias.items(), key=lambda x: x[1])
        
        for (cidade1, cidade2), distancia in self.arestas:
            if self.conjuntos[cidade1] != self.conjuntos[cidade2]:
                self.arvore.add_edge(cidade1, cidade2, weight=distancia)
                novo_conjunto = self.conjuntos[cidade1].union(self.conjuntos[cidade2])
                for cidade in novo_conjunto:
                    self.conjuntos[cidade] = novo_conjunto

    def calcular_distancia(self, cidade1, cidade2):
        origem = ox.geocode(cidade1 + ", SC")
        destino = ox.geocode(cidade2 + ", SC")
        origem_node = ox.distance.nearest_nodes(self.G, origem[1], origem[0])
        destino_node = ox.distance.nearest_nodes(self.G, destino[1], destino[0])
        distancia = nx.shortest_path_length(self.G, origem_node, destino_node, weight='length')
        return distancia / 1000  # Convertendo para km

    def plotar_grafo_completo(self):
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.grafo_completo)
        nx.draw(self.grafo_completo, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=15)
        plt.title('Grafo Completo das Cidades em relação a Florianópolis')
        plt.savefig('grafo_completo.png')
        plt.show()

        # Plotar a árvore geradora mínima
        plt.figure(figsize=(12, 8))
        nx.draw(self.arvore, pos, with_labels=True, node_color='lightgreen', node_size=1000, font_size=15)
        plt.title('Árvore Geradora Mínima')
        plt.savefig('arvore_geradora_minima.png')
        plt.show()

# Execução
arvore_alcan = Arvore_alcancabilidade_kruskal(cidades)
arvore_alcan.plotar_grafo_completo()

