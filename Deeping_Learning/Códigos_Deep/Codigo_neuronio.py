import numpy as np
import matplotlib.pyplot as plt


# def sigmoid(a):
#     return 1.0 / (1. + np.exp(-a))
#
#
# x = np.linspace(-5.0, 5.0)  # cria array de (50,)
# y = sigmoid(x)

# plt.plot(x,y)
# plt.show()

# class Neuron:
#     def __init__(self, input_size=5): #input_size e o numero de entradas
#         self.w = np.random.random(input_size) #pesos de cada entrada
#         self.b = np.random.random() # baia, um numero aleatorio
#     def compute(self, inputs): # calcula a saido do neuronio para uma determinada entrada
#         s = np.dot(self.w, inputs) + self.b # multiplica peso pela entrada
#         z = sigmoid(s)
#         return z
# n = Neuron() # instancia n
# print(n.compute([1.0, 2.0, 3.0, 4.0, 5.0])) # chama a funcao compute passando como entrada 5 numeros

# E02

def tangente_hiperb(a):
    return np.tanh(a)

class Neuron:
    def __init__(self, input_size): # input_size pesos
        self.w = np.array(input_size) #pesos
        self.b = -0.5 # bias, um numero somado ao resultado funcao de ativacao
    def compute(self, inputs): # calcula a saido do neuronio para uma determinada entrada
        s = np.dot(self.w, inputs) + self.b # multiplica peso pela entrada
        z = tangente_hiperb(s)
        return z
n = Neuron([-1, 0, 1]) # instancia n
print(n.compute([1.0, 20.0, 3.0])) # chama a funcao compute passando como entrada 5 numeros