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
    pos1 = round(abs((r[0]/(2*math.pi))*4095))
    pos2 = round(abs((r[1]/(2*math.pi))*4095))
    pos3 = round(abs((r[2]/(2*math.pi))*4095))
    pos4 = round(abs((r[3]/(2*math.pi))*4095))
    pos5 = round(abs((r[4]/(2*math.pi))*4095))
   
    print(pos1,pos2,pos3,pos4,pos5)
    #minimumValues = [none,800,950,900,none]
    #maximumValues = [none,3300,3200,3200,none]
    #connect()
    #enableTorque()
    #moveWithPos(pos1,pos2,pos3,pos4,pos5)
    #closePort()
    