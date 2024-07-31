import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog,QMessageBox
from frm_main import Ui_MainWindow
from dl_doiTenAnh import Ui_Dialog_DoiTenFile
from dl_tangGiamNhieu import Ui_Dialog_tg_Nhieu
from dl_doiDinhDang_ui import Ui_Dialog_Doi_Dinh_Dang
from dl_chuanHoaAnh_ui import Ui_Dialog_Chuan_Hoa
from dl_doiHeMau_ui import Ui_Dialog_Doi_He_Mau
from dl_doiKichCoAnh_ui import Ui_Dialog_Doi_Co_Anh
from dl_TGSang_ui import Ui_Dialog_TG_Sang
from dl_tangGiamTuongPhan_ui import Ui_Dialog_Tang_Giam_TP
from dl_giamDungLuong_ui import Ui_Dialog_Giam_Dung_Luong
from dl_tangGiamDoNetAnh_ui import Ui_Dialog_Dieu_Chinh_Do_Net
from dl_thuPhongAnh_ui import Ui_Dialog_Thu_Phong_Anh
from dl_xoayAnh_ui import Ui_Dialog_Xoay_Anh


import tienIch

# Khai báo biến toàn cục
global_folder_path = ""

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        clear_screen()
        self.setupUi(self)
        self.dialog_ui_DoiTenFile = Ui_Dialog_DoiTenFile()
        self.dialog_ui_TGNhieu = Ui_Dialog_tg_Nhieu()
        self.dialog_ui_DoiDinhDang = Ui_Dialog_Doi_Dinh_Dang()
        self.dialog_ui_ChuanHoa = Ui_Dialog_Chuan_Hoa()
        self.dialog_ui_DoiHeMau = Ui_Dialog_Doi_He_Mau()
        self.dialog_ui_DoiCoAnh = Ui_Dialog_Doi_Co_Anh()
        self.dialog_ui_TangGiamSang = Ui_Dialog_TG_Sang()
        self.dialog_ui_TangGiamTP = Ui_Dialog_Tang_Giam_TP()
        self.dialog_ui_GiamDungLuong = Ui_Dialog_Giam_Dung_Luong()
        self.dialog_ui_DieuChinhNet = Ui_Dialog_Dieu_Chinh_Do_Net()
        self.dialog_ui_ThuPhongAnh = Ui_Dialog_Thu_Phong_Anh()
        self.dialog_ui_XoayAnh = Ui_Dialog_Xoay_Anh()


        # Xử lý logic ở đây
        self.btn_chonThuMucAnh.clicked.connect(self.handle_chonThuMucAnh)
        # Mở dialog dl_doiTenAnh_ui.py
        self.btn_doiTenFile.clicked.connect(self.handle_moDialogDoiTen)
        self.btn_tangGiamNhieu.clicked.connect(self.handle_moDialogTGNhieu)
        self.btn_doiDinhDang.clicked.connect(self.handle_moDialogDoiDinhDang)
        self.btn_chuanHoaAnh.clicked.connect(self.handle_moDialogChuanHoa)
        self.btn_doiHeMau.clicked.connect(self.handle_moDialogDoiHeMau)
        self.btn_doiCoAnh.clicked.connect(self.handle_moDialogDoiCoAnh)
        self.btn_tangGiamSang.clicked.connect(self.handle_moDialogTGSang)
        self.btn_tangGiamTuongPhan.clicked.connect(self.handle_moDialogTangGiamTP)
        self.btn_giamDungLuongAnh.clicked.connect(self.handle_moDialogGiamDungLuong)
        self.btn_tangGiamNet.clicked.connect(self.handle_moDialogDieuChinhNet)
        self.btn_thuPhongAnh.clicked.connect(self.handle_moDialogThuPhongAnh)
        self.btn_xoaiNghienAnh.clicked.connect(self.handle_moDialogXoayNghienAnh)

    def handle_chonThuMucAnh(self):
        global global_folder_path
        folder_path = QFileDialog.getExistingDirectory(self, "Chọn thư mục ảnh", "../")
        if folder_path:
            num_images = tienIch.count_images_in_directory(folder_path)
            self.lb_soAnh.setText(str(num_images))
            self.lb_dongDanThuMuc.setText(folder_path)
            global_folder_path = folder_path
    
    
    def handle_moDialogTGNhieu(self):
        if not global_folder_path:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        # Tạo một đối tượng dialog mới
        dialog = QDialog(self)
        # Thiết lập giao diện cho dialog và truyền global_folder_path vào
        self.dialog_ui_TGNhieu.setupUi(dialog, global_folder_path)
        # Hiển thị dialog
        dialog.exec_()
        
    def handle_moDialogDoiDinhDang(self):
        if not global_folder_path:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        dialog = QDialog(self)
        self.dialog_ui_DoiDinhDang.setupUi(dialog, global_folder_path)
        dialog.exec_()
        
    def handle_moDialogDoiTen(self):
        if not global_folder_path:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        # Tạo một đối tượng dialog mới
        dialog = QDialog(self)
        # Thiết lập giao diện cho dialog và truyền global_folder_path vào
        self.dialog_ui_DoiTenFile.setupUi(dialog, global_folder_path)
        # Hiển thị dialog
        dialog.exec_()
        
    def handle_moDialogChuanHoa(self):
        if not global_folder_path:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        # Tạo một đối tượng dialog mới
        dialog = QDialog(self)
        # Thiết lập giao diện cho dialog và truyền global_folder_path vào
        self.dialog_ui_ChuanHoa.setupUi(dialog, global_folder_path)
        # Hiển thị dialog
        dialog.exec_()
        
    def handle_moDialogDoiHeMau(self):
        if not global_folder_path:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        # Tạo một đối tượng dialog mới
        dialog = QDialog(self)
        # Thiết lập giao diện cho dialog và truyền global_folder_path vào
        self.dialog_ui_DoiHeMau.setupUi(dialog, global_folder_path)
        # Hiển thị dialog
        dialog.exec_()
        
    def handle_moDialogDoiCoAnh(self):
        if not global_folder_path:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        # Tạo một đối tượng dialog mới
        dialog = QDialog(self)
        # Thiết lập giao diện cho dialog và truyền global_folder_path vào
        self.dialog_ui_DoiCoAnh.setupUi(dialog, global_folder_path)
        # Hiển thị dialog
        dialog.exec_()
        
    def handle_moDialogTGSang(self):
        if not global_folder_path:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        # Tạo một đối tượng dialog mới
        dialog = QDialog(self)
        # Thiết lập giao diện cho dialog và truyền global_folder_path vào
        self.dialog_ui_TangGiamSang.setupUi(dialog, global_folder_path)
        # Hiển thị dialog
        dialog.exec_()
        
    def handle_moDialogTangGiamTP(self):
        if not global_folder_path:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        # Tạo một đối tượng dialog mới
        dialog = QDialog(self)
        # Thiết lập giao diện cho dialog và truyền global_folder_path vào
        self.dialog_ui_TangGiamTP.setupUi(dialog, global_folder_path)
        # Hiển thị dialog
        dialog.exec_()
        
    def handle_moDialogGiamDungLuong(self):
        if not global_folder_path:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        # Tạo một đối tượng dialog mới
        dialog = QDialog(self)
        # Thiết lập giao diện cho dialog và truyền global_folder_path vào
        self.dialog_ui_GiamDungLuong.setupUi(dialog, global_folder_path)
        # Hiển thị dialog
        dialog.exec_()        
    
    def handle_moDialogDieuChinhNet(self):
        if not global_folder_path:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        # Tạo một đối tượng dialog mới
        dialog = QDialog(self)
        # Thiết lập giao diện cho dialog và truyền global_folder_path vào
        self.dialog_ui_DieuChinhNet.setupUi(dialog, global_folder_path)
        # Hiển thị dialog
        dialog.exec_()
                    
    def handle_moDialogThuPhongAnh(self):
        if not global_folder_path:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        # Tạo một đối tượng dialog mới
        dialog = QDialog(self)
        # Thiết lập giao diện cho dialog và truyền global_folder_path vào
        self.dialog_ui_ThuPhongAnh.setupUi(dialog, global_folder_path)
        # Hiển thị dialog
        dialog.exec_()
        
    def handle_moDialogXoayNghienAnh(self):
        if not global_folder_path:
            # Hiển thị cảnh báo
            QMessageBox.information(None, "Cảnh báo", "Vui lòng chọn thư mục chứa ảnh trước khi tiếp tục!")
            return
        # Tạo một đối tượng dialog mới
        dialog = QDialog(self)
        # Thiết lập giao diện cho dialog và truyền global_folder_path vào
        self.dialog_ui_XoayAnh.setupUi(dialog, global_folder_path)
        # Hiển thị dialog
        dialog.exec_()        
                
def clear_screen():
        # Xóa màn hình trên Windows
        if os.name == 'nt':
            os.system('cls')
        # Xóa màn hình trên Linux hoặc macOS
        else:
            os.system('clear')
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
