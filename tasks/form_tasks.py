import os
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from tasks import crud_tasks as crud
import utils


class FormTasks(QWidget):
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "tasks.ui")
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
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setHorizontalHeaderLabels(
                [
                    "Id",
                    "Title",
                    "Description",
                    "Status",
                    "Due Date",
                    "User Id",
                    "Project Id",
                ]
            )

            for row, tasks in enumerate(data):
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(tasks["id"])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(tasks["title"] or ""))
                self.tableWidget.setItem(
                    row, 2, QTableWidgetItem(tasks["description"] or "")
                )
                self.tableWidget.setItem(
                    row, 3, QTableWidgetItem(tasks["status"] or "")
                )
                self.tableWidget.setItem(
                    row,
                    4,
                    QTableWidgetItem(
                        str(tasks["due_date"]) if tasks["due_date"] else ""
                    ),
                )
                self.tableWidget.setItem(
                    row, 5, QTableWidgetItem(str(tasks["user_id"]))
                )
                self.tableWidget.setItem(
                    row, 6, QTableWidgetItem(str(tasks["project_id"]))
                )

    def get_data_from_table(self, row, column):
        try:
            id_item = self.tableWidget.item(row, 0)
            self.old_id = id_item.text()

            self.lineEdit_id.setText(self.tableWidget.item(row, 0).text())
            self.lineEdit_title.setText(self.tableWidget.item(row, 1).text())
            self.lineEdit_description.setText(self.tableWidget.item(row, 2).text())
            self.lineEdit_status.setText(self.tableWidget.item(row, 3).text())
            self.lineEdit_dueDate.setText(self.tableWidget.item(row, 4).text())
            self.lineEdit_userId.setText(self.tableWidget.item(row, 5).text())
            self.lineEdit_projectId.setText(self.tableWidget.item(row, 6).text())
        except Exception as e:
            print(f"Error ambil data: {e}")

    def handle_simpan(self):
        id = self.lineEdit_id.text()
        title = self.lineEdit_title.text()
        description = self.lineEdit_description.text()
        status = self.lineEdit_status.text()
        dueDate = self.lineEdit_dueDate.text()
        userId = self.lineEdit_userId.text()
        projectId = self.lineEdit_projectId.text()

        if not id or not title or not userId or not projectId:
            QMessageBox.warning(
                self, "Warning", "ID, Title, User ID, dan Project ID wajib diisi!"
            )
            return

        success, msg = crud.simpan_data(
            id, title, description, status, dueDate, userId, projectId
        )
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
        title = self.lineEdit_title.text()
        description = self.lineEdit_description.text()
        status = self.lineEdit_status.text()
        dueDate = self.lineEdit_dueDate.text()
        userId = self.lineEdit_userId.text()
        projectId = self.lineEdit_projectId.text()

        if not new_id or not title or not userId or not projectId:
            QMessageBox.warning(self, "Warning", "Data vital tidak boleh kosong!")
            return

        success, msg = crud.ubah_data(
            self.old_id, new_id, title, description, status, dueDate, userId, projectId
        )
        if success:
            QMessageBox.information(self, "Sukses", msg)
            self.tampilkan_data()
            self.clear_inputs()
        else:
            QMessageBox.critical(self, "Gagal", msg)

    def handle_hapus(self):
        if not self.old_id:
            QMessageBox.warning(self, "Warning", "Pilih data yang mau dihapus!")
            return

        reply = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Hapus task ID {self.old_id}?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            success, msg = crud.hapus_data(self.old_id)
            if success:
                QMessageBox.information(self, "Sukses", msg)
                self.tampilkan_data()
                self.clear_inputs()
            else:
                QMessageBox.critical(self, "Gagal", msg)

    def handle_cetak(self):
        utils.export_table_to_pdf(self.tableWidget, "Data Tasks", self)

    def clear_inputs(self):
        self.lineEdit_id.clear()
        self.lineEdit_title.clear()
        self.lineEdit_description.clear()
        self.lineEdit_status.clear()
        self.lineEdit_dueDate.clear()
        self.lineEdit_userId.clear()
        self.lineEdit_projectId.clear()
        self.old_id = None
