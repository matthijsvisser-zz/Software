def setServoPositions(XBee, servoNum, servoData):
    data = list()
    if servoNum < 0 or servoNum > 18:
        return 0
    data.append(servoNum)
    for i in range(0, servoNum):
        servoId = servoData[i*2]
        servoPosition = servoData[i*2 + 1]
        if(position < 0 or position > 1023):
            return 0
        data.append(servoId)
        data.append(servoPosition)
    XBee.sendPacket(1, bytearray(data))
