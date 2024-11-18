from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line
from random import random

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider

from kivy.properties import ListProperty, NumericProperty
from kivy.lang import Builder

KV = '''
<DrawingWidget>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

<ColourSlider@Slider>:
    min: 0
    max: 1
    value: 0.5
    size_hint_y: None
    height: 50

<Interface>:
    orientation: 'vertical'
    DrawingWidget:
        target_colour_rgb: red_slider.value, green_slider.value, blue_slider.value
        target_width_px: width_slider.value
    ColourSlider:
        id: red_slider
    ColourSlider:
        id: green_slider
    ColourSlider:
        id: blue_slider
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 50
        Label:
            text: 'output colour:'
        Widget:
            canvas:
                Color:
                    rgb: red_slider.value, green_slider.value, blue_slider.value
                Rectangle:
                    size: self.size
                    pos: self.pos
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 50
        Label:
            text: "width: {:.1f}".format(width_slider.value)
        Slider:
            id: width_slider
            min: 2
            max: 40
            value: 2
'''

Builder.load_string(KV)

class DrawingWidget(Widget):
    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)

        if not self.collide_point(*touch.pos):
            return

        with self.canvas:
            Color(*self.target_colour_rgb)
            self.line = Line(points=[touch.pos[0], touch.pos[1]],
                            width=self.target_width_px)

    def on_touch_move(self, touch):
        super(DrawingWidget, self).on_touch_move(touch)

        if not self.collide_point(*touch.pos):
            return

        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]

    def on_target_colour_rgb(self, instance, value):
        print(f"target_colour_rgb changed to {self.target_colour_rgb}")


class Interface(BoxLayout):
    pass

class DrawingApp(App):
    def build(self):
        return Interface()

DrawingApp().run()


