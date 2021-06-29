import math


# Seja f(x) continua no intervalo [a,b] e f(a).f(b) < 0 , então existe pelo menos um ponto em que x pertencente ao intervalo (a,b) tal que f(x) = 0.

# Teste continuidade no intervalo [a,b]:
#   f deve ser continua em [a,b].       lim f(x) = f(c) , para todo c pertencente ao intervalo (a,b).
#                                       x -> c
#   f deve ser continua a direita de a.     lim f(x) = f(a)
#                                           x -> a+
#   f deve ser continua a esquerda de b.    lim f(x) = f(b)
#                                           x -> b-
def bolzano(a,b,f):
    f

