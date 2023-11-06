import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

# Obtém o diretório atual do script
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Caminho relativo para a pasta "img/entrada" a partir do diretório do script
image_saida = os.path.join(diretorio_script, '../img/entrada/polen.png')

# Caminho relativo para a pasta "img/entrada" a partir do diretório do script
image_entrada = os.path.join(diretorio_script, '../img/entrada/einstein.jpg')

# Leitura de image1 com a função imread() 
imagem = cv2.imread(image_saida)

largura_imagem = imagem.shape[0]
altura_imagem = imagem.shape[1]

# Leitura de lena_gray(target) com a função imread() 
imagem_target = cv2.imread(image_entrada)

largura_imagem_target = imagem_target.shape[0]
altura_imagem_target = imagem_target.shape[1]


# Criando Histograma de image1
hist_imagem = np.zeros(256)
for i in range(0, largura_imagem):
    for j in range(0, altura_imagem):
        valor_pixel = int(imagem[i, j][0])
        hist_imagem[valor_pixel] += 1


# Histograma da FDA e da FDP de image1
num_pixels = largura_imagem * altura_imagem
hist_fda = np.zeros(256)
hist_fdp = np.zeros(256)
for i in range(0, len(hist_imagem)):
    pk = hist_imagem[i]/num_pixels
    hist_fdp[i] = pk 
    if i > 0:
        hist_fda[i] = pk + hist_fda[i-1]
    else:
        hist_fda[i] = pk


# Gerando a função de equalização de image1
func_eq = []
for intensidade_antiga in range(0, 256):
    intensidade_nova = int(np.ceil(hist_fda[intensidade_antiga] * 255))
    func_eq.append([intensidade_antiga, intensidade_nova])
      

# Criando Histograma da imagem target
hist_imagem_target = np.zeros(256)
for i in range(0, largura_imagem_target):
    for j in range(0, altura_imagem_target):
        valor_pixel = int(imagem_target[i, j][0])
        hist_imagem_target[valor_pixel] += 1


# Histograma da FDA e da FDP da imagem target
num_pixels_target = largura_imagem_target * altura_imagem_target
hist_fda_target = np.zeros(256)
hist_fdp_target = np.zeros(256)
for i in range(0, len(hist_imagem_target)):
    pk = hist_imagem_target[i]/num_pixels_target
    hist_fdp_target[i] = pk 
    if i > 0:
        hist_fda_target[i] = pk + hist_fda_target[i-1]
    else:
        hist_fda_target[i] = pk


# Gerando a função de equalização da imagem target
func_eq_target = []
for intensidade_antiga in range(0, 256):
    intensidade_nova = int(np.ceil(hist_fda_target[intensidade_antiga] * 255))
    func_eq_target.append([intensidade_antiga, intensidade_nova])       


# FAZENDO A ESPECIFICAÇÃO
func_espec = []
func_novo = []   
for i in range(0, 256):
    for j in range(0, 256):
        func_novo.append(func_eq_target[j][1])
    fuc_novo = np.asarray(func_novo)
    indice = (np.abs(fuc_novo - func_eq[i][1])).argmin()
    valor = func_novo[indice]
    func_espec.append([func_eq[i][0], valor, indice])


# Aplicando a função de especificação na imagem                    
for i in range(0, largura_imagem):
    for j in range(0, altura_imagem):
        imagem[i][j] = func_espec[imagem[i][j][0]][2]


cv2.imshow("janela", imagem) 
k = cv2.waitKey(0) #espera pressionar qualquer tecla

if k == ord("s"): # se s for pressionado salva a imagem
    cv2.imwrite("lena_gray_equalizada_v2.png", imagem)


# Gerando o histograma especificado
hist_especificado = np.zeros(256)
for i in range(0, largura_imagem):
    for j in range(0, altura_imagem):
        valor_pixel = int(imagem[i, j][0])
        hist_especificado[valor_pixel] += 1


plt.figure()
plt.title('Histograma especificado')
plt.bar(np.arange(len(hist_especificado)), hist_especificado, color='#34a0cf')
plt.ylabel('Nº de pixels')
plt.xlabel('Intensidade')
plt.xlim([0, 256])
plt.show() 