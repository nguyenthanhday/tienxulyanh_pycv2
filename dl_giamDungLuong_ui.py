import tienIch
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Giam_Dung_Luong(object):
    def setupUi(self, Dialog, global_folder_path):
        self.global_folder_path_root = global_folder_path
        self.global_folder_path_save = None
        Dialog.setObjectName("Dialog")
        Dialog.resize(512, 225)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 491, 208))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.sl_mucDo = QtWidgets.QSlider(self.widget)
        self.sl_mucDo.setMinimum(20)
        self.sl_mucDo.setMaximum(100)
        self.sl_mucDo.setSingleStep(0)
        self.sl_mucDo.setPageStep(1)
        self.sl_mucDo.setProperty("value", 0)
        self.sl_mucDo.setTracking(True)
        self.sl_mucDo.setOrientation(QtCore.Qt.Horizontal)
        self.sl_mucDo.setInvertedAppearance(False)
        self.sl_mucDo.setInvertedControls(False)
        self.sl_mucDo.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sl_mucDo.setTickInterval(5)
        self.sl_mucDo.setObjectName("sl_mucDo")
        self.verticalLayout.addWidget(self.sl_mucDo)
        self.btn_thuHienGiamNhieu = QtWidgets.QPushButton(self.widget)
        self.btn_thuHienGiamNhieu.setObjectName("btn_thuHienGiamNhieu")
        self.verticalLayout.addWidget(self.btn_thuHienGiamNhieu)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.chooseDirectory)
        self.sl_mucDo.sliderMoved.connect(self.on_slider_moved)
        self.btn_thuHienGiamNhieu.clicked.connect(self.handel_locNhieu)

    def chooseDirectory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Chọn thư mục", QtCore.QDir.currentPath())
        if directory:
            self.global_folder_path_save = directory
            self.label_2.setText(directory)  
    
    def on_slider_moved(self, value):
        # Kiểm tra xem thư mục và ảnh có tồn tại
        self.value_blr = value
        self.label_4.setText(f"Mức độ giảm dung lượng {value}%")
            
    def handel_locNhieu(self):
        # Kiểm tra nếu folder_path_save là None hoặc chuỗi rỗng
        if not self.global_folder_path_save:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục lưu ảnh trước khi tiếp tục!")
            return

        # Tiếp tục xử lý
        giaTriLoc = self.value_blr

        if tienIch.giam_dung_luong_nen_anh(self.global_folder_path_root, self.global_folder_path_save, giaTriLoc):
            QMessageBox.information(None, "Thông báo", "Giảm dung lượng ảnh thành công!")
            self.progressBar.setValue(100)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Giảm dung lượng ảnh</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Chọn thư mục lưu ảnh sau khi đổi"))
        self.label_2.setText(_translate("Dialog", "Đường dẫn thư mục"))
        self.label_3.setText(_translate("Dialog", "Dung lượng ảnh càn thấp thì chất lượng cũng càn thấp theo!"))
        self.label_4.setText(_translate("Dialog", "Mức độ giảm dung lượng"))
        self.btn_thuHienGiamNhieu.setText(_translate("Dialog", "Thực hiện"))
