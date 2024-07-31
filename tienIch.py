import os
import cv2
from PIL import Image
import numpy as np


def count_images_in_directory(directory_path):
    image_extensions = [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
    ]  # Các định dạng ảnh phổ biến

    image_count = 0

    # Duyệt qua tất cả các tệp trong thư mục
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        # Kiểm tra nếu là tệp ảnh bằng cách kiểm tra phần mở rộng
        if (
            os.path.isfile(filepath)
            and os.path.splitext(filepath)[1].lower() in image_extensions
        ):
            try:
                # Cố gắng mở tệp ảnh bằng PIL
                with Image.open(filepath) as img:
                    image_count += 1
            except:
                # Bỏ qua nếu không thể mở tệp ảnh hoặc có lỗi
                pass

    return str(image_count)+" Ảnh"


def giam_nhieu_anh(phan_tram_giam_nhieu, duong_dan_thu_muc, duong_dan_luu=None):
    # Kiểm tra nếu thư mục tồn tại
    if not os.path.isdir(duong_dan_thu_muc):
        print(f"Thư mục '{duong_dan_thu_muc}' không tồn tại.")
        return

    # Tạo thư mục đầu ra nếu chưa tồn tại
    thu_muc_dau_ra = os.path.join(duong_dan_thu_muc, "giam_nhieu")
    os.makedirs(thu_muc_dau_ra, exist_ok=True)

    # Duyệt qua từng file trong thư mục
    for ten_tap_tin in os.listdir(duong_dan_thu_muc):
        duong_dan_tap_tin = os.path.join(duong_dan_thu_muc, ten_tap_tin)
        # Kiểm tra nếu đó là file hình ảnh
        if os.path.isfile(duong_dan_tap_tin) and ten_tap_tin.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            # Đọc hình ảnh
            img = cv2.imread(duong_dan_tap_tin)
            if img is None:
                print(f"Không thể đọc hình ảnh {duong_dan_tap_tin}.")
                continue
            
            # Tính toán giá trị h cho hàm fastNlMeansDenoisingColored
            # giá trị h quyết định mức độ giảm nhiễu
            h = phan_tram_giam_nhieu * 10
            
            # Giảm nhiễu hình ảnh
            anh_giam_nhieu = cv2.fastNlMeansDenoisingColored(img, None, h, h, 7, 21)
            
            # Xác định đường dẫn lưu ảnh
            if duong_dan_luu:
                duong_dan_dau_ra = os.path.join(duong_dan_luu, ten_tap_tin)
            else:
                duong_dan_dau_ra = os.path.join(thu_muc_dau_ra, ten_tap_tin)

            # Lưu hình ảnh đã giảm nhiễu
            cv2.imwrite(duong_dan_dau_ra, anh_giam_nhieu)
            print(f"Đã lưu ảnh giảm nhiễu tại {duong_dan_dau_ra}.")

            # Xóa ảnh gốc nếu đường dẫn lưu không được cung cấp
            if not duong_dan_luu:
                os.remove(duong_dan_tap_tin)
                print(f"Đã xóa ảnh gốc {duong_dan_tap_tin}.")
            
    print("Hoàn thành giảm nhiễu cho tất cả các hình ảnh trong thư mục.")
    
    
