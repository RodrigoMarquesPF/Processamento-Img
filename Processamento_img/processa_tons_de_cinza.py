# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 02:34:21 2023

@author: rodri
"""

import cv2
import numpy 

def tons_de_cinza(nome_arquivo_entrada):
    imagem = cv2.imread(nome_arquivo_entrada)
    
    
    imagemCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            imagemCinza[i][j] = (imagem[i][j].sum() // 3)
            

    cv2.imshow("canal Cinza", imagemCinza)
    cv2.imwrite("saida_cinza.jpg", imagemCinza)
   

    cv2.waitKey(0)
    cv2.destroyAllWindows()