import networkx as nx

def kruskal_algorithm(graph):
    """
    Implementação do algoritmo de Kruskal para encontrar a Menor Árvore Geradora (MAG) de um grafo.

    Parâmetros:
    - graph: Um grafo ponderado representado como um objeto NetworkX.

    Retorna:
    - Uma lista de arestas que formam a MAG.
    """
    
    # Função auxiliar para encontrar o representante do conjunto
    def find(vertex):
        # Se o vértice não é o representante de seu conjunto, encontre o representante
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    # Função auxiliar para unir dois conjuntos
    def union(vertex1, vertex2):
        root1 = find(vertex1)
        root2 = find(vertex2)
        # Se os representantes são diferentes, una os conjuntos
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    # Inicialização
    mst = []
    edges = list(graph.edges(data=True))
    edges.sort(key=lambda x: x[2]['weight'])  # Ordena as arestas pelo peso
    parent = {vertex: vertex for vertex in graph.nodes()}  # Dicionário para armazenar o representante de cada conjunto
    rank = {vertex: 0 for vertex in graph.nodes()}  # Dicionário para armazenar o rank de cada conjunto

    # Para cada aresta, em ordem crescente de peso
    for edge in edges:
        src, dest, weight = edge
        # Se os vértices da aresta pertencem a conjuntos diferentes, adicione a aresta à MAG e una os conjuntos
        if find(src) != find(dest):
            union(src, dest)
            mst.append(edge)

    return mst

# Testando o algoritmo de Kruskal
G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)

print("MAG usando Kruskal:", kruskal_algorithm(G))