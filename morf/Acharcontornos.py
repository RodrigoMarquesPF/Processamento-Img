# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:17:08 2023

@author: rodri
"""

import cv2
import numpy 
import funcs_morf as morf
from negativo import negativoimg

img     = ('imagem_aranha.jpg')
imagem  = cv2.imread(img)


kernel_mascara4= numpy.ones((15,15),numpy.uint8)
kernel_mascara6= numpy.ones((3,3),numpy.uint8)



cinza   = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        cinza[i][j] = (imagem[i][j].sum() // 3)
        
        
imgPB = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if cinza[i][j] >128:
            imgPB[i][j] =255
        else:
            imgPB[i][j] =0
            
            


imgHit = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if morf.hit(kernel_mascara6, imgPB, i, j):
            imgHit[i][j] = 255
        else:
            imgHit[i][j] = 0
"""
kernel_size = 3
kernel_hit = numpy.ones((kernel_size, kernel_size), numpy.uint8)

def hit(image, kernel_hit):
    # Aplicar a operação "hit" (erosão) na imagem
    hit_result = cv2.erode(image, kernel_hit)
    return hit_result

hit_result = hit(imagem, kernel_hit)
"""

contornos = cv2.subtract(imgHit, imgPB)

cv2.imshow("img PB", imgPB)
cv2.imshow("img 1",imgHit)
cv2.imshow("img 2",contornos)

cv2.waitKey(0)
cv2.destroyAllWindows()
