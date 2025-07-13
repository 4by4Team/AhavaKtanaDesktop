from csv import excel

from PyQt6.QtGui import QIcon, QMovie
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QMessageBox, QFileDialog, QCheckBox, QTableWidget,
    QTableWidgetItem, QHeaderView, QHBoxLayout, QLabel
)
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from excel.excel_data import excel_to_dict
from excel.excel_to_json import excel_to_filtered_json, convert_excel_to_json
from helper.paths import resource_path
class ConvertExcelPage(QWidget):
    def __init__(self):
        super().__init__()
        self.excel_path = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        top_buttons_layout = QHBoxLayout()

        self.title_label = QLabel("המרת קובץ אקסל לקובץ JSON")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 25px; font-weight: bold; color: #008080;")

        self.gif_label = QLabel()
        self.movie = QMovie(resource_path("assets/gif/left-arrow.gif"))
        self.gif_label.setMovie(self.movie)
        self.gif_label.setFixedSize(50, 50)
        self.movie.setScaledSize(QSize(50, 50))
        self.gif_label.setToolTip("חזרה לעמוד הקודם")
        self.gif_label.mousePressEvent = self.go_back
        self.movie.start()

        self.gif_folder=QLabel()
        self.movie_folder = QMovie(resource_path("assets/gif/folder.gif"))
        self.gif_folder.setMovie(self.movie_folder)
        self.gif_folder.setFixedSize(50, 50)
        self.movie_folder.setScaledSize(QSize(50, 50))
        self.gif_folder.setToolTip("בחר קובץ אקסל")
        self.gif_folder.mousePressEvent = self.load_excel
        self.movie_folder.start()

        top_buttons_layout.addWidget(self.gif_label)
        top_buttons_layout.addStretch()
        top_buttons_layout.addWidget(self.title_label)
        top_buttons_layout.addStretch()
        top_buttons_layout.addWidget(self.gif_folder)

        self.empty_label = QLabel("לא נבחר קובץ")
        self.empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.empty_label.setStyleSheet("color: gray; font-size: 20px;")

        self.table = QTableWidget()

        self.convert_to_filter_btn = QPushButton(" Convert Excel file to Filter Json")
        self.convert_to_filter_btn.setIcon(QIcon("../assets/icons/document.png"))
        self.convert_to_filter_btn.clicked.connect(self.convert_to_filtered_json)

        self.convert_to_josn_btn = QPushButton(" Convert Excel file to Json")
        self.convert_to_josn_btn.setIcon(QIcon("../assets/icons/document.png"))
        self.convert_to_josn_btn.clicked.connect(self.convert_to_json)

        layout.addLayout(top_buttons_layout)
        layout.addWidget(self.empty_label)
        layout.addWidget(self.table)
        layout.addWidget(self.convert_to_filter_btn)
        layout.addWidget(self.convert_to_josn_btn)
        self.table.hide()  # טבלה מוסתרת עד שיהיה מידע

        self.setLayout(layout)

    go_back_requested = pyqtSignal()
    def load_excel(self, event):
        self.excel_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", filter="Excel Files (*.xlsx *.xls)")
        if self.excel_path:
            try:
                data = excel_to_dict(self.excel_path)
                self.populate_table(data)
            except Exception as e:
                QMessageBox.critical(self, "שגיאה", f"שגיאה בטעינת הקובץ:\n{e}")

    def populate_table(self, data: list[dict]):
        if not data:
            self.table.hide()
            self.empty_label.show()
            return

        self.empty_label.hide()
        self.table.show()

        headers = list(data[0].keys())
        self.table.clear()
        self.table.setColumnCount(len(headers))
        self.table.setRowCount(len(data))
        self.table.setHorizontalHeaderLabels(headers)

        for row_idx, row in enumerate(data):
            for col_idx, key in enumerate(headers):
                item = QTableWidgetItem(str(row[key]))
                item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(row_idx, col_idx, item)

        header = self.table.horizontalHeader()
        for col in range(len(headers)):
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.ResizeToContents)

    def convert_to_filtered_json(self):
        if not self.excel_path:
            QMessageBox.warning(self, "שגיאה", "לא נבחר קובץ אקסל")
            return
        try:
            data = excel_to_filtered_json(self.excel_path)
            if data:
                QMessageBox.information(self, "הצלחה", "✅ הקובץ הומר ונשמר בהצלחה")
            else:
                QMessageBox.warning(self, "שגיאה", "❌ ההמרה נכשלה – לא נוצרו נתונים")
        except Exception as e:
            QMessageBox.critical(self, "שגיאה", f"שגיאה בהמרה:\n{e}")


    def convert_to_json(self):
        if not self.excel_path:
            QMessageBox.warning(self, "שגיאה", "לא נבחר קובץ אקסל")
            return
        try:
            data = convert_excel_to_json(self.excel_path)
            if data:
                QMessageBox.information(self, "הצלחה", "✅ הקובץ הומר ונשמר בהצלחה")
            else:
                QMessageBox.warning(self, "שגיאה", "❌ ההמרה נכשלה – לא נוצרו נתונים")
        except Exception as e:
            QMessageBox.critical(self, "שגיאה", f"שגיאה בהמרה:\n{e}")


    def go_back(self, event):
        self.excel_path = None
        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.table.hide()
        self.empty_label.show()
        self.go_back_requested.emit()


