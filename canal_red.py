# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 02:30:57 2023

@author: rodri
"""

import cv2
import numpy 
import matplotlib.pyplot as plt

def imagem_red(nome_arquivo_entrada):
    imagem = cv2.imread(nome_arquivo_entrada)
    
    histR= [0]*256
    
    
    pixel = 256*[0]
    for i in range(256):
        pixel[i]=i

    #eixo x
    plt.xlabel('Pixel')

    #eixo y
    plt.ylabel('Quantidade')

    plt.title('Histograma da Imagem do canal Red')
    
    canalRed = numpy.zeros((imagem.shape[0],imagem.shape[1],imagem.shape[2]), dtype = numpy.uint8())
    for i in range (imagem.shape[0]):
        for j in range (imagem.shape[1]):
          histR[imagem [i][j][2]]+=1
            
    plt.bar(pixel, histR, color='red')
    plt.show()
    
    canalRed[:,:,2] = imagem[:,:,2]

    cv2.imshow("canal Red", canalRed)

    cv2.imwrite("saida_red.jpg", canalRed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()