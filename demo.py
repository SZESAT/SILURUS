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
#--------Antenna Demo---------
#-----------------------------

import time
import command
import config


def main():
    #demo positions---------------------------
    az_demo = [180,120,100,200,200,230,180]
    el_demo = [60, 60, 120,90, 135,135, 90]
    
    config.usb_config()
    config.usb_open()
    
    command.position_read()

    for i in range(7):
    
        command.position_set(az_demo[i], el_demo[i])
        time.sleep(.300)
    
        while (az_demo[i]!=command.ant_az or el_demo[i]!=command.ant_el):
        
            command.position_read()
            print(command.ant_az,command.ant_el,i)
            time.sleep(1.000)
    
    config.usb_close()    
            

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting")

        
