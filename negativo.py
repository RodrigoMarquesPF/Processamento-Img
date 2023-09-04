# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:43:51 2023

@author: rodri
"""

import cv2 
import numpy

def negativoimg (nome_arquivo_entrada):
    imagem = cv2.imread(nome_arquivo_entrada) 
    
    
    imagem_negativo = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8())
    for i in range (imagem.shape[0]):
        for j in range (imagem.shape[1]):
           imagem_negativo[i][j]=255-(imagem[i][j].sum()//3)
            
            
    cv2.imshow("Imagem negativo", imagem_negativo)    
    cv2.imwrite("imagem_negativo.jpg", imagem_negativo)
    
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()