import cv2
import math
import numpy as np
import os
from matplotlib import pyplot as plt

# Obtém o diretório atual do script
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Caminho relativo para a pasta "img/entrada" a partir do diretório do script
image_path = os.path.join(diretorio_script, '../img/entrada/lena_gray.bmp')

imagem = cv2.imread(image_path)  # Carrega a imagem "lena_gray.bmp"
largura_imagem = imagem.shape[1]  # Obtém a largura da imagem
altura_imagem = imagem.shape[0]  # Obtém a altura da imagem

c = 6  # Define o valor de c
b = 4  # Define o valor de b

# Letra a: Aplica a transformação linear (c * pixel + b) em cada pixel da imagem
#for i in range(0, largura_imagem):
#    for j in range(0, altura_imagem):
#        imagem[i, j] = (c * imagem[i][j][0]) + b

# Letra b: Aplica a função logarítmica base 2 (c * log2(pixel + 1)) em cada pixel da imagem
for i in range(0, largura_imagem):
    for j in range(0, altura_imagem):
        imagem[i][j] = c * (math.log(imagem[i][j][0] + 1, 2))

# Letra c: (Comentada) - teoricamente representaria uma função exponencial
#for i in range(0, largura_imagem):
#    for j in range(0, altura_imagem):
#        imagem[i, j] = c * math.exp(imagem[i, j][0] + 1)

cv2.imshow("janela", imagem)  # Exibe a imagem resultante
k = cv2.waitKey(0)  # Espera pressionar qualquer tecla

if k == ord("s"):  # Se a tecla "s" for pressionada, salva a imagem
    cv2.imwrite("image1_T3.png", imagem)
