import os
import cv2
import numpy as np
import tienIch
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Dialog_Dieu_Chinh_Do_Net(object):
    def setupUi(self, Dialog, global_folder_path):
        self.global_folder_path_root = global_folder_path
        self.global_folder_path_save = None
        Dialog.setObjectName("Dialog")
        Dialog.resize(806, 225)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.sl_mucDo = QtWidgets.QSlider(Dialog)
        self.sl_mucDo.setMinimum(-10)
        self.sl_mucDo.setMaximum(10)
        self.sl_mucDo.setSingleStep(0)
        self.sl_mucDo.setPageStep(1)
        self.sl_mucDo.setProperty("value", 0)
        self.sl_mucDo.setTracking(True)
        self.sl_mucDo.setOrientation(QtCore.Qt.Horizontal)
        self.sl_mucDo.setInvertedAppearance(False)
        self.sl_mucDo.setInvertedControls(False)
        self.sl_mucDo.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sl_mucDo.setTickInterval(1)
        self.sl_mucDo.setObjectName("sl_mucDo")
        self.verticalLayout.addWidget(self.sl_mucDo)
        self.btn_thuHienGiamNhieu = QtWidgets.QPushButton(Dialog)
        self.btn_thuHienGiamNhieu.setObjectName("btn_thuHienGiamNhieu")
        self.verticalLayout.addWidget(self.btn_thuHienGiamNhieu)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.lb_anh = QtWidgets.QLabel(Dialog)
        self.lb_anh.setObjectName("lb_anh")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lb_anh)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.load_first_image()
        self.pushButton.clicked.connect(self.chooseDirectory)
        self.sl_mucDo.sliderMoved.connect(self.on_slider_moved)
        self.sl_mucDo.valueChanged.connect(self.on_slider_moved)
        self.btn_thuHienGiamNhieu.clicked.connect(self.handel_dieuChinhDoNet)

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

    def chooseDirectory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Chọn thư mục", QtCore.QDir.currentPath())
        if directory:
            self.global_folder_path_save = directory
            self.label_2.setText(directory)  
            
    def on_slider_moved(self, value):
        # Kiểm tra xem thư mục và ảnh có tồn tại
        self.value_blr = value
        self.label_4.setText(f"Độ nét {value}%")
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
                    scale_factor = max_dimension / max(height, width)
                    img = cv2.resize(img, (int(width * scale_factor), int(height * scale_factor)))

                # Áp dụng tăng/giảm độ nét dựa trên giá trị value
                sharpened_img = tienIch.adjust_sharpness(img, value)

                # Chuyển đổi ảnh sang định dạng QImage để sử dụng trong QPixmap
                img_rgb = cv2.cvtColor(sharpened_img, cv2.COLOR_BGR2RGB)
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


    def handel_dieuChinhDoNet(self):
        # Kiểm tra nếu folder_path_save là None hoặc chuỗi rỗng
        if not self.global_folder_path_save:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục lưu ảnh trước khi tiếp tục!")
            return

        # Tiếp tục xử lý
        giaTriLoc = self.value_blr

        tienIch.dieu_chi_do_net_an(self.global_folder_path_root, self.global_folder_path_save, giaTriLoc)
        self.progressBar.setValue(100)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Tăng giảm độ nét của ảnh</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Chọn thư mục lưu ảnh sau khi đổi"))
        self.label_2.setText(_translate("Dialog", "Đường dẫn thư mục"))
        self.label_3.setText(_translate("Dialog", "Nếu không thay đổi đường dẫn lưu ảnh sau khi thay đổi, các ảnh sẽ ghi đè vào ảnh góc trước đó"))
        self.label_4.setText(_translate("Dialog", "Mức độ nét"))
        self.btn_thuHienGiamNhieu.setText(_translate("Dialog", "Thực hiện"))
        self.lb_anh.setText(_translate("Dialog", "TextLabel"))
