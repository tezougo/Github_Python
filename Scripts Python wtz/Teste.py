class Carro():
    def __init__(self,**args):
        
    def test1(self, aqui):
        self.aqui = aqui
        return self.aqui

    def test2(self, sera):
        self.sera = sera + self.aqui
        return self.sera

valor = Carro()
t1 = Carro().test1(3)
print(Carro().test2(2))