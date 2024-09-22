import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

# Get the current directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Relative path to the folder from the script directory
output_image_path = os.path.join(script_directory, '../resources/img/polen.png')

# Relative path to the folder from the script directory
input_image_path = os.path.join(script_directory, '../resources/img/einstein.jpg')

# Read image1 with the imread() function
image = cv2.imread(output_image_path)

image_width = image.shape[0]
image_height = image.shape[1]

# Read lena_gray (target) with the imread() function
target_image = cv2.imread(input_image_path)

target_image_width = target_image.shape[0]
target_image_height = target_image.shape[1]

# Create Histogram of image1
hist_image = np.zeros(256)
for i in range(0, image_width):
    for j in range(0, image_height):
        pixel_value = int(image[i, j][0])
        hist_image[pixel_value] += 1

# CDF and PDF Histogram of image1
num_pixels = image_width * image_height
hist_cdf = np.zeros(256)
hist_pdf = np.zeros(256)
for i in range(0, len(hist_image)):
    pk = hist_image[i] / num_pixels
    hist_pdf[i] = pk
    if i > 0:
        hist_cdf[i] = pk + hist_cdf[i - 1]
    else:
        hist_cdf[i] = pk

# Generating the equalization function of image1
func_eq = []
for old_intensity in range(0, 256):
    new_intensity = int(np.ceil(hist_cdf[old_intensity] * 255))
    func_eq.append([old_intensity, new_intensity])

# Create Histogram of the target image
hist_target_image = np.zeros(256)
for i in range(0, target_image_width):
    for j in range(0, target_image_height):
        pixel_value = int(target_image[i, j][0])
        hist_target_image[pixel_value] += 1

# CDF and PDF Histogram of the target image
num_pixels_target = target_image_width * target_image_height
hist_cdf_target = np.zeros(256)
hist_pdf_target = np.zeros(256)
for i in range(0, len(hist_target_image)):
    pk = hist_target_image[i] / num_pixels_target
    hist_pdf_target[i] = pk
    if i > 0:
        hist_cdf_target[i] = pk + hist_cdf_target[i - 1]
    else:
        hist_cdf_target[i] = pk

# Generating the equalization function of the target image
func_eq_target = []
for old_intensity in range(0, 256):
    new_intensity = int(np.ceil(hist_cdf_target[old_intensity] * 255))
    func_eq_target.append([old_intensity, new_intensity])

# SPECIFICATION
func_spec = []
func_new = []
for i in range(0, 256):
    for j in range(0, 256):
        func_new.append(func_eq_target[j][1])
    func_new = np.asarray(func_new)
    index = (np.abs(func_new - func_eq[i][1])).argmin()
    value = func_new[index]
    func_spec.append([func_eq[i][0], value, index])

# Applying the specification function to the image
for i in range(0, image_width):
    for j in range(0, image_height):
        image[i][j] = func_spec[image[i][j][0]][2]

# Automatically save the specified image
output_image_file = os.path.join(script_directory, '../resources/output/img/lena_gray_equalized_v2.png')
cv2.imwrite(output_image_file, image)

# Generating the specified histogram
hist_specified = np.zeros(256)
for i in range(0, image_width):
    for j in range(0, image_height):
        pixel_value = int(image[i, j][0])
        hist_specified[pixel_value] += 1

plt.figure()
plt.title('Specified Histogram')
plt.bar(np.arange(len(hist_specified)), hist_specified, color='#34a0cf')
plt.ylabel('Number of pixels')
plt.xlabel('Intensity')
plt.xlim([0, 256])
plt.savefig(os.path.join(script_directory, '../resources/output/histogram/specified_histogram.png'))
plt.close()