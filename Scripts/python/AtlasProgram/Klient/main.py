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
from moveR import *

connect()

enableTorque()
while True:
    print("Enter what point you want to move to: 1, 2, 3...\n")
    s = input()
    if(s == "1"):
        moveWithPos(1500,1500,3200,2500,1000)
    elif(s == "2"):
        moveWithPos(2000,2500,2500,3200,2000)
    elif(s == "3"):
        moveWithPos(3000,1700,2700,2000,3000)
    else: 
        break
closePort()
