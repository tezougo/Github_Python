
import numpy as np
import math
from sympy import *
a,b = Symbol('x y')
init_printing(use_unicode=True)
import metodosnumericos.metodosrefinamento.bissecao
# from metodosnumericos.metodosrefinamento.bissecao import pm

print("\nInforme os dados necessarios para realizacao dos metodos iterativos, sendo ele a funcao, intervalo [a,b] e sua precisao.")
print("\nExemplo: \n(2*ln(x**2))/sqrt(4)\na:3\nb:5\np:0,0005\n\n")
f = input("Digite a sua funcao: ")
a = int(input("Digite a: "))
b = int(input("Digite b: "))
xn= metodosnumericos.metodosrefinamento.bissecao.pm(a,b)
print(xn)
diff(a**2)