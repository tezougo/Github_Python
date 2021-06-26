def recebe(lista):
  dicionario = dict()
  for i in lista:
    if i not in dicionario:
      dicionario[i] = 1
    else:
      dicionario[i] += 1
  return  dicionario
lista_enviada =[ 4,'a','z', 4, 2, 4, 'f']
print(recebe(lista_enviada))