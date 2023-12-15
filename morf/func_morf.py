# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:19:36 2023

@author: rodri
"""

import math

def fit(filterShape, img, px, py):
    
    #para matrizes de dimensoes impares
    halfX = math.floor( len( filterShape ) /2 )
    halfY = math.floor( len( filterShape[0] )/2 )
    
    if px + halfX > len( img[0] - 1 ) or px - halfX < 0:
        return False
    if py + halfY >len( img[1] - 1 ) or py - halfY < 0:
        return False
    
    for i in range( len( filterShape[1] ) ):
        for j in range( len( filterShape ) ):
            if filterShape[i][j] == 1 and img[ px - halfX + i - 1 ][ py - halfY + j - 1 ] == 255:
                return True
    return False

def hit(filterShape, img, px, py):
    
    count = 0
    
    #para matrizes de dimensoes impares
    halfX = math.floor( len( filterShape ) /2 )
    halfY = math.floor( len( filterShape[0] )/2 )
    
    if px + halfX > len( img[0] - 1 ) or px - halfX < 0:
        return False
    if py + halfY >len( img[1] - 1 ) or py - halfY < 0:
        return False
    
    for i in range( len( filterShape[1] ) ):
        for j in range( len( filterShape ) ):
            if filterShape[i][j] == 1 :
                if img[ px - halfX + i - 1 ][ py - halfY + j - 1 ] == 0:
                    return False
                    
    return True