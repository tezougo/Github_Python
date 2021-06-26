import matplotlib.pyplot as plt
import math
import numpy as np


def y(x):
    return (np.exp(-x / 10)) * (np.sin(math.pi * x))


def z(x):
    return x * np.exp(-x / 3)


# y_1 = np.vectorize(y)
# z_1 = np.vectorize(z)

#intervalo_escala = np.linspace(-5.0, 5.0) # para um intervalo de 50 numeros
intervalo_escala = np.arange(0, 10, 0.001) # cria um array de x = {narray: (10000,)} sendo esses 10000 pontos

y_de_x = y(intervalo_escala)
z_de_x = z(intervalo_escala)
plt.plot(intervalo_escala, z_de_x)
plt.title("z = x * e^(-x/3)")
plt.xlabel("Intervalo [0 a 10]")
plt.show()
plt.plot(intervalo_escala, y_de_x)
plt.title("y = e^(-x/10) * sin(pi*x)")
plt.xlabel("Intervalo [0 a 10]")
plt.show()
