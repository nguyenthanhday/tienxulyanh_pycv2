import cv2
import numpy as np

def resize_image_around_center(image, scale_factor):

    # Get image dimensions
    height, width = image.shape[:2]

    # Calculate center
    center = (width // 2, height // 2)

    # Compute new dimensions
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    # Compute new top-left corner
    new_top_left = (center[0] - new_width // 2, center[1] - new_height // 2)

    # Resize image
    resized_image = cv2.resize(image, (new_width, new_height))

    # Create a black canvas with the same size as the original image
    canvas = np.zeros_like(image)

    # Paste the resized image onto the canvas at the new top-left corner
    canvas[new_top_left[1]:new_top_left[1]+new_height, new_top_left[0]:new_top_left[0]+new_width] = resized_image

    return canvas

# Example usage:
# Load image
input_image = cv2.imread("IMG_6430.jpg")

# Define scale factor (e.g., 0.5 for half size, 2.0 for double size)
scale_factor = 0.01

# Resize image around its center
resized_image = resize_image_around_center(input_image, scale_factor)

# Display the resized image
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
