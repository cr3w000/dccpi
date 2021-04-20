from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, NoTransition, WipeTransition
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty, StringProperty )
from kivy.core.window import Window
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

class Main_Screen(Screen):
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
        #super().__init__(**kwargs)
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

class Train_Screen(Screen):
    buttonBack = ObjectProperty(None)
    buttonStop = ObjectProperty(None)
    semafor = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def train_stop(self):
        if (self.buttonStop.state == "normal"):
            print("STOP UP")
        else:
            print("STOP DOWN")
            e.emergency_stop()
            self.semafor.color = (1, 0, 0, 1)


class Settings_Screen(Screen):
    buttonBack = ObjectProperty(None)
    buttonStop = ObjectProperty(None)
    semafor = ObjectProperty(None)

    def train_stop(self):
        if (self.buttonStop.state == "normal"):
            print("STOP UP")
        else:
            print("STOP DOWN")
            e.emergency_stop()
            self.semafor.color = (1, 0, 0, 1)


class RpiVlakApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(Main_Screen(name='main'))
        sm.add_widget(Train_Screen(name='train'))
        sm.add_widget(Settings_Screen(name='settings'))

        return sm
#        return Main_Screen()


if __name__ == '__main__':
    Window.size = (640, 480)
    Window.fullscreen = True
    RpiVlakApp().run()
