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

#----------------------------------
#-----TCP Socket intercept---------
#----------------------------------


import socket


Host = 'localhost'
Port = 4533
Buffer_size = 1024


#defnie TCP server

class server_socket:
    
    def __init__(self,sock=None):
        
        if sock is None:
            self.sock = socket.socket()
        
        else:
            self.sock = sock
        
        self.connected = None
        self.adress = None
            
    def connect(self,host,port,listeners = 1):
        try:
            self.sock.bind((host,port))
            self.sock.listen(listeners)
            self.connected, self.address = self.sock.accept()
        
        except Exception as e:
            print(e)
           
    def acceptNew(self):
        if self.connected:
            try:
                self.connected.close()
            except Exception as e:
                print(e)
        try:
            self.connected, self.address = self.sock.accept()
        except Exception as e:
            print(e)
              
              
    def receive(self):
        return str(self.connected.recv(Buffer_size),encoding ='ascii')
        
    def respond(self, response):
        self.connected.send(response)
          
    def __del__(self):
        if self.connected:
            try:
                self.connected.close()
                  
            except Exception as e:
                print(e)
                  
        self.sock.close()       
        
