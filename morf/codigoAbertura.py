# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:26:18 2023

@author: rodri
"""

import cv2
import numpy 
from funcs_morf import fit, hit

def abertura(imagem, kernel_mascara):
    
    _, imgPBt = cv2.threshold(imagem, 197, 255, cv2.THRESH_BINARY)
    
    imgA = numpy.ones( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )*255
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            if fit(kernel_mascara, imgPBt, i, j):
                imgA[i][j] = 255
            else:
                imgA[i][j] = 0
                
    imgA2 = numpy.ones( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )*255
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            if hit(kernel_mascara, imgA, i, j):
                imgA2[i][j] = 255
            else:
                imgA2[i][j] = 0 

    return imgA2