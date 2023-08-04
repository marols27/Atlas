'''This is the main folder where we import and run the fuctions from the other files 
whitin the atlas program. This file will be able to run using a U2D2 and a Dynamixel
chain og 5 motors. The motors are connected in the following order of IDs: 1, 2, 3, 4, 5.
The motors are connected to the U2D2 which is connected to the computer using a USB cable.
The input to the motors are the angles of the motors. The angles are calculated using the
inverse kinematics of the robot. The inverse kinematics are calculated using the forward
kinematics of the robot. The forward kinematics are calculated using the Denavit-Hartenberg
parameters of the robot. The Denavit-Hartenberg parameters are calculated using the
dimensions of the robot. The dimensions of the robot are given in the following file:
Scripts/python/AtlasProgram/robot_dimensions.py. The dimensions are given in millimeters.
'''
from userInterface import *


s = input("For move with position press 1, for wave press 2: ")
if s == "1":
    positionPlacer()
elif s == "2":
    wave()
else:
    print("Have a nice day!")
returnToBase()
time.sleep(2)
connect()
disableTorque()
closePort()