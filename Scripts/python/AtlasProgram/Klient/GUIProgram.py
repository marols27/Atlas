import sys
from DynamixelRobot import *
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os



class RobotControlGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Robot Control GUI")
        self.setGeometry(100, 100, 400, 300)

        self.backgroundLabel = QLabel(self)

        image_url = "https://raw.githubusercontent.com/HVLrobotics/project-reporting-example/9f3fef09243d8dec53e37df6c821e7fd0ef71b9e/%E2%80%ABimages/logo.png"
        response = requests.get(image_url)
        image_path = "backgorund.png"

        with open(image_path, "wb") as file:
            file.write(response.content)
          
        self.backgroundLabel = QLabel(self)
        pixmap = QPixmap(image_path)
        self.backgroundLabel.setPixmap(pixmap)
        self.backgroundLabel.move(0, 0)
        self.backgroundLabel.resize(400, 300)
        

        self.program_label = QLabel("Select Robot Program:", self)
        self.program_label.move(20, 20)
        self.program_label.resize(200, 20)

        self.program_combo = QComboBox(self)
        self.program_combo.addItem("Move to Positions")
        self.program_combo.addItem("Manual Control")
        self.program_combo.addItem("Wave")
        self.program_combo.move(200, 20)
        self.program_combo.resize(150, 20)
        self.program_combo.activated.connect(self.on_program_select)


        #move to positions program
        self.move_to_pos1 = QPushButton("Move to position 1", self)
        self.move_to_pos1.move(130, 100)
        self.move_to_pos1.resize(150, 50)
        self.move_to_pos1.clicked.connect(self.on_button_click)
        self.move_to_pos1.hide()

        self.move_to_pos2 = QPushButton("Move to position 2", self)
        self.move_to_pos2.move(130, 160)
        self.move_to_pos2.resize(150, 50)
        self.move_to_pos2.clicked.connect(self.on_button_click)
        self.move_to_pos2.hide()

        self.move_to_pos3 = QPushButton("Move to position 3", self)
        self.move_to_pos3.move(130, 220)
        self.move_to_pos3.resize(150, 50)
        self.move_to_pos3.clicked.connect(self.on_button_click)
        self.move_to_pos3.hide()

        #manual control program
        
        #Label for description
        self.manual_control_label = QLabel("To use manual control, press disable the torque \nand move the robot using you hands. \nPress set position to save for each position \nPress Run Program to run ", self)
        self.manual_control_label.move(35, 50)
        self.manual_control_label.resize(350, 70)
        self.manual_control_label.hide()

        #Button to disable torque
        self.disaeble_torque = QPushButton("Disable Torque", self)
        self.disaeble_torque.move(20, 130)
        self.disaeble_torque.resize(120, 20)
        self.disaeble_torque.clicked.connect(Atlas.disableTorque)
        self.disaeble_torque.hide()

        #Buttons to set position
        self.manual_pos1 = QPushButton("Set position 1", self)
        self.manual_pos1.move(20, 210)
        self.manual_pos1.clicked.connect(setPos1)
        self.manual_pos1.hide()

        self.manual_pos2 = QPushButton("Set position 2", self)
        self.manual_pos2.move(140, 210)
        self.manual_pos2.clicked.connect(setPos2)
        self.manual_pos2.hide()

        self.manual_pos3 = QPushButton("Set position 3", self)
        self.manual_pos3.move(260, 210)
        self.manual_pos3.clicked.connect(setPos3)
        self.manual_pos3.hide()

        #Button to run program
        self.run_manual = QPushButton("Run Program", self)
        self.run_manual.move(275, 250)
        self.run_manual.clicked.connect(runProgram)
        self.run_manual.setStyleSheet("background-color: green")
        self.run_manual.hide()

        #buttons for wave program
        self.wave = QPushButton("Wave", self)
        self.wave.move(100, 100)
        self.wave.resize(200, 100)
        self.wave.setStyleSheet("background-color: red")
        self.wave.clicked.connect(Atlas.makeAMove)
        self.wave.hide()



    def on_program_select(self):
        selected_program = self.program_combo.currentText()
        
        if selected_program == "Move to Positions":
            #show move to positions buttons
            self.move_to_pos1.show()
            self.move_to_pos2.show()
            self.move_to_pos3.show()

            #hide manual control buttons
            self.manual_control_label.hide()
            self.disaeble_torque.hide()

            self.manual_pos1.hide()
            self.manual_pos2.hide()
            self.manual_pos3.hide()
            
            self.run_manual.hide()

            #hide wave button
            self.wave.hide()

        elif selected_program == "Manual Control":
            #hide move to positions buttons
            self.move_to_pos1.hide()
            self.move_to_pos2.hide()
            self.move_to_pos3.hide()

            #show manual control buttons
            self.manual_control_label.show()
            self.disaeble_torque.show()

            self.manual_pos1.show()
            self.manual_pos2.show()
            self.manual_pos3.show()
            
            self.run_manual.show()

            #hide wave button 
            self.wave.hide()
        
        elif selected_program == "Wave":
            #hide move to positions buttons
            self.move_to_pos1.hide()
            self.move_to_pos2.hide()
            self.move_to_pos3.hide()

            #hide manual control buttons
            self.manual_control_label.hide()
            self.disaeble_torque.hide()

            self.manual_pos1.hide()
            self.manual_pos2.hide()
            self.manual_pos3.hide()
            
            self.run_manual.hide()

            #show wave button
            self.wave.show()


    def manualContorlProgram(self):
        self.button_program_pos1 = QPushButton("Set position 1", self)
        self.button_program_pos1.move(150, 160)
        self.button_program_pos1.hide()

        self.button_program_pos2 = QPushButton("Set position 2", self)
        self.button_program_pos2.move(150, 200)
        self.button_program_pos2.hide()

        self.button_program_pos3 = QPushButton("Set position 3", self)
        self.button_program_pos3.move(150, 240)
        self.button_program_pos3.hide()

    def on_button_click(self):
        print("Button clicked")



# Create a robot object using an instantiation of the Robot class
Atlas = Robot() # Create an instance of the robot named Atlas

poses = []
for i in range(3):
    poses.append([1140, 1599, 3191, 3110, 1000])

def setPos1():
    poses[0] = Atlas.getPose()
    print("Position 1 is set to: ", poses[0])

def setPos2():
    poses[1] = Atlas.getPose()
    print("Position 2 is set to: ", poses[1])

def setPos3():
    poses[2] = Atlas.getPose()
    print("Position 3 is set to: ", poses[2])


def runProgram():
    Atlas.enableTorque()
    Atlas.returnToBase()
    for i in range(poses.__len__()):
        time.sleep(3)
        Atlas.moveWithPos(poses[i])

    time.sleep(3)
    Atlas.returnToBase()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = RobotControlGUI()
    main_window.show()
    sys.exit(app.exec_())
