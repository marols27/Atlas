'''
The main file is used to make small programs using the functions
from the userInterface.py file. The user can choose which function to use.

It is also a test file for developin features to the userScreen.py file.
'''
from userInterface import *
from Robot import *

Atlas = Robot() # Create an instance of the robot named Atlas

#Startup routine
Atlas.openPort()
#Atlas.disableTorque()

Atlas.driveAJoint(1, 0)
"""
poses = []
for i in range(3):
    input()
    poses.append(Atlas.getPose())
    print(poses[i])

input()
Atlas.enableTorque()
Atlas.returnToBase()
for i in range(poses.__len__()):
    time.sleep(3)
    Atlas.moveWithPos(poses[i])

time.sleep(3)
Atlas.returnToBase()
"""
Atlas.closePort()