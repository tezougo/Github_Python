# coding=utf-8
import math
import random

def f(x):
    return (math.exp(x)) / ((math.exp(x)) + 1)
p = 0
v = 0
d = 0
for i in range(0, 10):

    print('\njogada {}'.format(i + 1))
    z = random.uniform(0, 1)
    mao1 = random.uniform(0, 1)
    mao2 = random.uniform(0, 1)
    if z >= f(mao1):
        # print('numero gerado com aleatoriedade verdadeira {}'.format(z))
        print('segunda mão é maior baseado no número {}'.format(z))
        print('primeira mão é {}, segunda mao é {}'.format(f(mao1), f(mao2)))
        if f(mao2) > f(mao1):
            v = (v+1)
            print('Você ganhou!')
        else:
            d = (d+1)
            print('Você perdeu!')
        print('valores sem f: da primeira mão {}, e da segunda mão {}'.format(mao1, mao2))
    if z <= f(mao1):
        # print('numero gerado com aleatoriedade verdadeira {}'.format(z))
        print('primeira mão é maior baseado no número {}'.format(z))
        print('primeira mão é {}, segunda mao é {}'.format(f(mao1), f(mao2)))
        if f(mao2) > f(mao1):
            v = (v+1)
            print('Você ganhou!')
        else:
            d = (d+1)
            print('Você perdeu!')
        print('valores sem f: da primeira mão {}, e da segunda mão {}'.format(mao1, mao2))
p = ((v/10)*100)
print('Derrotas {} e vitórias {}'.format(d,v))
#ptg = (v * 0.10  ) * 100
print("Porcentagem é {}%".format(p))
