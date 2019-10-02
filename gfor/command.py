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


#----------------------------
#-------Antenna commands-----
#----------------------------

import struct
import config

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
    
    config.port.write(set)
    #function ends
    
def position_read():
    #function starts
    global ant_az
    global ant_el
    read = 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1F, 0x20
    config.port.write(read)
    IDN = config.port.read(size = 12)
    data = struct.unpack('>BBBBBBBBBBBB', IDN) #converting bytes to unsigned char

    #calculating the angles 
    az = data[1]*100 + data[2]*10 + data[3] + data[4]/10 -360 
    el = data[6]*100 + data[7]*10 + data[8] + data[8]/10 -360
    
    ant_az = az
    ant_el = el
    
    ant_az = int(ant_az)
    ant_el = int(ant_el)
    
    #print("ant pos:",ant_az,ant_el)
    #function end