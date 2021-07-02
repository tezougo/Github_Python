import numpy
import math
import metodosnumericos.metodosrefinamento.criterios_para_solucao as verifica
import sympy
sympy.init_printing(use_unicode=True)


def bissec(f, a, b, precisao):
    if(f(a)*f(b) < 0):
        analise = verifica.criterio(f, a, b, precisao)
        if(analise == True):
            return analise
        else:
            ponto_m = (a+b)/2
            if(f(ponto_m)*f(b) < 0):
                return bissec(f, ponto_m, b, precisao)
            else:
                return bissec(f, a, ponto_m, precisao)
