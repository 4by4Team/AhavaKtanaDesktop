from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel, QSpacerItem, QSizePolicy, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap

class LoginPage(QWidget):
    def __init__(self, switch_to_main_callback):
        super().__init__()
        self.switch_to_main = switch_to_main_callback
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #1b2a41;")

        self.setFont(QFont("Segoe UI", 12))

        container = QFrame()
        container.setMaximumSize(500, 500)
        container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                padding: 20px;
            }
        """)
        container_layout = QVBoxLayout()
        container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # לוגו
        logo = QLabel()
        pixmap = QPixmap("../assets/logo.jpg")
        pixmap = pixmap.scaledToHeight(60, Qt.TransformationMode.SmoothTransformation)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        container_layout.addWidget(logo)


        title_label = QLabel("LOGIN TO YOUR ACCOUNT")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; margin: 3px; color: #222;")
        container_layout.addWidget(title_label)

        # שדות
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

        # הוספת רכיבים לתוך הקופסה
        for widget in [
            self.username_input, self.password_input, self.login_btn,
            self.code_input, self.confirm_btn
        ]:
            widget.setMinimumWidth(250)
            widget.setMaximumWidth(300)
            widget.setFixedHeight(40)
            widget.setStyleSheet("""
                QLineEdit, QPushButton {
                    font-size: 14px;
                    border-radius: 8px;
                }
                QPushButton {
                    background-color: #ef6c57;
                    color: white;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #d6523b;
                }
                QPushButton:pressed {
                    background-color: #bf3d28;
                }
            """)
            container_layout.addWidget(widget)
            container_layout.addSpacing(10)

        container.setLayout(container_layout)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
