from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QMovie, QCursor
from PyQt6.QtCore import Qt, QSize
from helper.paths import resource_path


class HomePage(QWidget):
    def __init__(self, switch_to_create_callback, switch_to_convert_callback):
        super().__init__()
        self.switch_create = switch_to_create_callback
        self.switch_convert = switch_to_convert_callback
        self.init_ui()

    def create_gif_button(self, gif_path: str, text: str, callback):
        # וידג'ט חיצוני (הכפתור)
        outer_widget = QWidget()
        outer_widget.setFixedSize(300, 250)
        outer_widget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        outer_widget.setObjectName("gifButton")  # חשוב: מזהה CSS ייחודי

        # עיצוב למסגרת בלבד
        outer_widget.setStyleSheet("""
            #gifButton {
                background-color: white;
                border: 2px solid #008080;
                border-radius: 12px;
            }
        """)

        # פריסת עמודה למלבן כולו
        outer_layout = QVBoxLayout()
        outer_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        outer_layout.setSpacing(10)

        # תוכן פנימי – gif + טקסט
        gif_label = QLabel()
        gif_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        movie = QMovie(gif_path)
        movie.setScaledSize(QSize(64, 64))
        gif_label.setMovie(movie)
        movie.start()

        text_label = QLabel(text)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #008080;")

        outer_layout.addWidget(gif_label)
        outer_layout.addWidget(text_label)
        outer_widget.setLayout(outer_layout)

        # לחיצה על הכפתור
        outer_widget.mousePressEvent = lambda event: callback()

        return outer_widget

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(30)
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)


        btn1 = self.create_gif_button(resource_path("assets/gif/download.gif"), "Create Excel", self.switch_create)
        btn2 = self.create_gif_button(resource_path("assets/gif/copy.gif"), "Convert & Update", self.switch_convert)

        buttons_layout.addWidget(btn1)
        buttons_layout.addWidget(btn2)

        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)
