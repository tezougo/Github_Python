class RedePetri:
    def __init__(self, marcacao_inicial):
        self.marcacao = marcacao_inicial
        self.transicoes = {}  # Dicionário para armazenar as transições e suas regras

    def adicionar_transicao(self, nome, regra):
        """Adiciona uma transição e sua regra à Rede de Petri."""
        self.transicoes[nome] = regra

    def transicoes_habilitadas(self):
        """Retorna uma lista de transições habilitadas para a marcação atual."""
        habilitadas = []
        for nome, regra in self.transicoes.items():
            if regra(self.marcacao):
                habilitadas.append(nome)
        return habilitadas

    def disparar_transicao(self, nome):
        """Dispara uma transição e atualiza a marcação."""
        if nome in self.transicoes:
            self.marcacao = self.transicoes[nome](self.marcacao.copy())
        else:
            raise ValueError(f"Transição {nome} não encontrada.")