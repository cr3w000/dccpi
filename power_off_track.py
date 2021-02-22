from dccpi import *

class POT():

    e = DCCRPiEncoder()
    controller = DCCController(e)  # Create the DCC controller with the RPi encodermodra

    def run(self):
        self.controller.stop()

if __name__ == '__main__':
    POT().run()

