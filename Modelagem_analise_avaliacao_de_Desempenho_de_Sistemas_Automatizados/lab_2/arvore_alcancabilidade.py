from rede_petri import RedePetri
class ArvoreAlcancabilidade:
    def __init__(self, rede_petri):
        self.rede_petri = rede_petri

    def arvore_alcancabilidade(self):
        """Constrói e retorna a árvore de alcançabilidade para a Rede de Petri dada."""
        arvore = {}  # Dicionário para armazenar a árvore de alcançabilidade
        visitados = set()  # Conjunto para armazenar os estados já visitados
        fila = [tuple(self.rede_petri.marcacao)]  # Fila para explorar os estados

        while fila:
            marcacao_atual = fila.pop(0)
            if marcacao_atual in visitados:
                continue
            visitados.add(marcacao_atual)
            arvore[marcacao_atual] = []

            # Para cada transição habilitada, dispara a transição e atualiza a árvore de alcançabilidade
            for transicao in self.rede_petri.transicoes_habilitadas():
                self.rede_petri.disparar_transicao(transicao)
                nova_marcacao = tuple(self.rede_petri.marcacao)
                arvore[marcacao_atual].append(nova_marcacao)
                fila.append(nova_marcacao)
                self.rede_petri.marcacao = list(marcacao_atual)  # Restaurar a marcacao anterior

        return arvore
    


    # Criando uma Rede de Petri
rede_petri = RedePetri([2, 0, 0])

# Adicionando transições e suas regras
def t1(marcacao):
    if marcacao[0] > 0:
        marcacao[0] -= 1
        marcacao[1] += 1
    return marcacao

def t2(marcacao):
    if marcacao[1] > 0:
        marcacao[1] -= 1
        marcacao[2] += 1
    return marcacao

rede_petri.adicionar_transicao("t1", t1)
rede_petri.adicionar_transicao("t2", t2)
# Criando uma instância da classe ArvoreAlcancabilidade
arvore_gen = ArvoreAlcancabilidade(rede_petri)

# Gerando a árvore de alcançabilidade
arvore = arvore_gen.arvore_alcancabilidade()
print(arvore)
