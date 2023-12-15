# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:16:49 2023

@author: rodri
"""

import cv2
import numpy 
import funcs_morf as morf
from negativo import negativoimg
import funcs_morf as morf







img     = ('imagem_quadrado2.jpg')
"""
image  = cv2.imread(img)
cv2.imshow('img_inicial.png', image)
"""
image = cv2.imread('imagem_quadrado2.jpg', 0)

cinza   = numpy.zeros( (image.shape[0], image.shape[1]), dtype=numpy.uint8 )
for i in range( image.shape[0] ):
    for j in range( image.shape[1] ):
        cinza[i][j] = (image[i][j].sum() // 3)
        
def hit(image, kernel_hit):
    # Aplicar a operação "hit" (erosão) na imagem
    hit_result = cv2.erode(image, kernel_hit)
    return hit_result

def fit(image, kernel_fit):
    # Aplicar a operação "fit" (dilatação) na imagem
    fit_result = cv2.dilate(image, kernel_fit)
    return fit_result

# Carregar a imagem de entrada binária


# Criar um kernel 15x15 preenchido com 1s para "hit" e "fit"
kernel_size = 15
kernel_hit = numpy.ones((kernel_size, kernel_size), numpy.uint8)
kernel_fit = numpy.ones((kernel_size, kernel_size), numpy.uint8)
                        
                        
inner_kernel_size = 15                       
total_kernel_size = 17

# Criar um kernel 17x17 com borda preta e interior 15x15 branco
border_thickness = (total_kernel_size - inner_kernel_size) // 2
kernel_hit2 = numpy.zeros((total_kernel_size, total_kernel_size), numpy.uint8)
kernel_hit2[border_thickness:border_thickness+inner_kernel_size, border_thickness:border_thickness+inner_kernel_size] = 1

# Aplicar a operação "hit" na imagem

hit_result = fit(image, kernel_hit)


imagem_erosao = hit_result
cv2.imshow('img__1.png', imagem_erosao)
imagem_negativo = negativoimg(img) 



hit2_result = hit(imagem_negativo, kernel_hit2)


negative_fit_result = 255 - hit2_result
cv2.imshow("img Negativo", imagem_negativo) 
cv2.imshow('img__2.png', negative_fit_result)
# Aplicar a operação "fi_t" na imagem

imgHit = numpy.zeros( (image.shape[0], image.shape[1]), dtype=numpy.uint8 )
imgHit = hit_result


imgFit = numpy.zeros( (image.shape[0], image.shape[1]), dtype=numpy.uint8 )
imgFit = negative_fit_result


resultado_intersecao = numpy.zeros((image.shape[0], image.shape[1]), dtype=numpy.uint8)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if imgHit[i, j] == 255 and imgFit[i, j] == 255:
           resultado_intersecao[i, j] = 255
        else:
            resultado_intersecao[i, j] = 0
# Salvar as imagens resultantes

#cv2.imwrite('fit_result.png', fit_result)

hit_result3 = hit(resultado_intersecao, kernel_hit)
           
         



 
cv2.imshow('interseção.png', resultado_intersecao)
cv2.imshow('final.png', hit_result3)
cv2.waitKey(0)
cv2.destroyAllWindows()