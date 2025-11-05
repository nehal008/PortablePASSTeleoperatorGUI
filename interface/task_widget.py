import sys
import re
from PyQt6.QtWidgets import * 
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import * 
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
import qdarktheme
import time
import os
import codecs
from enum import Enum
from datetime import datetime
from functools import partial
from passlist import *

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

class TaskWidget(QWidget):
    def __init__(self, user, parent=None, height=300, color="#00c4ff"):
        super(QWidget, self).__init__(parent)
        self.user = user
        self._color = color

        # make a container for scroll area and set layout
        bigBox = QVBoxLayout()
        self.scroll = QScrollArea(self)
        bigBox.addWidget(self.scroll)
        self.setLayout(bigBox)

        self.passlist = Passlist().passlist
        self.currentstep = '>_<'
        self.play_buttons = []
        # set characteristics for ScrollArea,
        # make container for task widgets layout
        self.scroll.setWidgetResizable(True)
        # self.scroll.setMaximumHeight(400)
        if height != -1:
            self.scroll.setFixedHeight(height)
        scrollContainer = QWidget()
        # scrollContainer.setMaximumHeight(400)
        self.scroll.setWidget(scrollContainer)

        # make list of tasks & play buttons
        self.steps_layout = QVBoxLayout()
        self.steps_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scrollContainer.setLayout(self.steps_layout)

    def makeList(self, dict, patient_name, add_record_button: bool = True):
        # reset the size of the scroll area
        # self.scroll.setFixedHeight(400)
        tasks = list(dict)
        self.play_buttons = []
        # Original code : tasks.insert(0, 'Sydney, please short click the button on the smartwatch.')
        current_readtime = datetime.now()
        hour_toRead = current_readtime.strftime('%I')
        hour = hour_toRead
        if hour_toRead[0] == '0':
            hour = hour_toRead[1:]
        
        minute_toRead = current_readtime.minute
        #makes the clock legible if minute is in the single digit range
        if minute_toRead < 10:
            minute_toRead = '0' + str(minute_toRead)
        second_toRead = current_readtime.second
        am_pm = current_readtime.strftime("%p")
        if add_record_button:
            tasks.insert(0, f"It is {hour_toRead}:{minute_toRead} {am_pm} and {second_toRead} seconds. Please short click the button on the smartwatch.")
        for task in tasks:
            curr_box = QHBoxLayout()
            container = QWidget()
            container.setMaximumHeight(80)
            container.setLayout(curr_box)
            # if re.search('SlowSpeed:', task):
            #     db.child("Speak").child("Speed").set(50, self.user['idToken'])
            # else:
            #     db.child("Speak").child("Speed").set(75, self.user['idToken'])
            if re.search('OptionalSay:',task):
                container.setStyleSheet(f"background-color: {'#60f784'};\
                    border-radius:8px;")
            else:
                container.setStyleSheet(f"background-color: {self._color};\
                    border-radius:8px;")

            task = re.sub(r"ParticipantName", patient_name, task)
            task = re.sub(r"OptionalSay:", '', task)
            task = re.sub(r"CurrentMonth",current_readtime.strftime('%B'),task)
            task = re.sub(r"CurrentYear", current_readtime.strftime('%Y'), task)
            task = re.sub(r"CurrentWeekDay", current_readtime.strftime('%A'), task)
            task = re.sub(r"CurrentHour", hour, task)
            task = re.sub(r"AMPM", current_readtime.strftime('%p'), task)
            date =  current_readtime.strftime('%d')
            #task = re.sub(r"CurrentDay", date, task)
            if date[-1] == '1':
                date+='st'
            elif date[-1] == '2':
                date+='nd'
            else:
                date+='th'
            task = re.sub(r"CurrentDate", date, task)
            task = re.sub(r"CurrentDay", date, task)
            task_label = task
            task_label = re.sub(r"SlowSpeed: ", '', task)


            label = QLabel(task_label)
            # limit how much is shown
            # if len(task) > 80:
            #     label.setText(task[:70] + " ...")
            label.setWordWrap(True)
            curr_box.addWidget(label)

            play_button = QPushButton('Play')
            #print(play_button)
            self.play_buttons.append(play_button)
            
            play_button.clicked.connect(partial(self.playStep, task, play_button))
            curr_box.addWidget(play_button, alignment=Qt.AlignmentFlag.AlignVCenter|Qt.AlignmentFlag.AlignRight)
            curr_box.setStretch(0,3)
            curr_box.setStretch(1,1)
            with open(os.path.join("assets", "light"), "r") as lightFile:
                play_button.setStyleSheet(lightFile.read())
            # play_button.setAutoFillBackground(True)
            # play_button.setStyleSheet("QButton{ background-color: #ffffff; }")
            # play_style = qdarktheme.load_stylesheet("light") + \
            #     '''
            #     QButton{
            #         background-color: #ffffff;
            #     }
            #     '''
            # # play_button.setAutoFillBackground(True)
            # play_button.setStyleSheet(play_style)
            # play_button
            self.steps_layout.addWidget(container)

        # add the submit button at the end of the list
        if add_record_button:
            submit_button = QPushButton('Stop Recording and Submit')
            submit_button.setStyleSheet("QPushButton{background-color: #ff766d; border-color: transparent; color: white}"
                                    "QPushButton::hover{ background-color : #ff473b }"
                                    "QPushButton::pressed{ background-color : #d40e00 }"
            )
            submit_button.clicked.connect(self.submitRecording)
            self.steps_layout.addWidget(submit_button)

    # send the step to the database
    def playStep(self, step, this_but) :
        if re.search('SlowSpeed:', step):
            db.child("Speak").child("Speed").set(50, self.user['idToken'])
        else:
            db.child("Speak").child("Speed").set(75, self.user['idToken'])
        step = re.sub(r"SlowSpeed: ", '', step)
        db.child("Speak").child("Content").set(step.strip(), self.user['idToken'])
        db.child("Speak").child("Pushed").set(True, self.user['idToken'])
        time.sleep(0.1)
        db.child("Speak").child("Pushed").set(False, self.user['idToken'])
        this_but.setStyleSheet("QPushButton{background-color: #b9ff00; border-color: transparent}"
                                "QPushButton::hover{ background-color : #b0f300 }"
                                "QPushButton::pressed{ background-color : #e0ff8c }")
        #print(step)
        self.currentstep = step

#        try:
 #           self.info_intervent_widget.makeList(self.passlist.get(listName).get(self.task_widg.currentstep).get('RemindSupport'), self._patient_name, False)
 #           self.redirect_intervent_widget.makeList(self.passlist.get(listName).get(self.task_widg.currentstep).get('Redirect'), self._patient_name, False)
 #       except:
 #           print('no applicable step')

        #self.pass.info_intervent_widget.makeList(self.passlist.get(listName).get(step).get('RemindSupport'), self._patient_name, False)

    def submitRecording(self):
        db.child("Recording").child("Status").set(False, self.user['idToken'])
        self.removeItems()

    # delete the list
    def removeItems(self):
        for i in reversed(range(self.steps_layout.count())):
            self.steps_layout.itemAt(i).widget().setParent(None)
        # set size 0 to hide the widget until a new list is added
        # self.scroll.setFixedHeight(0)
        self.update()