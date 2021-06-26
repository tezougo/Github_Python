import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

# class Perceptron():
#     def __init__(self, n_inputs=4, n_hidden=8, n_outputs=1):
#         self.w_ih = np.random.random((n_hidden, n_inputs))
#         self.w_ho = np.random.random((n_outputs, n_hidden))
#         self.b_hid = np.random.random((n_hidden))
#         self.b_out = np.random.random((n_outputs))
#     def compute(self, inputs):
#         self.s_hid = np.dot(self.w_ih, inputs) + self.b_hid
#         self.z_hid = sigmoid(self.s_hid)
#         self.s_out = np.dot(self.w_ho, self.z_hid) + self.b_out
#         self.z_out = sigmoid(self.s_out)
#         return self.s_out, self.z_out
#
# p = Perceptron()
# t = p.compute([1.0, 2.0, 3.0, 4.0])
# print(p.compute([1.0, 2.0, 3.0, 4.0]))
#
# plt.plot(p.compute([1.0, 2.0, 3.0, 4.0]))
# plt.show()

class Perceptron():
  def __init__(self, n_inputs=3, n_hidden=4, n_outputs=3):
    # Sinapses
    self.w_ih = np.array([[1.12, 0.92, 1.28], [-0.88, -1.02, -1.46], [1.06, 0.63, 0.38], [-1.5, -1.99, -2.31]])
    self.w_ho = np.array([[0.54, 2.51, -1.81, 5.15], [-6.22, -4.08, 1.75, -3.47], [5.89, 1.58, -1.72, -4.06]])
    # Biases
    self.b_hid = np.array([[-8.86], [+4.36], [-1.87], [+4.79]])
    self.b_out = np.array([[-0.82], [0.76], [-1.35]])
  def compute(self, inputs):
    # Garante que a entrada seja um vetor coluna
    inputs = np.reshape(inputs,(len(inputs),1))
    # Calcula as ativações, camada por camada
    self.s_hid = np.dot(self.w_ih, inputs) + self.b_hid
    self.z_hid = sigmoid(self.s_hid)
    self.s_out = np.dot(self.w_ho, self.z_hid) + self.b_out
    self.z_out = sigmoid(self.s_out)
    return self.z_out
#, [2.0, 2.0, 2.0], [3.0, 3.0, 3.0]
p = Perceptron()

print(p.compute([2.0, 2.0, 2.0])) #print(p.compute([[1.0, 1.0, 1.0], [2.0, 2.0, 2.0], [3.0, 3.0, 3.0]]))

# plt.plot(p.compute([1.0, 2.0, 3.0]))
# plt.show()
