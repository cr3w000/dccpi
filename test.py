from dccpi import *
e = DCCRPiEncoder()
controller = DCCController(e)  # Create the DCC controller with the RPi encoder
l1 = DCCLocomotive("DCC6", 6)  # Create locos, args: Name, DCC Address (see DCCLocomotive class)
l2 = DCCLocomotive("DCC7", 7)
l3 = DCCLocomotive("DCC8", 8)
controller.register(l1)        # Register locos on the controller
# DCC6 registered on address #6
controller.register(l2)
# DCC7 registered on address #7
controller.register(l3)
# DCC8 registered on address #8
controller.start()             # Start the controller. Removes brake signal
# Starting DCC Controller      # and starts sending bits to the booster
l1.reverse()                   # Change direction bit
l2.fl = True                   # Change fl function bit
l3.fl = True
l1.speed = 10                  # Change speed
l2.speed = 18
l3.speed = 23
l3.slower()                    # Reduce 1 speed step
l3.faster()                    # Increase 1 speed step
l1                             # Print loco information

controller.stop()              # IMPORTANT! Stop controller always. Emergency-stops
# DCC Controller stopped       # all locos and enables brake signal on tracks
