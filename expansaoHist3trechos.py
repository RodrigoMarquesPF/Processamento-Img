# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:13:01 2023

@author: rodri
"""

import cv2 
import numpy
import matplotlib.pyplot as plt

def expansao3trechos (nome_arquivo_entrada):

    imagem = cv2.imread(nome_arquivo_entrada)  
    
  
    histB= [0]*256 
    
    r1=20
    r2=80
    s1=10
    s2=200
    
    
    
    imagem_contraste = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8())
    for i in range (imagem.shape[0]):
        for j in range (imagem.shape[1]):
            r=(imagem[i][j].sum()//3)
            if (r) < r1:
                imagem_contraste[i][j] = (s1/r1)*r
            elif (r>=r1) and (r<=r2):
                imagem_contraste[i][j]=(((r-r1)*(s2-s1))/(r2-r1))+s1 #s=255*((r-r1)/(r2-r1))
            else:
                imagem_contraste[i][j]=(r-r2)*((255-s2)/(255-r2))+s2
        histB[imagem_contraste[i][j]]+=1
    
    cv2.imshow("canal Alterada", imagem_contraste)    
    cv2.imwrite("imagem_espansao3trechos.jpg", imagem_contraste) 
    
    pixel = 256*[0]
    for i in range(256):
        pixel[i]=i
    
    #eixo x
    plt.xlabel('Pixel')
    
    #eixo y
    plt.ylabel('Quantidade')
    
    plt.title('Histograma da Imagem alterada')
    
    plt.bar(pixel, histB, color='grey')
    plt.show()
    
    
    
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()