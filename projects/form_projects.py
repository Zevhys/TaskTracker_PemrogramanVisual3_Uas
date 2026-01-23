import os
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from projects import crud_projects as crud
import utils


class FormProjects(QWidget):
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "projects.ui")
        uic.loadUi(ui_path, self)
        self.old_id = None
        self.initUI()

    def initUI(self):
        self.pushButton_7.clicked.connect(self.handle_simpan)
        self.pushButton_8.clicked.connect(self.handle_ubah)
        self.pushButton_9.clicked.connect(self.handle_hapus)

        if hasattr(self, "pushButton_cetak"):
            self.pushButton_cetak.clicked.connect(self.handle_cetak)

        self.tableWidget.cellClicked.connect(self.get_data_from_table)
        self.tampilkan_data()

    def tampilkan_data(self):
        success, data = crud.load_data()
        if success:
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "User ID"])

            for row, project in enumerate(data):
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(project["id"])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(project["name"]))
                self.tableWidget.setItem(
                    row, 2, QTableWidgetItem(str(project["user_id"]))
                )

    def get_data_from_table(self, row, column):
        try:
            id_item = self.tableWidget.item(row, 0)
            self.old_id = id_item.text()

            self.lineEdit_id.setText(self.tableWidget.item(row, 0).text())
            self.lineEdit_name.setText(self.tableWidget.item(row, 1).text())
            self.lineEdit_userId.setText(self.tableWidget.item(row, 2).text())
        except Exception as e:
            print(f"Error ambil data: {e}")

    def handle_simpan(self):
        id = self.lineEdit_id.text()
        name = self.lineEdit_name.text()
        user_id = self.lineEdit_userId.text()

        if not id or not name:
            QMessageBox.warning(self, "Warning", "ID dan Name wajib diisi!")
            return

        success, msg = crud.simpan_data(id, name, user_id)
        if success:
            QMessageBox.information(self, "Sukses", msg)
            self.tampilkan_data()
            self.clear_inputs()
        else:
            QMessageBox.critical(self, "Gagal", msg)

    def handle_ubah(self):
        if not self.old_id:
            QMessageBox.warning(self, "Warning", "Klik data di tabel dulu!")
            return

        new_id = self.lineEdit_id.text()
        name = self.lineEdit_name.text()
        user_id = self.lineEdit_userId.text()

        success, msg = crud.ubah_data(self.old_id, new_id, name, user_id)
        if success:
            QMessageBox.information(self, "Sukses", msg)
            self.tampilkan_data()
            self.clear_inputs()

    def handle_hapus(self):
        if not self.old_id:
            QMessageBox.warning(self, "Warning", "Pilih data yang mau dihapus!")
            return

        reply = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Hapus ID {self.old_id}?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            success, msg = crud.hapus_data(self.old_id)
            if success:
                QMessageBox.information(self, "Sukses", msg)
                self.tampilkan_data()
                self.clear_inputs()

    def handle_cetak(self):
        utils.export_table_to_pdf(self.tableWidget, "Data Projects", self)

    def clear_inputs(self):
        self.lineEdit_id.clear()
        self.lineEdit_name.clear()
        self.lineEdit_userId.clear()
        self.old_id = None
