# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 19:25:07 2023

@author: rodri
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from histograma import calcular_histograma

imagem = cv2.imread('imagemsnow3.jpg')


pixel = 256*[0]
for i in range(256):
    pixel[i] = i
    
    
plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da Imagem em Tons de Cinza')


hist = calcular_histograma(imagem)

plt.bar(pixel, hist, color='grey')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()