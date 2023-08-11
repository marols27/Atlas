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

#### - self.MAX_JOINTS_VALUES = [4095]

MAX_JOINTS_VALUES is a list of the maximum joint values for your dynamixels. 
This has to be a list of integers with the same lenght as with the self.DXL_IDs list.

#### - Self.MIN_JOINT_VALUES = [0]

Same as the MAX_JOINTS_VALUES, but minimum instead. This also has to be at the same lenght as the self.DXL_IDs variable.
Default value is [0].

#### - self.HOME_POSE

