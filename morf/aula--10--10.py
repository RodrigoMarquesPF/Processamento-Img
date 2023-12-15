# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:36:06 2023

@author: rodri
"""

import cv2
import numpy 
import funcs_morf as morf

img     = ('imagem_teste_3.png')
imagem  = cv2.imread(img)




##kernel_size = int(input("Digite o tamanho da matriz da máscara (ímpar): "))
"""
kernel_mascara2 = ([[0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 1, 1, 1, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0]])
"""
"""
kernel_mascara2 = ([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])
"""


kernel_mascara2 = ([[1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1]])

"""
kernel_mascara = ([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]])
"""
"""
kernel_mascara2 = ([[0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 1, 1, 1, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0]])
"""
"""
kernel_mascara = ([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])

"""

kernel_mascara = ([[1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1]])

"""
print("Digite os valores da máscara:")
for i in range(kernel_size):
    for j in range(kernel_size):
        valor = float(input(f"Valor para a posição ({i},{j}): "))
        kernel_mascara[i, j] = valor
"""


cinza   = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        cinza[i][j] = imagem[i][j].sum() // 3
        
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
        if morf.hit(kernel_mascara2, imgPB, i, j):
            imgHit[i][j] = 255
        else:
            imgHit[i][j] = 0

imgFit = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if morf.fit(kernel_mascara, imgHit, i, j):
            imgFit[i][j] = 255
        else:
            imgFit[i][j] = 0 

            
     
            
            
            
cv2.imshow("img Cinza", cinza)
cv2.imshow("img PB", imgPB)
cv2.imshow("img Fit", imgFit)
cv2.imshow("img Hit", imgHit)
cv2.waitKey(0)
cv2.destroyAllWindows()