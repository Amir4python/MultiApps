from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("App 1 !")

    label = QLabel(win)
    label.setText("PYQT 5")
    label.move(50, 50)

    win.show()
    sys.exit(app.exec_())
 