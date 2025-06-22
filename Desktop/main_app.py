import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget
from PyQt6.QtGui import QFont, QIcon
from Desktop.login import LoginPage
from Desktop.home import HomePage
from Desktop.create_excel import CreateExcelPage
from Desktop.convert_excel import ConvertExcelPage

def load_styles(app):
    with open("../assets/style.qss", "r") as f:
        app.setStyleSheet(f.read())

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.login_page = LoginPage(self.show_home)
        self.home_page = HomePage(self.show_create_excel, self.show_convert_excel)
        self.create_excel_page = CreateExcelPage()
        self.convert_excel_page = ConvertExcelPage()
        for w in (self.login_page, self.home_page, self.create_excel_page, self.convert_excel_page):
            w.setFont(QFont("Segoe UI", 11))
        self.addWidget(self.login_page)
        self.addWidget(self.home_page)
        self.addWidget(self.create_excel_page)
        self.addWidget(self.convert_excel_page)
        self.setCurrentWidget(self.login_page)

    def show_home(self):
        self.setCurrentWidget(self.home_page)
    def show_create_excel(self):
        self.setCurrentWidget(self.create_excel_page)
    def show_convert_excel(self):
        self.setCurrentWidget(self.convert_excel_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    load_styles(app)
    main_app = MainApp()
    main_app.setWindowIcon(QIcon("../assets/logo.jpg"))  # ← שים כאן את הלוגו שלך
    main_app.setWindowTitle("Excel Automation Suite – Ahavaktana Style")
    main_app.resize(900, 650)
    main_app.show()
    sys.exit(app.exec())
