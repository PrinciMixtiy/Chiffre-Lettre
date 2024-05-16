from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from translator import translate


class Home(BoxLayout):

    chiffre = StringProperty('')

    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)

    def valide_input(self, widget):
        number = widget.text.replace(',', '.').replace(' ', '')
        self.chiffre = f"{widget.text}\n\n" + translate(float(number))
        widget.text = ''


class ConverterApp(App):
    def build(self):
        return Home()


if __name__ == '__main__':
    ConverterApp().run()
