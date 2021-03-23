from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty, StringProperty )
from end_to_end_distance import End_To_End
import ultrasonic_distance
import threading
import time
from kivy.clock import Clock

#from kivy.clock import Clock
e = End_To_End()
t = threading.Thread(target=e.run, name='EtE run')
t.daemon = True
t.start()
e.gentle_stop()


class Distance():
    dist = 0
    isRunning = 0
    def run(self):
        self.isRunning = 1
        while self.isRunning:
            self.dist = ultrasonic_distance.distance()
            Main_Screen.update()
            time.sleep(1)
    def stop(self):
        self.isRunning = 1

    def measure(self):
        return ultrasonic_distance.distance()

d = Distance()
#td = threading.Thread(target=d.run, name='D run')
#td.daemon = True
#td.start()


class Semafor(Widget):
    color = ListProperty((1, 0, 0, 1))
    pass

class TextRow(Widget):
    pass

class Main_Screen(Widget):
    buttonEtE = ObjectProperty(None)
    buttonStop = ObjectProperty(None)
    semafor = ObjectProperty(None)
    train_status = ObjectProperty(None)
    train_distance = ObjectProperty(None)
    dist = StringProperty()

    def update(self, *args):
        dist = str(round(d.measure()))
        self.train_distance.text = dist
        e.update_dist(dist)

    def __init__(self, **kwargs):
        super(Main_Screen, self).__init__(**kwargs)
        self.dist = ''
        Clock.schedule_interval(self.update, .1)


    def train_stop(self):
        if (self.buttonStop.state == "normal"):
            print("STOP UP")
        else:
            print("STOP DOWN")
            e.emergency_stop()
            self.semafor.color = (1, 0, 0, 1)
            self.buttonEtE.state="normal"

    def train_ete(self):
        if (self.buttonEtE.state == "normal"):
            print("ETE UP")
            e.gentle_stop()
            self.semafor.color = (1, 0, 0, 1)
        else:
            print("ETE DOWN")
            if(t.is_alive()):
                print("Thread alive, only set running flag")
                e.gentle_start()
            else:
                e.gentle_start()
            self.semafor.color = (0, 1, 0, 1)


class RpiVlakApp(App):
    def build(self):
        return Main_Screen()


if __name__ == '__main__':
    RpiVlakApp().run()
