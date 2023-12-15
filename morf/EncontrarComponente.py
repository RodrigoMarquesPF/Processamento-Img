# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:55:43 2023

@author: rodri
"""

import cv2
import numpy as np

def componentes_conectados(image):
    comp02 = np.zeros_like(image)
    comp_sum = 1
    stack = []

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if image[y, x] == 255 and comp02[y, x] == 0:
                stack.append((x, y))

                while stack:
                    current_x, current_y = stack.pop()

                    if 0 <= current_x < image.shape[1] and 0 <= current_y < image.shape[0] and image[current_y, current_x] == 255 and comp02[current_y, current_x] == 0:
                        comp02[current_y, current_x] = comp_sum

                        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            next_x, next_y = current_x + i, current_y + j
                            if 0 <= next_x < image.shape[1] and 0 <= next_y < image.shape[0]:
                                stack.append((next_x, next_y))

                comp_sum += 1

    return comp02

def extrair_componentes(image_path, ponto_escolhido):
    
    imagem_cinza = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("imagemCinza", imagem_cinza)

    
    _, imagemPB = cv2.threshold(imagem_cinza, 197, 255, cv2.THRESH_BINARY)
    cv2.imshow("imagemPB", imagemPB)

    
    comp = componentes_conectados(imagemPB)

    
    start_x, start_y = ponto_escolhido
    start_pri = comp[start_y, start_x]

   
    achou_componente = (comp == start_pri).astype(np.uint8) * 255
    cv2.imshow('Componente Achado', achou_componente)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


imagem = 'teste005.png'
ponto_inicial = (250, 110)
##ponto_inicial = (41, 28)

extrair_componentes(imagem, ponto_inicial)
