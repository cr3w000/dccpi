import time

from dccpi import *
e = DCCRPiEncoder()
controller = DCCController(e)  # Create the DCC controller with the RPi encodermodra
modra = DCCLocomotive("DCC3", 3)  # Create locos, args: Name, DCC Address (see DCCLocomotive class)

controller.register(modra)        # Register locos on the controller
# DCC6 registered on address #6
controller.start()             # Start the controller. Removes brake signal
# Starting DCC Controller      # and starts sending bits to the booster
#l1.reverse()                   # Change direction bit
#l2.fl = True                   # Change fl function bit
#l3.fl = True
#l1.speed = 10                  # Change speed
#l2.speed = 18
#l3.speed = 23
#l3.slower()                    # Reduce 1 speed step
#l3.faster()                    # Increase 1 speed step

modra.fl = True

while True:
  try:
    modra.speed=16
    print("Forward \n")
    time.sleep(11.5)
    modra.speed=0
    print("Stop \n")
    time.sleep(10)
    modra.reverse()
    time.sleep(.1)
    modra.speed=16
    print("Reverse \n")
    time.sleep(11.5)
    modra.speed=0
    print("Stop \n")
    time.sleep(10)
    modra.reverse()
    time.sleep(.1)




  except KeyboardInterrupt:
     controller.stop()
     break



controller.stop()              # IMPORTANT! Stop controller always. Emergency-stops
# DCC Controller stopped       # all locos and enables brake signal on tracks
