"""
===============================================================================                                      
==================   ____  _____ _____  ____     _   _____   ==================
==================  / ___||__  /| ____|/ ___|   / \ |_   _|  ================== 
==================  \___ \  / / |  _|  \___ \  / _ \  | |    ================== 
==================   ___) |/ /_ | |___  ___) |/ ___ \ | |    ================== 
==================  |____//____||_____||____//_/   \_\|_|    ================== 
==================                                           ==================
===============================================================================
======================  "Silurus" távvezérlő szoftver  ========================
===================  a SPID Bigras MD-02 antennavezérlőhöz  ===================
===============================================================================

Ez a program a Széchenyi István Egyetem Műholdas Laborjában található SPID MD-02
azimuth-eleváció motorvezérlő távoli vezérlését valósítja meg.

Működése: A "Gpredict" műholdkövető szoftver adatai alapján az azimuth és az
eleváció értékeit USB-n keresztül eljuttatja az antenna forgató számára

A programhoz felhasználtuk a "xxx" projektben található kódokat.
link: github

Verzió: 0.5
Készítette: Kiss Gábor
            Pataki Péter - patakip@tilb.sze.hu


"""


#--------------------------
#----USB configuration-----
#--------------------------

import serial

def usb_config():
    
    global port
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

def usb_open():
    
    if port.is_open:
        port.close()
    port.open()
    print("---< Megnyitott port: " + port.portstr +" >---")
    


def usb_close():
    
    if port.is_open:
        port.close()
        print("---< Port closed. Exit >---")
    
    
    

