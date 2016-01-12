import vrep
import sys
import time
import os

clear = lambda: os.system('cls')

vrep.simxFinish(-1)
# clientID = vrep.simxStart('192.168.10.151',19999,True,True,5000,5) # Connect to V-REP
clientID = vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID != -1:
	print "Connected to remote API server"
else:
	print "Connection not succesful"
	sys.exit("Could not connect")

error, handle_main_body = vrep.simxGetObjectHandle(clientID,'Main_Body',vrep.simx_opmode_oneshot_wait)

legs = [0,1,2,3,4,5]
handles_ = []

for leg in legs:
	_leg = list()
	_leg.append(vrep.simxGetObjectHandle(clientID,'Connector_'+str(leg),vrep.simx_opmode_oneshot_wait)[1])
	_leg.append(vrep.simxGetObjectHandle(clientID,'Motor_'+str(leg),vrep.simx_opmode_oneshot_wait)[1])
	_leg.append(vrep.simxGetObjectHandle(clientID,'Leg_'+str(leg),vrep.simx_opmode_oneshot_wait)[1])
	handles_.append(_leg)


# Initialize
for leg in legs:
	vrep.simxGetObjectOrientation(clientID,handles_[leg][0],handle_main_body,vrep.simx_opmode_streaming)
	vrep.simxGetObjectOrientation(clientID,handles_[leg][1],handles_[leg][0],vrep.simx_opmode_streaming)
	vrep.simxGetObjectOrientation(clientID,handles_[leg][2],handles_[leg][1],vrep.simx_opmode_streaming)

def GetObjectAngle(handle_parent,handle_child):
    servoEulerAngles = []
    eulerAngles = vrep.simxGetObjectOrientation(clientID,handle_child,handle_parent,vrep.simx_opmode_buffer)[1]
	
    for angle in eulerAngles:
        # print angle 
        servoEulerAngles.append(angle*(1023/360))
    # return servoEulerAngles
    if handle_parent is handle_main_body:
        return servoEulerAngles[2]
    else:
        return servoEulerAngles[2]

def GetAllAngles():
	allAngles = list()
	_leg = list()

	for leg in legs:
		_leg.append(GetObjectAngle(handle_main_body, handles_[leg][0]))
		_leg.append(GetObjectAngle(handle_main_body, handles_[leg][1]))
		_leg.append(GetObjectAngle(handle_main_body, handles_[leg][2]))
		allAngles.append(_leg)
	return allAngles


while 1:
    clear()
    print GetAllAngles()
    # time.sleep(0.5)
#     print GetObjectAngle(handle_main_body,handles_[1][0])
#     print GetObjectAngle(handles_[1][0],handles_[1][1])
#     print GetObjectAngle(handles_[1][1],handles_[1][2])
#     # print GetObjectAngle(handle_motor_1,handle_connector_1)
#     # print GetObjectAngle(handle_leg_1,handle_motor_1)
#     # print GetObjectAngle(handle_motor_1,handle_leg_1)
#     time.sleep(0.5)