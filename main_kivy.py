import json
import sys

import kivy
kivy.require('1.10.0') #trocar o null pela versão que temos

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


#from sinesp_client import SinespClient
#
# class Consulta():
#
#     def sinesp(placa):
#         sc = SinespClient()
#         plate = placa
#         result = sc.search(plate)
#         json_result = json.dumps(result)
#         print(json_result)

class Window(GridLayout):

    def __init__(self, **kwargs):

        super(Window, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Label(text='Placa'))
        self.placa = TextInput(multiline=False)
        self.add_widget(self.placa)
        self.btn = Button(text='Search')
        self.add_widget(self.btn)
#        self.btn.bind(on_press=Consulta.sinesp(self.placa))

class MyApp(App):

    def build(self):
        return Window()

if __name__ == '__main__':
    MyApp().run()


