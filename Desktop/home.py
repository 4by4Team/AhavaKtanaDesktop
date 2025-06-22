from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class HomePage(QWidget):
    def __init__(self, switch_to_create_callback, switch_to_convert_callback):
        super().__init__()
        self.switch_create = switch_to_create_callback
        self.switch_convert = switch_to_convert_callback
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn1 = QPushButton("\ud83d\udcc4 Create Excel from API")
        btn1.setIcon(QIcon.fromTheme("fa-solid fa-file-import"))
        btn1.setToolTip("Create new Excel files using API data")
        btn1.clicked.connect(self.switch_create)

        btn2 = QPushButton("\ud83d\udd04 Convert & Update Excel")
        btn2.setIcon(QIcon.fromTheme("fa-solid fa-file-export"))
        btn2.setToolTip("Upload, update and convert Excel files")
        btn2.clicked.connect(self.switch_convert)

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)