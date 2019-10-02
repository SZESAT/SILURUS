
import serial
import string

print('''
 ____  _____ _____  ____     _   _____ 
/ ___||__  /| ____|/ ___|   / \ |_   _|
\___ \  / / |  _|  \___ \  / _ \  | |  
 ___) |/ /_ | |___  ___) |/ ___ \ | |  
|____//____||_____||____//_/   \_\|_|''' )        


park = 0x57, 0x31, 0x30, 0x38, 0x30, 0x02, 0x30, 0x39, 0x30, 0x30, 0x02, 0x2F, 0x20
read = 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1F, 0x20


print("Antenna demo")

#port init----------

port= serial.Serial(
    "/dev/ttyUSB0", 
    baudrate=9600,
    bytesize=serial.EIGHTBITS, 
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE, 
    writeTimeout = 0,
    timeout=10,
    rtscts = False,
    dsrdtr = False,
    xonxoff = False
    )

if port.is_open:
    port.close()
port.open()

print("---< Megnyitott port: " + port.portstr +" >---")



port.write(read)
IDN = port.readline()
if IDN:
    print(IDN)
else:
    print("Nem érkezett adat")
    



#----------------------------------------------------------
#Port closing
#----------------------------------------------------------
if port.is_open:
    port.close()
    print("---< Port closed. Exit >---")
    

    
