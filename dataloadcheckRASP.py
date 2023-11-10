
# RASPBERRY PI CODE

import serial
import microbitsuck

data1 = 0
data2 = 0
data3 = 0

ser = serial.Serial('/dev/ttyACM0' , 9600)
while True:
    data = ser.readuntil(b'\n')   
    if data == "recycle":
    data1 += 1
    else data == "biowaste":
    data2 += 1
    elif data == "dangrous":
    data3 += 1
    elif data == "back":
    continue



    
        





   


