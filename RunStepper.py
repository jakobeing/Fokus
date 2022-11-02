import RPi.GPIO as GPIO
import time
from DRV8825 import DRV8825
import sys

print("test 1")

Wegstrecke_Positiv = int(0)
Wegstrecke_Negativ = int(0)


Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

print("test 2")
# Absolute Bewegung in Rellation zu 0
if sys.argv[1] == "absolut":
    soll_possition = int(sys.argv[2])                            # Werte werden gehohlt.
    datei = open('List-Fokus .rtf','r')                          # Werte werden gehohlt.   # Hier muss sich die passente Position gehohlt werden
    Aktuelle_position = int(datei.readline(9999999))             # Werte werden gehohlt.
    datei.close()                                                # Werte werden gehohlt.
    datei = open('List-Fokus .rtf','w')                          # Neuer wert wird gschrieben
    datei.write(str(soll_possition))                             # Neuer wert wird gschrieben
    datei.close()                                                # Neuer wert wird gschrieben
    print("test 3")
    if soll_possition < Aktuelle_position:
        Wegstrecke_Negativ = Aktuelle_position - soll_possition
        print("test 4")
    else:
        Wegstrecke_Positiv = soll_possition - Aktuelle_position
        print("test 5")

# Rellatieve bewegung in abhängigkeit vom aktuellen Standort (+, -)
if sys.argv[1] == "Rellativ_+":
    Wegstrecke = int(sys.argv[2])                        # Motoransteuerungswert (Positiv)
    datei = open('List-Fokus .rtf','r')                  # Die Liste wird zum auslesen geöfnet
    Aktuelle_position = int(datei.readline())            # Die aktuelle Position wird ausgelesen
    datei.close()
    Neue_position = str(Aktuelle_position+Wegstrecke)    # Die neue Position wird erechnet
    datei = open('List-Fokus .rtf','w')                  # Die liste wird zum übersreiben geöfnet
    datei.write(Neue_position)                           # Postionswert wird überschrieben
    datei.close()
    Wegstrecke_Positiv = Wegstrecke                      # ÜBERGABEWERT: Neue_position
    print("test 6")

if sys.argv[1] == "Rellativ_-":
    Wegstrecke = int(sys.argv[2])                        # Motoransteuerungswert (Positiv)
    datei = open('List-Fokus .rtf','r')                  # Die Liste wird zum auslesen geöfnet
    Aktuelle_position = int(datei.readline())            # Die aktuelle Position wird ausgelesen
    datei.close()
    Neue_position = str(Aktuelle_position-Wegstrecke)    # Die neue Position wird erechnet
    datei = open('List-Fokus .rtf','w')                  # Die liste wird zum übersreiben geöfnet
    datei.write(Neue_position)                           # Postionswert wird überschrieben
    datei.close()
    Wegstrecke_Negativ = Wegstrecke                      # ÜBERGABEWERT: Neue_position
    print("test 7")



Motor2.SetMicroStep('softward', 'halfstep')
Motor2.TurnStep(Dir='forward', steps=Wegstrecke_Positiv, stepdelay=0.0010)
print("test 8")
time.sleep(0.5)
Motor2.TurnStep(Dir='backward', steps=Wegstrecke_Negativ, stepdelay=0.0010)
Motor2.Stop()

print("test 9")
"""                                     
# 1.8 degree: nema23, nema14            
# softward Control :                    
# 'fullstep': A cycle = 200 steps        
# 'halfstep': A cycle = 200 * 2 steps    
# '1/4step': A cycle = 200 * 4 steps     
# '1/8step': A cycle = 200 * 8 steps     
# '1/16step': A cycle = 200 * 16 steps   
# '1/32step': A cycle = 200 * 32 steps  
"""


# except:
#    # GPIO.cleanup()
#    print("\nMotor stop")
#    Motor2.Stop()

#     exit()

exit()