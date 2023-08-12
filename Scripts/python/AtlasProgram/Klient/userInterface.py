'''
Different functions for the user to use to control the robot.
Before using moveR functions on the robot, you have to use the connect() function.
and the enableTorque() function.

For a program where you move the robot by hand and then setting the position you will
need to disable the torque. This is done with the disableTorque() function. Then save position
and enable torque again.

After using the moveR functions, you have to use the closePort() function.

'''
from DynamixelRobot import *
import math

#Moving the robot back to standby position.
Atlas = Robot()


def returnToBase():
    Atlas.returnToBase()

def positionPlacer():
    Atlas.connect()
    Atlas.enableTorque()
    while True:
        print("Enter what point you want to move to: 1, 2, 3...\n")
        s = input()
        #minimumValues = [none,800,950,900,none]
        #maximumValues = [none,3300,3200,3200,none]
        if(s == "1"):
            Atlas.moveWithPos(3000,1500,3200,3100, 1000)
        elif(s == "2"):
            Atlas.moveWithPos(2000,2500,3200,2300,2000)
        elif(s == "3"):
            Atlas.moveWithPos(3000,2900,2600,2200,2000)
        else: 
            break
    Atlas.closePort()
    print("Program has ended")

#Functions for moving the robot to a specific position. Inside the userScreen.py file, the user can choose which function to use.
def moveToOne():
    Atlas.makeAMove([3000,1500,3200,3100, 1000])
def moveToTwo():
    Atlas.makeAMove([2000,2500,3200,2300,2000])
def moveToThree():
    Atlas.makeAMove([3000,2900,2600,2200,2000])

#Function for maing the robot wave.
def wave():
    Atlas.connect()
    Atlas.enableTorque()
    while True:
        Atlas.moveWithPos(1000,1500,1500,1000, 1000)
        time.sleep(2)
        Atlas.moveWithPos(1000,2500,2600,2300,2000)
        time.sleep(2)
        if input("Press q to quit: ") == "q":
            returnToBase()
            break
    Atlas.closePort()
    print("Program has ended")

#Transforms the radians from the reverseKinematics function to the 
# position values matching the dynamixel motors.
def moveWithRadians(r):
    x = 4095/(2*math.pi)
    pos1 = int((r[0]+math.pi/2)%(2*math.pi)*x)
    pos2 = int((r[1]+math.pi/2)%(2*math.pi)*x)
    pos3 = -int((r[2]+math.pi/2)%(2*math.pi)*x)
    pos4 = int((r[3]+math.pi/2)%(2*math.pi)*x)
    pos5 = int((r[4]+math.pi/2)%(2*math.pi)*x)

    #print(r*180/math.pi)
    #minimumValues = [none,800,950,900,none]
    #maximumValues = [none,3300,3200,3200,none]
    if(pos1 < 800):
        pos1 = 800
    elif(pos1 > 3300):
        pos1 = 3300
    if(pos2 < 950):
        pos2 = 950
    elif(pos2 > 3200):
        pos2 = 3200
    if(pos3 < 900):
        pos3 = 900
    elif(pos3 > 3200):
        pos3 = 3200
    if(pos4 < 900):
        pos4 = 900
    elif(pos4 > 3200):
        pos4 = 3200
    if(pos5 < 800):
        pos5 = 800
    elif(pos5 > 3300):
        pos5 = 3300
    Atlas.makeAMove([pos1,pos2,pos3,pos4,pos5])
    