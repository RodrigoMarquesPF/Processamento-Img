# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:42:56 2023

@author: rodri
"""



import cv2
import numpy
"""
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
"""


kernel_size=3
kernel_mascara = ([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]])


kernel_mascara2 = ([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])
kernel_mascara4 = ([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])

kernel_mascara3=([[1,2,0,0,0],
                 [0,1,1,1,0],
                 [0,1,1,1,0],
                 [0,1,1,1,0],
                 [0,0,0,0,0]])

imagem = cv2.imread('imgSalePimenta.png')

array=[0]*9

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
        z=0
        for m in range(kernel_size):
            for n in range(kernel_size):
                kernel_mascara4[m][n] = imagem2[i + m-(kernel_size // 2)][ j + n-(kernel_size // 2)] * kernel_mascara2[m][n]
        flattened_list = sum(kernel_mascara4, [])
        ##sorted_array = sorted(flattened_list)
        ##imagem3[i, j]=sorted_array[4]
        median_value = numpy.median(flattened_list)
        imagem3[i, j]=median_value
        
        
        
cv2.imshow("imagem_cinza", imagemCinza)
cv2.imshow("imagem_processada", imagem3)
cv2.imwrite("imagem_processada.jpg", imagem3)

cv2.waitKey(0)
cv2.destroyAllWindows()