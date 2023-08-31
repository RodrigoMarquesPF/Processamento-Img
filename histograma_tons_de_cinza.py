# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 02:22:07 2023

@author: rodri
"""

import cv2
import numpy 
import matplotlib.pyplot as plt

def hist_tons_de_cinza(nome_arquivo_entrada):
    imagem = cv2.imread(nome_arquivo_entrada)

    pixel = 256*[0]
    for i in range(256):
        pixel[i] = i

    plt.xlabel('Pixel')
    plt.ylabel('Quantidade')
    plt.title('Histograma da Imagem em Tons de Cinza')

    hist = [0]*256

    imagemCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            imagemCinza[i][j] = (imagem[i][j].sum() // 3)
            hist[imagemCinza[i][j]] += 1

    plt.bar(pixel, hist, color='grey')
    plt.show()

     

    cv2.waitKey(0)
    cv2.destroyAllWindows()
