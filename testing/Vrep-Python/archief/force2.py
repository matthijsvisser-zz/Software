import vrep
import sys
import time
import math

vrep.simxFinish(-1)
# clientID = vrep.simxStart('192.168.10.151',19999,True,True,5000,5) # Connect to V-REP
clientID = vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID != -1:
    print "Connected to remote API server"
else:
    print "Connection not succesful"
    sys.exit("Could not connect")

# jointNameList = ["Joint_1_0", "Joint_1_1", "Joint_1_2", "Joint_2_0", "Joint_2_1", "Joint_2_2", "Joint_3_0",\
# 				 "Joint_3_1", "Joint_3_2", "Joint_4_0", "Joint_4_1", "Joint_4_2", "Joint_5_0", "Joint_5_1",\
# 				 "Joint_5_2", "Joint_6_0", "Joint_6_1", "Joint_6_2"]

# jointHandleList = [ Joint_1_0_handle,Joint_1_1_handle,Joint_1_2_handle,Joint_2_0_handle,Joint_2_1_handle,
#                     Joint_2_2_handle,Joint_3_0_handle,Joint_3_1_handle,Joint_3_2_handle,Joint_4_0_handle,
#                     Joint_4_1_handle,Joint_4_2_handle,Joint_5_0_handle,Joint_5_1_handle,Joint_5_2_handle,
#                     Joint_6_0_handle,Joint_6_1_handle,Joint_6_2_handle]

# for item in jointHandleList:
#     errorCode,jointHandleList[item] = vrep.simxGetObjectHandle(clientID,jointNameList[item],vrep.simx_opmode_oneshot_wait)

