import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

# Get the current directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Path to save the histograms
save_directory = os.path.join(script_directory, '../resources/output/histogram/')

# Relative path to the folder from the script directory
image_path = os.path.join(script_directory, '../resources/img/einstein.jpg')

# Extract the image name without extension
image_name = os.path.splitext(os.path.basename(image_path))[0]

# Reading the image
image = cv2.imread(image_path)

# Getting the dimensions of the image
image_height, image_width, _ = image.shape

# Initializing the histogram
histogram_image = np.zeros(256)

# Calculating the histogram
for i in range(image_width):
    for j in range(image_height):
        pixel_value = int(image[j, i][0])  # Pixel value in grayscale
        histogram_image[pixel_value] += 1  # Counting the occurrence of the pixel value

# Make sure the save directory exists
os.makedirs(save_directory, exist_ok=True)

# Saving the image histogram
plt.figure()
plt.title(f'Basic Histogram - {image_name}')
plt.bar(np.arange(len(histogram_image)), histogram_image, color='#34a0cf')
plt.ylabel('Number of pixels')
plt.xlabel('Intensity Value')
plt.xlim([0, 256])
plt.savefig(os.path.join(save_directory, f'basic_histogram_{image_name}.png'))
plt.close()

# Total number of pixels in the image
num_pixels = image_width * image_height

# Calculating the PDF and CDF
normalized_histogram = np.zeros(256)
cumulative_histogram = np.zeros(256)

for i in range(0, len(histogram_image)):
    pk = histogram_image[i] / num_pixels  # Probability of occurrence of a given pixel value
    normalized_histogram[i] = pk  # Storing the PDF
    if i > 0:
        cumulative_histogram[i] = pk + cumulative_histogram[i - 1]  # Calculating the CDF
    else:
        cumulative_histogram[i] = pk

# Saving the PDF histogram
plt.figure()
plt.title(f'Normalized Histogram - {image_name}')
plt.bar(np.arange(len(normalized_histogram)), normalized_histogram, color='#34a0cf')
plt.ylabel('Probability p(r)')
plt.xlabel('Intensity Value')
plt.xlim([0, 256])
plt.savefig(os.path.join(save_directory, f'normalized_histogram_{image_name}.png'))
plt.close()

# Saving the CDF histogram
plt.figure()
plt.title(f'Cumulative Histogram - {image_name}')
plt.bar(np.arange(len(cumulative_histogram)), cumulative_histogram, color='#34a0cf')
plt.ylabel('Cumulative Probability')
plt.xlabel('Intensity')
plt.xlim([0, 256])
plt.savefig(os.path.join(save_directory, f'cumulative_histogram_{image_name}.png'))
plt.close()