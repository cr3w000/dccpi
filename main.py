from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
#from kivy.clock import Clock



class Main_Screen(Widget):
    pass


class RpiVlakApp(App):
    def build(self):
        return Main_Screen()


if __name__ == '__main__':
    RpiVlakApp().run()
