# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:03:12 2015

@author: Isa
"""

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

errorCode,Dummy_Base_handle=vrep.simxGetObjectHandle(clientID,'Dummy_Base',vrep.simx_opmode_oneshot_wait)
errorCode,Force = vrep.simxGetJointForce(clientID,jointhadle,operationmode)



position = [0.0, 0.0, 0.0]
returnCode,pos = vrep.simxGetObjectPosition(clientID,Dummy_Base_handle,-1,vrep.simx_opmode_streaming)
time.sleep(0.1)
returnCode,pos = vrep.simxGetObjectPosition(clientID,Dummy_Base_handle,-1,vrep.simx_opmode_buffer) 
print pos
time.sleep(1)
returnCode=vrep.simxSetObjectPosition(clientID,Dummy_Base_handle,-1,position,vrep.simx_opmode_streaming)
time.sleep(1)
returnCode,pos = vrep.simxGetObjectPosition(clientID,Dummy_Base_handle,-1,vrep.simx_opmode_buffer) 
print pos



