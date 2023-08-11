# kivy_auto.py

from kivy.app import App
from kivy.uix.label import Label

class CustomLabel(Label):   # vytvorenie novej triedy
    pass

class MainApp(App):   
    def build(self):
        root = CustomLabel() # volanie novej triedy
        return root

MainApp().run()