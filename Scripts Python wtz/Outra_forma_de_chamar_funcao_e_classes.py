Pessoa = {}

def newPessoa(nome, nascimento):
    inst = {} # a nova instância
    inst['nome'] = nome
    inst['nascimento'] = nascimento
    return inst

def newClass(nome, atributos):
    cls = {} # cria o dicionário vazio para a classe
    for k, v in atributos.items(): # atribui os atributos (métodos e
        # atributos de classe)
        cls[k] = v
    return cls

def idade(hoje):
    hd, hm, ha = hoje
    nd, nm, na = inst['nascimento']
    idade = ha - na
    return idade


Pessoa = newClass('Pessoa', {'newPessoa':newPessoa, 'idade':idade})
hank = Pessoa['newPessoa']('Hank Moody', (8, 11, 1967))
print(hank)