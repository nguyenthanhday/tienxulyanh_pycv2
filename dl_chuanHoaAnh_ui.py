
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import tienIch

class Ui_Dialog_Chuan_Hoa(object):
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
        self.btn_thucHien.setGeometry(QtCore.QRect(120, 200, 291, 23))
        self.btn_thucHien.setObjectName("btn_thucHien")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 230, 521, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 191, 16))
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 120, 481, 19))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rd_minMax = QtWidgets.QRadioButton(self.widget)
        self.rd_minMax.setObjectName("rd_minMax")
        self.horizontalLayout.addWidget(self.rd_minMax)
        self.rd_zScore = QtWidgets.QRadioButton(self.widget)
        self.rd_zScore.setObjectName("rd_zScore")
        self.horizontalLayout.addWidget(self.rd_zScore)
        self.rd_scale = QtWidgets.QRadioButton(self.widget)
        self.rd_scale.setObjectName("rd_scale")
        self.horizontalLayout.addWidget(self.rd_scale)
        self.rd_minMax.setChecked(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btn_thucHien.clicked.connect(self.handel_chuanHoa)
        self.btn_chonFileSave.clicked.connect(self.chooseDirectory)

    def chooseDirectory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Chọn thư mục", QtCore.QDir.currentPath())
        if directory:
            self.global_folder_path_save = directory
            self.lb_duongDanLuu.setText(directory) 

    def handel_chuanHoa(self):
        if not self.global_folder_path_save:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        else:
            QMessageBox.information(None, "Lưu ý", "Đồng ý áp dụng chuẩn hóa cho toàn bộ ảnh trong thư mục")
            dinhDang = 'min-max'
            if self.rd_minMax.isChecked():
                dinhDang = 'min-max'
            if self.rd_zScore.isChecked():
                dinhDang = 'z-score'
            if self.rd_scale.isChecked():
                dinhDang = 'scale'

            if tienIch.chuan_hoa_anh(self.global_folder_path_root, self.global_folder_path_save, dinhDang):
                QMessageBox.information(None, "Thông báo", "Đã chuyển đổi thành công!")            

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Chuẩn hóa ánh"))
        self.btn_chonFileSave.setText(_translate("Dialog", "Chọn thư mục lưu ảnh sau khi chuẩn hóa"))
        self.lb_duongDanLuu.setText(_translate("Dialog", "Đường dẫn thư mục"))
        self.btn_thucHien.setText(_translate("Dialog", "Thực hiện"))
        self.label_3.setText(_translate("Dialog", "Phương thức chuẩn hóa ảnh"))
        self.rd_minMax.setText(_translate("Dialog", "min-max"))
        self.rd_zScore.setText(_translate("Dialog", "z-score"))
        self.rd_scale.setText(_translate("Dialog", "scale"))
