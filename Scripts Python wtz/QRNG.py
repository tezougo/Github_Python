import urllib.request
import numpy as np
import json
from plots import plotScatter
#------------------------------------------------------------------------------------


def GetAnysizeArray(dim):
   if dim <= 1024:
       little = GetRandomArray(dim)
       return little
   else:
       large = []
       m = dim
       while m > 1024:
           large.extend(GetRandomArray(1024))
           m = m - 1024
       else:
           large.extend(GetRandomArray(m))
           return large
#------------------------------------------------------------------------------------


def GetRandomArray(dim):
    d = str(dim)
    url1 = 'https://qrng.anu.edu.au/API/jsonI.php?length='
    url2 = '&type=uint16'
    url = url1+d+url2
    page = urllib.request.urlopen(url, timeout=5)
    aux = page.read()
    data = json.loads(aux.decode('utf-8'))
    num = data.get("data", "none")
    return num
#------------------------------------------------------------------------------------


def QRNG():
    a = float(GetRandomArray(1)[0])
    b = float(a/65535)
    return b
#------------------------------------------------------------------------------------


def QRNGtest2(d):
    x = GetAnysizeArray(d)
    y = GetAnysizeArray(d)
    return plotScatter(x, y)


QRNGtest2(5000)
