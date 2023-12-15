# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:34:19 2023

@author: rodri
"""

import cv2
import numpy

# Solicitar ao usuário o tamanho da matriz da máscara (deve ser ímpar)
kernel_size = int(input("Digite o tamanho da matriz da máscara (ímpar): "))

# Criar uma matriz de máscara vazia com o tamanho inserido pelo usuário
kernel_mascara = numpy.zeros((kernel_size, kernel_size), dtype=numpy.float32)


# Preencher a matriz de máscara com os valores inseridos pelo usuário
print("Digite os valores da máscara:")
for i in range(kernel_size):
    for j in range(kernel_size):
        valor = float(input(f"Valor para a posição ({i},{j}): "))
        kernel_mascara[i, j] = valor

imagem = cv2.imread('imagem99.jpg')


imagemCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())
imagem2= numpy.zeros((imagem.shape[0]+2, imagem.shape[1]+2), dtype=numpy.uint8())
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        imagemCinza[i][j] = (imagem[i][j].sum() // 3)
        imagem2[i+1][j+1] = imagemCinza[i][j]
        
imagem3= numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())

# Aplicar a máscara de convolução manualmente
for i in range(1, imagem.shape[0]):
    for j in range(1, imagem.shape[1]):
        soma = 0
        for m in range(kernel_size):
            for n in range(kernel_size):
                soma += imagem2[i + m-(kernel_size // 2)][ j + n-(kernel_size // 2)] * kernel_mascara[m][n]
        if (soma) < 0:
            soma=0
        elif(soma) > 255:
            soma=255
        imagem3[i, j] = soma

cv2.imshow("imagem_cinza", imagemCinza)
cv2.imshow("imagem_processada", imagem3)
cv2.imwrite("imagem_processada.jpg", imagem3)

cv2.waitKey(0)
cv2.destroyAllWindows()
