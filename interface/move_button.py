from PyQt6.QtWidgets import * 
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import * 
from PyQt6.QtCore import *
import sys
from enum import Enum
import time
from functools import partial

import pyrebase

# pyrebase config
config = {
    # # Start of Original
    # "apiKey": "AIzaSyDAleM7TLeMWddKrGIrQYe8zS0bWjdeCDw",
    # "authDomain": "dialogflowcx-test-tpk.firebaseapp.com",
    # "databaseURL": "https://dialogflowcx-test-tpk-default-rtdb.firebaseio.com",
    # "storageBucket": "dialogflowcx-test-tpk.appspot.com"
    # # # End of Original
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

class MoveButton(QWidget):
    def __init__(self, user, parent=None):
        
        #initialize widget
        super(MoveButton, self).__init__(parent)
        self.user = user
        self.setMaximumSize(250,250)
        self.__maxDistance = 100

        # navigation buttons
        navNames = [['Bedroom1', 'Bedroom2', 'HazCord'], 
                    ['HazScissors', 'HazCan', 'Table'], 
                    ['Bathroom', 'Sweeping', 'Meal']]

        horLayoutForBoth = QVBoxLayout()

        # make buttons, connect to func, put on grid
        navLayout = QGridLayout()
        currButton = None
        for i, row in enumerate(navNames):
            for j, col in enumerate(row):
                currButton = QPushButton(col)
                currButton.clicked.connect(partial(self.moveDirection, col))
                navLayout.addWidget(currButton, i, j)
        horLayoutForBoth.addItem(navLayout)

        # manual movement buttons
        meter = QPushButton("Up-1m")
        up = QPushButton("Up")
        down = QPushButton("Down")
        left = QPushButton("Left")
        right = QPushButton("Right")

        #connect buttons to funcs
        meter.clicked.connect(partial(self.moveManual, "Meter"))
        up.clicked.connect(partial(self.moveManual, "Forward"))
        down.clicked.connect(partial(self.moveManual, "Backward"))
        left.clicked.connect(partial(self.moveManual, "Left"))
        right.clicked.connect(partial(self.moveManual, "Right"))

        #create layout and add buttons to it
        manualLayout = QGridLayout()
        manualLayout.addWidget(meter, 0,1)
        manualLayout.addWidget(up, 1, 1)
        manualLayout.addWidget(down, 3, 1)
        manualLayout.addWidget(left, 2, 0)
        manualLayout.addWidget(right, 2, 2)

        # add this manual layout
        horLayoutForBoth.addItem(manualLayout)

        #set widget layout
        self.setLayout(horLayoutForBoth)

    def paintEvent(self, event):
        painter = QPainter(self)
        bounds = QRectF(0, 0, self.width()-1, self.height()-1)
        painter.setPen(QColor(255,217,73))
        painter.setBrush(QColor(255,217,73))
        painter.drawRoundedRect(bounds, 4, 4)
        # painter.drawEllipse(bounds)

    def _center(self):
        return QPointF(self.width()/2, self.height()/2)
    
    def moveDirection(self, dir):
        try:
            db.child("Movement").child("Direction").set(dir, self.user['idToken'])
            # db.child("Movement").child(dir).set(True, self.user['idToken'])
            db.child("Movement").child("Command").set(True, self.user['idToken'])
            time.sleep(0.1)
            # db.child("Movement").child(dir).set(False, self.user['idToken'])
            db.child("Movement").child("Command").set(False, self.user['idToken'])
        except:
            print(dir + "failed")

    def moveManual(self, dir):
        try:
            db.child("Movement").child(dir).set(True, self.user['idToken'])
            db.child("Movement").child("Command").set(True, self.user['idToken'])
            time.sleep(0.1)
            db.child("Movement").child(dir).set(False, self.user['idToken'])
            db.child("Movement").child("Command").set(False, self.user['idToken'])
        except:
            print(dir + "failed")


if __name__ == '__main__':
    # Create main application window
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Cleanlooks"))
    mw = QMainWindow()
    mw.setWindowTitle('Joystick example')

    # Create and set widget layout
    # Main widget container
    cw = QWidget()
    ml = QGridLayout()
    cw.setLayout(ml)
    mw.setCentralWidget(cw)

    # Create joystick 
    joystick = MoveButton()

    # ml.addLayout(joystick.get_joystick_layout(),0,0)
    ml.addWidget(joystick,0,0)

    mw.show()

    ## Start Qt event loop unless running in interactive mode or using pyside.
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        sys.exit(app.exec())