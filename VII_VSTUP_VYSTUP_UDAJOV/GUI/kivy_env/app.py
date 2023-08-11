# app.py

from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):  # konstrukcia OOP volana dole
    def build(self):
        return Label(text="Hello, World!")

MainApp().run()     # volanie MainApp
