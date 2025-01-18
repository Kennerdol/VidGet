#This is a main window for the application
import kivy
from kivy.app import App
from kivy.uix.label import Label


class VidGetApp(App):
    def build(self):
        self.icon = "assets/img/vg.png"
        self.title = "Vidget"
        return Label(text="Youtube Downloader", font_size=72)


if __name__ == "__main__":
    VidGetApp().run()