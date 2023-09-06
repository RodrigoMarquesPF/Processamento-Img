# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 19:23:19 2023

@author: rodri
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def calcular_histograma(imagem):
    hist = [0] * 256
    
    

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            pixel = int(imagem[i][j].sum() / 3)
            hist[pixel] += 1
           

    

    return hist