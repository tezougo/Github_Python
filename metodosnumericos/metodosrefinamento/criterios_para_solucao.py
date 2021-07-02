import numpy
import math
import sympy
x = sympy.symbols('x')
sympy.init_printing(use_unicode=True)

def criterio(f, a, b, precisao):
    if(abs(b-a) < precisao):
        print("\n Solucao pelo dominio |{} - {}| < {}".format(b, a, precisao))
        return True
    elif((abs(f(a)) < precisao) | (abs(f(b)) < precisao)):
        print("\n Solucao pela imagem |f({})|={} < |{}|ou |f({})|={} < |{}|".format(b,f(b),precisao,a,f(a),precisao))
        return True
