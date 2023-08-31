# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 02:30:54 2023

@author: rodri
"""

import cv2
import numpy 

def imagem_green(nome_arquivo_entrada):
    imagem = cv2.imread(nome_arquivo_entrada)
    
    canalGreen = numpy.zeros((imagem.shape[0],imagem.shape[1],imagem.shape[2]), dtype = numpy.uint8())
    
    canalGreen[:,:,1] = imagem[:,:,1]
    
    cv2.imshow("canal Green", canalGreen)

    cv2.imwrite("saida_green.jpg", canalGreen)
   
    cv2.waitKey(0)
    cv2.destroyAllWindows()