from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QTextDocument


def export_table_to_pdf(table_widget, title_text, parent_widget):
    filename, _ = QFileDialog.getSaveFileName(
        parent_widget, "Simpan PDF", "", "PDF Files (*.pdf)"
    )

    if filename:
        try:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(filename)
            printer.setPageSize(QPrinter.A4)

            rows = table_widget.rowCount()
            columns = table_widget.columnCount()

            html = f"""
            <h1 style="text-align: center; font-family: Arial;">Laporan {title_text}<br></h1>
            <table border="1" cellspacing="0" cellpadding="5" style="width: 100%; border-collapse: collapse; font-family: Arial; font-size: 10pt;">
                <thead>
                    <tr style="background-color: #f2f2f2;">
            """

            for col in range(columns):
                header_item = table_widget.horizontalHeaderItem(col)
                header_text = header_item.text() if header_item else f"Col {col}"
                html += f"<th>{header_text}</th>"
            html += "</tr></thead><tbody>"

            for row in range(rows):
                html += "<tr>"
                for col in range(columns):
                    item = table_widget.item(row, col)
                    cell_text = item.text() if item else ""
                    html += f"<td>{cell_text}</td>"
                html += "</tr>"

            html += "</tbody></table>"

            from datetime import datetime

            now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            html += f"<p style='text-align: left; font-size: 8pt; margin-top: 20px;'>Dicetak pada: {now}</p>"

            document = QTextDocument()
            document.setHtml(html)
            document.print_(printer)

            QMessageBox.information(
                parent_widget, "Sukses", f"Laporan berhasil disimpan ke:\n{filename}"
            )

        except Exception as e:
            QMessageBox.critical(parent_widget, "Error", f"Gagal mencetak PDF: {e}")
