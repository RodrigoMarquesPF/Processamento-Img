# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 02:30:54 2023

@author: rodri
"""

import cv2
import numpy 
import matplotlib.pyplot as plt

def imagem_green(nome_arquivo_entrada):
    imagem = cv2.imread(nome_arquivo_entrada)
    
    histG= [0]*256
    
    
    pixel = 256*[0]
    for i in range(256):
        pixel[i]=i

    #eixo x
    plt.xlabel('Pixel')

    #eixo y
    plt.ylabel('Quantidade')

    plt.title('Histograma da Imagem do canal Green')
    
    canalGreen = numpy.zeros((imagem.shape[0],imagem.shape[1],imagem.shape[2]), dtype = numpy.uint8())
    for i in range (imagem.shape[0]):
        for j in range (imagem.shape[1]):
          histG[imagem [i][j][1]]+=1
            
    plt.bar(pixel, histG, color='green')
    plt.show()
    
    canalGreen[:,:,1] = imagem[:,:,1]
    
    cv2.imshow("canal Green", canalGreen)

    cv2.imwrite("saida_green.jpg", canalGreen)
   
    cv2.waitKey(0)
    cv2.destroyAllWindows()