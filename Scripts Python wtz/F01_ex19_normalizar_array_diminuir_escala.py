import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

soma = (sum(sepallength**2))**(1/2) ## normalizacao de um vetor, razao do vetor pelo modulo do vetor, raiz da soma quadrada dos vetores
resultado = sepallength/soma
print(resultado)