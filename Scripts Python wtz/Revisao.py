import numpy as np

frutas = ['banana', 'uva', 'berga']

for i,fruta in enumerate(frutas[1:]):
    # print(fruta)
    print(fruta[0:-1].decode())

m = np.random.randint([(4,2),(3,1)])
# print(m)