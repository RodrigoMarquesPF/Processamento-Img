# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 23:05:08 2023

@author: rodri
"""

import cv2 
import numpy

def luminosidadeDef (nome_arquivo_entrada):
    imagem = cv2.imread(nome_arquivo_entrada) 
        
        
    l=100
    c=1
        
    imgD = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8())            
    for i in range (imagem.shape[0]):
         for j in range (imagem.shape[1]):
             imgD[i][j]=c*(imagem[i][j].sum()//3)+l
    
    cv2.imshow("Saida", imgD)    
    cv2.imwrite("saidaCL.jpg", imgD)  
    
        
        
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()