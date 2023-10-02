import sys
#O sys.path é uma lista em Python que contém os diretórios onde o interpretador Python procura por módulos. Quando você tenta importar um módulo, o Python verifica cada diretório em sys.path para ver se o módulo está lá.
sys.path.append('C:\\Users\wagne\OneDrive\\Documentos\Github_Repos\\Github_Python\Modelagem_analise_avaliacao_de_Desempenho_de_Sistemas_Automatizados')
from lab_dijkstra import Dijkstra

# Matriz descrita como D, mas trata-se da E

matriz_e = [
    [0, 6, 9, 15, 0, 3],
    [0, 0, 2, 0, 0, 0],
    [0, 0, 0, 3, 0, 0],
    [2, 0, 0, 0, 5, 0],
    [0, 1, 0, 0, 0, 1],
    [3, 0, 0, 0, 1, 0]
]

matriz_d =[ [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
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


dijkstra_1 = Dijkstra(matriz_e)
inicio = 0  # A é o 1º vértice, então seu índice é 0
dijkstra_1.plotar_grafo_circulo('matriz_e.png')
print(dijkstra_1.calcular_caminhos(inicio))

dijkstra_2 = Dijkstra(matriz_d)
inicio = 0
dijkstra_2.plotar_grafo_circulo('matriz_d.png')
print(dijkstra_2.calcular_caminhos(inicio))