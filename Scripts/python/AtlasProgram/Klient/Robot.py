from dynamixel_sdk import *                    # Uses Dynamixel SDK library
from dxlModDef import *

class Robot:
    def __init__(self):
        self.MAX_JOINTS_VALUES = [4095, 3308, 3190, 3242, 4095]
        self.MEDIAN_JOINT_VALUES = [3119, 2030, 2041, 2073, 0]
        self.MIN_JOINTS_VALUES = [0, 792, 903, 974, 0]
        self.DXL_IDs = DXL_IDs
        self.DXL_MOVING_SPEED = 0

    '''
    def driveJoints(self, newPos):
        oldPos = self.getPose()
        
        operators = []
        for i in range(len(oldPos)):
            if (oldPos[i] > newPos[i]):
                operators.append(-25)
            else:
                operators.append(25)

        for i in range(len(operators)):
            if operators[i] == 1:
                while (oldPos[i] <= newPos[i]):
                    oldPos[i] += operators[i]
                    self.moveWithPos(oldPos)
                    time.sleep(0.01)
            else:
                while (oldPos[i] >= newPos[i]):
                    oldPos[i] += operators[i]
                    self.moveWithPos(oldPos)
                    time.sleep(0.01)
    '''
    
    def driveAJoint(self, DXL_ID, newPos):
        print("teraz")

        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Dynamixel %d has been successfully connected" % (DXL_ID))
        '''
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_GOAL_POSITION, newPos)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        # Read present position
        dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL_ID, ADDR_PRESENT_POSITION)                
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID, newPos, dxl_present_position))

        portHandler.closePort()'''

    def minmax(self, pose):
        max = self.MAX_JOINTS_VALUES
        min = self.MIN_JOINTS_VALUES

        for i in range(len(pose)):
            if (pose[i] < min[i] + 5):
                pose[i] = min[i] + 5
            if (pose[i] > max[i] - 5):
                pose[i] = max[i] - 5
        
        return pose

    def openPort(self):
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
    def enableTorque(self):
        for i in range(DXL_IDs.__len__()):
            dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_IDs[i], ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            else:
                print("Dynamixel %d has been successfully connected" % (i+1))


    #Get the current pose.
    def getPose(self):
        pose = []

        for i in DXL_IDs:
            dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, i, ADDR_PRESENT_POSITION)
            
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            
            pose.append(dxl_present_position)

        return self.minmax(pose)


    #Moving the robot to a position using the positions of the motors.
    def moveWithPos(self, DXL_GOALS):
        DXL_GOALS = self.minmax(DXL_GOALS)
        
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

    def returnToBase(self):
        DXL_HOME_GOALS = [1140, 1599, 3191, 3110, 1000]
        self.moveWithPos(DXL_HOME_GOALS)

    def makeAMove(self, pose):
        self.openPort()
        self.enableTorque()
        self.moveWithPos()
        self.closePort()


    #Disabling the torque of the motors.
    def disableTorque(self):
        for i in range(DXL_IDs.__len__()):
            dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_IDs[i], ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            else:
                print("Dynamixel %d has been successfully disconnected" % (i+1))


    #Close the port.
    def closePort(self):
        portHandler.closePort()