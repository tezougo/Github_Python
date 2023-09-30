    # A arvore de alcançabilidade é um dicionário que armazena os estados visitados e seus estados sucessores
    # Tem como início a marcacao inicial da rede
    # Um exemplo de árvore de alcançabilidade seria: { (1, 1, 0, 0): [(0, 0, 1, 1), (0, 0, 2, 0)] }
    # Onde (1, 1, 0, 0) é a marcacao inicial, (0, 0, 1, 1) e (0, 0, 2, 0) são os estados sucessores
    # indicando a marcacao após disparar a transição tA e tB, respectivamente.
    # A árvore de alcançabilidade é construída usando busca em largura.
    # A fila armazena os estados a serem explorados, e o conjunto armazena os estados já visitados.
    # De forma resumida a árvore de alcançabilidade é construída da seguinte forma:
    # 1. Inicializa a fila com a marcacao inicial
    # 2. Enquanto a fila não estiver vazia:
    #    2.1. Retira o primeiro elemento da fila
    #    2.2. Se o elemento já foi visitado, continue
    #    2.3. Adiciona o elemento ao conjunto de visitados
    #    2.4. Adiciona o elemento à árvore de alcançabilidade
    #    2.5. Para cada transição habilitada, dispara a transição e adiciona o novo estado à fila
    #    2.6. Restaura a marcacao anterior
    # 3. Retorna a árvore de alcançabilidade

class RedePetri:
    def __init__(self):
        # Inicialização dos lugares da Rede de Petri
        # marcacao: Representa a quantidade de tokens em cada lugar.
        # [A, B, D, C]
        self.marcacao = [1, 1, 0, 0]  # Inicialmente, os carros estão em A e B, e D e C estão vazios.

        # Transições da Rede de Petri
        # tA representa a transição do carro A de A para D
        # tB representa a transição do carro B de B para D
        self.transicoes = [
            [1, 0, 0, 0],  # tA: A -> D
            [0, 1, 0, 0]   # tB: B -> D
        ]

    def transicoes_habilitadas(self):
        """Retorna a lista de transições que estão habilitadas para disparo."""
        habilitadas = []
        for i, transicao in enumerate(self.transicoes):
            # Verifica se a transição pode ser disparada (se há tokens suficientes nos lugares de entrada)
            if all(marc - tran >= 0 for marc, tran in zip(self.marcacao, transicao)):
                habilitadas.append(i)
        return habilitadas

    def disparar_transicao(self, transicao):
        """Dispara uma transição, atualizando a marcação da rede."""
        # Atualiza os tokens nos lugares de entrada e saída da transição
        self.marcacao = [marc - tran for marc, tran in zip(self.marcacao, self.transicoes[transicao])]
        # Se a transição tA ou tB for disparada, o carro chega ao lugar D
        if transicao in [0, 1]:  
            self.marcacao[2] += 1

def arvore_alcancabilidade(rede_petri):
    """Constrói e retorna a árvore de alcançabilidade para a Rede de Petri dada."""
    # A árvore de alcançabildiade trata-se de um dicionário onde as chaves são as marcações e os valores são listas de 
    # marcações alcançáveis a partir da chave.
    # Retorna a árvore de alcançabilidade para a Rede de Petri dada.
    arvore = {}  # Dicionário para armazenar a árvore de alcançabilidade
    visitados = set()  # Conjunto para armazenar os estados já visitados
    fila = [tuple(rede_petri.marcacao)]  # Fila para explorar os estados

    while fila:
        marcacao_atual = fila.pop(0)
        if marcacao_atual in visitados:
            continue
        visitados.add(marcacao_atual)
        arvore[marcacao_atual] = []

        # Para cada transição habilitada, dispara a transição e atualiza a árvore de alcançabilidade
        for transicao in rede_petri.transicoes_habilitadas():
            rede_petri.disparar_transicao(transicao)
            nova_marcacao = tuple(rede_petri.marcacao)
            arvore[marcacao_atual].append(nova_marcacao)
            fila.append(nova_marcacao)
            rede_petri.marcacao = list(marcacao_atual)  # Restaurar a marcacao anterior

    return arvore

# Exemplo de uso:
rede = RedePetri()
arvore = arvore_alcancabilidade(rede)
print(arvore)