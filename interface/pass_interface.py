import sys
from PyQt6.QtWidgets import * 
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import * 
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
from task_widget import TaskWidget
from move_button import MoveButton
from intervention_select import InterventionSelectWidget
from common_help_widg import CommonHelpWidget
from info_intervention import InformationIntervention
from interrupt_intervention import InterruptInterventionWidget
from reminder_intervention import ReminderInterventionWidget
from chat_intervention import ChatIntervention
from redirect_intervention import RedirectIntervention
import time
import os
from enum import Enum
import datetime
from functools import partial
from passlist import *
import pyrebase

# pyrebase config
config = {
    # # Start of Original
    # "apiKey": " ",
    # "authDomain": " ",
    # "databaseURL": " ",
    # "storageBucket": " "
    # # End of Original
    # Start of Modification by FY
    "apiKey": " ",
    "authDomain": " ",
    "databaseURL": " ",
    "storageBucket": " "
    # End of Modification by FY
    # "serviceAccount": r" "
}

# initialze pyrebase
fb = pyrebase.initialize_app(config)
db = fb.database()

##################################
#globals - taken from pass_ui.py
#don't know if we will actually
#need this?
##################################
move_directions = {
    "Left": 0,
    "Right": 0,
    "Up": 0,
    "Down": 0
}

