from lab_grafo import Grafo

w = [[0, 7, 4, 9, 7, float("inf")], [7, 0, 1, float("inf"), float("inf"), 6], [4, 1, 0, 3, float("inf"), float("inf")], [
    9, float("inf"), 3, 0, 1, 3], [7, float("inf"), float("inf"), 1, 0, 5], [float("inf"), 6, float("inf"), 3, 5, 0]]
s, a, b, c, d, t = w
print(s)
print(a)
print(b)
print(c)
print(d)
print(t)

#resposta s b c t menor caminho


resp = Grafo()
print(resp)