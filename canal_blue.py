# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 02:24:06 2023

@author: rodri
"""

import cv2
import numpy 
import matplotlib.pyplot as plt

def imagem_blue(nome_arquivo_entrada):
    imagem = cv2.imread(nome_arquivo_entrada)
    
    histB= [0]*256
    
    
    pixel = 256*[0]
    for i in range(256):
        pixel[i]=i

    #eixo x
    plt.xlabel('Pixel')

    #eixo y
    plt.ylabel('Quantidade')

    plt.title('Histograma da Imagem do canal Blue')
    
    canalBlue = numpy.zeros((imagem.shape[0],imagem.shape[1],imagem.shape[2]), dtype = numpy.uint8())
    for i in range (imagem.shape[0]):
        for j in range (imagem.shape[1]):
          histB[imagem [i][j][0]]+=1
              
    plt.bar(pixel, histB, color='blue')
    plt.show()

    canalBlue[:,:,0] = imagem[:,:,0]

    cv2.imshow("canal Blue", canalBlue)

    cv2.imwrite("saida_blue.jpg", canalBlue)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()