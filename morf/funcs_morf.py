# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:19:36 2023

@author: rodri
"""


def fit(mascara, img, px, py):
    # Calcula o tamanho da máscara
    halfX = len(mascara) // 2
    halfY = len(mascara[0]) // 2

    # Verifica se a máscara se encaixa na imagem
    if px + halfX >= len(img) or px - halfX < 0:
        return False
    if py + halfY >= len(img[0]) or py - halfY < 0:
        return False

    # Verifica se a máscara coincide com a imagem
    for i in range(len(mascara)):
        for j in range(len(mascara[0])):
            if mascara[i][j] == 1 and img[px - halfX + i][py - halfY + j] == 255:
                return True
    return False

def hit(mascara, img, px, py):
    # Calcula o tamanho da máscara
    halfX = len(mascara) // 2
    halfY = len(mascara[0]) // 2

    # Verifica se a máscara se encaixa na imagem
    if px + halfX >= len(img) or px - halfX < 0:
        return False
    if py + halfY >= len(img[0]) or py - halfY < 0:
        return False

    # Verifica se a máscara coincide com a imagem
    for i in range(len(mascara)):
        for j in range(len(mascara[0])):
            if mascara[i][j] == 1:
                if img[px - halfX + i][py - halfY + j] == 0:
                    return False
    return True