# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 02:24:06 2023

@author: rodri
"""

import cv2
import numpy 

def imagem_blue(nome_arquivo_entrada):
    imagem = cv2.imread(nome_arquivo_entrada)
    
    canalBlue = numpy.zeros((imagem.shape[0],imagem.shape[1],imagem.shape[2]), dtype = numpy.uint8())

    canalBlue[:,:,0] = imagem[:,:,0]

    cv2.imshow("canal Blue", canalBlue)

    cv2.imwrite("saida_blue.jpg", canalBlue)
   

    cv2.waitKey(0)
    cv2.destroyAllWindows()