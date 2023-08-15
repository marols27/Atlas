# Atlas/

![Cannot load image](https://raw.githubusercontent.com/HVLrobotics/project-reporting-example/9f3fef09243d8dec53e37df6c821e7fd0ef71b9e/%E2%80%ABimages/logo.png)

## Quick about

This is an smal doccumentation to the DynamixelRobot.py file, or library we created an used to controll our robot. 
You can find the file at our repository "Atlas" at Atlas/Scripts/python/AtlasProgram/Klient/DynamixelRobot.py

## The Robot Class, its Functions and parameters

### Parameters

NOTE: Remember to check the [Dynamixel E-Manual] for the propperties and specifications of your Dynamixel settings before setting them
in the variables below.

#### - self.PortHandler = None

NOTE: This is set automaticaly.
The porthandler takes care of handeling the port and conection between the computer and the U2D2.
You should be able to ignore this setting as most of it is configured automaticaly throught the portPicker() function.

#### - self.DXL_IDs = [1]

DXL_IDs is a list of your dynamixels identities as integers or hole numbers. This you will have to set manualy before using your robot.
Default value is [1] as the dynamixels default ID is 1.

#### - self.JOINTS = sg.get_robot_config_1(
####  link1=(1), link1_offset=0,
####  link2=(1), link2_offset=0,
####  link3=(1), link3_offset=0,
####  link4=(1), link4_offset=0
#### )

This is a definition of your dynamixels arm lenght. So the lenght between the joint axis center points. 
By default in our program the four lenghts available is set to 1 meter each it is set to only one arm lenght at 1 meter. But you can change it like this for up to four engines:
self.JOINTS = sg.get_robot_config_1(
link1=(0.5), link1_offset=0,
link2=(0.35), link2_offset_config_1
)

Where the first arm lnght is set to 50 cm and the seccond is set to 35 cm.

#### - self.REST_POSE = [int(4095 / 2)]

This is a saved pose that the robot can return to as a resting or home position. It is not strictly neccesary, but you wil have to set the array to the same lenght as the
self.DXL_IDs list with your own values. The default here is the median point value of the "XM430-W350-T" and "XM540-W150-T" dynamixel models that we used when building our robot.
The mid point and the range of rotation points may varry for each dynamixel, so remember to check the E-Manua for your dynamixel rotation ranges.

#### - self.MAXVALUES = [4095]  and self.MINVALUES = [0]

This is defining your robots joint limmits. When you input positions for the IKinMove() function, the IKinMove if we have programmed it correctly will not exceed any joint limits.
More about the function below.


#### - self.IKINOFFSET = [0]

This is an important value at the same level as the minimum and maximum values as it ensures that the IKinMove() calculates the correct pose for the robot.
The Inverse Kinematic Structure method we are using to create this script,
demands that the Zero points of the robot engines is sett to a specific pose that not neccecearily coresponds to the Zero points of the Dynamixels. 
Remember to be shure of this before atempting to use the IKinMove() function.

### Functions()

#### - __init__(self):

Is automaticaly run once at the initialisation of a new Robot class object, and defines the class' attributes with default settings. 
For more info about the defaults, look throught the folder itself or check out the attributes section above.

#### - portPicker(self, portCount = 10):

Checks every port between "COM0" - "COM10" and "/dev/ttyUSB0" - "/dev/ttyUSB10" on your computer if they have any possible connections, and lets you pick one manualy if there are any.
Make sure your connection with the robot is working. You can also check more or less ports by setting the portCount value.

#### - openPort(self):

Atempts to open a port. It is reccomended to use the portPicker() function before this one,
as it propperly creates a portHandler automaticaly for this function to work propperly.

#### - enableTorque(self):

Whenever you need to make a move with the robot, or just lock the robot in its current position. 
You use enableTorque() to start the current running throught the dynamixels to drive them.

#### - driveAJoint(self, DXL_ID, newPos, lockPose = True):

DriveAJoint moves only one of your joints to a new pose by requesting a dynamixel ID, and a new pose. 
By default the pose that the joint is moved to is locked, but by setting the lockPose variable to False the move will be an unlocked move.

#### - getPose(self):

This returns the joint pose values of your robot as they are physicaly as an array at the same length as how manny dynamixels you have deffined in the self.DXL_IDS.
You can use this to get the max and min limits of your robot joints, or to coppy poses if you might want to.

#### - moveWithPos(self, pose):

This moves the robot to a pose specified by the step values of each joint in an array of intagers pose. The pose array has to be at the same lenght as the amount self.DXL_IDS.
NOTE: This move robot function does not take your limits into account, so you have to remember to keep track of the values you give to the robot manualy.

#### - IKinMove(self, Tgoal, printInfo = False): WARNING STIL A WORK IN PROGRESS

This function uses a coordinate system measured in meters, with an origo point at your robot base center. 
The Tgoal value should bee a pose of the type: Tgoal = SE3(28.5 * cm, 0, 118.724 * mm) * SE3.Rx(180, 'deg')
If you ever want to see what the IKinMove() is calculating, with the calculations we have implemented, you can set the printInfo to True.
