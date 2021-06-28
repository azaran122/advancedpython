import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGridLayout(GridLayout):
    # Initialize
    def __init__(self, **kwargs):
        # Call grid Layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        # set Coloumns
        self.cols = 2

        # Add widget
        self.add_widget(Labl(text="Name"))


class HelloKivy(App):
    def build(self):
        return Label(text='Hello Kivy', font_size=72)


if __name__ == '__main__':
    helloKivy = HelloKivy()

    helloKivy.run()
