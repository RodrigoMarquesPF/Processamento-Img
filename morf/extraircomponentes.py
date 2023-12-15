# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 19:13:56 2023

@author: rodri
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 17:28:58 2023

@author: rodri
"""

import cv2
import numpy 
import funcs_morf as morf
import time

# Grava o tempo inicial
start_time = time.time()
img     = ('teste005.png')
imagem  = cv2.imread(img)




##kernel_size = int(input("Digite o tamanho da matriz da máscara (ímpar): "))




kernel_mascara = ([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1
                    ]])
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
        
_, imgPBt = cv2.threshold(cinza, 197, 255, cv2.THRESH_BINARY)
        
       
imgA  = numpy.ones( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )*255
x, y = 239, 19  # Substitua esses valores pelas coordenadas desejadas


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
        if imgB[i, j] == 0 and imgPBt[i, j] == 255:
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
            if imgB[i, j] == 0 and imgPBt[i, j] == 255:
                resultado_intersecao[i, j] = 0
            else:
                resultado_intersecao[i, j] = 255            
            
resultado_final = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255      

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if resultado_intersecao[i, j] == 0 and imgPBt[i, j] == 255:
            resultado_final[i, j] =255
        elif imgPBt[i, j] == 0 and resultado_intersecao[i, j] == 255:
            resultado_final[i, j] = 0
        else:
            
            resultado_final[i, j] = 0

        
"""
imgPBt2 = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if resultado_final[i][j] >197:
            imgPBt2[i][j] =0
        else:
            imgPBt2[i][j] =255 
"""           
cv2.imshow("img Cinza", cinza)
cv2.imshow("img PB", imgPBt)
##cv2.imshow("img TESTE", imgA)
##cv2.imshow("img TESTE2", imgB)
##cv2.imshow("img TESTE3", resultado_intersecao)
cv2.imshow("img Final", resultado_final)
###cv2.imshow("img Final2", imgPBt2)


end_time = time.time()

# Calcula e imprime o tempo total
elapsed_time = end_time - start_time
print(f"Tempo de execução: {elapsed_time} segundos")
cv2.waitKey(0)
cv2.destroyAllWindows()