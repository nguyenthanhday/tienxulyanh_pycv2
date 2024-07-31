
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import tienIch

class Ui_Dialog_Doi_Co_Anh(object):
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
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.label_4.setObjectName("label_4")
        self.txt_coAnh = QtWidgets.QTextEdit(Dialog)
        self.txt_coAnh.setGeometry(QtCore.QRect(90, 110, 111, 31))
        self.txt_coAnh.setObjectName("txt_coAnh")
        self.btn_thucHien = QtWidgets.QPushButton(Dialog)
        self.btn_thucHien.setGeometry(QtCore.QRect(100, 190, 291, 23))
        self.btn_thucHien.setObjectName("btn_thucHien")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 230, 521, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.ch_styleRes = QtWidgets.QCheckBox(Dialog)
        self.ch_styleRes.setGeometry(QtCore.QRect(20, 150, 271, 21))
        self.ch_styleRes.setObjectName("ch_styleRes")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btn_thucHien.clicked.connect(self.handel_doiCoAnh)
        self.btn_chonFileSave.clicked.connect(self.chooseDirectory)

    def chooseDirectory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Chọn thư mục", QtCore.QDir.currentPath())
        if directory:
            self.global_folder_path_save = directory
            self.lb_duongDanLuu.setText(directory) 

    def handel_doiCoAnh(self):
        if not self.global_folder_path_save:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        else:
            QMessageBox.information(None, "Lưu ý", "Đồng ý áp dụng thay đổi cở ảnh cho toàn bộ ảnh trong thư mục")

            target_size = self.txt_coAnh.toPlainText()
            if(len(target_size)<=0):
                QMessageBox.information(None, "Cảnh báo", "Vui lòng cở ảnh cần đổi trước khi tiếp tục!")
                return
            if tienIch.doi_co_anh(self.global_folder_path_root, self.global_folder_path_save,target_size, self.ch_styleRes.isChecked()):
                QMessageBox.information(None, "Thông báo", "Đã chuyển đổi thành công!")  
                
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Đổi cở ảnh"))
        self.btn_chonFileSave.setText(_translate("Dialog", "Chọn thư mục lưu ảnh sau khi đổi"))
        self.lb_duongDanLuu.setText(_translate("Dialog", "Đường dẫn thư mục"))
        self.label_4.setText(_translate("Dialog", "Nhập cở ảnh"))
        self.btn_thucHien.setText(_translate("Dialog", "Thực hiện"))
        self.ch_styleRes.setText(_translate("Dialog", "Ép ảnh thành cở hình vuông theo kích thước trên"))
