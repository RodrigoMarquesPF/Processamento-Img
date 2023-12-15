# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:38:35 2023

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
                   [1, 1, 1],
                   [0, 1, 0]])




imagemPB = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        valor=0
        valor = (imagem[i][j].sum() // 3)
        if(valor<=100):
            imagemPB[i][j]=0
        else:
            imagemPB[i][j]=255
        
imagem3= numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if((imagemPB[i][j]==0) and (imagemPB[i+1][j-1]==0) and (imagemPB[i+1][j]==0) and (imagemPB[i+1][j+1]==0) and (imagemPB[i+2][j]==0) ):
            imagem3[i, j] = 0
        
        else:
            imagem3[i, j] = 255
        
        
        
        
     
                            
                                
                            
        
        
        
        
      





cv2.imshow("imagemPB.jpg", imagemPB)     
cv2.imwrite("imagem_cinza03-10.jpg", imagemPB)
cv2.imshow("imagem_erosao", imagem3) 


cv2.waitKey(0)
cv2.destroyAllWindows()