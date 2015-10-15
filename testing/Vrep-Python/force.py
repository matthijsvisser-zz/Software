import vrep
import sys
import time

vrep.simxFinish(-1) # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP

if clientID != -1:
    print "Connected to remote API server"
else:
    print "Connection not succesful"
    sys.exit("Could not connect")

errorCode,Joint_1_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_1_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_1_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_1_2',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_1_3_handle = vrep.simxGetObjectHandle(clientID,'Joint_1_3',vrep.simx_opmode_oneshot_wait)

returnCode, force = vrep.simxGetJointForce(clientID,Joint_1_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_1_2_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_1_3_handle,vrep.simx_opmode_streaming)

errorCode,DummyT1_handle = vrep.simxGetObjectHandle(clientID,'DummyT1',vrep.simx_opmode_oneshot_wait)
returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT1_handle,-1,vrep.simx_opmode_streaming)

returnCode = vrep.simxSetJointForce(clientID,Joint_1_1_handle,100,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_1_2_handle,100,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_1_3_handle,100,vrep.simx_opmode_oneshot)


time.sleep(1)
returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_1_handle,vrep.simx_opmode_buffer)
print "Current force 1_1:",force
returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_2_handle,vrep.simx_opmode_buffer)
print "Current force 1_2:",force
returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_3_handle,vrep.simx_opmode_buffer)
print "Current force 1_3:",force


time.sleep(0.1)
returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT1_handle,-1,vrep.simx_opmode_buffer) 
print "Current position:",pos
time.sleep(1)

for x in xrange(1,25):
	setPosition = [0.25, 0.20, 0.01*x]
	print "Position set to:",setPosition
	returnCode=vrep.simxSetObjectPosition(clientID,DummyT1_handle,-1,setPosition,vrep.simx_opmode_streaming)
	time.sleep(1)
	returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT1_handle,-1,vrep.simx_opmode_buffer) 
	print "Current position:",pos


time.sleep(1)
returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_2_handle,vrep.simx_opmode_buffer)
print "Current force:",force


time.sleep(1)
returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_1_handle,vrep.simx_opmode_buffer)
print "Current force 1_1:",force
returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_2_handle,vrep.simx_opmode_buffer)
print "Current force 1_2:",force
returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_3_handle,vrep.simx_opmode_buffer)
print "Current force 1_3:",force