# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 02:23:01 2023

@author: rodri
"""

from processa_tons_de_cinza import tons_de_cinza
from histograma_tons_de_cinza import hist_tons_de_cinza
from canal_blue import imagem_blue
from canal_green import imagem_green
from canal_red import imagem_red
from expansaoHist3trechos import expansao3trechos
from expansaoHist import expansaoHist
from negativo import negativoimg
from altoContraste import contrasteimg
from luminosidade import luminosidadeDef

arquivo_entrada = 'imagem13.jpg'
##arquivo_saida = 'saidaCinza2.jpg'

tons_de_cinza(arquivo_entrada)
hist_tons_de_cinza(arquivo_entrada)
imagem_blue(arquivo_entrada)
imagem_green(arquivo_entrada)
imagem_red(arquivo_entrada)
expansao3trechos(arquivo_entrada)
expansaoHist(arquivo_entrada)
negativoimg(arquivo_entrada)
contrasteimg(arquivo_entrada)
luminosidadeDef(arquivo_entrada)