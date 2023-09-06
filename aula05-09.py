# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 14:34:56 2023

@author: rodri
"""


import cv2
import numpy 
import matplotlib.pyplot as plt

pixel = 256*[0]
nTotal = 0

imagem = cv2.imread('imagemsnow3.jpg')

pixel = 256*[0]
for i in range(256):
    pixel[i] = i

plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da Imagem em Tons de Cinza')

hist = [0]*256
histnormalizado = [0]*256
histnormalizadoAcumulado = [0]*256
hist5=[0]*256
hist6=[0]*256

imagemCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        imagemCinza[i][j] = (imagem[i][j].sum() // 3)
        hist[imagemCinza[i][j]] += 1
        nTotal +=1

plt.bar(pixel, hist, color='grey')
plt.show()

for i in range (256):
    histnormalizado[i] = hist[i]/nTotal
print(nTotal)



plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da normalizado')    

plt.bar(pixel, histnormalizado, color='grey')
plt.show()

for i in range (256):
    if (i) == 0:
        histnormalizadoAcumulado [i]= hist[i]/nTotal
    else:
        histnormalizadoAcumulado [i]= hist[i]/nTotal
        histnormalizadoAcumulado [i]= histnormalizadoAcumulado[i]+histnormalizadoAcumulado[i-1]
        ##print(histnormalizadoAcumulado[i])

plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da normalizado acumulado') 
plt.bar(pixel, histnormalizadoAcumulado, color='grey')
plt.show()

for i in range (256):
    hist5[i]=round(histnormalizadoAcumulado[i]*255)
    ##print(hist5[i])
    
imagemNova = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        imagemCinza[i][j] = (imagem[i][j].sum() // 3)
        imagemNova[i][j] = hist5[imagemCinza[i][j]]
        hist6[imagemNova[i][j]]+=1

plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da equalizado') 
plt.bar(pixel, hist6, color='grey')
plt.show()

cv2.imshow("imagem_eq.jpg", imagemNova)    
cv2.imwrite("imagem_eq2.jpg", imagemNova)

cv2.waitKey(0)
cv2.destroyAllWindows()