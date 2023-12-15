# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:14:21 2023

@author: rodri
"""

import cv2
import numpy as np

def preencher_regioes(imagem):
    # Converte a imagem para escala de cinza
    ##imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    
    cinza   = np.zeros( (imagem.shape[0], imagem.shape[1]), dtype=np.uint8 )
    for i in range( imagem.shape[0] ):
        for j in range( imagem.shape[1] ):
            cinza[i][j] = (imagem[i][j].sum() // 3)

    # Binariza a imagem para encontrar as regiões
    ##_, binarizada = cv2.threshold(cinza, 1, 255, cv2.THRESH_BINARY)
    
    imgPB = np.zeros( (imagem.shape[0], imagem.shape[1]), dtype=np.uint8 )
    for i in range( imagem.shape[0] ):
        for j in range( imagem.shape[1] ):
            if cinza[i][j] >128:
                imgPB[i][j] =255
            else:
                imgPB[i][j] =0

    # Encontra os contornos na imagem binarizada
    contornos, _ = cv2.findContours(imgPB, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Preenche todas as regiões com pixels brancos
    cv2.drawContours(imagem, contornos, -1, (255, 255, 255), thickness=cv2.FILLED)

    return imagem

# Carrega a imagem
imagem = cv2.imread('triangulo01.png')

# Realiza o preenchimento de todas as regiões na imagem
imagem_preenchida = preencher_regioes(imagem.copy())

# Exibe a imagem original e a imagem com as regiões preenchidas
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Preenchida', imagem_preenchida)
cv2.waitKey(0)
cv2.destroyAllWindows()


