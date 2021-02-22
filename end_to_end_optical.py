import time
from dccpi import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class End_To_End():

    e = DCCRPiEncoder()
    controller = DCCController(e)  # Create the DCC controller with the RPi encodermodra
    modra = DCCLocomotive("DCC3", 3)  # Create locos, args: Name, DCC Address (see DCCLocomotive class)

    controller.register(modra)        # Register locos on the controller
#    controller.start()             # Start the controller. Removes brake signal

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def my_callback(channel, *args):
        print("Train detected")


    isRunning = False

    def lights_on(self):
        self.modra.fl = True

    def lights_off(self):
        self.modra.fl = False


    def run(self):
        self.controller.start()             # Start the controller. Removes brake signal

        self.isRunning = True
        self.lights_on()
        GPIO.add_event_detect(36, GPIO.RISING, callback=self.my_callback, bouncetime=1000)

        while self.isRunning:
            try:
                self.modra.speed=16
                print("Forward \n")
                time.sleep(11.5)
                self.modra.speed=0
                print("Stop \n")
                time.sleep(10)
                self.modra.reverse()
                time.sleep(.1)
                self.modra.speed=16
                print("Reverse \n")
                time.sleep(11.5)
                self.modra.speed=0
                print("Stop \n")
                time.sleep(10)
                self.modra.reverse()
                time.sleep(.1)

            except KeyboardInterrupt:
                self.controller.stop()
                break

        self.controller.stop()              # IMPORTANT! Stop controller always. Emergency-stops
        print("Controller stopped")

    def gentle_stop(self):
        self.lights_off()
        self.isRunning = False

    def emergency_stop(self):
        self.controller.stop()
        self.gentle_stop()


if __name__ == '__main__':
    End_To_End().run()

