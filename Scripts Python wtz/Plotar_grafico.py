import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)       # plotagem da linha
plt.plot(x, y, 'o')  # plotagem dos pontos
plt.show()           # <-- mostra o gráfico

import matplotlib.pyplot as plt

image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.jet)
plt.colorbar()
plt.show()


import numpy as np
from mayavi import mlab

grafico = mlab.surf(np.random.rand(30, 30))
mlab.colorbar(grafico, orientation='horizontal')
mlab.axes(grafico)