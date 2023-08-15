from dxlModDef import *
from DynamixelRobot import *
import numpy as np

Atlas = Robot()                  # Create an instance of the robot class named Atlas
Atlas.DXL_IDs = [1, 2, 3, 4, 5]  # Specify the IDs of each joint as an array of integers, default is [1]


Atlas.portPicker()               # Lets the user choose which port to use for the connection
Atlas.openPort()                 # Opens the chosen port
Atlas.disableTorque()            # Disables the torque of all joints
print("Move to a limited position and press enter")
input()
print("The first limit: ", Atlas.getPose())
print("Move to the other limited position and press enter")
input()
print("The seccond limit: ", Atlas.getPose())