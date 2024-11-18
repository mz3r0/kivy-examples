from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang import Builder


arrangement_1 = '''
<RootWidget>:
    LevelOneWidget:
        id: level1
        LevelTwoWidget:
            id: level2
'''


arrangement_2 = '''
<LevelOneWidget>:
    custom: "Lvl"
    LevelTwoWidget:
        id: level2
    Label:
        text: root.custom

<RootWidget>:
    custom: "Root"
    LevelOneWidget:
        id: level1
        Label:
            text: "RootLabel has: " + root.custom
'''

Builder.load_string(arrangement_2)


class RootWidget(Widget):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        print(type(self), self.ids)

    def on_touch_down(self, touch):
        super(RootWidget, self).on_touch_down(touch)
        print(type(self), self.ids)


class LevelOneWidget(Widget):
    def __init__(self, **kwargs):
        super(LevelOneWidget, self).__init__(**kwargs)
        print(type(self), self.ids)

    def on_touch_down(self, touch):
        super(LevelOneWidget, self).on_touch_down(touch)
        print(type(self), self.ids)


class LevelTwoWidget(Widget):
    def __init__(self, **kwargs):
        super(LevelTwoWidget, self).__init__(**kwargs)
        print(type(self), self.ids)

    def on_touch_down(self, touch):
        super(LevelTwoWidget, self).on_touch_down(touch)
        print(type(self), self.ids)


class MyApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MyApp().run()
