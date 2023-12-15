# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 00:50:27 2023

@author: rodri
"""

import cv2
import numpy 
import time
from codigoAbertura import abertura

# Grava o tempo inicial
start_time = time.time()
img     = ('jotaP2.png')
imagem  = cv2.imread(img)




##kernel_size = int(input("Digite o tamanho da matriz da máscara (ímpar): "))




kernel_mascara = ([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]])

kernel_mascara2 = numpy.array([[0, 1, 0],
                           [1, 1, 1],
                           [0, 1, 0]], dtype=numpy.uint8)
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

  
resultado = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255              
resultado = abertura(imgPBt, kernel_mascara)


intersecao = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255      
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if resultado[i, j] == 255 and imgPBt[i, j] == 0:
            intersecao[i, j] =255
        else:
            intersecao[i, j] = 0

# Inicializa a imagem binária original
imgErosao = imgPBt.copy()

# Número máximo de iterações permitidas
max_iteracoes = 20  # Defina um valor máximo razoável

# Limiar para a diferença entre iterações consecutivas
limiar_diff = 10

# Aplica erosão e abertura até atingir a condição de parada
for i in range(1, max_iteracoes + 1):
    # Aplica erosão
    imgErosao_temp = cv2.erode(imgErosao, kernel_mascara2, iterations=1)

    # Aplica abertura
    resultado = abertura(imgErosao_temp, kernel_mascara)

    # Subtrai o resultado da erosão do resultado da abertura
    intersecao = cv2.subtract(imgErosao_temp, resultado)

    # Calcula a diferença entre iterações consecutivas
    diff = cv2.norm(imgErosao, imgErosao_temp, cv2.NORM_L2)

    # Atualiza o resultado para a próxima iteração
    imgErosao = resultado

    # Mostra a imagem intermediária (opcional)
    cv2.imshow(f"img inter{i}", intersecao)

    # Verifica a condição de parada
    if diff < limiar_diff:
        print(f"Convergência atingida após {i} iterações.")
        break

soma1 = intersecao
for i in range(2, max_iteracoes + 1):
    intersecao_i = cv2.subtract(cv2.erode(imgPBt, kernel_mascara2, iterations=i), abertura(cv2.erode(imgPBt, kernel_mascara2, iterations=i), kernel_mascara))
    soma1 = cv2.add(soma1, intersecao_i)

# Limiarização da soma
imgfinal = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if soma1[i][j] > 197:
            imgfinal[i][j] = 0
        else:
            imgfinal[i][j] = 255 

# Processamento final
resultado_final = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)      
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if imgfinal[i, j] == 0 and imgPBt[i, j] == 255:
            resultado_final[i, j] = 0
        elif imgfinal[i, j] == 0 and imgPBt[i, j] == 0:
            resultado_final[i, j] = 255
        elif imgfinal[i, j] == 255 and imgPBt[i, j] == 255:
            resultado_final[i, j] = 255
        else:
            resultado_final[i,j] = 0

final = cv2.add(imgPBt, imgfinal)

cv2.imshow("img final", imgfinal)
cv2.imshow("img FINAAAAAAAAALl", resultado_final)



end_time = time.time()

# Calcula e imprime o tempo total
elapsed_time = end_time - start_time
print(f"Tempo de execução: {elapsed_time} segundos")

cv2.waitKey(0)
cv2.destroyAllWindows()
