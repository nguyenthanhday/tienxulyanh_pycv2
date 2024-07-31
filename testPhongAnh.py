import cv2
import numpy as np

def zoom_image_around_center(image, scale_factor):
    # Get image dimensions
    height, width = image.shape[:2]

    # Calculate center
    center = (width // 2, height // 2)

    # Compute new dimensions
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    # Define the transformation matrix for scaling
    scale_matrix = np.array([[scale_factor, 0, (1 - scale_factor) * center[0]],
                             [0, scale_factor, (1 - scale_factor) * center[1]]], dtype=np.float32)

    # Apply the scaling transformation
    zoomed_image = cv2.warpAffine(image, scale_matrix, (width, height))

    return zoomed_image

# Example usage:
# Load image
input_image = cv2.imread("IMG_6430.jpg")

# Define scale factor (e.g., 1.5 for 1.5 times larger, 0.5 for half size)
scale_factor = 2

# Zoom image around its center
zoomed_image = zoom_image_around_center(input_image, scale_factor)

# Display the zoomed image
cv2.imshow("Zoomed Image", zoomed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
