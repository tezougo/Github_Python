#from lab_grafo import Grafo
import igraph
from igraph import plot

# w = [[0, 7, 4, 9, 7, float("inf")], [7, 0, 1, float("inf"), float("inf"), 6], [4, 1, 0, 3, float("inf"), float("inf")], [
#     9, float("inf"), 3, 0, 1, 3], [7, float("inf"), float("inf"), 1, 0, 5], [float("inf"), 6, float("inf"), 3, 5, 0]]
# s, a, b, c, d, t = w
# print(s)
# print(a)
# print(b)
# print(c)
# print(d)
# print(t)


# #resposta s b c t menor caminho


# resp = Grafo()
# print(resp)



# Matriz de adjacência (a)
matrix_a = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]
]

# Matriz de adjacência (b)
matrix_b = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0]
]

# Matriz de adjacência (c)
matrix_c = [
    [0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0]
]

# Matriz de adjacência (d)
matrix_d = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
]

# Matriz de adjacência (e)
matrix_e = [
    [0, 6, 9, 15, 0, 3],
    [0, 0, 2, 0, 0, 0],
    [0, 0, 0, 3, 0, 0],
    [2, 0, 0, 0, 5, 0],
    [0, 1, 0, 0, 0, 1],
    [3, 0, 0, 0, 1, 0]
]

# Criação dos objetos Graph
graph_a = igraph.Graph.Adjacency(matrix_a)
graph_b = igraph.Graph.Adjacency(matrix_b)
graph_c = igraph.Graph.Adjacency(matrix_c)
graph_d = igraph.Graph.Adjacency(matrix_d)
graph_e = igraph.Graph.Adjacency(matrix_e, mode='directed')

# Lista de layouts disponíveis
layouts = ['circle', 'fr', 'lgl', 'rt', 'fr3d', 'kk3d']

# Função para plotar e salvar gráficos com um layout específico
def plot_and_save_with_layout(graph, layout_name, filename):
    layout = layout_name
    plot(graph, layout=layout, bbox=(300, 300), vertex_label=range(len(graph.vs))).save(f"./grafos_plot/{filename}")

# Executar a plotagem e salvamento para cada layout
for layout_name in layouts:
    plot_and_save_with_layout(graph_a, layout_name, f"grafo_a_{layout_name}.png")
    plot_and_save_with_layout(graph_b, layout_name, f"grafo_b_{layout_name}.png")
    plot_and_save_with_layout(graph_c, layout_name, f"grafo_c_{layout_name}.png")
    plot_and_save_with_layout(graph_d, layout_name, f"grafo_d_{layout_name}.png")
    plot_and_save_with_layout(graph_e, layout_name, f"grafo_e_{layout_name}.png")