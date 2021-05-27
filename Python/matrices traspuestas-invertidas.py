# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:05:11 2021

@author: marin
"""

import numpy as np
matriz= np.array([[1, 1, 1], [1, 2, 3], [1, 3, 4]])
matriz_traspuesta = matriz.T
matriz_inversa = np.linalg.inv(matriz)
print(matriz_inversa)