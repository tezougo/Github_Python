# Definindo os pontos em um array numpy
import numpy as np
from MAG import Mag

XY_Points = np.array([
            [10, 25],
            [10, 42],
            [20, 6],
            [30, 11],
            [40, 33],
            [22, 18],
            [26, 25]
        ])
nodesName = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
mag_instance = Mag()
mag_instance.calcular_menor_arvore_geradora(XY_Points, nodesName)