import numpy as np

# a = [[1,4,5],[3,4,2]]
# def cria_array_numpy(lista):
#     array_pronto = np.array(lista)
#     return array_pronto
# print(cria_array_numpy(a))

lista_coluna = []
lista_linha = []
# array_1 = np.identity(2, int)
# array_2 = np.full((2,2), 0.3)
array_3 = [[1,2],[3,4]]

def cria_listas_a_partir_de_array(recebe):
    if recebe[0][0] > recebe[1][0]:
        lista_coluna.append(recebe[0][0])
    else:
        lista_coluna.append(recebe[1][0])
    if recebe[0][1] > recebe[1][1]:
        lista_coluna.append(recebe[0][1])
    else:
        lista_coluna.append(recebe[1][1])

    if recebe[0][0] > recebe[0][1]:
        lista_linha.append(recebe[0][0])
    else:
        lista_linha.append(recebe[0][1])
    if recebe[1][0] > recebe[1][1]:
        lista_linha.append(recebe[1][0])
    else:
        lista_linha.append(recebe[1][1])
    return print(f'A lista de elementos da coluna e {lista_coluna} e a de linhas e {lista_linha}')


cria_listas_a_partir_de_array(array_3)
