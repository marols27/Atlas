from dynamixel_sdk import *                    # Uses Dynamixel SDK library
from dxlModDef import *
from adatools import config_generator as cg
from adatools import plotting_tools as pt
from spatialmath import SE3
import numpy as np

class Robot:
    # Set the class' propperties:
    def __init__(self):
        # The two folowing propperties are set automaticaly by using the portDiscovery() and portPicker() functions
        self.portHandler = None                                         # Specify the portHandler as a variable

        # The folowing propperties are set to default values, but can be changed by the user
        self.DXL_IDs = [1]                                              # Specify the IDs of the dynamixel as an array of integers
        self.JOINTS = cg.get_robot_config_1(
            link1=(0.1), link1_offset=0.0,
            link2=(0.1), link2_offset=0.0,
            link3=(0.1), link3_offset=0.0,
            link4=(0.1), link4_offset=0.0)
        self.REST_POSE = [int(4095/2)]                                  # Specify the home pose of the robot as an array of integers
        self.MAXVALUES = [4095]                                         # Specify the max and min values of the joints in an array of integers in steps
        self.MINVALUES = [0]                                            # Specify the min and min values of the joints in an array of integers in steps
        self.IKINOFFSET = [0]   # WARNING!: THIS HAS TO BE MANUALY CALCULATED FOR YOUR UNIQUE ROBOT NOT BASED ON ANNY DYNAMIXEL DOCUMENTATIONS!



        # To set the speed and modes of the dynamixel, you unfortunatly have to use the 
        # Dynamixel Wizard or somehow extract the settings from the Dynamixel SDK.
        # We used the Dynamixel Wizard to set the following values:
        # The dynamixel IDs
        # Movement type: Position
        # Profile acceleration: 500
        # Profile velocity: 2000
        
        # The IDs are saved by the Dynamixel Engines, so you only have to set them once. The same goes for the movement type.
        # But the profile acceleration and velocity are not saved by the Dynamixel Engines, so you have to set them every time you turn on the robot.


    def IKinMove(self, Tgoal, printInfo = False): # Moves the robot to the goal pose (Tgoal) using the inverse kinematics
        self.JOINTS.qlim = np.array([self.MINVALUES, self.MAXVALUES]) # Uppdates the limmits before use!
        
        # Creates the new solution for the goal pose
        solutions = (self.JOINTS.ikine_LM(Tgoal, q0=self.JOINTS.qr, mask=[1, 1, 1, 0.1, 0.1, 0.1], joint_limits = True, ilimit = 300, slimit=1000))
        for i in range(len(solutions.q)):
            solutions.q[i] = int((solutions.q[i] + np.pi) * 4095/(2*np.pi) - self.IKINOFFSET[i])    # Convert the radiants to steps output_steps = (input_radians + pi) * 4095 / (2 * pi)
            if solutions.q[i] < self.MINVALUES[i]:
                solutions.q[i] = self.MAXVALUES[i] - (self.MINVALUES[i] - solutions.q[i])
        
        if printInfo:           # Prints the solutions to the terminal if specified
            print(solutions)
        
        if solutions.success:
            self.moveWithPos(solutions.q)                                                              # Move the robot to the goal pose
            time.sleep(3)                                                                              # Wait 3 seconds before moving to the next pose
        else:
            print("The goal pose is outside of the joint limits")

    # Function for making the Port discovery Easier
    def portPicker(self, portCount = 10):
        avalilablePorts = []
        for i in range(0, portCount + 1):
            try:
                test = PortHandler('/dev/ttyUSB' + str(i))
                test.openPort()
                test.closePort()
                avalilablePorts.append('/dev/ttyUSB' + str(i))
            except:
                pass

            try:
                test = PortHandler('COM' + str(i))
                test.openPort()
                test.closePort()
                avalilablePorts.append('COM' + str(i))
            except:
                pass
        if len(avalilablePorts) == 0:
            print("No available ports where discovered, check your cable conections.")

        print("Available ports:")
        for i in range(len(avalilablePorts)):
            print(str(i) + ": " + avalilablePorts[i])
        
        while True:
            print("Choose a port by typing the number or the name of the port:")
            port = input()
            try:
                index = int(port)
                try:
                    print("Trying to choose port: " + avalilablePorts[index] + "...")
                    self.portHandler = PortHandler(avalilablePorts[index])
                    break
                except:
                    print("Index out of range, try a different number or port name.")
            except:
                if port in avalilablePorts:
                    try:
                        print("Trying to choose port: " + port + "...")
                        self.portHandler = PortHandler(port)
                        break
                    except:
                        print("Something went wrong try again:")
                else:
                    print("Port not recognised or listed, try a different number or port name.")
        print("Port chosen successfully.")

    #Opens the port to the robot and setts the baudrate.
    def openPort(self):
        # Open port
        if self.portHandler.openPort(): 
            print("Succeeded to open the port")
        else:
            print("Failed to open the port")
            print("Press any key to terminate...")
            getch()
            quit()
        # Set port baudrate
        if self.portHandler.setBaudRate(BAUDRATE):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")
            print("Press any key to terminate...")
            getch()
            quit()
            
    #Enabling the torque of all motors specified in the self.DXL_IDs list.
    def enableTorque(self):
        for i in self.DXL_IDs:
            dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(self.portHandler, i, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            else:
                print("Dynamixel with ID: %d has been successfully connected" % i)

    '''
    #Limiting the values of the motors.
    def minmax(self, pose):
        if len(pose) != len(self.MAX_JOINTS_VALUES) or len(pose) != len(self.MIN_JOINTS_VALUES):
            print("ERROR: The length of the pose array is not equal to the length of the MAX_JOINTS_VALUES or the MIN_JOINTS_VALUES array.")
            print("The length of self.DXL_IDs is: " + str(len(self.DXL_IDs)) + " and the length of the pose array is: " + str(len(pose)))
            print("The length of the pose array is: " + str(len(pose)))
            print("The length of the MAX_JOINTS_VALUES array is: " + str(len(self.MAX_JOINTS_VALUES)))
            print("The length of the MIN_JOINTS_VALUES array is: " + str(len(self.MIN_JOINTS_VALUES)))
            return None
        else:
            max = self.MAX_JOINTS_VALUES
            min = self.MIN_JOINTS_VALUES
            
            for i in range(len(pose)):
                pose[i] = pose[i] % 4095
                if (pose[i] < min[i] + int(10 / 2)):
                    pose[i] = min[i] + int(10 / 2)
                if (pose[i] > max[i] - int(10 / 2)):
                    pose[i] = max[i] - int(10 / 2)
            
            return pose
    '''

    #Drives only one of the joints.
    def driveAJoint(self, DXL_ID, newPos):
        newPos = newPos % 4095
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(self.portHandler, DXL_ID, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Dynamixel with ID: %d has been successfully connected" % DXL_ID)
    
        # Write goal position
            dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(self.portHandler, DXL_ID, ADDR_GOAL_POSITION, newPos)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))

            # Read present position
            if (MY_DXL == 'XL320'): # XL320 uses 2 byte Position Data, Check the size of data in your DYNAMIXEL's control table
                dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(self.portHandler, DXL_ID, ADDR_PRESENT_POSITION)
            else:
                dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(self.portHandler, DXL_ID, ADDR_PRESENT_POSITION)                
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))

            print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID, newPos, dxl_present_position))

    #Get the current pose.
    def getPose(self):
        pose = []

        for i in self.DXL_IDs:
            dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(self.portHandler, i, ADDR_PRESENT_POSITION)
            
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            
            pose.append(dxl_present_position % 4095)

        return pose #self.minmax(pose)


    #Moving the robot to a position using the positions of the motors.
    def moveWithPos(self, pose):
        #pose = self.minmax(pose)
        
        for i in range(len(self.DXL_IDs)):
            # Write goal position
            dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(self.portHandler, self.DXL_IDs[i], ADDR_GOAL_POSITION, int(pose[i]))
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))

            # Read present position
            if (MY_DXL == 'XL320'): # XL320 uses 2 byte Position Data, Check the size of data in your DYNAMIXEL's control table
                dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(self.portHandler, self.DXL_IDs[i], ADDR_PRESENT_POSITION)
            else:
                dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(self.portHandler, self.DXL_IDs[i], ADDR_PRESENT_POSITION)                
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))

            print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (self.DXL_IDs[i], pose[i], dxl_present_position))

    #Returns the robot to the base position.
    def returnToHomePose(self):
        self.moveWithPos(self.REST_POSE)

    #Disabling the torque of the motors.
    def disableTorque(self):
        for i in self.DXL_IDs:
            dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(self.portHandler, i, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            else:
                print("Dynamixel with ID; %d has been successfully disconnected" % i)


    #Close the port.
    def closePort(self):
        self.portHandler.closePort()
    
    #Opens the port, enables the torque, moves the robot to a specified position and closes the port with the robot in a fixed pose.
    def makeAMove(self, pose, lockedMove = True):
        self.openPort()
        self.enableTorque()
        self.moveWithPos()
        if ~lockedMove:
            self.disableTorque()
        self.closePort()