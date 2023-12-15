# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 18:15:40 2023

@author: rodri
"""

import cv2
import numpy 
import funcs_morf as morf

img     = ('teste006.png')
imagem  = cv2.imread(img)




##kernel_size = int(input("Digite o tamanho da matriz da máscara (ímpar): "))




kernel_mascara = ([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]])
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
            
imgA  = numpy.ones( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )*255
x, y = 2, 2  # Substitua esses valores pelas coordenadas desejadas


imgA[y, x] = 0


if morf.hit(kernel_mascara, imgA, y, x):
    # Linha horizontal
    imgA[y, x - 1:x + 2] = 0
    # Linha vertical
    imgA[y - 1:y + 2, x] = 0

"""
if morf.hit(kernel_mascara, imgA, x, y):
    imgA[y, :] = 0  # Linha horizontal
    imgA[:, x] = 0  # Linha vertical
"""
"""
m=2
n=2
for m in range(2,2):
    for n in range(2,2):        
        if morf.hit(kernel_mascara, imgA, m, n):
            imgA[m][n] = 255
        else:
            imgA[m][n] = 0
imgB = imgA
 """       
"""
imgFit = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if morf.fit(kernel_mascara, imgPB, i, j):
            imgFit[i][j] = 255
        else:
            imgFit[i][j] = 0           


imgHit = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if morf.hit(kernel_mascara, imgFit, i, j):
            imgHit[i][j] = 255
        else:
            imgHit[i][j] = 0

""" 

         
     
            
            
            
cv2.imshow("img Cinza", cinza)
cv2.imshow("img PB", imgPB)
cv2.imshow("img TESTE", imgA)

cv2.waitKey(0)
cv2.destroyAllWindows()