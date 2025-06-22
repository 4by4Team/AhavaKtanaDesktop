from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QMessageBox, QFileDialog, QCheckBox, QTableWidget,
    QTableWidgetItem, QHeaderView
)
from PyQt6.QtCore import Qt

class ConvertExcelPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.load_btn = QPushButton("\ud83d\udcc1 Load Excel File")
        self.load_btn.setToolTip("Select an Excel file to load")
        self.load_btn.clicked.connect(self.load_excel)

        self.table = QTableWidget()
        self.table.setColumnCount(0)

        self.update_btn = QPushButton("\u270f\ufe0f Update Selected Rows")
        self.update_btn.setToolTip("Apply updates to selected rows")
        self.update_btn.clicked.connect(self.update_rows)

        layout.addWidget(self.load_btn)
        layout.addWidget(self.table)
        layout.addWidget(self.update_btn)

        self.setLayout(layout)

    def load_excel(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Excel File", filter="Excel Files (*.xlsx *.xls)")
        if file:
            # TODO: קריאה לפונקציה שלך
            self.populate_table([{"dbId": 1, "name": "Test", "status": "Ready"}])

    def populate_table(self, data: list[dict]):
        if not data:
            return

        headers = list(data[0].keys())
        self.table.setColumnCount(len(headers) + 1)
        self.table.setRowCount(len(data))
        self.table.setHorizontalHeaderLabels(headers + ["Select"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for row_idx, row in enumerate(data):
            for col_idx, key in enumerate(headers):
                item = QTableWidgetItem(str(row[key]))
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(row_idx, col_idx, item)
            chk = QCheckBox()
            self.table.setCellWidget(row_idx, len(headers), chk)

    def update_rows(self):
        QMessageBox.information(self, "Updated", "Rows updated successfully")
