# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:28:48 2023

@author: rodri
"""

import cv2
import numpy 
import funcs_morf as morf
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
            
imgErosao = cv2.erode(imgPBt, kernel_mascara2, iterations=1)
"""
imgErosao = numpy.ones( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )*255
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if morf.fit(kernel_mascara, imgPBt, i, j):
            imgErosao[i][j] = 255
        else:
            imgErosao[i][j] = 0
"""
resultado2 = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255              
resultado2 = abertura(imgErosao, kernel_mascara)            
intersecao2= cv2.subtract(imgErosao,resultado2)
"""
intersecao2 = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255      
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if imgErosao[i, j] == 255 and resultado2[i, j] == 0:
            intersecao2[i, j] =255
        else:
            intersecao2[i, j] = 0  
"""
"""
imgErosao2 = numpy.ones( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )*255   
for i in range (2):
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            if morf.fit(kernel_mascara, imgPBt, i, j):
                imgErosao[i][j] = 255
            else:
                imgErosao[i][j] = 0
"""
imgErosao2 = cv2.erode(imgPBt, kernel_mascara2, iterations=2)
resultado3 = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255              
resultado3 = abertura(imgErosao2, kernel_mascara)  

intersecao3= cv2.subtract(imgErosao2,resultado3)
"""
intersecao3 = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255      
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if imgErosao2[i, j] == 255 and resultado3[i, j] == 0:
            intersecao3[i, j] =255
        else:
            intersecao3[i, j] = 0 
            
"""            
            
imgErosao3 = cv2.erode(imgPBt, kernel_mascara2, iterations=3)
resultado4 = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255              
resultado4 = abertura(imgErosao3, kernel_mascara)  

subtracao= cv2.subtract(imgErosao3,resultado4)
 

imgErosao4 = cv2.erode(imgPBt, kernel_mascara2, iterations=4)
resultado5 = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255              
resultado5 = abertura(imgErosao4, kernel_mascara) 

intersecao4= cv2.subtract(imgErosao4,resultado5)


imgErosao5 = cv2.erode(imgPBt, kernel_mascara2, iterations=5)
resultado6 = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255              
resultado6 = abertura(imgErosao5, kernel_mascara) 

intersecao5= cv2.subtract(imgErosao5,resultado6)


imgErosao6 = cv2.erode(imgPBt, kernel_mascara2, iterations=6)
resultado7 = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255              
resultado7 = abertura(imgErosao6, kernel_mascara) 

intersecao6= cv2.subtract(imgErosao6,resultado7)
         
imgErosao7 = cv2.erode(imgPBt, kernel_mascara2, iterations=7)
resultado8 = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8) * 255              
resultado8 = abertura(imgErosao7, kernel_mascara) 

intersecao7= cv2.subtract(imgErosao7,resultado8)

soma1=cv2.add(intersecao2,intersecao3)
soma2=cv2.add(soma1,subtracao)
soma3=cv2.add(soma2,intersecao4)
soma4=cv2.add(soma3,intersecao5)
soma5=cv2.add(soma4,intersecao6)
soma6=cv2.add(soma5,intersecao7)



imgfinal = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if soma6[i][j] >197:
            imgfinal[i][j] =0
        else:
            imgfinal[i][j] =255 
            
resultado_final = numpy.ones((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)      

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if imgfinal[i, j] == 0 and imgPBt[i, j] == 255:
            resultado_final[i, j] =0
        elif imgfinal[i, j] == 0 and imgPBt[i, j] == 0:
            resultado_final[i, j] = 255
        elif imgfinal[i, j] == 255 and imgPBt[i, j] == 255:
            resultado_final[i, j] = 255
        else:
            resultado_final[i,j]=0
        
final=cv2.add(imgPBt,imgfinal)

cv2.imshow("img Cinza", cinza)
cv2.imshow("img PB", imgPBt)
cv2.imshow("img aaaaa", imgErosao)
cv2.imshow("img bbbbb", imgErosao2)
cv2.imshow("img ccccc", imgErosao3)
cv2.imshow("img cffff", imgErosao4)
cv2.imshow("img Final", intersecao)
cv2.imshow("img mmmm", resultado)
cv2.imshow("img kkkk", resultado2)
cv2.imshow("img llll", resultado3)
cv2.imshow("img pppp", resultado4)
cv2.imshow("img result5", resultado5)
cv2.imshow("img result6", resultado6)
cv2.imshow("img result7", resultado7)
cv2.imshow("img result8", resultado8)
cv2.imshow("img Final2", intersecao2)
cv2.imshow("img Final3", intersecao3)
cv2.imshow("img Final4", subtracao)
cv2.imshow("img inter4", intersecao4)
cv2.imshow("img inter5", intersecao5)
cv2.imshow("img inter6", intersecao6)
cv2.imshow("img inter7", intersecao7)
cv2.imshow("img soma", soma1)
cv2.imshow("img soma2", soma6)
cv2.imshow("img final", imgfinal)
cv2.imshow("img FINAAAAAAAAALl", resultado_final)

end_time = time.time()

# Calcula e imprime o tempo total
elapsed_time = end_time - start_time
print(f"Tempo de execução: {elapsed_time} segundos")
cv2.waitKey(0)
cv2.destroyAllWindows()