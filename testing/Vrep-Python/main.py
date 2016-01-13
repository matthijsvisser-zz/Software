import vrep
import sys
import time

vrep.simxFinish(-1)
# clientID = vrep.simxStart('192.168.10.151',19999,True,True,5000,5) # Connect to V-REP
clientID = vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID != -1:
    print "Connected to remote API server"
else:
    print "Connection not succesful"
    sys.exit("Could not connect")

# Define object handles
DummyHandle_ = [-1,-1,-1,-1,-1,-1,-1]
for i in range(1,7):
    DummyHandle_[i] = (vrep.simxGetObjectHandle(clientID,'DummyT'+str(i),vrep.simx_opmode_oneshot_wait)[1])

DummyHandle_Main = vrep.simxGetObjectHandle(clientID,'Main_Dummy',vrep.simx_opmode_oneshot_wait)[1]


# Get object positions
pos = [-1,-1,-1,-1,-1,-1,-1]
for i in range(1,7):
    pos[i] = vrep.simxGetObjectPosition(clientID,DummyHandle_[i],-1,vrep.simx_opmode_buffer)[1]
    print pos [i]
time.sleep(1)

#standup
for x in xrange(1,10):
    for i in xrange(1,7):
        setPosition = [pos[i][0], pos[i][1], -0.01*x]
        returnCode=vrep.simxSetObjectPosition(clientID,DummyHandle_[i],-1,setPosition,vrep.simx_opmode_streaming)
    time.sleep(0.1)
    

#Walking pattern
# for x in xrange(1,10):
#     setPosition = [pos[1][0], pos[1][1]+ 0.001*x, 0.001*x]
#     returnCode=vrep.simxSetObjectPosition(clientID,DummyHandle_[1],DummyHandle_Main,setPosition,vrep.simx_opmode_streaming)
#     setPosition = [pos[3][0], pos[3][1]+ 0.001*x, 0.001*x]
#     returnCode=vrep.simxSetObjectPosition(clientID,DummyHandle_[3],DummyHandle_Main,setPosition,vrep.simx_opmode_streaming)
#     setPosition = [pos[5][0], pos[5][1] + 0.001*x, 0.001*x]
#     returnCode=vrep.simxSetObjectPosition(clientID,DummyHandle_[5],DummyHandle_Main,setPosition,vrep.simx_opmode_streaming)
#     time.sleep(0.1)
    
# for x in xrange(1,10):
#     setPosition = [pos[1][0], pos[1][1], -0.01*x]
#     returnCode=vrep.simxSetObjectPosition(clientID,DummyHandle_[1],DummyHandle_Main,setPosition,vrep.simx_opmode_streaming)
#     setPosition = [pos[3][0], pos[3][1], -0.01*x]
#     returnCode=vrep.simxSetObjectPosition(clientID,DummyHandle_[3],DummyHandle_Main,setPosition,vrep.simx_opmode_streaming)
#     setPosition = [pos[5][0], pos[5][1], -0.01*x]
#     returnCode=vrep.simxSetObjectPosition(clientID,DummyHandle_[5],DummyHandle_Main,setPosition,vrep.simx_opmode_streaming)
#     time.sleep(0.1)
   
# for x in xrange(1,10):
#     setPosition = [pos[2][0], pos[2][1], 0.01*x]
#     returnCode=vrep.simxSetObjectPosition(clientID,DummyHandle_[2],DummyHandle_Main,setPosition,vrep.simx_opmode_streaming)
#     setPosition = [pos[4][0], pos[4][1], 0.01*x]
#     returnCode=vrep.simxSetObjectPosition(clientID,DummyHandle_[4],DummyHandle_Main,setPosition,vrep.simx_opmode_streaming)
#     setPosition = [pos[6][0], pos[6][1], 0.01*x]
#     returnCode=vrep.simxSetObjectPosition(clientID,DummyHandle_[6],DummyHandle_Main,setPosition,vrep.simx_opmode_streaming)
#     time.sleep(0.1)
    
    

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
