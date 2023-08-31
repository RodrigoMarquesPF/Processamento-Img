# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 02:30:57 2023

@author: rodri
"""

import cv2
import numpy 

def imagem_red(nome_arquivo_entrada):
    imagem = cv2.imread(nome_arquivo_entrada)
    
    canalRed = numpy.zeros((imagem.shape[0],imagem.shape[1],imagem.shape[2]), dtype = numpy.uint8())
    
    canalRed[:,:,2] = imagem[:,:,2]

    cv2.imshow("canal Red", canalRed)

    cv2.imwrite("saida_red.jpg", canalRed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()