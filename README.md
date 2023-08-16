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

#### - self.__init__(self):

Is automaticaly run once at the initialisation of a new Robot class object, and defines the class' attributes with default settings. 
For more info about the defaults, look throught the folder itself or check out the attributes section above.

#### - self.PortDiscoverer(self, portCount = 10):

Checks every port between "COM0" - "COM10" and "/dev/ttyUSB0" - "/dev/ttyUSB10" on your computer if they have any possible connections, and lets you pick one manualy if there are any.
Make sure your connection with the robot is working. You can also check more or less ports by setting the portCount value.

#### - self.OpenPort(self):

Atempts to open a port by using the porthandler variable defined by using the portPicker() method.

#### - self.SetTorqueState(self, state):

Turns the torque on or off based on the boolean state variable True or False. 
If the state is on, the computer controlls your robot, but if it is of you can controll your robot by hand.

#### - self.DriveAJoint(self, DXL_ID, newPos, lockPose = True):

Drives a single joint on your robot by requesting your joint or dynamixel ID and the new pose as a single integer. 
If you want to lock your robot in the new pose, you let the lockPose stay as True, 
and if you dont want it locked you set the lockPose to False. 

#### - self.GetPose(self):

Returns the current robot pose as an array with integers, at the lenght of the amount of dynamixels.

#### - self.MoveWithPose(self, pose):

This moves the robot to a pose specified by the step values of each joint in an array of intagers pose. 
The pose array has to be at the same lenght as the amount self.DXL_IDS. 
If the pose array passed violates the min max limits set for your robot, the robot will not move, but inform you that the limits are violated.
If you pass pose that does not have the same shape as your self.DXL_IDs array, you will also not move the robot but instead get notified.

#### - self.IKinMove(self, x, y, z, printInfo = False):

This function moves the robot based on 3 dimentional coordinates (x, y, z) in meters, 
where your robots base center point, is the origo of your coordinatesystem.
The function requieres the xyz coordinates measured in meter,
and has an optional boolean printInfo setting to se what the inverse kinematic 
method calculates for debugging purposes defaulted to False and not to print.

#### - self.HomePose(self):

This function moves your robot to the home or resting pose defined as an integer array at the lenght of your self.DXL_IDs array.
This is just a pose you can use to set a home destination for your robot. 
It is not neccecary, but it can be useful to set a pose for the robot to return to ehen turned off.
During the Atlas project, we used this pose as a resting pose for the 
robot where it did not need to be locked by power to stay in place.

#### - closePort(self):

Closes the connection between your computer and your robot.

#### - MakeAMove(self, lockedMove = True):

This was just a simplification for making a single move. Likewise with the MoveWithPose() function, 
this also uses an integer array width the length of your self.DXL_IDs, and moves the robot to that pose. 
But it also opens the port, enables the torque, disables the torque again if you pass the lockedMove parameter as False,
and  closes the port again all in one command.
