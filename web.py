"""
===============================================================================
===================  SILURUS azimuth-eleváció motorvezérlő  ===================
===============================================================================

Ez a program a Széchenyi István Egyetem Műholdas Laborában található SPID MD-02
azimuth-eleváció motorvezérlőt távvezérlő weboldal és a kommunikációt végző
program forráskódja.

Verzió: 0.1
Készítette: Kiss Gábor
            Pataki Péter - patakip@tilb.sze.hu
            
Hardware felépítés

    -------------    USB    ----------------        -----------
    | Raspberry | --------- | Motorvezérlő | ------ | BIG-RAS |
    -------------           ----------------    |   -----------
                                                |   -------------
                                                --- | Szenzorok |
                                                    -------------

Parancsok felépítése:
Bájt:    0   1    2    3    4    5    6    7    8    9    10   11  12
       -----------------------------------------------------------------
Mező:  | S | H1 | H2 | H3 | H4 | PH | V1 | V2 | V3 | V4 | PV | K | END |
       -----------------------------------------------------------------
Érték:   57  3x   3x   3x   3x   0x   3x   3x   3x   3x   0x   xF  20 (hex)

===============================================================================
"""

# Szükséges változók meghívása
#-------------------------------
import serial
import struct
import time
from flask import Flask, render_template

# Változók rögzítése
#-------------------------------

# Aktuális állapot kiolvasása a vezérlőből
  read = 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1F, 0x20
  statusz = 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1F, 0x20
  
# Stop parancs
  stop = 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x20
  # A stop parancs után a vezérlő automatikusan kiküldi az aktuális állapotát
  
# Demo pozíciók
  azimut_demo = [180,120,100,200,200,230,180]
  elevation_demo = [60,60,120,90,135,135,90]


# Funkciók definiálása
#--------------------------------

# Pozíció beállítsa
def position_set(az,el):
    
    H = [0,0,0,0]
    E = [0,0,0,0]
    
    # az azimuth és elevációs fokok átszámítása a vezérlő számára
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




app = Flask(__name__)

probaszam = '12fgf'



@app.route('/')
def index():
    return render_template('index.html', probaszam=probaszam)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