def doi_dinh_dang(input_directory, output_directory=None, output_format='png'):
    # Kiểm tra định dạng đầu ra có hợp lệ không
    if output_format.lower() not in ['jpg', 'tiff', 'png', 'bmp', 'gif']:
        print("Định dạng đầu ra không hợp lệ!")
        return

    # Tạo thư mục đầu ra nếu được chỉ định
    if output_directory:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

    # Lặp qua các tệp trong thư mục đầu vào
    for filename in os.listdir(input_directory):
        input_filepath = os.path.join(input_directory, filename)
        # Kiểm tra xem tệp có phải là một tệp ảnh hay không
        if os.path.isfile(input_filepath) and any(filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']):
            # Đọc ảnh
            image = cv2.imread(input_filepath)
            # Tạo tên file mới với định dạng đầu ra mong muốn
            new_filename = os.path.splitext(filename)[0] + '.' + output_format
            # Xác định đường dẫn lưu trữ đối với tệp đầu ra
            if output_directory:
                output_filepath = os.path.join(output_directory, new_filename)
            else:
                output_filepath = input_filepath  # Giữ nguyên địa chỉ nếu không có thư mục đầu ra
            # Ghi ảnh ra file mới với định dạng mong muốn
            cv2.imwrite(output_filepath, image)
            print(f"Đã chuyển đổi {filename} thành {new_filename}")
            
    return True


def normalize_image(image, method='min-max'):
    if method == 'min-max':
        norm_image = cv2.normalize(image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    elif method == 'z-score':
        mean = np.mean(image)
        std = np.std(image)
        norm_image = (image - mean) / std
    elif method == 'scale':
        norm_image = image / 255.0
    else:
        raise ValueError("Unsupported normalization method. Choose 'min-max', 'z-score', or 'scale'.")
    
    return norm_image

def chuan_hoa_anh(input_dir, output_dir, method='min-max'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(input_dir, filename)
            image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
            
            if image is not None:
                norm_image = normalize_image(image, method)
                
                # Rescale the normalized image to [0, 255] range and convert to uint8
                if method == 'min-max' or method == 'z-score':
                    norm_image = cv2.normalize(norm_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
                    norm_image = norm_image.astype(np.uint8)
                elif method == 'scale':
                    norm_image = (norm_image * 255).astype(np.uint8)
                
                output_path = os.path.join(output_dir, filename)
                cv2.imwrite(output_path, norm_image)
                print(f"Saved normalized image: {output_path}")
            else:
                print(f"Failed to read image: {image_path}")
        else:
            print(f"Skipped non-image file: {filename}")
    return True

def chuyen_doi_he_mau(input_dir, output_dir, color_space):
    # Chuyển các tên hệ màu thành mã hệ màu của OpenCV
    color_spaces = {
        "RGB": cv2.COLOR_BGR2RGB,
        "BGR": cv2.COLOR_RGB2BGR,
        "Grayscale": cv2.COLOR_BGR2GRAY,
        "HSV": cv2.COLOR_BGR2HSV,
        "AnhXam": cv2.COLOR_BGR2GRAY
    }
    
    # Kiểm tra xem hệ màu được chỉ định có hợp lệ không
    if color_space not in color_spaces:
        print("Hệ màu không hợp lệ.")
        return

    # Tạo thư mục đầu ra nếu nó không tồn tại
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Lặp qua tất cả các tệp ảnh trong thư mục đầu vào
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            # Đường dẫn đầy đủ đến tệp ảnh đầu vào
            input_path = os.path.join(input_dir, filename)
            
            # Đọc ảnh từ đường dẫn
            image = cv2.imread(input_path)
            
            # Kiểm tra xem ảnh có được đọc thành công không
            if image is not None:
                # Chuyển đổi hệ màu
                converted_image = cv2.cvtColor(image, color_spaces[color_space])
                
                # Đường dẫn đến tệp ảnh đầu ra
                output_path = os.path.join(output_dir, filename)
                
                # Lưu ảnh đã chuyển đổi vào thư mục đầu ra
                cv2.imwrite(output_path, converted_image)
                print(f"Đã chuyển đổi và lưu {output_path}")
            else:
                print(f"Không thể đọc ảnh từ {input_path}")
    return True


def doi_co_anh(folder_path_root, folder_path_save, target_size, style_resSize=True):
    # Ép kiểu target_size thành số (nếu nó là một chuỗi)
    target_size = int(target_size)

    for filename in os.listdir(folder_path_root):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            input_path = os.path.join(folder_path_root, filename)
            output_path = os.path.join(folder_path_save, filename)

            image = cv2.imread(input_path)
            height, width, _ = image.shape

            aspect_ratio = width / height

            if style_resSize:  # Nếu ép thành hình vuông
                if aspect_ratio > 1:  # Chiều rộng lớn hơn chiều cao
                    new_width = new_height = target_size
                    # Tính toán phần thừa để thêm vào chiều cao để tạo hình vuông
                    padding = int((width - height) / 2)
                    # Thêm padding vào chiều cao
                    resized_image = cv2.copyMakeBorder(image, padding, padding, 0, 0, cv2.BORDER_CONSTANT, value=[0, 0, 0])
                else:  # Chiều cao lớn hơn hoặc bằng chiều rộng
                    new_width = new_height = target_size
                    padding = int((height - width) / 2)
                    # Thêm padding vào chiều rộng
                    resized_image = cv2.copyMakeBorder(image, 0, 0, padding, padding, cv2.BORDER_CONSTANT, value=[0, 0, 0])
            else:  # Nếu điều chỉnh kích thước theo tỷ lệ
                new_width = int(target_size)
                new_height = int(target_size / aspect_ratio)

            resized_image = cv2.resize(image, (new_width, new_height))

            cv2.imwrite(output_path, resized_image)
            print(f"Đã chuyển đổi và lưu {output_path}")
    return True

def tang_giam_sang(root_folder, save_folder, brightness_value):
    # Kiểm tra và ép kiểu brightness_value thành số
    try:
        brightness_value = float(brightness_value)
    except ValueError:
        print("Giá trị độ sáng không hợp lệ. Vui lòng nhập một số.")
        return

    # Kiểm tra xem thư mục nguồn có tồn tại không
    if not os.path.isdir(root_folder):
        print("Thư mục nguồn không tồn tại.")
        return

    # Tạo thư mục đích nếu chưa tồn tại
    if not os.path.isdir(save_folder):
        os.makedirs(save_folder)

    # Lặp qua tất cả các tệp trong thư mục nguồn
    for file_name in os.listdir(root_folder):
        # Kiểm tra xem tệp có phải là ảnh không
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            file_path = os.path.join(root_folder, file_name)
            # Đọc ảnh từ đường dẫn bằng OpenCV
            img = cv2.imread(file_path)

            # Kiểm tra xem ảnh có đọc được không
            if img is None:
                print(f"Không thể đọc ảnh: {file_name}")
                continue

            # Điều chỉnh độ sáng của ảnh
            bright_img = np.zeros_like(img, img.dtype)
            alpha = 1.0  # Hệ số tăng sáng, giữ nguyên
            beta = brightness_value * 2.55  # Giá trị thay đổi độ sáng, từ -255 đến 255

            # Dùng hàm addWeighted để điều chỉnh độ sáng của ảnh
            bright_img = cv2.addWeighted(img, alpha, bright_img, 0, beta)

            # Lưu ảnh đã điều chỉnh vào thư mục đích
            save_path = os.path.join(save_folder, file_name)
            cv2.imwrite(save_path, bright_img)
            print(f"Đã lưu ảnh: {save_path}")
    return True


def thay_doi_tuong_phan(root_folder, save_folder, contrast_value):
    # Kiểm tra và ép kiểu contrast_value thành số
    try:
        contrast_value = float(contrast_value)
    except ValueError:
        print("Giá trị độ tương phản không hợp lệ. Vui lòng nhập một số.")
        return

    # Kiểm tra xem thư mục nguồn có tồn tại không
    if not os.path.isdir(root_folder):
        print("Thư mục nguồn không tồn tại.")
        return

    # Tạo thư mục đích nếu chưa tồn tại
    if not os.path.isdir(save_folder):
        os.makedirs(save_folder)

    # Lặp qua tất cả các tệp trong thư mục nguồn
    for file_name in os.listdir(root_folder):
        # Kiểm tra xem tệp có phải là ảnh không
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            file_path = os.path.join(root_folder, file_name)
            # Đọc ảnh từ đường dẫn bằng OpenCV
            img = cv2.imread(file_path)

            # Kiểm tra xem ảnh có đọc được không
            if img is None:
                print(f"Không thể đọc ảnh: {file_name}")
                continue

            # Điều chỉnh độ tương phản của ảnh
            alpha = 1.0 + contrast_value / 100.0  # Hệ số tăng giảm tương phản
            beta = 0  # Không thay đổi độ sáng

            # Dùng hàm convertScaleAbs để điều chỉnh độ tương phản của ảnh
            contrast_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

            # Lưu ảnh đã điều chỉnh vào thư mục đích
            save_path = os.path.join(save_folder, file_name)
            cv2.imwrite(save_path, contrast_img)
            print(f"Đã lưu ảnh: {save_path}")
            
            
def giam_dung_luong_nen_anh(root, output_dir, quality):
    quality = max(0, min(100, 100 - quality))
    # Kiểm tra và tạo thư mục đầu ra nếu chưa tồn tại
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Duyệt qua tất cả các file trong thư mục gốc
    for filename in os.listdir(root):
        # Tạo đường dẫn đầy đủ đến file
        file_path = os.path.join(root, filename)
        
        # Kiểm tra xem đó có phải là file ảnh không
        if os.path.isfile(file_path):
            # Đọc ảnh từ file
            img = cv2.imread(file_path)
            
            # Kiểm tra xem ảnh có được đọc thành công không
            if img is not None:
                # Tạo tên file đầu ra với định dạng jpg
                output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + '.jpg')
                
                # Thiết lập mức độ nén
                compression_params = [cv2.IMWRITE_JPEG_QUALITY, quality]
                
                # Lưu ảnh với mức độ nén đã thiết lập
                cv2.imwrite(output_file, img, compression_params)
                print(f'Đã nén và lưu: {output_file}')
            else:
                print(f'Không thể đọc ảnh: {file_path}')
        else:
            print(f'{file_path} không phải là file ảnh.')
    return True


def adjust_sharpness(image, factor):
    if factor == 0:
        return image
    else:
        # Tạo kernel làm rõ
        kernel = np.array([[-1, -1, -1],
                           [-1, 9 + factor, -1],
                           [-1, -1, -1]])

        # Tạo một ảnh trống cùng kích thước với img để chứa kết quả
        sharpened_image = np.zeros_like(image, dtype=np.float32)

        # Áp dụng kernel lên ảnh để làm rõ
        sharpened_image[:,:,0] = cv2.filter2D(image[:,:,0], -1, kernel)
        sharpened_image[:,:,1] = cv2.filter2D(image[:,:,1], -1, kernel)
        sharpened_image[:,:,2] = cv2.filter2D(image[:,:,2], -1, kernel)

        # Đảm bảo các giá trị pixel không vượt quá phạm vi [0, 255]
        sharpened_image = np.clip(sharpened_image, 0, 255)

        # Điều chỉnh độ sáng của hình ảnh sau khi làm rõ
        if factor < 0:
            darkening_factor = 1.0 + abs(factor) / 5.0
            sharpened_image *= darkening_factor
            sharpened_image = np.clip(sharpened_image, 0, 255)

        # Chuyển về định dạng uint8
        sharpened_image = np.uint8(sharpened_image)

        return sharpened_image


def dieu_chi_do_net_an(input_directory, output_directory, factor):
    # Tạo thư mục đầu ra nếu nó không tồn tại
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Lặp qua tất cả các tệp trong thư mục đầu vào
    for filename in os.listdir(input_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Đọc ảnh
            image_path = os.path.join(input_directory, filename)
            image = cv2.imread(image_path)

            # Điều chỉnh độ nét của ảnh
            adjusted_image = adjust_sharpness(image, factor)

            # Lưu ảnh đã điều chỉnh vào thư mục đầu ra
            output_path = os.path.join(output_directory, filename)
            cv2.imwrite(output_path, adjusted_image)
            
            
# def zoom_image(img, scale_factor):
#     # Lấy kích thước ảnh
#     height, width = img.shape[:2]
#     # Tính toán kích thước mới dựa trên mức độ thu phóng
#     new_height = int(height * scale_factor)
#     new_width = int(width * scale_factor)
#     # Thu phóng ảnh
#     zoomed_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
#     return zoomed_img
            
# def thu_phong_anh(input_dir, output_dir, scale_factor):
#     # Tạo thư mục đầu ra nếu chưa tồn tại
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     # Lặp qua tất cả các tệp trong thư mục đầu vào
#     for filename in os.listdir(input_dir):
#         # Đường dẫn đầy đủ đến tệp ảnh đầu vào
#         input_path = os.path.join(input_dir, filename)
#         # Đọc ảnh từ đường dẫn đầu vào
#         image = cv2.imread(input_path)
#         if image is not None:
#             # Lấy kích thước ảnh
#             height, width = image.shape[:2]
#             # Tính toán kích thước mới dựa trên mức độ thu phóng
#             new_height = int(height * scale_factor)
#             new_width = int(width * scale_factor)
#             # Thu phóng ảnh
#             resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
#             # Ghi ảnh đã thu phóng vào thư mục đầu ra
#             output_path = os.path.join(output_dir, filename)
#             cv2.imwrite(output_path, resized_image)
#             print(f"Đã lưu {output_path}")
            
            
def thu_phong_anh(root_folder_path, output_folder_path, scale_factor):
    # Kiểm tra sự tồn tại của thư mục gốc và thư mục đích
    if not os.path.isdir(root_folder_path):
        print("Thư mục gốc không tồn tại")
        return
    if not os.path.isdir(output_folder_path):
        os.makedirs(output_folder_path)
        print(f"Tạo thư mục đích: {output_folder_path}")

    # Lấy danh sách các tệp hình ảnh từ thư mục gốc
    files = os.listdir(root_folder_path)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    if not image_files:
        print("Không có ảnh trong thư mục gốc")
        return

    for image_file in image_files:
        image_path = os.path.join(root_folder_path, image_file)

        # Đọc ảnh từ đường dẫn bằng OpenCV
        img = cv2.imread(image_path)
        if img is None:
            print(f"Không thể đọc ảnh: {image_file}")
            continue

        # Áp dụng thu phóng ảnh
        zoomed_img = zoom_image_around_center(img, scale_factor)

        # Tạo đường dẫn lưu ảnh đã thu phóng
        output_image_path = os.path.join(output_folder_path, image_file)

        # Lưu ảnh đã thu phóng
        cv2.imwrite(output_image_path, zoomed_img)
        print(f"Đã lưu ảnh đã thu phóng: {output_image_path}")
    return True

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
            
            
            
def xoay_anh(input_dir, output_dir, angle):
    # Kiểm tra xem thư mục đầu vào có tồn tại không
    if not os.path.isdir(input_dir):
        print(f"Thư mục {input_dir} không tồn tại.")
        return
    
    # Kiểm tra xem thư mục đầu ra có tồn tại không, nếu không, tạo mới
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Lặp qua tất cả các tệp trong thư mục đầu vào
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            # Đọc ảnh từ thư mục đầu vào
            img = cv2.imread(input_path)
            
            # Áp dụng góc xoay
            rotated_img = rotate_image(img, angle)
            
            # Lưu ảnh đã xoay vào thư mục đầu ra
            cv2.imwrite(output_path, rotated_img)
            print(f"Đã áp dụng góc xoay và lưu ảnh {filename} vào {output_path}")

def rotate_image(image, angle):
    # Lấy kích thước của ảnh
    (h, w) = image.shape[:2]

    # Tính tâm của ảnh
    center = (w / 2, h / 2)

    # Tạo ma trận xoay
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Thực hiện xoay ảnh
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

    return rotated_image