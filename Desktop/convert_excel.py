from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QMessageBox, QFileDialog, QCheckBox, QTableWidget,
    QTableWidgetItem, QHeaderView, QHBoxLayout
)
from PyQt6.QtCore import Qt


class ConvertExcelPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        top_buttons_layout = QHBoxLayout()

        self.back_btn = QPushButton("⬅️ חזרה")
        self.back_btn.setFixedWidth(100)
        self.back_btn.clicked.connect(self.go_back)

        self.load_btn = QPushButton("📁 בחר קובץ אקסל")
        self.load_btn.setFixedHeight(40)
        self.load_btn.setFixedWidth(200)
        self.load_btn.clicked.connect(self.load_excel)

        top_buttons_layout.addWidget(self.back_btn)
        top_buttons_layout.addStretch()  # מוסיף רווח דינמי בין הכפתורים
        top_buttons_layout.addWidget(self.load_btn)

        self.select_all_checkbox = QCheckBox("בחר/י את כל השורות")
        self.select_all_checkbox.stateChanged.connect(self.toggle_all_checkboxes)

        self.table = QTableWidget()

        self.update_btn = QPushButton("✏️ עדכן נתונים")
        self.update_btn.clicked.connect(self.update_rows)


        layout.addLayout(top_buttons_layout)
        layout.addWidget(self.table)
        layout.addWidget(self.select_all_checkbox)
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
                item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(row_idx, col_idx, item)
            chk = QCheckBox()
            self.table.setCellWidget(row_idx, len(headers), chk)

    def update_rows(self):
        QMessageBox.information(self, "Updated", "Rows updated successfully")


    def go_back(self):
        # כאן צרי callback בעתיד למעבר בין עמודים
        self.close()  # או emit signal

    def toggle_all_checkboxes(self, state):
        for row in range(self.table.rowCount()):
            checkbox = self.table.cellWidget(row, self.table.columnCount() - 1)
            if checkbox:
                checkbox.setChecked(state == Qt.CheckState.Checked)
