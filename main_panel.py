#This is a main window for the application
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('vidget.kv')

Window.minimum_width = 800
Window.minimum_height = 500

class VidGetApp(App):
    def build(self):
        pass


if __name__ == "__main__":
    VidGetApp().run()