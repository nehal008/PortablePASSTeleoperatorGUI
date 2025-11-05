import sys
import os
from PyQt6.QtWidgets import * 
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import * 
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
from task_widget import TaskWidget

class InformationIntervention(TaskWidget):
    def __init__(self, list_file: str, *args, **kwargs):
        super(InformationIntervention, self).__init__(*args, **kwargs)

        # self.makeList(list_file, "{name}", add_record_button=False)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = InformationIntervention(os.path.join("data", "info_intervention", "info1"), None)
    window.show()
    sys.exit(App.exec())