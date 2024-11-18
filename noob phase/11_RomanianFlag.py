from kivy.app import App
from kivy.lang import Builder


KV = '''
#:import random random.random
BoxLayout:
    orientation: 'horizontal'
    Widget:
        size_hint: 1, 1
        canvas:
            Color:
                rgb: 0, 43/255, 127/255
            Rectangle:
                pos: self.pos
                size: self.size	
    Widget:
        size_hint: 1, 1
        canvas:
            Color:
                rgb: 252/255, 209/255, 22/255
            Rectangle:
                pos: self.pos
                size: self.size
    Widget:
        size_hint: 1, 1
        canvas:
            Color:
                rgb: 206/255, 17/255, 38/255
            Rectangle:
                pos: self.pos
                size: self.size
'''


class RomanianFlagApp(App):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    RomanianFlagApp().run()
