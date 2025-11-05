import sys
from PyQt6.QtWidgets import * 
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import * 
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt

class InterventionSelectWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(InterventionSelectWidget, self).__init__(*args, **kwargs)
        gl = QGridLayout()
        self.setLayout(gl)
        buttons = []
        buttons.append(QPushButton("Reminder"))
        buttons.append(QPushButton("Information"))
        buttons.append(QPushButton("Chat"))
        buttons.append(QPushButton("Interrupt"))

        num_rows = 2
        num_cols = 2
        for i in range(num_rows):
            for j in range(num_cols):
                gl.addWidget(buttons[i * num_cols + j], i, j)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = InterventionSelectWidget()
    window.show()
    sys.exit(App.exec())