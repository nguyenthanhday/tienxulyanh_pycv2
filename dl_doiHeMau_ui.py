from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import tienIch

class Ui_Dialog_Doi_He_Mau(object):
    def setupUi(self, Dialog, global_folder_path):
        self.global_folder_path_root = global_folder_path
        self.global_folder_path_save = None
        Dialog.setObjectName("Dialog")
        Dialog.resize(546, 268)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_chonFileSave = QtWidgets.QPushButton(Dialog)
        self.btn_chonFileSave.setGeometry(QtCore.QRect(20, 50, 191, 31))
        self.btn_chonFileSave.setObjectName("btn_chonFileSave")
        self.lb_duongDanLuu = QtWidgets.QLabel(Dialog)
        self.lb_duongDanLuu.setGeometry(QtCore.QRect(220, 60, 191, 16))
        self.lb_duongDanLuu.setObjectName("lb_duongDanLuu")
        self.btn_thucHien = QtWidgets.QPushButton(Dialog)
        self.btn_thucHien.setGeometry(QtCore.QRect(100, 180, 291, 23))
        self.btn_thucHien.setObjectName("btn_thucHien")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 230, 521, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 110, 481, 19))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.rd_bgr = QtWidgets.QRadioButton(self.widget)
        self.rd_bgr.setObjectName("rd_bgr")
        self.horizontalLayout.addWidget(self.rd_bgr)
        
        self.rd_rgb = QtWidgets.QRadioButton(self.widget)
        self.rd_rgb.setObjectName("rd_rgb")
        self.horizontalLayout.addWidget(self.rd_rgb)
        
        self.rd_grayscale = QtWidgets.QRadioButton(self.widget)
        self.rd_grayscale.setObjectName("rd_grayscale")
        self.horizontalLayout.addWidget(self.rd_grayscale)
        
        self.rd_hsv = QtWidgets.QRadioButton(self.widget)
        self.rd_hsv.setObjectName("rd_hsv")
        self.horizontalLayout.addWidget(self.rd_hsv)
        
        self.rd_anh_xam = QtWidgets.QRadioButton(self.widget)
        self.rd_anh_xam.setObjectName("rd_anh_xam")
        self.horizontalLayout.addWidget(self.rd_anh_xam)

        self.rd_bgr.setChecked(True)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btn_thucHien.clicked.connect(self.handel_doiHeMau)
        self.btn_chonFileSave.clicked.connect(self.chooseDirectory)

    def chooseDirectory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Chọn thư mục", QtCore.QDir.currentPath())
        if directory:
            self.global_folder_path_save = directory
            self.lb_duongDanLuu.setText(directory)  
    
    def handel_doiHeMau(self):
        if not self.global_folder_path_save:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        else:
            QMessageBox.information(None, "Lưu ý", "Đồng ý chuyển đổi định dạng cho toàn bộ ảnh trong thư mục")
            dinhDang = 'BGR'
            if self.rd_bgr.isChecked():
                dinhDang = 'BGR'
            if self.rd_rgb.isChecked():
                dinhDang = 'RGB'
            if self.rd_grayscale.isChecked():
                dinhDang = 'Grayscale'
            if self.rd_hsv.isChecked():
                dinhDang = 'HSV'
            if self.rd_anh_xam.isChecked():
                dinhDang = 'AnhXam'
            
            if tienIch.chuyen_doi_he_mau(self.global_folder_path_root, self.global_folder_path_save, dinhDang):
                QMessageBox.information(None, "Thông báo", "Đã chuyển đổi thành công!")
                
                
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Đổi tên file"))
        self.btn_chonFileSave.setText(_translate("Dialog", "Chọn thư mục lưu ảnh sau khi đổi"))
        self.lb_duongDanLuu.setText(_translate("Dialog", "Đường dẫn thư mục"))
        self.btn_thucHien.setText(_translate("Dialog", "Thực hiện"))
        self.rd_bgr.setText(_translate("Dialog", "BGR"))
        self.rd_rgb.setText(_translate("Dialog", "RGB"))
        self.rd_grayscale.setText(_translate("Dialog", "Grayscale"))
        self.rd_hsv.setText(_translate("Dialog", "HSV"))
        self.rd_anh_xam.setText(_translate("Dialog", "Ảnh xám"))
