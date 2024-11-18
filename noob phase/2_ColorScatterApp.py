import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import random
import kwad


kivy.require('2.3.0')


KV = '''
#:kivy 2.3

<ScatterTextWidget>:
    orientation: 'vertical'
    text_colour: (1,0,0,1)
    canvas:
        Color:
            rgba: 0, 0, 1, 0.1
        Rectangle:
            pos: self.pos
            size: self.size
    TextInput:
        id: my_textinput
        font_size: 150
        size_hint_y: None
        height: 200
        text: 'default'
        on_text: root.change_label_colour()
    FloatLayout:
        Scatter:
            size_hint: None, None
            size: my_label.size
            d: self.show_area('g', group='after') # REQUIRES kwad
            Label:
                id: my_label
                text: my_textinput.text
                font_size: 150
                color: root.text_colour
                size: self.texture_size
                d: self.show_area('r', group='before') # REQUIRES kwad
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
    text_colour = ObjectProperty([1, 0, 0, 1])
    
    def change_label_colour(self, *args):
        self.text_colour = [random.random() for _ in range(3)] + [1]


class ColorScatterApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    kwad.attach()
    ColorScatterApp().run()
