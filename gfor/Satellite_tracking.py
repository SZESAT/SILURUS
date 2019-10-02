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

Verzió: 1.0
Készítette: Kiss Gábor
            Pataki Péter - patakip@tilb.sze.hu
"""

#----------------------------------------------------
#--------------Satellite Tracking--------------------
#----------------------------------------------------

import command
import config
import TCP_server
import keyboard

def main():
        
    try:
        gpredict = TCP_server.server_socket()
    
    except Exception as e:
        print(e)

    print("Waiting for engage to Gredict")
    gpredict.connect(TCP_server.Host,TCP_server.Port)
    print("Engaged") 


    config.usb_config()
    config.usb_open()

    command.position_read()


    while True:

        command.ant_az = str(command.ant_az)
        command.ant_el = str(command.ant_el)

        response = command.ant_az+'\n'+command.ant_el+'\n'
        response = bytes(response,'utf-8')
        gpredict.respond(response)
    
        data = gpredict.receive()
        
        
        if data[0] == 'S':
            print("Connection terminated")
            print("Waiting for re-engage")
            gpredict.acceptNew()
            print("Engaged")
        
        
        if data[0] =="":
            print("Waiting for connect")
            gpredict.acceptNew()
            print("Engaged")
    
    
        if data[0] =='P':
            az_el = str(data)
            az_el = az_el.replace(",",".")
            az_el = az_el.split()
        
            az = int(float(az_el[1]))
            el = int(float(az_el[2]))
        

            command.position_set(az,el)
            command.position_read()
            print("sat pos:",az,el)
                  
            
    config.usb_close()
    
    
if __name__ == "__main__":
    
    try:
        main()
    
    except KeyboardInterrupt:
        
        print("Program aborted by Keyborad Interrupt")


        

