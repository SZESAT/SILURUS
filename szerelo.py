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
#--------Antenna Park---------
#-----------------------------

import config
import time
import command

def main():
    
    print("Antenna_park_position")

    config.usb_config()
    config.usb_open()

    command.position_read()
    command.position_set(165,0)

    while (command.ant_az != 165 or command.ant_el != 0):
    
        command.position_read()
        print(command.ant_az, command.ant_el)
        time.sleep(1.000)

    config.usb_close()

if __name__ == "__main__":
    
    try:
        main()
        
    except KeyboardInterrupt:
        print("Exiting")







    
     
    