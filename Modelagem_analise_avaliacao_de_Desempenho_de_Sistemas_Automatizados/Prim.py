import networkx as nx
from queue import PriorityQueue

def prim_algorithm(graph):
    """
    Implementação do algoritmo de Prim para encontrar a Menor Árvore Geradora (MAG) de um grafo.

    Parâmetros:
    - graph: Um grafo ponderado representado como um objeto NetworkX.

    Retorna:
    - Uma lista de arestas que formam a MAG.
    """
    
    # Inicialização
    visited = set()  # Conjunto para armazenar os vértices visitados
    start_vertex = list(graph.nodes())[0]  # Escolhe um vértice inicial arbitrário
    visited.add(start_vertex)
    edges = PriorityQueue()  # Fila de prioridade para armazenar as arestas por peso

    # Função auxiliar para adicionar arestas à fila de prioridade
    def add_edges(vertex):
        for dest, weight in graph[vertex].items():
            # Se o destino não foi visitado, adicione a aresta à fila de prioridade
            if dest not in visited:
                edges.put((weight['weight'], vertex, dest))

    # Adiciona as arestas do vértice inicial à fila de prioridade
    add_edges(start_vertex)
    mst = []  # Lista para armazenar as arestas da MAG

    # Enquanto a fila de prioridade não estiver vazia
    while not edges.empty():
        weight, src, dest = edges.get()
        # Se o destino não foi visitado, adicione a aresta à MAG e visite o destino
        if dest not in visited:
            visited.add(dest)
            mst.append((src, dest, weight))
            add_edges(dest)

    return mst

# Testando o algoritmo de Prim
G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)

print("MAG usando Prim:", prim_algorithm(G))