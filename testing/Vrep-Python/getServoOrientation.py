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
error, handle_connector_1 = vrep.simxGetObjectHandle(clientID,'Connector_1',vrep.simx_opmode_oneshot_wait)
error, handle_motor_1 = vrep.simxGetObjectHandle(clientID,'Motor_1',vrep.simx_opmode_oneshot_wait)
error, handle_leg_1 = vrep.simxGetObjectHandle(clientID,'Leg_1',vrep.simx_opmode_oneshot_wait)

# Initialize
returnCode,eulerAngles=vrep.simxGetObjectOrientation(clientID,handle_connector_1,handle_main_body,vrep.simx_opmode_streaming)
returnCode,eulerAngles=vrep.simxGetObjectOrientation(clientID,handle_motor_1,handle_connector_1,vrep.simx_opmode_streaming)
returnCode,eulerAngles=vrep.simxGetObjectOrientation(clientID,handle_leg_1,handle_motor_1,vrep.simx_opmode_streaming)

def GetObjectAngle(handle_parent,handle_child):
    servoEulerAngles = []
    eulerAngles = vrep.simxGetObjectOrientation(clientID,handle_child,handle_parent,vrep.simx_opmode_buffer)[1]
    
    for angle in eulerAngles:
        # print angle 
        servoEulerAngles.append(angle*(1023/360))
    return servoEulerAngles
    # if handle_parent is handle_main_body:
    #     return servoEulerAngles#[2]
    # else:
    #     return servoEulerAngles#[2]

while 1:
    clear()
    print GetObjectAngle(handle_main_body,handle_connector_1)
    print GetObjectAngle(handle_connector_1,handle_motor_1)
    # print GetObjectAngle(handle_motor_1,handle_connector_1)
    # print GetObjectAngle(handle_leg_1,handle_motor_1)
    print GetObjectAngle(handle_motor_1,handle_leg_1)
    time.sleep(0.5)