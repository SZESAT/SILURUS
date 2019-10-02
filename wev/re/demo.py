#-----------------------------
#--------Antenna Demo---------
#-----------------------------

import serial
import struct
import time

read = 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1F, 0x20

#demo positions---------------------------
azimut_demo = [180,120,100,200,200,230,180]
elevation_demo = [60,60,120,90,135,135,90]


#define fuctions-------------------------

def position_set(az,el): 
    #function starts
    H = [0,0,0,0]
    E = [0,0,0,0]
    
    #calculating azimut, elevation digits to controller
    az = 2*(360+az)
    el = 2*(360+el)
    H[0] = az//1000
    H[1] = (az-H[0]*1000)//100
    H[2] = (az-(H[0]*1000+H[1]*100))//10
    H[3] = (az-(H[0]*1000+H[1]*100))%10
    
    E[0] = el//1000
    E[1] = (el-E[0]*1000)//100
    E[2] = (el-(E[0]*1000+E[1]*100))//10
    E[3] = (el-(E[0]*1000+E[1]*100))%10
    
    #creating set command
    set = 0x57, 0x30+H[0], 0x30+H[1], 0x30+H[2], 0x30+H[3], 0x02, 0x30+E[0], 0x30+E[1], 0x30+E[2], 0x30+E[3], 0x02, 0x2F, 0x20
    
    port.write(set)
    #function ends


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
   

print("Antenna demo")

#port init----------

port= serial.Serial(
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

#port opening---------------
if port.is_open:
    port.close()
port.open()



print("---< Megnyitott port: " + port.portstr +" >---")

position_read()

for i in range(7):
    
    position_set(azimut_demo[i],elevation_demo[i])
    time.sleep(.300)
    
    while (azimut_demo[i]!=az_real or elevation_demo[i]!=el_real):
        position_read()
        time.sleep(1.000)
        print(i)
    #time.sleep(2.500)    


#Port closing----------------------
if port.is_open:
    port.close()
    print("---< Port closed. Exit >---")
        
