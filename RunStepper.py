#  import RPi.GPIO as GPIO
import time
from DRV8825 import DRV8825
import sys

if sys.argv[0] == "absolut":
    soll = sys.argv[1]
    datei = open('List-Fokus .rtf','r')
    ist = datei.readline()
    aktion = (ist - soll)

# try:
#
#    Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))
#
#    """
#    # 1.8 degree: nema23, nema14
#    # softward Control :
#    # 'fullstep': A cycle = 200 steps
#    # 'halfstep': A cycle = 200 * 2 steps
#    # '1/4step': A cycle = 200 * 4 steps
#    # '1/8step': A cycle = 200 * 8 steps
#    # '1/16step': A cycle = 200 * 16 steps
#    # '1/32step': A cycle = 200 * 32 steps
#    """
#    Motor2.SetMicroStep('softward', 'halfstep')
#    Motor2.TurnStep(Dir='forward', steps=2000, stepdelay=0.0010)
#    time.sleep(0.5)
#    Motor2.TurnStep(Dir='backward', steps=2000, stepdelay=0.0010)
#    Motor2.Stop()
#
#
# except:
#    # GPIO.cleanup()
#    print("\nMotor stop")
#    Motor2.Stop()
#    exit()
#
#
