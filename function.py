# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:52:56 2023

@author: rodri
"""

def mapeamento(equaliz, acumulado):
    mapa2={}
    
    for valor in equaliz:
        menor=abs(valor-acumulado[0])
        menor_indice=0
        for j in range (len(acumulado)):
            if abs(valor-acumulado[j])<menor:
                menor=abs(valor-acumulado[j])
                menor_indice=j
        mapa2[valor]=menor_indice
    return mapa2


def remove_repetido(lista):
    l=[]
    for i in lista:
        if i not in l:
            l.append(i)
    return l
        
