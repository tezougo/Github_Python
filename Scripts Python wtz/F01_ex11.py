sampleDict = {
    "class": {
       "student":{
           "name": "Mike",
           "marks":{
               "physics":70,
               "history":80
           }
       }
    }
}

#primeiro metodo

print(sampleDict['class']['student']['marks']['history'])

#segundo metodo

# A função abaixo procura todas ocorrências
# da chave numa estrutura de dicionários
# dentro de dicionários

def procurando2(item_procurado, dicionario):
  '''
  Retorna uma lista com todos valores cuja chave
  seja igual à string item_procurado.
  '''
  resultados = list()
  for chave in dicionario:
    if chave == item_procurado:
      resultados.append(dicionario[chave])
    elif isinstance(dicionario[chave], dict):
      for resultado in procurando2(item_procurado, dicionario[chave]):
        resultados.append(resultado)
  return resultados

print(procurando2('history', sampleDict))

## outra questao

# sampleDict = {
#                "class" : {
#                    "students":
#                    [ # <= note essa lista dentro do dicionário
#                     {
#                         "name" : "Mike",
#                         "marks" : {
#                             "physics" : 70,
#                             "history" : 80
#                         }
#                     },
#                     {
#                         "name" : "John",
#                         "marks" : {
#                             "physics" : 75,
#                             "history" : 90
#                         }
#                     },
#                     {
#                         "name" : "Mary",
#                         "marks" : {
#                             "physics" : 80,
#                             "history" : 70
#                         }
#                     }
#                    ] # <= encerra a lista
#                }
#             }

# O código acima contém uma lista de dicionários,
# e cada dicionário interno dessa lista repete a chave aluno e as notas do aluno não estão dentro da estrutura.
# Precisa nesse caso percorrer a lista, encontrar o dicionário cuja chave aluno corresponde ao nome que tu queres,
# e naquele dicionário olhar a chave 'history'. Fica um pouco mais complicado,
# e o código acima que eu sugeri precisaria ser modificado para lidar com listas também.

#outro problema

# Note que o código abaixo itera as tuplas
# (chave, valor)

# b = {'banana':12, 'abacaxi':24, 'uva':6}
# for a in b.items():
#   print(a)

#outro problema

# Note que o código abaixo itera as chaves

# b = {'banana':12, 'abacaxi':24, 'uva':6}
# for a in b:
#   print(a)

