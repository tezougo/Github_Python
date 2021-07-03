import numpy
import math
import sympy
x,y = sympy.symbols('x y')
sympy.init_printing(use_unicode=True)

# Seja f(x) continua no intervalo [a,b] e f(a).f(b) < 0 , então existe pelo menos um ponto em que x pertencente ao intervalo (a,b) tal que f(x) = 0.

# Teste continuidade no intervalo [a,b]:
#   f deve ser continua em [a,b].       lim f(x) = f(c) , para todo c pertencente ao intervalo (a,b).
#                                       x -> c
#   f deve ser continua a direita de a.     lim f(x) = f(a)
#                                           x -> a+
#   f deve ser continua a esquerda de b.    lim f(x) = f(b)
#                                           x -> b-

def bolzano(f,a,b):
    c = numpy.random.uniform(0, 2)
    print(f)
    print("\n f(c)=",f(c))
    print("\n limit(f(x),x,c)=", sympy.limit(f(x), x, c))
    print("\n f(a)=", f(a))
    print("\n limit(f(x),x,a)=", sympy.limit(f(x), x, a))
    print("\n f(b)=", f(b))
    print("\n limit(f(x),x,b)={} e o resultado t(b)={}".format(sympy.limit(f(x), x, b), sympy.limit(f(x), x, b).doit()))
    if((sympy.limit(f(x), x, c) == f(c)) and (sympy.limit(f(x), x, a) == f(a)) and (sympy.limit(f(x), x, b) == f(b))):

        if(f(a)*f(b) < 0):
            return True
        else:
            return False
    else:
        print("\nA funcao nao e considera continua no intervalo dado, por esse motivo nao pode-se aplicar o Teorema de Bolzano")
        return False


