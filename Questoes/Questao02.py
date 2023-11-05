import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

# Obtém o diretório atual do script
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Caminho relativo para a pasta "img/entrada" a partir do diretório do script
image_path = os.path.join(diretorio_script, '../img/entrada/einstein.jpg')

# Leitura da imagem
image = cv2.imread(image_path) 

# Obtendo as dimensões da imagem
image_height = image.shape[0]
image_width = image.shape[1]

# Inicialização do histograma
histograma_image = np.zeros(256)  

# Cálculo do histograma
for i in range(image_width):
    for j in range(image_height):
        pixel_value = int(image[j, i][0])  # Valor do pixel na escala de cinza
        histograma_image[pixel_value] += 1  # Contagem da ocorrência do valor do pixel

# Plotagem do histograma da imagem
plt.figure()
plt.title('Histograma basico')
plt.bar(np.arange(len(histograma_image)), histograma_image, color='#34a0cf')
plt.ylabel('Número de pixels')
plt.xlabel('Valor de Intensidade')
plt.xlim([0, 256])
plt.show()

# Número total de pixels na imagem
num_pixels = image_width * image_height  

# histograma normalizado e acumulado
histograma_normalizado = np.zeros(256) 
histograma_acumulado = np.zeros(256)

# Cálculo da FDP e FDA
for i in range(0, len(histograma_image)):
    pk = histograma_image[i] / num_pixels  # Probabilidade de ocorrência de um determinado valor de pixel
    histograma_normalizado[i] = pk  # Armazenando a FDP
    if i > 0:
        histograma_acumulado[i] = pk + histograma_acumulado[i - 1]  # Calculando a FDA
    else:
        histograma_acumulado[i] = pk

# Plotagem do histograma da FDP
plt.figure()
plt.title('Histograma normalizado')
plt.bar(np.arange(len(histograma_normalizado)), histograma_normalizado, color='#34a0cf')
plt.ylabel('Probabilidade p(r)')
plt.xlabel('Valor de Intensidade')
plt.xlim([0, 256])
plt.show()

# Plotagem do histograma da FDA
plt.figure()
plt.title('Histograma acumulado')
plt.bar(np.arange(len(histograma_acumulado)), histograma_acumulado, color='#34a0cf')
plt.ylabel('Probabilidade acumulada')
plt.xlabel('Intensidade')
plt.xlim([0, 256])
plt.show()