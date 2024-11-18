from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import random


KV = '''
<ScatterTextWidget>:
    orientation: 'vertical'
    TextInput:
        id: my_textinput
        font_size: 150
        size_hint_y: None
        height: 200
        text: 'default'
        on_text: root.change_label_colour()
    FloatLayout:
        Scatter:
            Label:
                text: my_textinput.text
                font_size: 150
                color: root.text_colour
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 150
        Label:
            text: my_textinput.text[:3][::-1]
            font_size: 100
            color: root.text_colour
        Label:
            text: my_textinput.text[-3:][::-1]
            font_size: 100
            color: root.text_colour
'''

Builder.load_string(KV)


class ScatterTextWidget(BoxLayout):
    text_colour = ObjectProperty((1, 0, 0, 1))

    def change_label_colour(self, *args):
        colour = [random.random() for _ in range(3)] + [1]
        self.text_colour = colour


class ColorScatterApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    ColorScatterApp().run()
