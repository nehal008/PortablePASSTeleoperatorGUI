import sys
from PyQt6.QtWidgets import * 
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import * 
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt

class ErrorPopup(QMessageBox):
    def __init__(self, error_text: str, *args, **kwargs):
        super(ErrorPopup, self).__init__(*args, **kwargs)

        self.setText(error_text)
        # self.setIcon(QMessageBox.)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    popup = QMessageBox.warning(None, "Error!", "ahhhhh")
    popup.show()
    sys.exit(App.exec())