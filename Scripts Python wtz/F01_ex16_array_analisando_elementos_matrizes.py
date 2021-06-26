import numpy as np

array_x = np.arange(1,5)
array_a = np.random.randint(0, 16, (4,4))


def recebe_array_np(array_0):
    array_0[array_0 % 2 == 0] = -1
    return array_0


print(recebe_array_np(array_a))

