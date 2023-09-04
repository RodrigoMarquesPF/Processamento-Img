# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:27:51 2023

@author: rodri
"""

import cv2 
import numpy
import matplotlib.pyplot as plt

def expansaoHist (nome_arquivo_entrada):

    imagem = cv2.imread(nome_arquivo_entrada)  
    

    histB= [0]*256 
    
    #alterar valores de r1 e r2 de pendendo do Histigrama de tons de cinza
    r1=5
    r2=80
    
        
    imagem_contraste = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8())
    for i in range (imagem.shape[0]):
        for j in range (imagem.shape[1]):
            r=(imagem[i][j].sum()//3)
            if (r) <= r1:
                imagem_contraste[i][j] = 0
            elif (r>=r1) and (r<=100):
                imagem_contraste[i][j]=255*((r-r1)/(r2-r1)) #s=255*((r-r1)/(r2-r1))
            else:
                imagem_contraste[i][j]=255
        histB[imagem_contraste[i][j]]+=1
    
    cv2.imshow("canal Alterada", imagem_contraste)    
    cv2.imwrite("imagem_alterada.jpg", imagem_contraste) 
    
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