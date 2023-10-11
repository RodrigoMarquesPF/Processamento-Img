# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:19:35 2023

@author: rodri
"""

import cv2
import numpy
import matplotlib.pyplot as plt
import random
import math
##import filtroFuncoes as f
import funcs_morf as morf



img     = ('imagem_moeda.png')
imagem  = cv2.imread(img)


""" ----- ----- canais ----- ----- """
blue    = numpy.zeros( (imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8 )
green   = numpy.zeros( (imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8 )
red     = numpy.zeros( (imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8 )
cinza   = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
teste   = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )

blue    [ : , : , 0 ] = imagem[ : , : , 0 ]
green   [ : , : , 1 ] = imagem[ : , : , 1 ]
red     [ : , : , 2 ] = imagem[ : , : , 2 ]

alturaImg = imagem.shape[0]
larguraImg = imagem.shape[1]
totalPixels = alturaImg * larguraImg


""" ----- ----- cinza ----- ----- """
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        cinza[i][j] = imagem[i][j].sum() // 3
        
imgPB = numpy.zeros( (imagem.shape[0]+2, imagem.shape[1]+2), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if cinza[i][j] > 128:
            imgPB[i][j] = 255
        else:
            imgPB[i][j] = 0

op = [
      [0, 1, 0],
      [1, 1, 1],
      [0, 1, 0]
      ]



imgFit = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if morf.fit(op, imgPB, i, j):
            imgFit[i][j] = 255
        else:
            imgFit[i][j] = 0
            
imgHit = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        if morf.hit(op, imgPB, i, j):
            imgHit[i][j] = 255
        else:
            imgHit[i][j] = 0
       
        

cv2.imshow("img cinza", cinza)
cv2.imshow("img p&b", imgPB)
cv2.imshow("img Fit", imgFit)
cv2.imshow("img Hit", imgHit)
cv2.waitKey(0)
cv2.destroyAllWindows()