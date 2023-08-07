'''
This is the user interface for the robot. The user can choose between different functions.
The functions are imported from the userInterface.py file.

The porgram gives you the option to move the robot to three different positions, wave and return to base.

'''





from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from userInterface import *

import sys

class MainWindow(QMainWindow):
     def __init__(self):
        super().__init__()

        self.setWindowTitle("Atlas Robot Control")
        #move program
        mLabel = QLabel("Move program")
        mButton1 = QPushButton("Position 1")
        mButton2 = QPushButton("Position 2")
        mButton3 = QPushButton("Position 3")

        mButton1.clicked.connect(moveToOne)
        mButton2.clicked.connect(moveToTwo)
        mButton3.clicked.connect(moveToThree)

        #wave program
        wLabel = QLabel("Wave program")
        wButton = QPushButton("Wave")
        wButton.clicked.connect(wave)

        #stop program
        sLabel = QLabel("Stop program")
        sButton = QPushButton("Stop")
        sButton.clicked.connect(closeWindow)


        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(mLabel)
        layout.addWidget(mButton1)
        layout.addWidget(mButton2)
        layout.addWidget(mButton3)

        layout.addWidget(wLabel)
        layout.addWidget(wButton)

        layout.addWidget(sLabel)
        layout.addWidget(sButton)

        # Set the central widget of the Window.
        widget = QWidget()
        widget.setLayout(layout)
        widget.setFixedSize(600, 200)

        self.setFixedSize(600, 200)

        self.setCentralWidget(widget)
        



app = QApplication(sys.argv)

def closeWindow():
    #returnToBase()
    time.sleep(2)
    sys.exit()

window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

app.exec_()





