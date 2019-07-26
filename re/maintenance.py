#-----------------------------
#-----Antenna Maintenance-----
#-----------------------------

import serial
import time
import struct

read = 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1F, 0x20
maintenance = 0x57, 0x31, 0x30, 0x38, 0x30, 0x02, 0x30, 0x37, 0x32, 0x32, 0x02, 0x2F, 0x20

port = serial.Serial(
     "/dev/ttyUSB0", 
    baudrate=600,
    bytesize=serial.EIGHTBITS, 
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE, 
    writeTimeout = 0,
    timeout = 5,
    rtscts = False,
    dsrdtr = False,
    xonxoff = False
     )

def position_read():
    #function starts
    global az_real
    global el_real
    port.write(read)
    IDN = port.read(size = 12)
    data = struct.unpack('>BBBBBBBBBBBB', IDN) #converting bytes to unsigned char

    #calculating the angles 
    az = data[1]*100 + data[2]*10 + data[3] + data[4]/10 -360 
    el = data[6]*100 + data[7]*10 + data[8] + data[8]/10 -360
    
    az_real = az
    el_real = el
    
    az_real = int(az_real)
    el_real = int(el_real)
    
    print(az_real,el_real)
    #function end
    

if port.is_open:
    port.close()
 
port.open() 

print("Antenna_maintenance_position")
print("---< Megnyitott port: " + port.portstr +" >---")

position_read()
port.write(maintenance)

while (az_real != 180 or el_real != 1):
        position_read()
        time.sleep(1.000)


if port.is_open:
    port.close()
    print("---< Port closed. Exit >---")



    
     
    