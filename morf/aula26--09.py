# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:22:18 2023

@author: rodri
"""


import cv2
import numpy 

##from processa_tons_de_cinza import tons_de_cinza

##imagemCinza = tons_de_cinza('imagem13.jpg')

primeiro=[0]*256

##imagemCinza,primeiro = tons_de_cinza('imagem13.jpg')
imagem = cv2.imread('imagem_moeda.png')

kernel_mascara = ([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])




imagemCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())
imagem2= numpy.zeros((imagem.shape[0]+2, imagem.shape[1]+2), dtype=numpy.uint8())
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        imagemCinza[i][j] = (imagem[i][j].sum() // 3)
        imagem2[i+1][j+1] = imagemCinza[i][j]
 

     
imagem3= numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())
for i in range(1,imagem.shape[0]):
    for j in range(1,imagem.shape[1]):
        soma=0
        soma=kernel_mascara[0][0]*imagem2[i-1][j-1]+kernel_mascara[0][1]*imagem2[i-1][j]+kernel_mascara[0][2]*imagem2[i-1][j+1]+kernel_mascara[1][0]*imagem2[i][j-1]+kernel_mascara[1][1]*imagem2[i][j]+kernel_mascara[1][2]*imagem2[i][j+1]+kernel_mascara[2][0]*imagem2[i+1][j-1]+kernel_mascara[2][1]*imagem2[i+1][j]+kernel_mascara[2][2]*imagem2[i+1][j+1]
        if (soma) < 0:
            soma=0
        elif(soma) > 255:
            soma=255
        ##print(soma)
        imagem3[i][j]=soma


cv2.imshow("imagem_cinza263-09.jpg", imagem3)    
cv2.imshow("imagem_cinza26-09.jpg", imagem2)
cv2.imshow("imagem_cinza262-09.jpg", imagemCinza)     
cv2.imwrite("imagem_cinza26-09.jpg", imagemCinza)



cv2.waitKey(0)
cv2.destroyAllWindows()