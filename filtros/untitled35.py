# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:16:23 2023

@author: rodri
"""

import cv2

def filtro_mediana(imagem, tamanho_kernel):
    # Aplicar o filtro de mediana usando a função medianBlur do OpenCV
    resultado = cv2.medianBlur(imagem, tamanho_kernel)

    return resultado

# Carregar a imagem
imagem = cv2.imread('imgSalePimenta.png')

# Definir o tamanho do kernel (ímpar)
tamanho_kernel = 5

# Aplicar o filtro de mediana
imagem_suavizada = filtro_mediana(imagem, tamanho_kernel)

# Mostrar as imagens original e suavizada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Suavizada com Filtro de Mediana', imagem_suavizada)
cv2.waitKey(0)
cv2.destroyAllWindows()