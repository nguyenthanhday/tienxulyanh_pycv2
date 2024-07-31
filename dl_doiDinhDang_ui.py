
import tienIch
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog_Doi_Dinh_Dang(object):
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
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 521, 16))
        self.label_3.setObjectName("label_3")
        self.btn_thucHien = QtWidgets.QPushButton(Dialog)
        self.btn_thucHien.setGeometry(QtCore.QRect(100, 200, 291, 23))
        self.btn_thucHien.setObjectName("btn_thucHien")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 230, 521, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 191, 16))
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 140, 481, 19))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rd_tiff = QtWidgets.QRadioButton(self.widget)
        self.rd_tiff.setObjectName("rd_tiff")
        self.rd_tiff.setChecked(True)
        self.horizontalLayout.addWidget(self.rd_tiff)
        self.rd_gif = QtWidgets.QRadioButton(self.widget)
        self.rd_gif.setObjectName("rd_gif")
        self.horizontalLayout.addWidget(self.rd_gif)
        self.rd_png = QtWidgets.QRadioButton(self.widget)
        self.rd_png.setObjectName("rd_png")
        self.horizontalLayout.addWidget(self.rd_png)
        self.rd_jpg = QtWidgets.QRadioButton(self.widget)
        self.rd_jpg.setObjectName("rd_jpg")
        self.horizontalLayout.addWidget(self.rd_jpg)
        self.rd_bmp = QtWidgets.QRadioButton(self.widget)
        self.rd_bmp.setObjectName("rd_bmp")
        self.horizontalLayout.addWidget(self.rd_bmp)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btn_thucHien.clicked.connect(self.handel_doiDinhDang)
        self.btn_chonFileSave.clicked.connect(self.chooseDirectory)


    def chooseDirectory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Chọn thư mục", QtCore.QDir.currentPath())
        if directory:
            self.global_folder_path_save = directory
            self.lb_duongDanLuu.setText(directory)  
    
    def handel_doiDinhDang(self):
        if not self.global_folder_path_save:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        else:
            QMessageBox.information(None, "Lưu ý", "Đồng ý chuyển đổi định dạng cho toàn bộ ảnh trong thư mục")
            dinhDang = 'tiff'
            if self.rd_tiff.isChecked():
                dinhDang = 'tiff'
            if self.rd_gif.isChecked():
                dinhDang = 'gif'
            if self.rd_png.isChecked():
                dinhDang = 'png'
            if self.rd_jpg.isChecked():
                dinhDang = 'jpg'
            if self.rd_bmp.isChecked():
                dinhDang = 'bmp'
            
            if tienIch.doi_dinh_dang(self.global_folder_path_root, self.global_folder_path_save, dinhDang):
                QMessageBox.information(None, "Thông báo", "Đã chuyển đổi thành công!")
            
                
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Đổi định dạng ảnh"))
        self.label.setText(_translate("Dialog", "Đổi định dạng ảnh"))
        self.btn_chonFileSave.setText(_translate("Dialog", "Chọn thư mục lưu ảnh sau khi đổi"))
        self.lb_duongDanLuu.setText(_translate("Dialog", "Đường dẫn thư mục"))
        self.label_3.setText(_translate("Dialog", "Nếu không thay đổi đường dẫn lưu ảnh sau khi thay đổi, các ảnh sẽ ghi đè vào ảnh góc trước đó"))
        self.btn_thucHien.setText(_translate("Dialog", "Thực hiện"))
        self.label_4.setText(_translate("Dialog", "Chọn định dạng thay đổi"))
        self.rd_tiff.setText(_translate("Dialog", "TIFF"))
        self.rd_gif.setText(_translate("Dialog", "GIF"))
        self.rd_png.setText(_translate("Dialog", "PNG"))
        self.rd_jpg.setText(_translate("Dialog", "JPG"))
        self.rd_bmp.setText(_translate("Dialog", "BMP"))
