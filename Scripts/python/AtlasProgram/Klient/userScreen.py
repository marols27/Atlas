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
        label = QLabel("Move program")
        mButton1 = QPushButton("Position 1")
        mButton2 = QPushButton("Position 2")
        mButton3 = QPushButton("Position 3")

        mButton1.clicked.connect(moveToOne)
        mButton2.clicked.connect(moveToTwo)
        mButton3.clicked.connect(moveToThree)

        #wave program
        label = QLabel("Wave program")
        wButton = QPushButton("Wave")
        wButton.clicked.connect(wave)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(mButton1)
        layout.addWidget(mButton2)
        layout.addWidget(mButton3)

        layout.addWidget(label)
        layout.addWidget(wButton)

        # Set the central widget of the Window.
        widget = QWidget()
        widget.setLayout(layout)
        widget.setFixedSize(600, 200)

        self.setFixedSize(600, 200)

        self.setCentralWidget(widget)
        



app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

app.exec_()





