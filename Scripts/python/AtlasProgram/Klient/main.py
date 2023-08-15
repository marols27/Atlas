'''
The main file is used to make small programs using the functions
from the Robot.py file. The user can freely choose which functions to use.

It is also a test file for developing features to the userScreen.py file.
'''
#from userInterface import *
from dxlModDef import *
from DynamixelRobot import *
import numpy as np

m = 1       # Remember to multiply your measurements with the correct unit
cm = 0.01   # this program is using [meter] as its input unit, so for simplicity 
mm = 0.001  # multply your measurements with the correct unit before using them


# NOTE: Remember to set the correct Dynamixel model in dxlModDef.py before use!

# Before running the program, the user has to specify the settings for the robot
Atlas = Robot()                                                     # Create an instance of the robot class named Atlas
Atlas.DXL_IDs = [1, 2, 3, 4, 5]                                     # Specify the IDs of each joint as an array of integers, default is [1]
Atlas.REST_POSE = [1140, 1599, 3191, 3110, 1000]                    # The home pose of the robot as an array of integers, must be the same lenght as DXL_IDs
Atlas.MAXVALUES = [4080, 3343, 3216, 3272, 4095]           # Specify the max and min values of the joints in an array of integers in steps
Atlas.MINVALUES = [15, 779, 886, 990, 0]                  # Specify the min and min values of the joints in an array of integers in steps
Atlas.IKINOFFSET = [0, int(4095*0.25), 0, int(4095*0.25), 0]

Atlas.JOINTS = cg.get_robot_config_1(                               # Specify the lenghts of each joint as an array of floats in [meter], default is [0.1] for each join
    link1=(163.474 * mm), link1_offset=0.0,
    link2=(190 * mm),     link2_offset=0.0,
    link3=(208.216 * mm), link3_offset=0.0,
    link4=(73.15 * mm),   link4_offset=0.0)

Tgoal = SE3(28.5 * cm, 0, 118.724 * mm) * SE3.Rx(180, 'deg')                               # Specify the goal poses of the robot as an array of SE3 objects, default is


#Atlas.Tgoals = SE3([                                # Specify the goal poses of the robot as an array of SE3 objects, default is 
#    SE3(28.5 * cm, 0, 118.724 * mm),               # SE3([SE3(0.4, 0.4, 0.4), SE3(0.5, 0.5, 0.5), SE3(0.6, 0.6, 0.6)]) * SE3.Rx(180, 'deg')
#    SE3(0.2, -0.1, 118.724 * mm + 10 * cm),                                 # This is because the robot is mounted upside down in the base plate.
#    SE3(-0.2, 0.1, 118.724 * mm)                                 # The goal poses are specified in the base plate coordinate system.
#    ]) * SE3.Rx(180, 'deg')




Atlas.portPicker()                                  # Lets the user choose which port to use for the connection
Atlas.openPort()                                    # Opens the chosen port


Atlas.enableTorque()                                # Enables the torque, so the robot cannot be moved manually.
Atlas.closePort()                                   # Closes the port
