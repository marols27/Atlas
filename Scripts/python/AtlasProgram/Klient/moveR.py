'''This file contains functions that make the robot move. The functions are used in the main file.
'''

from dxlModDef import *


from dynamixel_sdk import * # Uses Dynamixel SDK library

MY_DXL = 'X_SERIES'       # X330 (5.0 V recommended), X430, X540, 2X430

DEVICENAME = "/dev/ttyUSB0"  # Check which port is being used on your controller

# DYNAMIXEL Protocol Version (1.0 / 2.0)
# https://emanual.robotis.com/docs/en/dxl/protocol2/
PROTOCOL_VERSION            = 2.0

portHandler = PortHandler(DEVICENAME)

packetHandler = PacketHandler(PROTOCOL_VERSION)

def connect():
    # Open port
    if portHandler.openPort():
        print("Succeeded to open the port")
    else:
        print("Failed to open the port")
        print("Press any key to terminate...")
        getch()
        quit()
    # Set port baudrate
    if portHandler.setBaudRate(BAUDRATE):
        print("Succeeded to change the baudrate")
    else:
        print("Failed to change the baudrate")
        print("Press any key to terminate...")
        getch()
        quit()

#Enabling the torque of the motors.
def enableTorque():
    for i in range(DXL_IDs.__len__()):
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_IDs[i], ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Dynamixel %d has been successfully connected" % (i+1))


#Moving the robot to a position using the positions of the motors.
def moveWithPos(posL1,posL2,posL3,posL4,posL5):
    DXL_GOALS = [posL1,posL2,posL3,posL4,posL5]
    j = 0
    while 1:
        print("Press any key to continue! (or press ESC to quit!)")
        if getch() == chr(0x1b):
            break

        for i in range(DXL_IDs.__len__()):
            # Write goal position
            dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_IDs[i], ADDR_GOAL_POSITION, DXL_GOALS[j])
                
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))

            while 1:
                # Read present position
                if (MY_DXL == 'XL320'): # XL320 uses 2 byte Position Data, Check the size of data in your DYNAMIXEL's control table
                    dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_IDs[i], ADDR_PRESENT_POSITION)
                else:
                    dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL_IDs[i], ADDR_PRESENT_POSITION)
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))

                print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_IDs[i], DXL_GOALS[j], dxl_present_position))

                j = j + 1

                if not abs(dxl_goal_position[index] - dxl_present_position) > DXL_MOVING_STATUS_THRESHOLD:
                    break

#Close the port.
def closePort():
    portHandler.closePort()



