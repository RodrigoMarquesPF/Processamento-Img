# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 17:28:58 2023

@author: rodri
"""

import cv2
import numpy 
import funcs_morf as morf

img     = ('novo.png')
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
        
imgPBt = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if cinza[i][j] >128:
            imgPBt[i][j] =0
        else:
            imgPBt[i][j] =255    
        
imgPB = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if imgPBt[i][j] >128:
            imgPB[i][j] =255
        else:
            imgPB[i][j] =0
            
imgA  = numpy.ones( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )*255
##x, y = 48, 17  # Substitua esses valores pelas coordenadas desejadas
x, y = 24, 18 

imgA[y, x] = 0



imgB = numpy.ones( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )*255
resultado_intersecao  = numpy.ones( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )*255


testeee = resultado_intersecao
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if morf.hit(kernel_mascara, imgA, i, j):
            imgB[i][j] = 0
        else:
            imgB[i][j] = 255



for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if imgB[i, j] == 0 and imgPB[i, j] == 255:
           resultado_intersecao[i, j] = 0
        else:
            resultado_intersecao[i, j] = 255      
            
resultado_intersecao_anterior = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255     
while not numpy.array_equal(resultado_intersecao, resultado_intersecao_anterior):
    resultado_intersecao_anterior = resultado_intersecao.copy()

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            if morf.hit(kernel_mascara, resultado_intersecao, i, j):
                imgB[i][j] = 0
            else:
                imgB[i][j] = 255

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            if imgB[i, j] == 0 and imgPB[i, j] == 255:
                resultado_intersecao[i, j] = 0
            else:
                resultado_intersecao[i, j] = 255            
            
resultado_final = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255      

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if resultado_intersecao[i, j] == 0 and imgPB[i, j] == 255:
            resultado_final[i, j] = 0
        elif imgPB[i, j] == 0 and resultado_intersecao[i, j] == 255:
            resultado_final[i, j] = 0
        else:
            resultado_final[i, j] = 255 

        

imgPBt2 = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):

    for j in range( imagem.shape[1] ):
        if resultado_final[i][j] >128:
            imgPBt2[i][j] =0
        else:
            imgPBt2[i][j] =255 
            
            
cv2.imshow("img Original", cinza)
cv2.imshow("img PB", imgPB)
##cv2.imshow("img TESTE", imgA)
##cv2.imshow("img TESTE2", imgB)
##cv2.imshow("img TESTE3", resultado_intersecao)
##cv2.imshow("img TESTE3", resultado_final)
cv2.imshow("img Final", imgPBt2)
cv2.waitKey(0)
cv2.destroyAllWindows()