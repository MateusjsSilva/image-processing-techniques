import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

# Get the current directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Path to save the equalized image and histograms
save_directory = os.path.join(script_directory, '../resources/output/img')
save_histogram = os.path.join(script_directory, '../resources/output/histogram')

# Ensure the save directory exists
os.makedirs(save_directory, exist_ok=True)

# Relative path to the folder from the script directory
image_path = os.path.join(script_directory, '../resources/img/einstein.jpg')

# Extract the image name without extension
image_name = os.path.splitext(os.path.basename(image_path))[0]

# Load the image from the relative path
image = cv2.imread(image_path)

# Get the dimensions of the image
image_width = image.shape[0]
image_height = image.shape[1]

# Initialize the image histogram
image_histogram = np.zeros(256)

# Calculate the histogram of the original image
for i in range(0, image_width):
    for j in range(0, image_height):
        pixel_value = int(image[i, j][0])
        image_histogram[pixel_value] += 1

# Calculate the CDF (Cumulative Distribution Function) and PDF (Probability Density Function)
num_pixels = image_width * image_height
cumulative_histogram = np.zeros(256)
probability_histogram = np.zeros(256)
for i in range(0, len(image_histogram)):
    pk = image_histogram[i] / num_pixels
    probability_histogram[i] = pk
    if i > 0:
        cumulative_histogram[i] = pk + cumulative_histogram[i - 1]
    else:
        cumulative_histogram[i] = pk

# Calculate the equalization function
equalization_function = []
for old_intensity in range(0, 256):
    new_intensity = int(np.ceil(cumulative_histogram[old_intensity] * 255))
    equalization_function.append([old_intensity, new_intensity])

# Apply the equalization function to the image
for i in range(0, image_width):
    for j in range(0, image_height):
        image[i][j] = equalization_function[image[i][j][0]][1]

# Calculate the histogram of the equalized image
equalized_histogram = np.zeros(256)
for i in range(0, image_width):
    for j in range(0, image_height):
        pixel_value = int(image[i, j][0])
        equalized_histogram[pixel_value] += 1

# Save the equalized image automatically
equalized_image_path = os.path.join(save_directory, f'{image_name}_equalized.png')
cv2.imwrite(equalized_image_path, image)

# Save the equalized histogram
plt.figure()
plt.title('Equalized Histogram')
plt.bar(np.arange(len(equalized_histogram)), equalized_histogram, color='#34a0cf')
plt.ylabel('Number of pixels')
plt.xlabel('Intensity')
plt.xlim([0, 256])

# Automatically save the histogram plot
histogram_path = os.path.join(save_histogram, f'equalized_histogram_{image_name}.png')
plt.savefig(histogram_path)
plt.close()