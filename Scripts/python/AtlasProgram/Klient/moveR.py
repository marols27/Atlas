'''This file contains functions that make the robot move. The functions are used in the main file.
'''

from baseFunctions import *


from dynamixel_sdk import * # Uses Dynamixel SDK library


#Moving the robot to a position using the positions of the motors.
def moveWithPos(posL1,posL2,posL3,posL4,posL5):
    DXL_GOALS = [posL1,posL2,posL3,posL4,posL5]

    for i in range(DXL_IDs.__len__()):
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_IDs[i], ADDR_GOAL_POSITION, DXL_GOALS[i])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

            
                # Read present position
        if (MY_DXL == 'XL320'): # XL320 uses 2 byte Position Data, Check the size of data in your DYNAMIXEL's control table
            dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_IDs[i], ADDR_PRESENT_POSITION)
        else:
            dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL_IDs[i], ADDR_PRESENT_POSITION)                
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))

        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_IDs[i], DXL_GOALS[i], dxl_present_position))




