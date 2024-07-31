import cv2
import numpy as np

def rotate_image(image, angle, scale=1.0):
    # Lấy kích thước của ảnh
    (h, w) = image.shape[:2]

    # Tính tâm của ảnh
    center = (w / 2, h / 2)

    # Tạo ma trận xoay
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    # Thực hiện xoay ảnh
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

    return rotated_image

# Đường dẫn của ảnh cần xoay và nghiêng
image_path = "IMG_6430.jpg"

# Đọc ảnh
image = cv2.imread(image_path)

# Gọi hàm để xoay ảnh
angle = -100 # Đổi góc theo ý muốn
rotated_image = rotate_image(image, angle)

# Hiển thị ảnh gốc và ảnh đã xoay
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
