import numpy as np


def numero(n):
  fib = np.arange(1, n+1)
  for i in range(n):
    if i <= 1 :
      fib[i] = i
    else:
      fib[i] = fib[i-1]+fib[i-2]
  return fib
print(numero(10))