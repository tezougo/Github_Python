class Veiculo:
    def __init__(self, nome, max_vel, quilometragem):
        self.nome = nome
        self.max_vel = max_vel
        self.quilometragem = quilometragem

# class Onibus:
#      def __init__(self, onibus_1):
#          self.onibus_1 = onibus_1
#
# altomovel = Onibus(Veiculo('fusca','60','2000'))
#
# print('Nome do veiculo' + ' '+ str(altomovel.onibus_1.nome)+',',
#       'velocidade maxima do veiculo'+ ' ' +str(altomovel.onibus_1.max_vel)+' ''e a',
#       'quilometragem do veiculo'+ ' '+str(altomovel.onibus_1.quilometragem))

#outra forma

class Onibus(Veiculo):
    def __init__(self, onibus_1, nome, max_vel, quilometragem):
        super().__init__(nome, max_vel, quilometragem)
        self.onibus_1 = onibus_1
saida=Onibus('Escolar','bixo papao', '60', '1000')
print('O onibus '+str(saida.onibus_1)+' rodou '+str(saida.quilometragem)+' km ate agora.')