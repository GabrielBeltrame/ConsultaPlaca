import kivy
kivy.require('1.10.0') #trocar o null pela versão que temos

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='Search'))
        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed)
        self.add_widget(cb)

    def btn_pressed(self, instance, pos):
        print('pos: printed from root widget: {pos}'.format(pos=pos))

class CustomBtn(Widget):

    pressed = ListProperty([0, 0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            # we consumed the touch. return False here to propagate
            # the touch further to the children.
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print ('pressed at {pos}'.format(pos=pos))

class WindowSearch(GridLayout):

    def __init__(self, **kwargs):
        super(WindowSearch, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Label(text='Placa'))
        self.placa = TextInput(multiline=False)
        self.add_widget(self.placa)
        self.add_widget(RootWidget())

class MyApp(App):

    def build(self):
        return WindowSearch()

if __name__ == '__main__':
    MyApp().run()


