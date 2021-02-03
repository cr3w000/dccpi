import time

from dccpi import *
e = DCCRPiEncoder()
controller = DCCController(e)  # Create the DCC controller with the RPi encodermodra
address = 1



while True:
  try:
    modra = DCCLocomotive("DCC6", address)  # Create locos, args: Name, DCC Address (see DCCLocomotive class)

    controller.register(modra)        # Register locos on the controller
# DCC6 registered on address #6
    controller.start()             # Start the controller. Removes brake signal

    print("Address %d",address)

    modra.fl = True
    time.sleep(.5)
    modra.fl = False
    time.sleep(.5)
    modra.fl = True
    time.sleep(.5)
    modra.fl = False
    time.sleep(.5)
    modra.fl = True
    time.sleep(.5)
    modra.fl = False
    time.sleep(.5)
    modra.fl = True
    time.sleep(.5)
    modra.fl = False
    time.sleep(.5)

    address = address + 1

    if(address == 256):
      break

  except KeyboardInterrupt:
     controller.stop()
     break



controller.stop()              # IMPORTANT! Stop controller always. Emergency-stops
# DCC Controller stopped       # all locos and enables brake signal on tracks
