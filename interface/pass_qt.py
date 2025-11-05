import sys
import os
import qdarktheme
from about import About
from pass_interface import Pass

from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from move_button import MoveButton

import pyrebase


# pyrebase config
config = {
    # # Start of Original
    # "apiKey": "AIzaSyDAleM7TLeMWddKrGIrQYe8zS0bWjdeCDw",
    # "authDomain": "dialogflowcx-test-tpk.firebaseapp.com",
    # "databaseURL": "https://dialogflowcx-test-tpk-default-rtdb.firebaseio.com",
    # "storageBucket": "dialogflowcx-test-tpk.appspot.com"
    # # End of Original
    # Start of Modification by FY
    "apiKey": "AIzaSyB5X2MKtUIiNecy-768pslZ9XADiRpo4jw",
    "authDomain": "passexperiment-bfa25.firebaseapp.com",
    "databaseURL": "https://passexperiment-bfa25.firebaseio.com",
    "storageBucket": "passexperiment-bfa25.appspot.com"
    # End of Modification by FY
    # this works without the serviceAccount credential so ?
    #"serviceAccount": r"/home/rob/Downloads/passexperiment-bfa25-firebase-adminsdk-7ljxj-2145fbcabf.json"
}

# initialze pyrebase
fb = pyrebase.initialize_app(config)
db = fb.database()

class Window(QMainWindow):
    def __init__(self, user, auth):
        super().__init__()
        self.setWindowTitle("PASS Assessment")
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.user = user
        self.auth = auth

        #set view mode (i'm just having fun at this point)
        # self.setStyleSheet(qdarktheme.load_stylesheet("light"))
        with open(os.path.join("assets", "light"), "r") as lightFile:
            self.setStyleSheet(lightFile.read())
        self.currMode = 'l'

        #create widgets for stacking
        pass_widget = Pass(self.user, self.auth)
        about_widget = About()

        #add widgets to stack
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(pass_widget)
        self.Stack.addWidget(about_widget)
        self.Stack.setCurrentIndex(0)

        #set view toggle
        view_toggle = QPushButton("Change View Mode")
        view_toggle.clicked.connect(lambda: self.changeViewMode())

        #set spacer
        spacer = QToolBar()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        spacer.setVisible(True)

        #set actions
        pass_action = QAction("PASS",self)
        about_action = QAction("About",self)
        pass_action.triggered.connect(lambda: self.Stack.setCurrentIndex(0))
        about_action.triggered.connect(lambda: self.Stack.setCurrentIndex(1))
        
        #set up toolbar here (trying to avoid menu dropdown because it's ugly)
        tool_bar = self.addToolBar("Navbar")
        tool_bar.addAction(pass_action)
        tool_bar.addAction(about_action)
        tool_bar.addWidget(spacer)
        tool_bar.addWidget(view_toggle)
        tool_bar.setMovable(False)

        #add stack to page
        widget = QWidget()
        grid = QGridLayout()
        grid.addWidget(self.Stack)
        grid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        widget.setLayout(grid)
        self.setCentralWidget(widget)
    
    def changeViewMode(self):
        if(self.currMode == 'l'):
            self.setStyleSheet(qdarktheme.load_stylesheet("dark"))
            self.currMode = 'd'
        elif(self.currMode == 'd'):
            self.setStyleSheet(qdarktheme.load_stylesheet("light"))
            self.currMode = 'l'
            
if __name__ == "__main__":
    # login
    if(len(sys.argv) != 3):
        print('usage: python pass_qt.py email password')
        exit()
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    print(sys.argv[1], sys.argv[2])
    try:
        user = auth.sign_in_with_email_and_password(sys.argv[1], sys.argv[2])
    except Exception as e:
        print(e)
        print('Invalid email or password! Try again.')
        exit()


    app = QApplication(sys.argv)
    window = Window(user, auth)
    window.setMinimumWidth(600)
    window.show()
    sys.exit(app.exec())
