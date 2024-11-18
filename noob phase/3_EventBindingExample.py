from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty


class CustomBtn(Button):
    pressed = ListProperty([0, 0])

    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        # Return a value to consume the touch
        # Return False to further propagate it to the children
        #   of this widget
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        # print(type(self))
        print('From CustomBtn: pressed at {pos}'.format(pos=pos))


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        # Use either approach:
        #   self.btn_pressed
        #   btn_pressed_local

        def btn_pressed_local(instance, pos):
            print('From rootWidget local: pos: {pos}'.format(pos=pos))

        self.add_widget(Button(text='btn 1'))

        cb = CustomBtn(text='btn 2')
        cb.bind(pressed=self.btn_pressed)
        self.add_widget(cb)

        self.add_widget(Button(text='btn 3'))

    def btn_pressed(self, instance, pos):
        # print(type(self))
        print('From rootWidget member: pos: {pos}'.format(pos=pos))


class TestApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()