class Pass(QWidget):
    # declare the layout for playable steps
    steps_layout = QVBoxLayout()
    task_widg = None
    passlist = Passlist().passlist

    def __init__(self, user="", auth=""):
        super().__init__()
        self.user = user
        self.auth = auth
        self.setWindowTitle("PASS Assessment Page")
        self.UiComponents()
        self.show()
        self.passlist = Passlist().passlist
        self.test = 'test'
        

    # update task playable listee
    def runTask(self, listName):
        if self._patient_name == None:
            warning_widg = QWidget()
            

        # refresh the user token
        self.user = self.auth.refresh(self.user['refreshToken'])

        if self.task_widg == None:
            self.task_widg = TaskWidget(self.user, parent=self, height=-1)
        #print(self.task_widg.currentstep)
        
        self.task_widg.removeItems()
        self.task_widg.makeList(self.passlist.get(listName), self._patient_name)
        self.steps_layout.addWidget(self.task_widg)

        # get number and populate other lists
        num = listName.split("pass")[-1]

        #print(list(self.passlist.get(listName)))
 #       try:
 #           self.info_intervent_widget.makeList(self.passlist.get(listName).get(self.task_widg.currentstep).get('RemindSupport'), self._patient_name, False)
 #           self.redirect_intervent_widget.makeList(self.passlist.get(listName).get(self.task_widg.currentstep).get('Redirect'), self._patient_name, False)
 #       except:
 #           print('no applicable step')
        # self.reminder_widget.makeList(os.path.join("data", "reminder", f"reminder{num}"), self._patient_name, False)
        self.chat_intervent_widget.removeItems()
        self.chat_intervent_widget.makeList(self.passlist.get('allPass').get('Chat'), self._patient_name, False)

        # stop last recording and start new one
        # self.stopRecording()
        self.startRecording()

        #print(list(self.passlist.get(listName)))

        #print(self.task_widg.play_buttons)
        try:
            for pb in self.task_widg.play_buttons:
                pb.clicked.connect(partial(self.play_update,listName))
        except:
            print('no buttons')
        # taskFile = open(f'./task_files/{listName}', 'r')
        # tasks = taskFile.readlines()
        # for task in tasks:
        #     play_button = QPushButton('Play')
        #     play_button.clicked.connect(partial(self.playStep, task))
        #     label = QLabel(task)
        #     label.setWordWrap(True)
        #     container = QWidget()
        #     container.setStyleSheet("background-color: rgb(211,211,211);")
        #     curr_box = QHBoxLayout(container)
        #     curr_box.addWidget(label)
        #     curr_box.addWidget(play_button, alignment=Qt.AlignmentFlag.AlignVCenter|Qt.AlignmentFlag.AlignRight)
            
        #     self.steps_layout.addWidget(container)
    
    def play_update(self,listName):
        #print(self.task_widg.currentstep)
        try:
            self.info_intervent_widget.removeItems()
            self.redirect_intervent_widget.removeItems()
            self.info_intervent_widget.makeList(self.passlist.get(listName).get(self.task_widg.currentstep).get('RemindSupport'), self._patient_name, False)
            self.redirect_intervent_widget.makeList(self.passlist.get(listName).get(self.task_widg.currentstep).get('Redirect'), self._patient_name, False)
        except:
            print(None)

    def rotateDirection(self, dir):
        try:
            db.child("Rotation").child(dir).set(True, self.user['idToken'])
            db.child("Rotation").child("Command").set(True, self.user['idToken'])
            time.sleep(0.1)
            db.child("Rotation").child(dir).set(False, self.user['idToken'])
            db.child("Rotation").child("Command").set(False, self.user['idToken'])
        except Exception as e:
            print(dir + "failed")
            print(e)

    

    # method for widgets
    def UiComponents(self): 
        #path variable to hold recording path - todo
        self.path_val = ""

        # grid layout for whole screen
        main_grid = QGridLayout(self)

        #create main layout
        main_layout = QVBoxLayout()
        # self.upperStack = QStackedWidget()
        self.upperStack = QStackedLayout()
        main_grid.addLayout(main_layout, 0, 0, 1, 1)

        # create interruptions column
        interrupt_layout = QVBoxLayout()
        main_grid.addLayout(interrupt_layout, 0, 1, 1, 1)

        # initialize ID fields
        self.date_val = QLineEdit()
        self.time_val = QLineEdit()
        self.id_val = QLineEdit()
        self.name_val = QLineEdit()

        #date input layout
        today = datetime.date.today()
        date_str = f'{today.month}/{today.day}/{today.year}'
        date_field = QHBoxLayout()
        date = QLabel("Date:")
        self.date_val = QLineEdit(date_str)
        date_field.addWidget(date)
        date_field.addWidget(self.date_val)

        #time input layout
        time_str = datetime.datetime.now().strftime("%H:%M")
        time_field = QHBoxLayout()
        time = QLabel("Time:")
        self.time_val = QLineEdit(time_str)
        time_field.addWidget(time)
        time_field.addWidget(self.time_val)

        #patient id input layout
        self.curr_id = int(db.child("Identifiers").child("last_patient_id").get(self.user['idToken']).val()) + 1
        id_field = QHBoxLayout()
        idl = QLabel("Patient ID:")
        self.id_val = QLineEdit(f'{self.curr_id}')
        id_field.addWidget(idl)
        id_field.addWidget(self.id_val)

        #patient name input layout
        name_field = QHBoxLayout()
        name = QLabel("Name:")
        self.name_val = QLineEdit()
        # comment out for now
        name_field.addWidget(name)
        name_field.addWidget(self.name_val)

        #variables to store these

        #create registered user greeting layout
        usr_final = QHBoxLayout()
        self.usr_greet = QLabel("")
        self.usr_greet.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        usr_final.addWidget(self.usr_greet)

        #set input layout
        form_buts_lay = QVBoxLayout()
        form_buts_widget = QWidget()
        upper_input_layout = QHBoxLayout()
        input_widget = QWidget()
        input_layout = QVBoxLayout()
        input_layout.addLayout(date_field)
        input_layout.addLayout(time_field)
        input_layout.addLayout(id_field)
        input_layout.addLayout(name_field)
        input_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        input_widget.setLayout(input_layout)
        # record_widget = QPushButton("Record")
        # record_widget.clicked.connect(lambda: self.startRecording())
        submit_widget = QPushButton("Submit")
        submit_widget.clicked.connect(lambda: self.setIdentifiers())
        # form_buts_lay.addWidget(record_widget)
        form_buts_lay.addWidget(submit_widget)
        form_buts_widget.setLayout(form_buts_lay)
        upper_input_layout.addWidget(input_widget)
        upper_input_layout.addWidget(form_buts_widget)
        upper_input_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        #set registered layout
        upper_result_layout = QVBoxLayout()
        upper_result_layout.addLayout(usr_final)
        upper_result_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
    
        #create widget stack for upper half of gameplay screen
        upper_input_widget = QWidget()
        upper_input_widget.setLayout(upper_input_layout)
        upper_result_widget = QWidget()
        upper_result_widget.setLayout(upper_result_layout)
        self.upperStack.addWidget(upper_input_widget)
        # self.upperStack.addWidget(upper_input_layout)
        self.upperStack.addWidget(upper_result_widget)
        self.upperStack.setCurrentIndex(0)
        self.upper_stack_container = QWidget()
        self.upper_stack_container.setLayout(self.upperStack)
        self.upper_stack_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)

        #task list dropdown - just filled with dummy values for now
        self.task_widget = QWidget()
        self.task_layout = QHBoxLayout()
        self.taskList = QComboBox()
        # create ComboBox for pass functions
        file_names = list(self.passlist.keys())
        file_names.remove('allPass')
        self.taskList.addItems(file_names)

        #create a list of the info files
        self.intr_names = []
        for file_name in os.listdir('./data/info_intervention'):
            self.intr_names.append(file_name)
        #print(intr_names)

        run_task = QPushButton("Run")
        run_task.clicked.connect(lambda: self.runTask(self.taskList.currentText()))
        self.task_layout.addWidget(self.taskList)
        self.task_layout.addWidget(run_task)
        self.task_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.task_widget.setLayout(self.task_layout)
        self.task_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        #list steps based on selected task here
        steps_widget = QWidget()
        #steps_holder = QLabel("Steps for selected task will be displayed here")
        #self.steps_layout.addWidget(steps_holder)
        # self.steps_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        steps_widget.setLayout(self.steps_layout)
        self.steps_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        #assessment window will go here
        text_widget = QWidget()
        text_layout = QVBoxLayout()
        #text_holder = QLabel("Actual task/assessment window here")
        #text_layout.addWidget(text_holder)
        text_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        text_widget.setLayout(text_layout)

        # common help section
        # common_help_label = QLabel("Common Help")
        # common_help_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # self.common_help_widget = CommonHelpWidget(os.path.join("data", "common_help", "common1"), self.user, parent=self, height=200, color="#ffd949")

    #    for pb in self.task_widg.play_buttons:
    #        print(pb)
    #        try:
    #            self.info_intervent_widget.makeList(self.passlist.get(listName).get(self.task_widg.currentstep).get('RemindSupport'), self._patient_name, False)
    #            self.redirect_intervent_widget.makeList(self.passlist.get(listName).get(self.task_widg.currentstep).get('Redirect'), self._patient_name, False)
    #        except:
    #            print('no applicable step')


        # info intervention
        info_intervent_label = QLabel("Remind and Support")
        info_intervent_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.info_intervent_widget = InformationIntervention(os.path.join("data", "info_intervention", "info1"), self.user, parent=self, height=200, color="#00d949")
        
        # redirect intervention
        redirect_intervent_label = QLabel("Redirect")
        redirect_intervent_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.redirect_intervent_widget = RedirectIntervention(os.path.join("data", "redirect", "redirect1"), self.user, parent=self, height=200, color="#f9b6ff")
        
        # chat intervention
        chat_intervent_label = QLabel("Chat")
        chat_intervent_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.chat_intervent_widget = ChatIntervention(os.path.join("data", "chat", "chat1"), self.user, parent=self, height=200, color="#00d949")
        
        

        # reminder Intervention
        # reminder_label = QLabel("Reminder")
        # reminder_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # self.reminder_widget = ReminderInterventionWidget(os.path.join("data", "reminder", "reminder1"), self.user, parent=self, height=200, color="#f9b6ff")
        
        # interrupt Intervention
        # interrupt_label = QLabel("Others")
        # interrupt_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.interrupt_widget = InterruptInterventionWidget(self.user)

        # intervention selection widget
        # intervent_select = InterventionSelectWidget()

        #reset button
        reset_button = QPushButton("Reset Assessment")
        reset_button.clicked.connect(lambda: self.resetAssessment())

        #Firebase sign-in
        firebase_signin_but = QPushButton("Firebase: Re-sign In")
        firebase_signin_but.clicked.connect(lambda: self.resignIn())

        #set main layout
        # main_layout.addWidget(self.upperStack)
        main_layout.addWidget(self.upper_stack_container)
        main_layout.addWidget(self.task_widget)
        main_layout.addWidget(steps_widget)
        # layout.addWidget(text_widget)
        # main_layout.addWidget(intervent_select)
        main_layout.addWidget(reset_button)
        # main_layout.addStretch()
        # main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        # main_layout.addStretch()
        self.setLayout(main_grid)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # set interrupt layout
        # interrupt_layout.addWidget(common_help_label)
        # interrupt_layout.addWidget(self.common_help_widget)
        interrupt_layout.addWidget(info_intervent_label)
        interrupt_layout.addWidget(self.info_intervent_widget)
        # interrupt_layout.addWidget(reminder_label)
        # interrupt_layout.addWidget(self.reminder_widget)
        interrupt_layout.addWidget(redirect_intervent_label)
        interrupt_layout.addWidget(self.redirect_intervent_widget)
        interrupt_layout.addWidget(chat_intervent_label)
        interrupt_layout.addWidget(self.chat_intervent_widget)
        interrupt_layout.addStretch()
        # interrupt_layout.addWidget(interrupt_label)
        interrupt_layout.addWidget(self.interrupt_widget)
        

    def resetAssessment(self):
        #date input layout
        today = datetime.date.today()
        date_str = f'{today.month}/{today.day}/{today.year}'
        date_field = QHBoxLayout()
        date = QLabel("Date:")
        self.date_val.setText(date_str)

        #time input layout
        time_str = datetime.datetime.now().strftime("%H:%M")
        time_field = QHBoxLayout()
        time = QLabel("Time:")
        self.time_val.setText(time_str)

        #patient id input layout
        curr_id = int(db.child("Identifiers").child("last_patient_id").get(self.user['idToken']).val()) + 1
        id_field = QHBoxLayout()
        idl = QLabel("Patient ID:")
        self.id_val.setText(f'{curr_id}')

        #patient name input layout
        name_field = QHBoxLayout()
        name = QLabel("Name:")
        self.name_val.setText("")

        self.upperStack.setCurrentIndex(0)

    # def resignIn():


    def sendNext(self):
        db.child("PASS").child("next_repeat").set("next", self.user['idToken'])
        time.sleep(1)
        db.child("PASS").child("next_repeat").set("nothing", self.user['idToken'])

    def sendRepeat(self):
        db.child("PASS").child("next_repeat").set("repeat", self.user['idToken'])
        time.sleep(1)
        db.child("PASS").child("next_repeat").set("nothing", self.user['idToken'])

    # ### Start of Original by 2023/04/04
    # def sendFile(self) :
    #     db.child("PASS").child("curr_file").set(file_setter.get(self.user['idToken'])) 
    # ### End of Original by 2023/04/04

    ## Start of Add by FY
    def sendFile(self):
        file_value = self.createVideoName()  # Assuming you want to use the video name as the value for the file
        db.child("PASS").child("curr_file").set(file_value, self.user['idToken'])

    ## End of Add by FY

    def startRecording(self):
        #set value for recording
        db.child("Recording").child("Status").set(False, self.user['idToken'])

        #delay for tiny amount
        time.sleep(0.1)

        #set value for recording
        db.child("Recording").child("Status").set(True, self.user['idToken'])

        #set the patient id for recording name
        db.child("Recording").child("patientId").set(self.curr_id, self.user['idToken'])
        # idRef = db.child("Identifiers").child("last_patient_id")
        # db.child("Recording").child("patientId").set(idRef.get().val)

        # make file name and set it for Pepper to grab
        db.child("Recording").child("Filename").set(self.createVideoName(), self.user['idToken'])

    def stopRecording(self):
        #set value for recording
        db.child("Recording").child("Status").set(False, self.user['idToken'])

    def createVideoName(self):
        str_date = self.date_val.text().replace('/', '-')
        time_str = datetime.datetime.now().strftime("%H:%M:%S")
        str_time = time_str.replace(':', '')
        str_id = 'id' + self.id_val.text()
        pass_id = self.taskList.currentText()
        final_str = str_date + '_' + str_time + '_' + str_id + '_' + pass_id
        return final_str
        

    def setIdentifiers(self):
        #this is an option if we dont want date and time fields on the screen (also makes sure we have an accurate date and time)
        #curr_time = datetime.now()
        #db.child("Identifiers").child("date").set(str(curr_time.day) + '/' +  str(curr_time.month) + '/' + str(curr_time.year))
        #db.child("Identifiers").child("time").set(str(curr_time.hour) + ':' +  str(curr_time.minute) + ':' + str(curr_time.second))
        newPerson = {
            "date" : self.date_val.text(),
            "time" : self.time_val.text(),
            "patient_id" : self.id_val.text(),
            "patient_name" : ""
        }
        self._patient_name = self.name_val.text()
        self.curr_id = newPerson['patient_id']
        db.child("Identifiers").push(newPerson, self.user['idToken'])
        db.child("Identifiers").child("last_patient_id").set(self.id_val.text(), self.user['idToken'])
        
        # delayed to get the patient name
        # self.common_help_widget.makeList(os.path.join("data", "common_help", "common1"), self._patient_name, False)

        # #set video path and update status
        # db.child("Recording").child("VideoStatus").set("recording uploaded")
        # db.child("Recording").child("Status").set(False)
        # db.child("Recording").child("patientId").set(newPerson['patient_id'])
        
        #update upper stack layout to display patient greeting
        self.usr_greet.setText("Welcome " + self.name_val.text() + "!")
        self.upperStack.setCurrentIndex(1)
        
        #ATTEMPTING to handle unwanted whitespace

        #self.upperStack.addWidget(self.task_widget)

        #.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        #self.task_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        #self.task_widget.setLayout(self.task_layout)

    def onMove(self,dir):
        print("handle movement buttons here")

    def onRotate(self,dir):
        print("handle rotation buttons here")

if __name__ == "__main__"   :
    App = QApplication(sys.argv)
    window = Pass()
    sys.exit(App.exec())

  
