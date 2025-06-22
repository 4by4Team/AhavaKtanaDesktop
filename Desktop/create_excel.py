from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QFileDialog, QDateEdit, QMessageBox
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QDate

class CreateExcelPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.product_select = QComboBox()
        self.product_select.addItems(["Product A", "Product B", "Product C"])

        self.order_status_select = QComboBox()
        self.order_status_select.addItems(["Ready", "Not Ready"])

        self.graphic_status_select = QComboBox()
        self.graphic_status_select.addItems(["Approved", "Rejected", "In Process"])

        self.date_picker = QDateEdit()
        self.date_picker.setCalendarPopup(True)
        self.date_picker.setDate(QDate.currentDate())

        self.path_button = QPushButton("Select Folder")
        self.path_button.setIcon(QIcon.fromTheme("fa-solid fa-folder-open"))
        self.path_button.clicked.connect(self.select_folder)

        self.path_label = QLabel("No path selected")

        self.submit_btn = QPushButton("\ud83d\udd04 Generate Excel Files")
        self.submit_btn.setToolTip("Generate files based on the selected criteria")
        self.submit_btn.clicked.connect(self.generate_excels)

        for w in [QLabel("Select Product:"), self.product_select,
                  QLabel("Order Status:"), self.order_status_select,
                  QLabel("Graphic Status:"), self.graphic_status_select,
                  QLabel("Date:"), self.date_picker,
                  self.path_button, self.path_label, self.submit_btn]:
            layout.addWidget(w)

        self.setLayout(layout)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder:
            self.path_label.setText(folder)

    def generate_excels(self):
        # TODO: קריאה ל-API + שמירת אקסלים
        QMessageBox.information(self, "Done", "Excel files created successfully")

