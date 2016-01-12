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

error, handle_connector_1 = vrep.simxGetObjectHandle(clientID,'Connector_1',vrep.simx_opmode_oneshot_wait)
error, handle_motor_1 = vrep.simxGetObjectHandle(clientID,'Motor_1',vrep.simx_opmode_oneshot_wait)
error, handle_leg_1 = vrep.simxGetObjectHandle(clientID,'Leg_1',vrep.simx_opmode_oneshot_wait)

print handle_motor_1
print handle_connector_1
print handle_leg_1

# Initialize
returnCode,eulerAngles=vrep.simxGetObjectOrientation(clientID,handle_connector_1,handle_motor_1,vrep.simx_opmode_streaming)

def GetObjectAngle(handle_child,handle_parent):
    servoEulerAngles = []
    eulerAngles = vrep.simxGetObjectOrientation(clientID,handle_child,handle_parent,vrep.simx_opmode_buffer)[1]
    
    for angle in eulerAngles:
        print angle 
        servoEulerAngles.append((angle/300)*1023)   
    return servoEulerAngles[2]

while 1:
    clear()
    print GetObjectAngle(handle_connector_1,handle_motor_1)
    time.sleep(0.5)