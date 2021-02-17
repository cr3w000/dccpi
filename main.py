from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty )
from end_to_end import End_To_End
import threading

#from kivy.clock import Clock

class Semafor(Widget):
    color = ListProperty((1, 0, 0, 1))
    pass

class Main_Screen(Widget):
    buttonEtE = ObjectProperty(None)
    buttonStop = ObjectProperty(None)
    e = End_To_End()
    semafor = ObjectProperty(None)

    def train_stop(self):
        if (self.buttonStop.state == "normal"):
            print("STOP UP")
        else:
            print("STOP DOWN")
            self.e.emergency_stop()
            self.semafor.color = (1, 0, 0, 1)
            self.buttonEtE.state="normal"

    def train_ete(self):
        if (self.buttonEtE.state == "normal"):
            print("ETE UP")
            self.e.gentle_stop()
            self.semafor.color = (1, 0, 0, 1)
        else:
            print("ETE DOWN")
            t = threading.Thread(target=self.e.run, name='EtE run')
            t.daemon = True
            t.start()
            #self.e.run()
            self.semafor.color = (0, 1, 0, 1)





class RpiVlakApp(App):
    def build(self):
        return Main_Screen()


if __name__ == '__main__':
    RpiVlakApp().run()
