s = 'carro eragrande'

x = "-".join([c for c in s if c.isalpha()])
z = "-".join(s.split(" "))

print(x)
print(z)
