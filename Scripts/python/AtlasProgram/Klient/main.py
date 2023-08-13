'''
The main file is used to make small programs using the functions
from the Robot.py file. The user can freely choose which functions to use.

It is also a test file for developing features to the userScreen.py file.
'''
#from userInterface import *
from dxlModDef import *
from DynamixelRobot import *
import numpy as np

# NOTE: Remember to set the correct Dynamixel model in dxlModDef.py before use!

# Before running the program, the user has to specify the settings for the robot
Atlas = Robot()                                                     # Create an instance of the robot class named Atlas
Atlas.DXL_IDs = [1, 2, 3, 4, 5]                                     # Specify the IDs of each joint as an array of integers, default is [1]

#Atlas.MAX_JOINTS_VALUES = [4080, 3308, 3190, 3242, 4095]           # The maximum joint values for your joints in an array of integers, must be the same lenght as DXL_IDs
#Atlas.MIN_JOINTS_VALUES = [15, 1024, 1024, 1024, 0]                # The minimum joint values for your joints in an array of integers, must be the same lenght as DXL_IDs
Atlas.HOME_POSE = [1140, 1599, 3191, 3110, 1000]                    # The home pose of the robot as an array of integers, must be the same lenght as DXL_IDs
Atlas.MINMAX_MARGIN = 10                                            # The margin for the accuracy min and max values of the Dynamixels, default is 10 / 2 in each direction


Atlas.JOINTS = cg.get_robot_config_1(                               # Specify the lenghts of each joint as an array of floats in [meter], default is [0.1] for each join
    link1=(163.474 / 1000), link1_offset=0.0,
    link2=(190 / 1000),     link2_offset=0.0,
    link3=(208.216 / 1000), link3_offset=0.0,
    link4=(73.15 / 1000),   link4_offset=0.0)

maxValues = np.array([4080, 3308, 3190, 3242, 4095]) * 2 * np.pi / 4095 - np.pi # Specify the max and min values of the joints in an array of floats in [rad]
minValues = np.array([15, 1024, 1024, 1024, 0]) * 2 * np.pi / 4095 - np.pi      # The default is [-np.pi, np.pi] for each joint
Atlas.JOINTS.qlim = [minValues, maxValues]

Atlas.Tgoals = SE3([                                                # Specify the goal poses of the robot as an array of SE3 objects, default is 
            SE3(0.4, 118.724, 0.4),                                   # SE3([SE3(0.4, 0.4, 0.4), SE3(0.5, 0.5, 0.5), SE3(0.6, 0.6, 0.6)]) * SE3.Rx(180, 'deg')
            SE3(0.5, 118.724, 0.5),                                     # The  * SE3.Rx(180, 'deg') is used to rotate the goal poses 180 degrees around the x-axis.
            SE3(0.6, 118.724, 0.6)
        ]) * SE3.Rx(180, 'deg')



for Tg in Atlas.Tgoals:
    solutions = (Atlas.JOINTS.ikine_LM(Tg, q0=Atlas.JOINTS.qr, mask=[1, 0.1, 0.1, 0.1, 0.1, 0.1], joint_limits=True)) # Calculate the inverse kinematics for each goal pose
    for i in range(len(solutions.q)):
        solutions.q[i] = int((solutions.q[i] % (2 * np.pi)) * 4095 / (2 * np.pi))   # Normalize the joint values to be between 0 and 2*pi
    print(solutions)










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