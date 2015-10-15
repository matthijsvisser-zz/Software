import vrep
import sys
import time

vrep.simxFinish(-1) # just in case, close all opened connections
# clientID = vrep.simxStart('192.168.10.151',19999,True,True,5000,5) # Connect to V-REP
clientID = vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
if clientID != -1:
    print "Connected to remote API server"
else:
    print "Connection not succesful"
    sys.exit("Could not connect")

errorCode,Joint_1_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_1_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_1_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_1_2',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_1_3_handle = vrep.simxGetObjectHandle(clientID,'Joint_1_3',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_2_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_2_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_2_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_2_2',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_2_3_handle = vrep.simxGetObjectHandle(clientID,'Joint_2_3',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_3_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_3_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_3_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_3_2',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_3_3_handle = vrep.simxGetObjectHandle(clientID,'Joint_3_3',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_4_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_4_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_4_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_4_2',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_4_3_handle = vrep.simxGetObjectHandle(clientID,'Joint_4_3',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_5_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_5_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_5_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_5_2',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_5_3_handle = vrep.simxGetObjectHandle(clientID,'Joint_5_3',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_6_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_6_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_6_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_6_2',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_6_3_handle = vrep.simxGetObjectHandle(clientID,'Joint_6_3',vrep.simx_opmode_oneshot_wait)
errorCode,Dummy_Base_handle = vrep.simxGetObjectHandle(clientID,'Dummy_Base',vrep.simx_opmode_oneshot_wait)

returnCode, force = vrep.simxGetJointForce(clientID,Joint_1_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_1_2_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_1_3_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_2_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_2_2_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_2_3_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_3_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_3_2_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_3_3_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_4_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_4_2_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_4_3_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_5_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_5_2_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_5_3_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_6_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_6_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_6_3_handle,vrep.simx_opmode_streaming)

errorCode,DummyT1_handle = vrep.simxGetObjectHandle(clientID,'DummyT1',vrep.simx_opmode_oneshot_wait)
errorCode,DummyT2_handle = vrep.simxGetObjectHandle(clientID,'DummyT2',vrep.simx_opmode_oneshot_wait)
errorCode,DummyT3_handle = vrep.simxGetObjectHandle(clientID,'DummyT3',vrep.simx_opmode_oneshot_wait)
errorCode,DummyT4_handle = vrep.simxGetObjectHandle(clientID,'DummyT4',vrep.simx_opmode_oneshot_wait)
errorCode,DummyT5_handle = vrep.simxGetObjectHandle(clientID,'DummyT5',vrep.simx_opmode_oneshot_wait)
errorCode,DummyT6_handle = vrep.simxGetObjectHandle(clientID,'DummyT6',vrep.simx_opmode_oneshot_wait)

returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT1_handle,-1,vrep.simx_opmode_streaming)
returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT2_handle,-1,vrep.simx_opmode_streaming)
returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT3_handle,-1,vrep.simx_opmode_streaming)
returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT4_handle,-1,vrep.simx_opmode_streaming)
returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT5_handle,-1,vrep.simx_opmode_streaming)
returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT6_handle,-1,vrep.simx_opmode_streaming)

torque = 100
returnCode = vrep.simxSetJointForce(clientID,Joint_1_1_handle,torque,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_1_2_handle,torque,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_1_3_handle,torque,vrep.simx_opmode_oneshot)

torque = 100
returnCode = vrep.simxSetJointForce(clientID,Joint_2_1_handle,torque,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_2_2_handle,torque,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_2_3_handle,torque,vrep.simx_opmode_oneshot)

torque = 100
returnCode = vrep.simxSetJointForce(clientID,Joint_3_1_handle,torque,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_3_2_handle,torque,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_3_3_handle,torque,vrep.simx_opmode_oneshot)

torque = 100
returnCode = vrep.simxSetJointForce(clientID,Joint_4_1_handle,torque,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_4_2_handle,torque,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_4_3_handle,torque,vrep.simx_opmode_oneshot)

torque = 100
returnCode = vrep.simxSetJointForce(clientID,Joint_5_1_handle,torque,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_5_2_handle,torque,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_5_3_handle,torque,vrep.simx_opmode_oneshot)

torque = 100
returnCode = vrep.simxSetJointForce(clientID,Joint_6_1_handle,torque,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_6_2_handle,torque,vrep.simx_opmode_oneshot)
returnCode = vrep.simxSetJointForce(clientID,Joint_6_3_handle,torque,vrep.simx_opmode_oneshot)


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

for x in xrange(1,50):
	
	# print "Position set to:",setPosition
	setPosition = [0.0, 0.0, 0.01*x]
	returnCode=vrep.simxSetObjectPosition(clientID,DummyT1_handle,Dummy_Base_handle,setPosition,vrep.simx_opmode_streaming)
	setPosition = [0.0, 0.0, 0.01*x]
	returnCode=vrep.simxSetObjectPosition(clientID,DummyT2_handle,Dummy_Base_handle,setPosition,vrep.simx_opmode_streaming)
	setPosition = [0.0, 0.0, 0.01*x]
	returnCode=vrep.simxSetObjectPosition(clientID,DummyT3_handle,Dummy_Base_handle,setPosition,vrep.simx_opmode_streaming)
	setPosition = [0.0, 0.0, 0.01*x]
	returnCode=vrep.simxSetObjectPosition(clientID,DummyT4_handle,Dummy_Base_handle,setPosition,vrep.simx_opmode_streaming)
	setPosition = [0.0, 0.0, 0.01*x]
	returnCode=vrep.simxSetObjectPosition(clientID,DummyT5_handle,Dummy_Base_handle,setPosition,vrep.simx_opmode_streaming)
	setPosition = [0.0, 0.0, 0.01*x]
	returnCode=vrep.simxSetObjectPosition(clientID,DummyT6_handle,Dummy_Base_handle,setPosition,vrep.simx_opmode_streaming)
	time.sleep(0.5)
	returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT1_handle,-1,vrep.simx_opmode_buffer) 
	# print "Current position:",pos


# time.sleep(1)
# returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_2_handle,vrep.simx_opmode_buffer)
# print "Current force:",force


# time.sleep(1)
# returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_1_handle,vrep.simx_opmode_buffer)
# print "Current force 1_1:",force
# returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_2_handle,vrep.simx_opmode_buffer)
# print "Current force 1_2:",force
# returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_3_handle,vrep.simx_opmode_buffer)
# print "Current force 1_3:",force