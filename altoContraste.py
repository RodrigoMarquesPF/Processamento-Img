# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:48:54 2023

@author: rodri
"""

import cv2 
import numpy

def contrasteimg (nome_arquivo_entrada):
    imagem = cv2.imread(nome_arquivo_entrada) 
    
    
    alto_contraste = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8())
    for i in range (imagem.shape[0]):
        for j in range (imagem.shape[1]):
            alto_contraste[i][j]=(((1/256)*(imagem[i][j].sum()//3))**2)*256
            
            
    cv2.imshow("Alto_contraste", alto_contraste)    
    cv2.imwrite("Alto_contraste.jpg", alto_contraste) 

    
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()