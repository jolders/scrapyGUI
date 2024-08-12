import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Stylesheet option disengaged at the moment
    # with open("style.css", "r") as file:
    #     app.setStyleSheet(file.read())
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
