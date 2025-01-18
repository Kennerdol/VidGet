#This is a main window for the application
import kivy
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        self.icon = "assets/img/vg.png"  # Set the application icon (replace with your icon file path)
        self.title = "Vidget"  # Set the application title
        return Label(text="Youtube Downloader", font_size=72)


if __name__ == "__main__":
    MyApp().run()