import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

# Obtém o diretório atual do script
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Caminho relativo para a pasta "img/entrada" a partir do diretório do script
image_path = os.path.join(diretorio_script, '../img/entrada/einstein.jpg')

# Carrega a imagem a partir do caminho relativo
imagem = cv2.imread(image_path)

# Obtém as dimensões da imagem
largura_imagem = imagem.shape[0]
altura_imagem = imagem.shape[1]

print(largura_imagem)
print(altura_imagem)

# Inicialização do histograma da imagem
histograma_imagem = np.zeros(256)

# Calcula o histograma da imagem original
for i in range(0, largura_imagem):
    for j in range(0, altura_imagem):
        valor_pixel = int(imagem[i, j][0])
        histograma_imagem[valor_pixel] += 1

# Calcula a função de distribuição acumulada (FDA) e a função de distribuição de probabilidade (FDP)
num_pixels = largura_imagem * altura_imagem
histograma_acumulado = np.zeros(256)
histograma_probabilidade = np.zeros(256)
for i in range(0, len(histograma_imagem)):
    pk = histograma_imagem[i] / num_pixels
    histograma_probabilidade[i] = pk
    if i > 0:
        histograma_acumulado[i] = pk + histograma_acumulado[i - 1]
    else:
        histograma_acumulado[i] = pk

# Calcula a função de equalização
funcao_eq = []
for intensidade_antiga in range(0, 256):
    intensidade_nova = int(np.ceil(histograma_acumulado[intensidade_antiga] * 255))
    funcao_eq.append([intensidade_antiga, intensidade_nova])

# Aplica a função de equalização na imagem
for i in range(0, largura_imagem):
    for j in range(0, altura_imagem):
        imagem[i][j] = funcao_eq[imagem[i][j][0]][1]

# Calcula o histograma da imagem equalizada
histograma_equalizado = np.zeros(256)
for i in range(0, largura_imagem):
    for j in range(0, altura_imagem):
        valor_pixel = int(imagem[i, j][0])
        histograma_equalizado[valor_pixel] += 1

# Plota o histograma equalizado
plt.figure()
plt.title('Histograma equalizado')
plt.bar(np.arange(len(histograma_equalizado)), histograma_equalizado, color='#34a0cf')
plt.ylabel('Nº de pixels')
plt.xlabel('Intensidade')
plt.xlim([0, 256])
plt.show()

# Exibe a imagem equalizada em uma janela
cv2.imshow("janela", imagem)
k = cv2.waitKey(0)

# Salva a imagem equalizada se a tecla "s" for pressionada
if k == ord("s"):
    cv2.imwrite(os.path.join(diretorio_script, '../img/saida/einstein_equalizada.png'), imagem)
