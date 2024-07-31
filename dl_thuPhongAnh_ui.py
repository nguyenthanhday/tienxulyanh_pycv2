import os
import cv2
import numpy as np
import tienIch
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer


class Ui_Dialog_Thu_Phong_Anh(object):
    def setupUi(self, Dialog, global_folder_path):
        self.global_folder_path_root = global_folder_path
        self.global_folder_path_save = None
        self.lb_anh = QtWidgets.QLabel(Dialog)
        self.lb_anh.setGeometry(QtCore.QRect(414, 9, 381, 640))
        self.lb_anh.setObjectName("lb_anh")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 160, 381, 52))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_thuHienGiamNhieu = QtWidgets.QPushButton(self.widget)
        self.btn_thuHienGiamNhieu.setObjectName("btn_thuHienGiamNhieu")
        self.verticalLayout.addWidget(self.btn_thuHienGiamNhieu)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.sl_mucDo = QtWidgets.QTextEdit(Dialog)
        self.sl_mucDo.setGeometry(QtCore.QRect(10, 120, 101, 31))
        self.sl_mucDo.setObjectName("sl_mucDo")
        self.sl_mucDo.setAcceptRichText(False)
        self.sl_mucDo.setText('1')
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 399, 109))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.last_text = ""
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.load_first_image()
        self.pushButton.clicked.connect(self.chooseDirectory)
        self.sl_mucDo.textChanged.connect(self.on_editing_finished)
        self.value_zoom = '1'
        self.btn_thuHienGiamNhieu.clicked.connect(self.handel_locNhieu)
        
    # def on_text_changed(self):
    #     # Kiểm tra nội dung nhập liệu có hợp lệ hay không
    #     #QTimer.singleShot(1000, self.on_editing_finished)
    #     self.on_editing_finished

    def on_editing_finished(self):
        try:
            current_text = self.sl_mucDo.toPlainText()
            self.value_zoom = float(current_text.strip())
            if 0.1 <= self.value_zoom <= 2:
                # Áp dụng thu phóng ảnh với mức độ được nhập
                self.apply_zoom(self.value_zoom)
            else:
                print("Mức độ phải nằm trong khoảng từ 0.1 đến 2")
        except ValueError:
            print("Đã nhập sai định dạng")
            
    def chooseDirectory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Chọn thư mục", QtCore.QDir.currentPath())
        if directory:
            self.global_folder_path_save = directory
            self.label_2.setText(directory)  

    def apply_zoom(self, scale_factor):
        # Kiểm tra xem thư mục và ảnh có tồn tại
        if os.path.isdir(self.global_folder_path_root):
            files = os.listdir(self.global_folder_path_root)
            # Lọc ra các tệp hình ảnh
            image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            if image_files:
                first_image_path = os.path.join(self.global_folder_path_root, image_files[0])

                # Đọc ảnh từ đường dẫn bằng OpenCV
                img = cv2.imread(first_image_path)

                # Thay đổi kích thước ảnh thành kích thước cực đại là 640
                max_dimension = 640
                height, width, _ = img.shape
                if max(height, width) > max_dimension:
                    #scale_factor = max_dimension / max(height, width)
                    img = cv2.resize(img, (int(width * scale_factor), int(height * scale_factor)))

                # Áp dụng thu phóng ảnh
                zoomed_img = self.zoom_image_around_center(img, scale_factor)

                # Chuyển đổi ảnh sang định dạng QImage để sử dụng trong QPixmap
                img_rgb = cv2.cvtColor(zoomed_img, cv2.COLOR_BGR2RGB)
                h, w, ch = img_rgb.shape
                bytes_per_line = ch * w
                q_img = QtGui.QImage(img_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)

                # Tạo QPixmap từ QImage và hiển thị trên QLabel
                pixmap = QtGui.QPixmap.fromImage(q_img)
                self.lb_anh.setPixmap(pixmap)
                self.lb_anh.setScaledContents(True)
            else:
                self.lb_anh.setText("Không có ảnh trong thư mục")
        else:
            self.lb_anh.setText("Thư mục không tồn tại")

    def zoom_image_around_center(self, image, scale_factor):
        # Get image dimensions
        print(scale_factor)
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
        
       
     
    def load_first_image(self):
            # Kiểm tra xem thư mục tồn tại và có chứa ảnh không
            if os.path.isdir(self.global_folder_path_root):
                files = os.listdir(self.global_folder_path_root)
                image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
                if image_files:
                    first_image_path = os.path.join(self.global_folder_path_root, image_files[0])

                    # Đọc ảnh từ đường dẫn bằng OpenCV
                    img = cv2.imread(first_image_path)

                    # Thay đổi kích thước ảnh thành kích thước cực đại là 640
                    max_dimension = 640
                    height, width, _ = img.shape
                    if max(height, width) > max_dimension:
                        scale_factor = max_dimension / max(height, width)
                        img = cv2.resize(img, (int(width * scale_factor), int(height * scale_factor)))

                    # Chuyển đổi ảnh sang định dạng QImage để sử dụng trong QPixmap
                    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    h, w, ch = img_rgb.shape
                    bytes_per_line = ch * w
                    q_img = QtGui.QImage(img_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)

                    # Tạo QPixmap từ QImage và hiển thị trên QLabel
                    pixmap = QPixmap.fromImage(q_img)
                    self.lb_anh.setPixmap(pixmap)
                    self.lb_anh.setScaledContents(True)
                else:
                    self.lb_anh.setText("Không có ảnh trong thư mục")
            else:
                self.lb_anh.setText("Thư mục không tồn tại")
                
    def handel_locNhieu(self):
        # Kiểm tra nếu folder_path_save là None hoặc chuỗi rỗng
        if not self.global_folder_path_save:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục lưu ảnh trước khi tiếp tục!")
            return

        # Tiếp tục xử lý
        giaTriLoc = self.value_zoom

        if tienIch.thu_phong_anh(self.global_folder_path_root, self.global_folder_path_save, giaTriLoc):
            QMessageBox.information(None, "Thông báo", "Đã áp dụng thu phóng ảnh ảnh thành công cho các ảnh!")
            self.progressBar.setValue(100)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb_anh.setText(_translate("Dialog", "TextLabel"))
        self.btn_thuHienGiamNhieu.setText(_translate("Dialog", "Thực hiện"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Thu phóng ảnh</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Chọn thư mục lưu ảnh sau khi đổi"))
        self.label_2.setText(_translate("Dialog", "Đường dẫn thư mục"))
        self.label_3.setText(_translate("Dialog", "Nếu không thay đổi đường dẫn lưu ảnh sau khi thay đổi, các ảnh sẽ ghi đè vào ảnh góc trước đó"))
        self.label_4.setText(_translate("Dialog", "Mức độ thu, phóng ảnh: chỉ nhận trong [0.1: 2]"))
