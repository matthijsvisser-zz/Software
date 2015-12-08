#!/usr/bin/python

import sys
import base64
import time
import serial
import getopt
import binascii

class XBee_packet:
    def __init__(self):
        self.command = 0
        self.length = 0
        self.data = list()
        self.checksum = 0

class XBee_communication:
    def __init__(self, portName = None, baudRate = 115200):
        self.RxPackets = []
        self.TxPackets = []
        self.state = 0
        self.checksum = 0
        self.RxPacket = XBee_packet()
        self.TxPacket = XBee_packet()
        self.serial = serial.Serial(portName, baudRate)

    def sendPacket(self, command, data):
        packet = []
        packet.append(command)
        packet.append(len(data))
        packet.extend(data)

        checksum = 0
        checksum |= command
        checksum |= length
        for c in data:
            checksum |= ord(c)

        packet.append(checksum)
        self.serial.write(packet)



    def processSerialData(self, data):

        countNewPackets = 0
        for c in data:
            if self.state == 0:  # First start byte
                if ord(c) == 0x5A:
                    self.state = 1
                else:
                    self.state = 0
            elif self.state == 1:  # Second start byte
                if ord(c) == 0x3C:
                    self.state = 2
                else:
                    self.state = 0
            elif self.state == 2:  # Third start byte
                if ord(c) == 0x42:
                    self.state = 3
                else:
                    self.state = 0
            elif self.state == 3:  # Fourth start byte
                if ord(c) == 0x99:
                    self.state = 4
                else:
                    self.state = 0
            elif self.state == 4:  # Packet length
                self.RxPacket = XBee_packet(); # Create new packet instance
                self.RxPacket.length = ord(c)
                self.checksum |= self.RxPacket.length # Update checksum

                self.state = 5
            elif self.state == 5: # Packet command
                self.RxPacket.command = ord(c)
                self.checksum |= self.RxPacket.command # Update checksum
                self.state = 6
            elif self.state == 6: # Packet data
                    self.RxPacket.data.append(ord(c))
                    self.checksum |= ord(c)

                    if len(self.RxPacket.data) >= self.RxPacket.length: # Data length
                        self.state = 7
            elif self.state == 7: # checksum
                self.RxPacket.checksum = ord(c)
                self.state = 0
                if self.checksum == self.RxPacket.checksum: # Add packet to packet list if received correct
                    self.RxPackets.append(self.RxPacket)
                    self.checksum = 0
                    countNewPackets += 1
        return countNewPackets

    def readPacket(self):
        if len(self.RxPackets) > 0:
            return self.RxPackets.pop(0);
        else:
            return False

    def TX(self):
        if(self.serial.isOpen() == False):
            self.serial.open()

    def RX(self):
        if(self.serial.isOpen() == False):
            self.serial.open()
        else:
            data = self.serial.read(self.serial.inWaiting())
            if len(data) > 0:
                print "__"
                print "Length:", type(data)
                print data
                #for c in data:
                    #print type(c)
                #print data.decode("utf-8")
                #print data.encode('hex')

                self.processSerialData(data)

    def connectSerial(self, portName):
        if(self.serial.isOpen() == True):
            self.serial.close()

        self.serial.port = portName
        if(self.serial.isOpen() == False):
            self.serial.open()

def main(argv):
    portName = None
    baudRate = 115200
    try:
        opts, args = getopt.getopt(argv,"hp:r:",["portName=","baudRate="])
    except getopt.GetoptError:
        print 'main.py -p <portName> -r <baudRate>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'main.py -p <portName> -r <baudRate>'
            sys.exit()
        elif opt in ("-p", "--portName"):
            portName = arg
        elif opt in ("-r", "--baudRate"):
            baudRate = arg


    XBee = XBee_communication(portName, baudRate)
    if(XBee.serial.isOpen() == False):
        XBee.serial.open()

    while True:
        XBee.TX()
        XBee.RX()

        for packet in iter(XBee.readPacket, False):
            print "New packet!", packet

        time.sleep(.5)


if __name__ == "__main__":
   main(sys.argv[1:])
