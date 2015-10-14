import vrep
import sys
import time

vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP

if clientID!=-1:
    print "Connected to remote API server"
else:
    print "Connection not succesful"
    sys.exit("Could not connect")
    
#errorCode,RoboSpider_handle=vrep.simxGetObjectHandle(clientID,'RoboSpider',vrep.simx_opmode_oneshot_wait)
errorCode,DummyT1_handle=vrep.simxGetObjectHandle(clientID,'DummyT1',vrep.simx_opmode_oneshot_wait)
errorCode,DummyT2_handle=vrep.simxGetObjectHandle(clientID,'DummyT2',vrep.simx_opmode_oneshot_wait)
errorCode,DummyT3_handle=vrep.simxGetObjectHandle(clientID,'DummyT3',vrep.simx_opmode_oneshot_wait)
errorCode,DummyT4_handle=vrep.simxGetObjectHandle(clientID,'DummyT4',vrep.simx_opmode_oneshot_wait)
errorCode,DummyT5_handle=vrep.simxGetObjectHandle(clientID,'DummyT5',vrep.simx_opmode_oneshot_wait)
errorCode,DummyT6_handle=vrep.simxGetObjectHandle(clientID,'DummyT6',vrep.simx_opmode_oneshot_wait)

"program here"

returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT1_handle,-1,vrep.simx_opmode_streaming) 
returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT2_handle,-1,vrep.simx_opmode_streaming)
returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT3_handle,-1,vrep.simx_opmode_streaming)
returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT4_handle,-1,vrep.simx_opmode_streaming)
returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT5_handle,-1,vrep.simx_opmode_streaming)
returnCode,pos = vrep.simxGetObjectPosition(clientID,DummyT6_handle,-1,vrep.simx_opmode_streaming)
time.sleep(0.1)
for x in range(0,10,1):   
    returnCode1,pos1 = vrep.simxGetObjectPosition(clientID,DummyT1_handle,-1,vrep.simx_opmode_buffer)
    time.sleep(0.1)
    returnCode2,pos2 = vrep.simxGetObjectPosition(clientID,DummyT2_handle,-1,vrep.simx_opmode_buffer)
    time.sleep(0.1)
    returnCode3,pos3 = vrep.simxGetObjectPosition(clientID,DummyT3_handle,-1,vrep.simx_opmode_buffer)
    time.sleep(0.1)
    returnCode4,pos4 = vrep.simxGetObjectPosition(clientID,DummyT4_handle,-1,vrep.simx_opmode_buffer)
    time.sleep(0.1)
    returnCode5,pos5 = vrep.simxGetObjectPosition(clientID,DummyT5_handle,-1,vrep.simx_opmode_buffer)
    time.sleep(0.1)
    returnCode6,pos6 = vrep.simxGetObjectPosition(clientID,DummyT6_handle,-1,vrep.simx_opmode_buffer)
                
    time.sleep(1)
    print returnCode1+returnCode2+returnCode3+returnCode4+returnCode5+returnCode6
    print pos1+pos2+pos3+pos4+pos5+pos6


#RoboSpider = vrep.simxGetObjectPosition(clientID,RoboSpider_handle,-1,vrep.simx_opmode_buffer)
#DummyT1 = vrep.simxGetObjectPosition(clientID,DummyT1_handle,RoboSpider_handle,vrep.simx_opmode_buffer)
#DummyT2 = vrep.simxGetObjectPosition(clientID,DummyT2_handle,RoboSpider_handle,vrep.simx_opmode_buffer)
#DummyT3 = vrep.simxGetObjectPosition(clientID,DummyT3_handle,RoboSpider_handle,vrep.simx_opmode_buffer)
#DummyT4 = vrep.simxGetObjectPosition(clientID,DummyT4_handle,RoboSpider_handle,vrep.simx_opmode_buffer)
#DummyT5 = vrep.simxGetObjectPosition(clientID,DummyT5_handle,RoboSpider_handle,vrep.simx_opmode_buffer)
#DummyT6 = vrep.simxGetObjectPosition(clientID,DummyT6_handle,RoboSpider_handle,vrep.simx_opmode_buffer)

#returnCode,handles,intData,floatData,stringData = vrep.simxGetObjectGroupData(clientID,vrep.sim_object_dummy_type,0,vrep.simx_opmode_streaming)

"program end here"

 

