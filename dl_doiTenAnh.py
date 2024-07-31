
import os

from PyQt5 import QtCore, QtGui, QtWidgets


global_folder_path_save_doi_ten = ""
class Ui_Dialog_DoiTenFile(object):
    def setupUi(self, Dialog, global_folder_path):
        self.folder_path_root = global_folder_path
        Dialog.setObjectName("Đổi tên file hàng loạt")
        Dialog.resize(546, 268)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 191, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 60, 191, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 521, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(120, 110, 111, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 180, 291, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 230, 521, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.pushButton.clicked.connect(self.chooseDirectory)
        self.pushButton_2.clicked.connect(self.renameFile)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Đổi tên file trong thư mục: "+self.folder_path_root))
        self.pushButton.setText(_translate("Dialog", "Chọn thư mục lưu ảnh sau khi đổi"))
        self.label_2.setText(_translate("Dialog", "Đường dẫn thư mục"))
        self.label_3.setText(_translate("Dialog", "Nếu không thay đổi đường dẫn lưu ảnh sau khi thay đổi, các ảnh sẽ ghi đè vào ảnh góc trước đó"))
        self.label_4.setText(_translate("Dialog", "Nhập tên file cần đổi"))
        self.pushButton_2.setText(_translate("Dialog", "Thực hiện"))

    def chooseDirectory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Chọn thư mục", QtCore.QDir.currentPath())
        if directory:
            global_folder_path_save_doi_ten = directory
            self.label_2.setText(directory)  

    def renameFile(self):
        new_name_file = self.textEdit.toPlainText()
        folder_path_root = self.folder_path_root
        folder_path_save = global_folder_path_save_doi_ten

        if not os.path.exists(folder_path_root):
            # Xử lý khi folder_path_root không tồn tại
            return

        if not os.path.exists(folder_path_save):
            folder_path_save = folder_path_root

        file_list = os.listdir(folder_path_root)
        file_count = 1

        for file_name in file_list:
            old_file_path = os.path.join(self.folder_path_root, file_name)
            if os.path.isfile(old_file_path):
                file_name_without_extension, file_extension = os.path.splitext(file_name)
                new_file_name = f"{new_name_file}_{file_count}{file_extension}"
                new_file_path = os.path.join(folder_path_save, new_file_name)
                os.rename(old_file_path, new_file_path)
                file_count += 1

        self.progressBar.setValue(100)


