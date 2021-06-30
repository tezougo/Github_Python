
import numpy as np
import math
import sympy
import metodosnumericos.localizacao.teorema_bolzano as teorema
# from metodosnumericos.metodosrefinamento.bissecao import pm
#from sympy import symbols
#from sympy.core.function import diff
#from sympy.interactive.printing import init_printing


print("\nInforme os dados necessarios para realizacao dos metodos iterativos, sendo ele a funcao, intervalo [a,b] e sua precisao.")
print("\nExemplo:" , "(2*ln(x**2))/sqrt(4)", "a:3", "b:5", "precisao: 0.0005\n", sep="\n")
f = sympy.sympify(input("Digite a sua funcao: "))
a = int(input("Digite a: "))
b = int(input("Digite b: "))
precisao = float(input("Digite precisao: "))
if(teorema.bolzano(a,b,f) == False):
    print("Nao e possivel afirma a existencia de uma solucao no intervalo [{},{}]".format(a,b))
else:
    print("Intervalo contem pelo menos uma solucao, pois f({})*f({})<0!".format(a,b))
    print("{}".format(precisao))
#print(sympy.diff(f))
