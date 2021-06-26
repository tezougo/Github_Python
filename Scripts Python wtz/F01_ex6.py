def recebe_listas(lista1,lista2):
    grupo = []
    for i in range(len(lista1)):
        temporario = lista1[i], lista2[i]
        grupo.append(temporario)
    return tuple(grupo)

lista_1 =[4,3,6,2]
lista_2 =[2,4,5,1]
print(recebe_listas(lista_1,lista_2))