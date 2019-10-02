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


#-----------------------------
#----Antenna maintenance------
#-----------------------------

import config
import time
import cmd


print("Antenna_maintenance_position")

config.usb_config()
config.usb_open()

cmd.position_read()

cmd.position_set(180,3)

while (cmd.ant_az != 180 or cmd.ant_el != 3):
    cmd.position_read()
    print(cmd.ant_az,cmd.ant_el)
    time.sleep(1.000)

config.usb_close()

   







    
     
    