from dynamixel_sdk import *                    # Uses Dynamixel SDK library
from dxlModDef import *

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

#Disabling the torque of the motors.
def disableTorque():
    for i in range(DXL_IDs.__len__()):
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_IDs[i], ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Dynamixel %d has been successfully disconnected" % (i+1))

#Close the port.
def closePort():
    portHandler.closePort()