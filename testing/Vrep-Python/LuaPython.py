clientID = vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID != -1:
    print "Connected to remote API server"
else:
    print "Connection not succesful"
    sys.exit("Could not connect")




stepVelocity = 
stepAmplitude = 
stepHeight = 
movementDirection = 
rotationMode = 
movementStrength = 

vrep.simxGetObjectHandle(clientID,'Main_Dummy',vrep.simx_opmode_oneshot_wait)
vrep.simxGetObjectHandle(clientID,'Leg_Dummy',vrep.simx_opmode_oneshot_wait)

sizeFactor=1
vel=0.05
accel=0.05
initialP={0,0,0}
initialO={0,0,0}
initialP[3]=initialP[3]-0.03*sizeFactor

vrep.simxSetObjectPosition(clientID,legBase,antBase,p,vrep.simx_opmode_streaming)
vrep.simxSetObjectOrientation(clientID,legBase,antBase,o,vrep.simx_opmode_streaming)

stepHeight=0.04*sizeFactor
maxWalkingStepSize=0.08*sizeFactor
walkingVel=0.5

def moveBody(index)
    p = {initialP[0],initialP[1],initialP[2]}
    o = {initialO[0],initialO[1],initialO[2]}

    vrep.simxSetObjectPosition(clientID,legBase,antBase,p,vrep.simx_opmode_streaming)
    vrep.simxSetObjectOrientation(clientID,legBase,antBase,o,vrep.simx_opmode_streaming)


    if (index == 0):
        # up/down
        p[2]=p[2]-0.07*sizeFactor

        vrep.simxSetObjectPosition(clientID,legBase,antBase,p,vrep.simx_opmode_streaming)
        time.sleep(0.1)

        p[2]=p[2]+0.07*sizeFactor

        vrep.simxSetObjectPosition(clientID,legBase,antBase,p,vrep.simx_opmode_streaming)
        time.sleep(0.1)



for x in xrange(1,10):
    # Forward walk while keeping a fixed body posture:
    setStepMode(walkingVel,maxWalkingStepSize,stepHeight,90,0,1)
    simWait(10)

    # Rotate on the spot:
    setStepMode(walkingVel,maxWalkingStepSize,stepHeight,0,1,1)
    simWait(9.25)
    