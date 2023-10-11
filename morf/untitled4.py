# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:18:13 2023

@author: rodri
"""


import cv2
import numpy 

##from processa_tons_de_cinza import tons_de_cinza

##imagemCinza = tons_de_cinza('imagem13.jpg')

primeiro=[0]*256

kernel_size = int(input("Digite o tamanho da matriz da máscara (ímpar): "))


kernel_mascara = numpy.zeros((kernel_size, kernel_size), dtype=numpy.float32)



print("Digite os valores da máscara:")
for i in range(kernel_size):
    for j in range(kernel_size):
        valor = float(input(f"Valor para a posição ({i},{j}): "))
        kernel_mascara[i, j] = valor

##imagemCinza,primeiro = tons_de_cinza('imagem13.jpg')
imagem = cv2.imread('imagem_moeda.png')






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
        
imagem3= numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())        
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        soma = 0
        if(imagemPB[i][j]==0):
            for m in range(kernel_size):
                for n in range(kernel_size):
                    if(kernel[i][j]==1):
                    soma += imagem2[i + m-(kernel_size // 2)][ j + n-(kernel_size // 2)] * kernel_mascara[m][n]
      
        
     




cv2.imshow("imagemPB.jpg", imagemPB)     
cv2.imwrite("imagem_cinza03-10.jpg", imagemPB)
cv2.imshow("imagem_erosao", imagem3) 


cv2.waitKey(0)
cv2.destroyAllWindows()