errorCode,Joint_1_0_handle = vrep.simxGetObjectHandle(clientID,'Joint_1_0',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_1_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_1_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_1_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_1_2',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_2_0_handle = vrep.simxGetObjectHandle(clientID,'Joint_2_0',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_2_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_2_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_2_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_2_2',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_3_0_handle = vrep.simxGetObjectHandle(clientID,'Joint_3_0',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_3_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_3_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_3_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_3_2',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_4_0_handle = vrep.simxGetObjectHandle(clientID,'Joint_4_0',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_4_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_4_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_4_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_4_2',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_5_0_handle = vrep.simxGetObjectHandle(clientID,'Joint_5_0',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_5_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_5_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_5_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_5_2',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_6_0_handle = vrep.simxGetObjectHandle(clientID,'Joint_6_0',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_6_1_handle = vrep.simxGetObjectHandle(clientID,'Joint_6_1',vrep.simx_opmode_oneshot_wait)
errorCode,Joint_6_2_handle = vrep.simxGetObjectHandle(clientID,'Joint_6_2',vrep.simx_opmode_oneshot_wait)
errorCode,Main_Dummy_handle = vrep.simxGetObjectHandle(clientID,'Main_Dummy',vrep.simx_opmode_oneshot_wait)

returnCode, force = vrep.simxGetJointForce(clientID,Joint_1_0_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_1_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_1_2_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_2_0_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_2_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_2_2_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_3_0_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_3_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_3_2_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_4_0_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_4_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_4_2_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_5_0_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_5_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_5_2_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_6_0_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_6_1_handle,vrep.simx_opmode_streaming)
returnCode, force = vrep.simxGetJointForce(clientID,Joint_6_2_handle,vrep.simx_opmode_streaming)

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

def setTorque (torque):
    returnCode = vrep.simxSetJointForce(clientID,Joint_1_0_handle,torque,vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetJointForce(clientID,Joint_1_1_handle,torque,vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetJointForce(clientID,Joint_1_2_handle,torque,vrep.simx_opmode_oneshot)

    returnCode = vrep.simxSetJointForce(clientID,Joint_2_0_handle,torque,vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetJointForce(clientID,Joint_2_1_handle,torque,vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetJointForce(clientID,Joint_2_2_handle,torque,vrep.simx_opmode_oneshot)

    returnCode = vrep.simxSetJointForce(clientID,Joint_3_0_handle,torque,vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetJointForce(clientID,Joint_3_1_handle,torque,vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetJointForce(clientID,Joint_3_2_handle,torque,vrep.simx_opmode_oneshot)

    returnCode = vrep.simxSetJointForce(clientID,Joint_4_0_handle,torque,vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetJointForce(clientID,Joint_4_1_handle,torque,vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetJointForce(clientID,Joint_4_2_handle,torque,vrep.simx_opmode_oneshot)

    returnCode = vrep.simxSetJointForce(clientID,Joint_5_0_handle,torque,vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetJointForce(clientID,Joint_5_1_handle,torque,vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetJointForce(clientID,Joint_5_2_handle,torque,vrep.simx_opmode_oneshot)

    returnCode = vrep.simxSetJointForce(clientID,Joint_6_0_handle,torque,vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetJointForce(clientID,Joint_6_1_handle,torque,vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetJointForce(clientID,Joint_6_2_handle,torque,vrep.simx_opmode_oneshot)


# time.sleep(1)
# returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_0_handle,vrep.simx_opmode_buffer)
# print "Current force 1_0:",force
# returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_1_handle,vrep.simx_opmode_buffer)
# print "Current force 1_1:",force
# returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_2_handle,vrep.simx_opmode_buffer)
# print "Current force 1_2:",force


setTorque(250)

time.sleep(0.1)
returnCode,pos1 = vrep.simxGetObjectPosition(clientID,DummyT1_handle,-1,vrep.simx_opmode_buffer) 
returnCode,pos2 = vrep.simxGetObjectPosition(clientID,DummyT2_handle,-1,vrep.simx_opmode_buffer) 
returnCode,pos3 = vrep.simxGetObjectPosition(clientID,DummyT3_handle,-1,vrep.simx_opmode_buffer) 
returnCode,pos4 = vrep.simxGetObjectPosition(clientID,DummyT4_handle,-1,vrep.simx_opmode_buffer) 
returnCode,pos5 = vrep.simxGetObjectPosition(clientID,DummyT5_handle,-1,vrep.simx_opmode_buffer) 
returnCode,pos6 = vrep.simxGetObjectPosition(clientID,DummyT6_handle,-1,vrep.simx_opmode_buffer) 
time.sleep(1)


for x in xrange(1,10):
    setPosition = [pos1[0], pos1[1], -0.01*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT1_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    setPosition = [pos2[0], pos2[1], -0.01*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT2_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    setPosition = [pos3[0], pos3[1], -0.01*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT3_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    setPosition = [pos4[0], pos4[1], -0.01*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT4_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    setPosition = [pos5[0], pos5[1], -0.01*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT5_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    setPosition = [pos6[0], pos6[1], -0.01*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT6_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    time.sleep(0.1)

#Walking patern
 
for x in xrange(1,10):
    setPosition = [pos1[0], pos1[1]+ 0.001*x, 0.001*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT1_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    setPosition = [pos3[0], pos3[1]+ 0.001*x, 0.001*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT3_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    setPosition = [pos5[0], pos5[1] + 0.001*x, 0.001*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT5_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    time.sleep(0.1)
    
for x in xrange(1,10):
    setPosition = [pos1[0], pos1[1], -0.01*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT1_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    setPosition = [pos3[0], pos3[1], -0.01*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT3_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    setPosition = [pos5[0], pos5[1], -0.01*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT5_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    time.sleep(0.1)
   
for x in xrange(1,10):
    setPosition = [pos2[0], pos2[1], 0.01*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT2_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    setPosition = [pos4[0], pos4[1], 0.01*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT4_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    setPosition = [pos6[0], pos6[1], 0.01*x]
    returnCode=vrep.simxSetObjectPosition(clientID,DummyT6_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
    time.sleep(0.1)
    
    

#for x in xrange(1,20):
 #   setPosition = [0.2, 0.2, pos[2]-0.01*x]
  #  returnCode=vrep.simxSetObjectPosition(clientID,DummyT1_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
   # time.sleep(0.1)


#r = 0.2681
#r = 0.1
#for degree in xrange(0,90):
	#setPosition = [math.cos(degree)*r + 0.0585, math.sin(degree)*r + 0.1184, 0.01]
	#returnCode=vrep.simxSetObjectPosition(clientID,DummyT1_handle,Main_Dummy_handle,setPosition,vrep.simx_opmode_streaming)
	#time.sleep(1)
	#returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT1_handle,-1,vrep.simx_opmode_buffer) 
	#print "Current position:",pos


# time.sleep(1)
# returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_1_handle,vrep.simx_opmode_buffer)
# print "Current force:",force


# time.sleep(1)
# returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_0_handle,vrep.simx_opmode_buffer)
# print "Current force 1_0:",force
# returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_1_handle,vrep.simx_opmode_buffer)
# print "Current force 1_1:",force
# returnCode, force=vrep.simxGetJointForce(clientID,Joint_1_2_handle,vrep.simx_opmode_buffer)
# print "Current force 1_2:",force
