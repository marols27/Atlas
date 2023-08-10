'''
The main file is used to make small programs using the functions
from the Robot.py file. The user can freely choose which functions to use.

It is also a test file for developing features to the userScreen.py file.
'''
from userInterface import *
from dxlModDef import *
from Robot import *

# NOTE: Remember to set the correct Dynamixel model in dxlModDef.py before use!

# Before running the program, the user has to specify the settings for the robot
Atlas = Robot()                                                 # Create an instance of the robot class named Atlas
Atlas.DXL_IDs = [1, 2, 3, 4, 5]                                 # Specify the IDs of each joint as an array of integers, default is [1]
Atlas.MAX_JOINTS_VALUES = [4095 - 15, 3308, 3190, 3242, 4095]   # The maximum joint values for your joints in an array of integers, must be the same lenght as DXL_IDs
Atlas.MIN_JOINTS_VALUES = [15, 1024, 1024, 1024, 0]             # The minimum joint values for your joints in an array of integers, must be the same lenght as DXL_IDs
Atlas.HOME_POSE = [1140, 1599, 3191, 3110, 1000]                # The home pose of the robot as an array of integers, must be the same lenght as DXL_IDs
Atlas.MINMAX_MARGIN = 10                                        # The margin for the accuracy min and max values of the Dynamixels, default is 10 / 2 in each direction

# Handeling the conection to the Dynamixels
while Atlas.avalilablePorts.__len__() == 0:
    Atlas.portDiscovery()                           # Discovers the available ports
if Atlas.portHandler == None:
    Atlas.portPicker()                              # Lets the user choose which port to use for the connection




# Your robot program goes here
Atlas.openPort()                                    # Opens the chosen port



Atlas.closePort()                                   # Closes the port   