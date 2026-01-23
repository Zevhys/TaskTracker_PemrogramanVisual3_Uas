import os
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from task_tags import crud_task_tags as crud
import utils


class FormTaskTags(QWidget):
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "task_tags.ui")
        uic.loadUi(ui_path, self)
        self.old_task_id = None
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
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(["Task Id", "Tag Id"])

            for row, taskTags in enumerate(data):
                self.tableWidget.setItem(
                    row, 0, QTableWidgetItem(str(taskTags["task_id"]))
                )
                self.tableWidget.setItem(
                    row, 1, QTableWidgetItem(str(taskTags["tag_id"]))
                )

    def get_data_from_table(self, row, column):
        try:
            task_id_item = self.tableWidget.item(row, 0)
            tag_id_item = self.tableWidget.item(row, 1)
            self.old_task_id = task_id_item.text()
            self.lineEdit_taskId.setText(task_id_item.text())
            self.lineEdit_tagId.setText(tag_id_item.text())
        except Exception as e:
            print(f"Error ambil data: {e}")

    def handle_simpan(self):
        task_id = self.lineEdit_taskId.text()
        tag_id = self.lineEdit_tagId.text()

        if not tag_id or not task_id:
            QMessageBox.warning(self, "Warning", "Tag Id dan Task Id wajib diisi!")
            return

        success, msg = crud.simpan_data(task_id, tag_id)
        if success:
            QMessageBox.information(self, "Sukses", msg)
            self.tampilkan_data()
            self.clear_inputs()
        else:
            QMessageBox.critical(self, "Gagal", msg)

    def handle_ubah(self):
        if not self.old_task_id:
            QMessageBox.warning(self, "Warning", "Klik data di tabel dulu!")
            return

        new_task_id = self.lineEdit_taskId.text()
        new_tag_id = self.lineEdit_tagId.text()

        success, msg = crud.ubah_data(self.old_task_id, new_task_id, new_tag_id)
        if success:
            QMessageBox.information(self, "Sukses", msg)
            self.tampilkan_data()
            self.clear_inputs()
        else:
            QMessageBox.critical(self, "Gagal", msg)

    def handle_hapus(self):
        if not self.old_task_id:
            QMessageBox.warning(self, "Warning", "Pilih data yang mau dihapus!")
            return

        reply = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Hapus Task ID {self.old_task_id}?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            success, msg = crud.hapus_data(self.old_task_id)
            if success:
                QMessageBox.information(self, "Sukses", msg)
                self.tampilkan_data()
                self.clear_inputs()
            else:
                QMessageBox.critical(self, "Gagal", msg)

    def handle_cetak(self):
        utils.export_table_to_pdf(self.tableWidget, "Data Task Tags", self)

    def clear_inputs(self):
        self.lineEdit_taskId.clear()
        self.lineEdit_tagId.clear()
        self.old_task_id = None
