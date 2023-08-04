'''
Different layouts for the user interface, to be used in the main program.
'''

from moveR import *
import math

def returnToBase():
    connect()
    enableTorque()
    moveWithPos(3000,1550,3200,3100, 1000)
    closePort()

def positionPlacer():

    connect()
    enableTorque()
    while True:
        print("Enter what point you want to move to: 1, 2, 3...\n")
        s = input()
        #minimumValues = [none,800,950,900,none]
        #maximumValues = [none,3300,3200,3200,none]
        if(s == "1"):
            moveWithPos(3000,1500,3200,3100, 1000)
        elif(s == "2"):
            moveWithPos(2000,2500,3200,2300,2000)
        elif(s == "3"):
            moveWithPos(3000,2900,2600,2200,2000)
        else: 
            break
    closePort()
    print("Program has ended")

def moveToOne():
    connect()
    enableTorque()
    moveWithPos(3000,1500,3200,3100, 1000) 
    closePort()
def moveToTwo():
    connect()
    enableTorque()
    moveWithPos(2000,2500,3200,2300,2000)
    closePort() 
def moveToThree():
    connect()
    enableTorque()
    moveWithPos(3000,2900,2600,2200,2000)
    closePort() 

def wave():
    connect()
    enableTorque()
    while True:
        moveWithPos(1000,1500,1500,1000, 1000)
        time.sleep(2)
        moveWithPos(1000,2500,2600,2300,2000)
        time.sleep(2)
        if input("Press q to quit: ") == "q":
            returnToBase()
            break
    closePort()
    print("Program has ended")

def moveWithRadians(r):
    x = 4095/(2*math.pi)
    deg90 = int(4095/4)
    pos1 = int(r[0]*x)+deg90
    pos2 = int(r[1]*x)+deg90
    pos3 = int(r[2]*x)+deg90
    pos4 = int(r[3]*x)+deg90
    pos5 = int(r[4]*x)+deg90

    
    print(pos1,pos2,pos3,pos4,pos5)
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
    connect()
    enableTorque()
    moveWithPos(pos1,pos2,pos3,pos4,pos5)
    closePort()
    