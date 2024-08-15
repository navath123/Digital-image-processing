import cv2
import numpy as np
import matplotlib.pyplot as plt

grayscale_image = cv2.imread('img.jpeg', cv2.IMREAD_GRAYSCALE)

if grayscale_image is None:
    print("Failed to load the image.")
else:
    print("Image loaded successfully.")

bit_plane_layers = []

for bit_position in range(8):
    current_bit_plane = np.zeros_like(grayscale_image)
    current_bit_plane = cv2.bitwise_and(grayscale_image, 1 << bit_position)
    current_bit_plane = np.where(current_bit_plane > 0, 255, 0).astype(np.uint8)
    bit_plane_layers.append(current_bit_plane)

figure, axis = plt.subplots(2, 4, figsize=(20, 10))
axis = axis.ravel()

for index in range(8):
    axis[index].imshow(bit_plane_layers[index], cmap='gray')
    axis[index].set_title(f'Bit Plane {index}')
    axis[index].axis('off')

plt.tight_layout()
plt.show()

reconstructed_image_from_bits = np.zeros_like(grayscale_image)

for bit_position in range(4, 8):
    reconstructed_image_from_bits += bit_plane_layers[bit_position] * (1 << bit_position)

plt.figure(figsize=(10, 7))
plt.imshow(reconstructed_image_from_bits, cmap='gray')
plt.title('Reconstructed Image Using Bit Planes 4 to 7')
plt.axis('off')
plt.show()
