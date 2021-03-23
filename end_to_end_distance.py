import time
from dccpi import *

class End_To_End():

    e = DCCRPiEncoder()
    controller = DCCController(e)  # Create the DCC controller with the RPi encodermodra
    modra = DCCLocomotive("DCC3", 3)  # Create locos, args: Name, DCC Address (see DCCLocomotive class)

    controller.register(modra)        # Register locos on the controller
#    controller.start()             # Start the controller. Removes brake signal

    isRunning = False
    direction = 0
    speed = 0
    distance = 0

    def lights_on(self):
        self.modra.fl = True

    def lights_off(self):
        self.modra.fl = False


    def run(self):
        self.controller.start()             # Start the controller. Removes brake signal

        self.isRunning = True
        self.lights_on()
        if(self.distance < 30): # check initial position and set proper direction
            self.modra.reverse()
            self.direction = 1

        self.modra.speed=14  #set speed
        while True:
          if(self.isRunning):
            try:
#                Main_Screen.train_status.text = "ON"

                if(self.direction == 0):
                    if(self.distance < 29): # too close to end - reverse
                        self.modra.reverse()
                        self.direction = 1
                else:
                    if(self.distance > 46): # too close to end - reverse
                        self.modra.reverse()
                        self.direction = 0
            except KeyboardInterrupt:
                print("Keyboard interrupt")
                self.controller.stop()
                break
            except:
                print("General exception")
                self.controller.stop()
          time.sleep(.1)
        self.controller.stop()              # IMPORTANT! Stop controller always. Emergency-stops
        print("Controller stopped")

    def gentle_stop(self):
        self.lights_off()
        self.isRunning = False

    def emergency_stop(self):
        self.controller.stop()
        self.gentle_stop()

    def gentle_start(self):
        self.controller.start()
        self.lights_on()
        self.isRunning = True

    def update_dist(self, dist):
        self.distance = int(dist)

if __name__ == '__main__':
    End_To_End().run()

