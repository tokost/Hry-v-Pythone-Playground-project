from kivy.app import App
from kivy.uix.widget import Widget

class CustomRectangle(Widget):
    pass

class MainRec(App):
    def build(self):
        return CustomRectangle()

MainRec().run()