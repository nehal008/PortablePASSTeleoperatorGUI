"""
about page with information about assessment
"""

from PyQt6.QtWidgets import * 
from PyQt6 import QtCore, QtGui
import sys

class About(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Page")
        self.setGeometry(500, 200, 400, 300)
        self.UiComponents()
        self.show()
  
    # method for widgets
    def UiComponents(self):

        #form layout for first two rows
        layout = QVBoxLayout()
        upper_layout = QVBoxLayout()
        layout.addLayout(upper_layout)
        
        #title/intro blurb for about page
        title = QLabel("About the PASS Assessment")
        title.setFont(QtGui.QFont("Calibri", 20))
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        upper_layout.addWidget(title)
        
        #add widgets, configure, and set layout
        self.setLayout(layout)

if __name__ == "__main__"   :
    App = QApplication(sys.argv)
    window = About()
    sys.exit(App.exec())

  