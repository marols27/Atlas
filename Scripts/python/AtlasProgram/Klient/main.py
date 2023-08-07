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
Atlas.enableTorque()
startPose = Atlas.getPose()
clonedPose = Atlas.getPose()

Atlas.returnToBase()

time.sleep(2)

Atlas.disableTorque()
Atlas.closePort()




'''
# Ask the user for input
command = input("Press 1 to move the robot to a position, press 2 to wave: ")
if command == "1":
    Atlas.positionPlacer()
elif command == "2":
    Atlas.wave()
else:
    print("Have a nice day!")

# Disable torque and close the port
'''
#print(Atlas.getPose())

#Atlas.returnToBase()