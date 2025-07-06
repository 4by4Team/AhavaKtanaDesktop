from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel, QSpacerItem, QSizePolicy, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from helper.paths import resource_path

class LoginPage(QWidget):
    def __init__(self, switch_to_main_callback):
        super().__init__()
        self.switch_to_main = switch_to_main_callback
        self.init_ui()

    def init_ui(self):

        self.setFont(QFont("Segoe UI", 12))

        container = QFrame()
        container.setMaximumSize(500, 500)
        container.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 2px solid #40E0D0;
                border-radius: 12px;
                padding: 20px;
            }
        """)
        container_layout = QVBoxLayout()
        container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        logo = QLabel()
        pixmap = QPixmap(resource_path("assets/logo.png"))
        pixmap = pixmap.scaledToHeight(60, Qt.TransformationMode.SmoothTransformation)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)


        title_label = QLabel("LOGIN TO YOUR ACCOUNT")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; margin: 3px; color: #008080;")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("User Name *")
        self.username_input.setToolTip("Enter your username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password *")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setToolTip("Enter your password")

        self.login_btn = QPushButton("LOGIN")
        self.login_btn.clicked.connect(self.reveal_code_input)

        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Enter verification code")
        self.code_input.setToolTip("Code sent to your email")
        self.code_input.setVisible(False)

        self.confirm_btn = QPushButton("CONFIRM")
        self.confirm_btn.setVisible(False)
        self.confirm_btn.clicked.connect(self.confirm_login)

        for widget in [
            self.username_input, self.password_input, self.login_btn,
            self.code_input, self.confirm_btn
        ]:
            widget.setMinimumWidth(250)
            widget.setMaximumWidth(300)
            widget.setFixedHeight(40)
            widget.setStyleSheet("")
            container_layout.addWidget(widget)
            container_layout.addSpacing(10)


        container.setLayout(container_layout)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(logo)
        main_layout.addWidget(title_label)

        main_layout.addWidget(container)

        self.setLayout(main_layout)


    def reveal_code_input(self):
        try:
            self.username_input.setVisible(False)
            self.password_input.setVisible(False)
            self.login_btn.setVisible(False)
            self.code_input.setVisible(True)
            self.confirm_btn.setVisible(True)
            QMessageBox.information(self, "Code Sent", "Verification code has been sent to your email.")
        except:
            QMessageBox.information(self, "Not valid user", "Try again – not valid details.")

    def confirm_login(self):
        self.switch_to_main()
