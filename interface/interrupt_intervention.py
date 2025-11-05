import sys
import re
import time
from functools import partial
from PyQt6.QtWidgets import * 
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import * 
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt

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
    # this works without the serviceAccount credential so ?
    #"serviceAccount": r"/home/rob/Downloads/passexperiment-bfa25-firebase-adminsdk-7ljxj-2145fbcabf.json"
}

# initialze pyrebase
fb = pyrebase.initialize_app(config)
db = fb.database()

class InterruptInterventionWidget(QWidget):
    def __init__(self, user, *args, **kwargs):
        super(InterruptInterventionWidget, self).__init__(*args, **kwargs)

        self._user = user
        
        self._interrupt_label = QLabel("Others")
        self._interrupt_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self._input = QTextEdit(self)
        self._input.setPlaceholderText("Input your interruption here...")
        self._input.setFixedHeight(30)

        self._submit_button = QPushButton("Send")
        # self._submit_button.clicked.connect(partial(self.play_step, self._input.toPlainText()))
        self._submit_button.clicked.connect(partial(self.play_step, self._input))

        self._box_layout = QVBoxLayout()
        self._box_layout.addWidget(self._interrupt_label)
        self._box_layout.addWidget(self._input)
        self._box_layout.addWidget(self._submit_button)
        self.setLayout(self._box_layout)

    def submit_text(self):
        if self._input.textChanged and self._input.toPlainText():
            print(self._input.toPlainText())

    # send the step to the database
    def play_step(self, input: QTextEdit) :
        # clear input
        self.current_step = input.toPlainText().strip()
        input.clear()
        # print(self.current_step)
        # push to database
        db.child("Speak").child("Content").set(self.current_step, self._user['idToken'])
        # if re.search('SlowSpeed:', self.current_step):
        #     db.child("Speak").child("Speed").set(50, self.user['idToken'])
        # else:
        #     db.child("Speak").child("Speed").set(75, self.user['idToken'])
        db.child("Speak").child("Pushed").set(True, self._user['idToken'])
        time.sleep(0.1)
        db.child("Speak").child("Pushed").set(False, self._user['idToken'])

        

    def paintEvent(self, event):
        painter = QPainter(self)
        bounds = QRectF(0, 0, self.width()-1, self.height()-1)
        painter.setPen(QColor("#f9b6ff"))
        painter.setBrush(QColor("#f9b6ff"))
        painter.drawRoundedRect(bounds, 4, 4)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = InterruptInterventionWidget()
    window.show()
    sys.exit(App.exec())