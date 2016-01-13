import serial
import sys
import time
from time import sleep

port = "COM7"
ser = serial.Serial(port, 38400, timeout=0)

while True:
    data = ser.read(9999)
    if len(data) > 0:
        print(data)
    ser.write("sanda")
    time.sleep(1)

ser.close()