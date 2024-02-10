from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from ChLttrCls import Chiffre


class Home(BoxLayout):

    chiffre = StringProperty('')

    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)

    def valide_input(self, widget):
        self.chiffre = f"{widget.text}\n\n" + Chiffre(widget.text).lettre
        widget.text = ''


class ConverterApp(App):
    def build(self):
        return Home()


if __name__ == '__main__':
    ConverterApp().run()
