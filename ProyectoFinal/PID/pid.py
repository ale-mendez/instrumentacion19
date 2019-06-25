import serial
import struct

arduino = serial.Serial('COM7', 9600)
bvalue=(254).to_bytes(4, byteorder="big")
#print(bvalue)
arduino.write(255)
rawString = arduino.readline()
print('rawString=',rawString)
arduino.close()