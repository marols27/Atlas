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
Atlas.HOME_POSE = [1140, 1599, 3191, 3110, 1000]                    # The home pose of the robot as an array of integers, must be the same lenght as DXL_IDs

Atlas.JOINTS = cg.get_robot_config_1(                               # Specify the lenghts of each joint as an array of floats in [meter], default is [0.1] for each join
    link1=(163.474 * mm), link1_offset=0.0,
    link2=(190 * mm),     link2_offset=0.0,
    link3=(208.216 * mm), link3_offset=0.0,
    link4=(73.15 * mm),   link4_offset=0.0)

maxValues = [4080, 3343, 3216, 3272, 4095]          # Specify the max and min values of the joints in an array of floats in steps
minValues = [15, 779, 886, 990, 0]

Atlas.JOINTS.qlim = [                               # The min max is then converted into radiants and stored in the qlim variable
    np.array(minValues) * 2 * np.pi / 4095 - np.pi, # the intervall convertion is from 0 to 4095 steps to -pi to pi radiants
    np.array(maxValues) * 2 * np.pi / 4095 - np.pi  # which is why the min max values are multiplied with 2*pi/4095 and then subtracted with pi
    ]

Atlas.Tgoals = SE3([                                                # Specify the goal poses of the robot as an array of SE3 objects, default is 
            SE3(28.5 * cm, 118.724 * mm, 0 * m),                                   # SE3([SE3(0.4, 0.4, 0.4), SE3(0.5, 0.5, 0.5), SE3(0.6, 0.6, 0.6)]) * SE3.Rx(180, 'deg')
            SE3(20 * cm, 20 * mm, 0 * m),                                     # The  * SE3.Rx(180, 'deg') is used to rotate the goal poses 180 degrees around the x-axis.
            #SE3(0.6, 118.724, 0.6)
        ]) * SE3.Rx(180, 'deg')


Atlas.portPicker()                                  # Lets the user choose which port to use for the connection
Atlas.openPort()                                    # Opens the chosen port
Atlas.enableTorque()                                # Enables the torque of all joints

print(int(63.4))

for Tg in Atlas.Tgoals:
    solutions = (Atlas.JOINTS.ikine_LM(Tg, q0=Atlas.JOINTS.qr, mask=[1, 1, 1, 0.1, 0.1, 0.1]))  # Calculate the inverse kinematics for each goal pose
    for i in range(len(solutions.q)):
        solutions.q[i] = int((solutions.q[i] + np.pi) * 4095 / (2 * np.pi))                     # Convert the radiants to steps output_steps = (input_radians + pi) * 4095 / (2 * pi)
    print(np.array(solutions.q)).astype(int)
    Atlas.moveWithPos(solutions.q)                                                              # Move the robot to the goal pose

Atlas.closePort()                                   # Closes the port








'''
# Handeling the conection to the Dynamixels
if Atlas.portHandler == None:
    Atlas.portPicker()                              # Lets the user choose which port to use for the connection



# Your robot program goes here                                    
Atlas.openPort()                 # Opens the chosen port



poses = []
Atlas.disableTorque()
for i in range(3):
    poses.append(Atlas.getPose())
    input()

input()
Atlas.enableTorque()

for i in range(3):
    Atlas.moveWithPos(poses[i])
    time.sleep(3)


Atlas.returnToHomePose()
#Atlas.disableTorque()           # Disables the torque, so the robot can be moved manually.
                                # If tou dont disable the torque, the robot will not be able to move manually
                                # this is helpfull if you want to lock the robot in a pose.



Atlas.closePort()               # Closes the port   
'''