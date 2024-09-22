import cv2
import math
import numpy as np
import os
from matplotlib import pyplot as plt

# Get the current directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the folder from the script directory
image_path = os.path.join(script_directory, '../resources/img/lena_gray.bmp')

image = cv2.imread(image_path)  # Load the "lena_gray.bmp" image
image_width = image.shape[1]  # Get the image width
image_height = image.shape[0]  # Get the image height

c = 6  # Set the value of c
b = 4  # Set the value of b

# Letter a: Apply linear transformation (c * pixel + b) to each pixel in the image
#for i in range(0, image_width):
#    for j in range(0, image_height):
#        image[i, j] = (c * image[i][j][0]) + b

# Letter b: Apply the logarithmic function c * log2(pixel + 1) to each pixel in the image
for i in range(0, image_width):
    for j in range(0, image_height):
        image[i][j] = c * (math.log(image[i][j][0] + 1, 2))

# Letter c: (Commented) - theoretically represents an exponential function
#for i in range(0, image_width):
#    for j in range(0, image_height):
#        image[i, j] = c * math.exp(image[i, j][0] + 1)

# Automatically save the resulting image
save_directory = os.path.join(script_directory, '../resources/output/img')
os.makedirs(save_directory, exist_ok=True)  # Ensure the output directory exists

# Save the transformed image
output_image_path = os.path.join(save_directory, 'lena_log_transformation.png')
cv2.imwrite(output_image_path, image)

# Display the resulting image in a window
cv2.imshow("Resulting Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()