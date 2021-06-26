import re

def recebe_frase(frase_recebida):
    frase_recebida = re.findall(r'[^,.\s]\w+', frase_recebida)
    print(frase_recebida)
    palavras_maiusculas = []
    for i in frase_recebida:
        if 64 < ord(i[0]) < 91:
            palavras_maiusculas.append(i)
            print('palavra maiuscula encontrada:\n {}'.format(i))
    print('Frase recebida:\n {}'.format(frase_recebida))
    print('Palavras maiusculas encontradas:')
    return palavras_maiusculas


print(recebe_frase('Fui.no maTo,Pega tatU .MaS sO'))
