'''
Different layouts for the user interface, to be used in the main program.
'''

from moveR import *

def positionPlacer():
    connect()
    enableTorque()
    while True:
        print("Enter what point you want to move to: 1, 2, 3...\n")
        s = input()
        if(s == "1"):
            moveWithPos(1500,1500,3200,2500,1000)
        elif(s == "2"):
            moveWithPos(1000,2500,3200,2200,2000)
        elif(s == "3"):
            moveWithPos(1000,2800,2600,2700,2000)
        else: 
            break
    closePort()